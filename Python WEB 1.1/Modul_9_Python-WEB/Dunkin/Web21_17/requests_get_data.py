import requests


scrap_url = "https://index.minfin.com.ua/ua/russian-invading/casualties/"



def get_data(url, file_name="data") -> None:
    data = requests.get(url).text

    with open(f"{file_name}.html", "w", encoding="utf-8") as f:
        f.write(data)


if __name__ == "__main__":
    get_data(scrap_url)   