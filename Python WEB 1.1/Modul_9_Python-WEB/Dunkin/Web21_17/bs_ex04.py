from bs4 import BeautifulSoup

from requests_get_data import get_data

start_url = "https://index.minfin.com.ua/ua/"

with open("data.html", encoding="utf-8") as f:
    data = f.read()
    
soup = BeautifulSoup(data, "lxml")

refs = soup.find_all("div", class_="ajaxmonth")

print(len(refs))
for ref in refs[:2]:
    link = ref.find("a")
    full_url = start_url + link.get("href")
    file_name = link.text.replace(" ", "")
    print(full_url, file_name)
    # get_data(full_url, file_name)
