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
                purchase_rate = currency_data[
                    "purchaseRate"
                ]  # Отримуємо курс купівлі
                # Створюємо словник для валюти з курсами продажу та купівлі
                currency_dict = {"sale": sale_rate, "purchase": purchase_rate}
                # Додаємо валюту до результату
                result.update({currency_code: currency_dict})

            result_list.append({date: result})
            return result_list

        except HttpError as err:
            print(err)
            return None