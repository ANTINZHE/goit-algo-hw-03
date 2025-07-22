from datetime import datetime

# Функція отримання різниці між заданою і поточною датою
def get_days_from_today(date: str) -> int:
    today = datetime.today()
    try:
        formatted_date = datetime.strptime(date, '%Y-%m-%d') 
        target_days = (today - formatted_date).days

        return target_days

    except ValueError:
        print("Невірний формат дати. Спробуйте за цим шаблоном - 'РРРР-ММ-ДД'")


print(get_days_from_today("2025-07-"))