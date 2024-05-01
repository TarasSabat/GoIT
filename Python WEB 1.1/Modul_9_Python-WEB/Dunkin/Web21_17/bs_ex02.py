from bs4 import BeautifulSoup
from pprint import pprint as print


with open("simple.xml") as file:
    data = file.read()
    
soup = BeautifulSoup(data, "xml")

foods = soup.find_all("food")

result = []
fields_names = ["name", "price", "description", "calories"]
for food in foods:
    # print(food.get_text())
    food_dict = {}
    for field in fields_names:
        food_dict[field] = food.find(field).text
        # print(f"{field = } {food.find(field).text}")
    result.append(food_dict)

print(result, sort_dicts=False)