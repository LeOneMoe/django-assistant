import datetime
import random


HI = ["Привет", "Здарова", "Здравствуйте", "Здаров"]

DATA_QUESTION = ["Какой сегодня день?", "Какое сегодня число?", ]

TIME_QUESTION = ["Какое сейчас время?", "Сколько времени?"]

HI_ANSWERS = ["Привет!", "Здравтствуйте"]

TIME_ANSWERS = ["Сейчас ", "Время "]

DATA_ANSWERS = ["Сейчас ", "Сегодня "]

WEEK_DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

MONTHS = ["января", "февраля", "марта", "апреля",
          "мая", "июня", "июля", "августа",
          "сентября", "октября", "ноября", "декабря"]



def asker(expression):

    time = str(datetime.datetime.now().strftime("%H:%M:%S"))
    weekday = str(WEEK_DAYS[int(datetime.datetime.now().strftime("%w"))]) + ", "
    mounthday = str(int(datetime.datetime.now().strftime("%d"))) + " "
    mounth = str(MONTHS[int(datetime.datetime.now().strftime("%m"))]) + " "
    year = str(int(datetime.datetime.now().strftime("%Y"))) + " "

    if expression in HI:
        answer = random.choice(HI_ANSWERS)
        is_ok = True

    elif expression in TIME_QUESTION:
        answer = random.choice(TIME_ANSWERS) + time
        is_ok = True

    elif expression in DATA_QUESTION:
        answer = weekday + mounthday + mounth + year + "года"
        is_ok = True

    else:
        answer = "Неизвестный вопрос"
        is_ok = True

    return is_ok, answer
