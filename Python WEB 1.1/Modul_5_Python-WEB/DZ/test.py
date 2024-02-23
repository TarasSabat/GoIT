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
    # Якщо введено поточний день (1)
    if int(index_day) == 1:
        return await one_func(index_day)

    # Якщо введено 2-10 днів
    if 1 < int(index_day) <= 10:
        return await more_one_func(index_day)

    # Якщо введено більше 10 днів
    if int(index_day) > 10:
        index_day = 10
        return await more_one_func(index_day)


async def one_func(index_day_1):
    result = {}
    result_list = []
    if int(index_day_1) == 1:
        try:
            shift = datetime.now().strftime("%d.%m.%Y")
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
            return result_list

        except HttpError as err:
            print(err)
            return None


async def more_one_func(index_day_10):
    counter = 0  # int(index_day)
    result = {}
    result_list = []

    while counter < int(index_day_10):
        print(counter, "--1")
        try:
            d = datetime.now() - timedelta(days=counter)
            shift = d.strftime("%d.%m.%Y")
            print(shift)
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

        except HttpError as err:
            print(err)
            return None

    return result_list


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # print(sys.argv)
    r = asyncio.run(main(sys.argv[1]))
    print(r)
