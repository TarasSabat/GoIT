from pathlib import Path
import shutil
import sys
import re

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

MY_OTHER = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENT,
    'DOCX': DOCX_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():
            if item.name not in ('archives', 'videos', 'audios', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        # Робота з файлом
        extension = get_extension(item.name)
        full_name = folder / item.name
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)
                MY_OTHER.append(full_name)


CYRILLIC_SYMBOLS = 'абвгдежзйклмнопрстуфхцчшщюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "j", "z", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "yu", "ja", "je", 'i', "ji", "g")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str) -> str:
    translate_name = name.split('.')
    translate_name[0] = re.sub(r'\W', '_', translate_name[0].translate(TRANS))
    my_name = ('.'.join(translate_name))
    return my_name


def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))


def handle_document(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))


def handle_other(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))


def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()


def main(folder: Path):
    scan(folder)
    for file in JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in AVI_VIDEO:
        handle_media(file, folder / 'videos' / 'AVI')
    for file in MP4_VIDEO:
        handle_media(file, folder / 'videos' / 'MP4')
    for file in MOV_VIDEO:
        handle_media(file, folder / 'videos' / 'MOV')
    for file in MKV_VIDEO:
        handle_media(file, folder / 'videos' / 'MKV')
    for file in MP3_AUDIO:
        handle_media(file, folder / 'audios' / 'MP3')
    for file in OGG_AUDIO:
        handle_media(file, folder / 'audios' / 'OGG')
    for file in WAV_AUDIO:
        handle_media(file, folder / 'audios' / 'WAV')
    for file in AMR_AUDIO:
        handle_media(file, folder / 'audios' / 'AMR')

    for file in DOC_DOCUMENT:
        handle_document(file, folder / 'documents' / 'DOC')
    for file in DOCX_DOCUMENT:
        handle_document(file, folder / 'documents' / 'DOCX')
    for file in TXT_DOCUMENT:
        handle_document(file, folder / 'documents' / 'TXT')
    for file in PDF_DOCUMENT:
        handle_document(file, folder / 'documents' / 'PDF')
    for file in XLSX_DOCUMENT:
        handle_document(file, folder / 'documents' / 'XLSX')
    for file in PPTX_DOCUMENT:
        handle_document(file, folder / 'documents' / 'PPTX')

    for file in MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')

    for file in ZIP_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'ZIP')
    for file in GZ_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'GZ')
    for file in TAR_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'TAR')

    for folder in FOLDERS[::-1]:
        # Видаляємо пусті папки після сортування
        try:
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')


def start():
    if sys.argv[1]:
        folder_process = Path(sys.argv[1])
        main(folder_process)