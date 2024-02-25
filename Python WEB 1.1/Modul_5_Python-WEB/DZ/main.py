import json
import sys
from datetime import datetime, timedelta

import aiohttp
import asyncio
import platform


class HttpError(Exception):
    pass


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result
                else:
                    raise HttpError(f"Error status: {resp.status} for {url}")
        except (aiohttp.ClientConnectorError, aiohttp.InvalidURL) as err:
            raise HttpError(f"Connection error: {url}", str(err))


async def main(index_day):
    if int(index_day) > 10:  # Якщо введено понад 10 днів
        return await more_one_func(10)
    else:
        return await more_one_func(index_day)


async def more_one_func(index_day_10):
    counter = 0
    result = {}
    result_list = []

    while counter < int(index_day_10):
        try:
            d = datetime.now() - timedelta(days=counter)
            shift = d.strftime("%d.%m.%Y")
            response = await request(
                f"https://api.privatbank.ua/p24api/exchange_rates?date={shift}"
            )
            date = response["date"]
            desired_currencies = ["EUR", "USD"]
            selected_rates = [
                rate
                for rate in response["exchangeRate"]
                if rate["currency"] in desired_currencies
            ]  # Відбираємо з загального реєстру курсу валют курс EUR та USD

            for currency_data in selected_rates:
                currency_code = currency_data["currency"]  # Отримуємо код валюти
                sale_rate = currency_data["saleRate"]  # Отримуємо курс продажу
                purchase_rate = currency_data["purchaseRate"]  # Отримуємо курс купівлі

                # Створюємо словник для валюти з курсами продажу та купівлі
                currency_dict = {"sale": sale_rate, "purchase": purchase_rate}

                # Додаємо валюту до результату
                result.update({currency_code: currency_dict})
            result_list.append({date: result})
            counter += 1
            result = {}

        except HttpError as err:
            print(err)
            return None

    return await appearance(result_list)


# Форма виведення результату
async def appearance(data):
    result = []
    for item in data:
        new_item = {}
        for date, currencies in item.items():
            new_item[date] = currencies
        result.append(new_item)

    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main(sys.argv[1]))
    print(r)
