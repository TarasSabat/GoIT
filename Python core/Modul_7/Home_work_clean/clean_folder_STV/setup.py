from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_STV',
    version='0.0.2',
    author='Taras Sabat',
    packages=find_namespace_packages(),
    entry_points={'console_scripts':['clean=clean_folder.clean:start']}
)