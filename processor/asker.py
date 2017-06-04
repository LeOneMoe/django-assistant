import datetime
import random


HI = ["привет", "здарова", "здравствуйте", "здаров"]

DATA_QUESTION = ["какой сегодня день", "какое сегодня число", ]

TIME_QUESTION = ["какое сейчас время", "сколько времени"]

HI_ANSWERS = ["Привет!", "Здравтствуйте!"]

TIME_ANSWERS = ["Сейчас ", "Время "]

DATA_ANSWERS = ["Сейчас ", "Сегодня "]

WEEK_DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

MONTHS = ["января", "февраля", "марта", "апреля",
          "мая", "июня", "июля", "августа",
          "сентября", "октября", "ноября", "декабря"]



def asker(user_says):

    time = str(datetime.datetime.now().strftime("%H:%M:%S"))
    weekday = str(WEEK_DAYS[int(datetime.datetime.now().strftime("%w"))]) + ", "
    monthday = str(int(datetime.datetime.now().strftime("%d"))) + " "
    month = str(MONTHS[int(datetime.datetime.now().strftime("%m"))]) + " "
    year = str(int(datetime.datetime.now().strftime("%Y"))) + " "

    if user_says.lower() in HI:
        answer = random.choice(HI_ANSWERS)

    elif user_says.lower() in TIME_QUESTION:
        answer = random.choice(TIME_ANSWERS) + time

    elif user_says.lower() in DATA_QUESTION:
        answer = weekday + monthday + month + year + "года"

    else:
        answer = "Я не понимаю, может потому что я тупой или мой создатель"

    return answer
