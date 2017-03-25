import datetime
import random


HI = ["привет", "здарова", "здравствуйте", "здаров"]

DATA_QUESTION = ["какой сегодня день", "какое сегодня число", ]

TIME_QUESTION = ["какое сейчас время", "сколько времени"]

HI_ANSWERS = ["Привет", "Здравтствуйте", "Здаров"]

TIME_ANSWERS = ["Сейчас ", "Время "]

DATA_ANSWERS = ["Сейчас ", "Сегодня "]

WEEK_DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

MONTHS = ["января", "февраля", "марта", "апреля",
          "мая", "июня", "июля", "августа",
          "сентября", "октября", "ноября", "декабря"]



def asker(expression):

	TIME_ = datetime.datetime.now()
    time = TIME_.strftime("%H:%M:%S")
    weekday = WEEK_DAYS[int(TIME_.strftime("%w"))] + ", "
    mounthday = int(TIME_.strftime("%d")) + " "
    mounth = MONTHS[int(TIME_.strftime("%m"))] + " "
    year = TIME_.strftime("%Y") + " "

    if expression.lower() in HI:
        answer = random.choice(HI_ANSWERS)[0]

    elif expression.lower() in TIME_QUESTION:
        answer = "{0} {1}".format(random.choice(TIME_ANSWERS), time)            

    elif expression.lower() in DATA_QUESTION:
        answer = "{0} {1} {2} {3} года.".format(weekday, mounthday, mounth, year)                                   

    else:
        answer = "Неизвестный вопрос"

    return answer
