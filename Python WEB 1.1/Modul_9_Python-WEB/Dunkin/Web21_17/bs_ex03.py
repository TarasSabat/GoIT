from bs4 import BeautifulSoup


with open("Березень2024.html", encoding="utf-8") as f:
    data = f.read()
    
soup = BeautifulSoup(data, "lxml")

# print(len(soup.find_all("ul", class_="see-also")))

uls = soup.find_all("ul", class_="see-also")

for li in uls[:1]:
    elements = li.find_all("li", class_="gold")
    raw_item = elements[1]
    raw_div = raw_item.find("div", class_="casualties")
    if raw_div:
        # print(raw_div.prettify())
        for li in raw_div.find_all("li"):
            print(li.text)
            # for i in li.text:
            #     print(f"{i} - {ord(i)}")
    # for element in elements:
    #     print(element.text)
    #     for ch in element.children:
    #         print(ch)

