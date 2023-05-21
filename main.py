import telebot
import requests
import psycopg2
from datetime import datetime
from telebot import types

conn = psycopg2.connect(
    database='Raspisanie',
    user='postgres',
    password='Dan12345',
    host='localhost',
    port='5432'
)

cursor = conn.cursor()


token = "6159349051:AAFb1mc6BYX9wuDZgBB_rWbxmT1GHNLmmsE"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?' '\r\n'
                                      '\r\n"Напишите "Хочу", если Вам жизнь недорога))"')
    bot.send_message(message.chat.id, '* Если Вы хотите узнать расписание, то напишите "Расписание"')
    bot.send_message(message.chat.id, '* Если Вы хотите узнать, что я могу вытворить, то используйте команду /help')


@bot.message_handler(commands=['help'])
def help1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Обо Мне")
    item2 = types.KeyboardButton("Моя Любимая Музыка")
    item3 = types.KeyboardButton("Любимая Игра")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id, 'Я ничо не маагуу （πーπ）' '\r\n'
                                      '\r\nМой создатель дал мне только три кнопки с командами, если он с вами, то дайте ему подзатыльник, но небольно конечно :3'
                                      '\r\n'
                                      '\r\nВыберите команду',
                                      reply_markup = markup)


@bot.message_handler(commands=['mtuci'])
def week(message):
    bot.send_message(message.chat.id, "Всю информацию об институте Вы сможете найти здесь: https://mtuci.ru/")


@bot.message_handler(commands=['week'])
def week_raspisanie(message):
    current_date = datetime.now()
    day = current_date.day
    month = current_date.month

    a = ['Января', 'Февраля', 'Марта', 'Апреля', 'Майя', 'Июнь', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября',
         'Декабря']
    realmonth = a[month - 1]

    if month == 1:
        if 2 <= day <= 8 or 16 <= day <= 22 or 30 <= day <= 31:
            itog = 0
        if 1 == day or 9 <= day <= 15 or 23 <= day <= 29:
            itog = 1

    if month == 2:
        if 1 <= day <= 5 or 13 <= day <= 19 or 27 <= day <= 28:
            itog = 0
        if 6 <= day <= 12 or 20 <= day <= 26:
            itog = 1

    if month == 3:
        if 1 <= day <= 5 or 13 <= day <= 19 or 27 <= day <= 31:
            itog = 0
        if 6 <= day <= 12 or 20 <= day <= 26:
            itog = 1

    if month == 4:
        if 1 <= day <= 2 or 10 <= day <= 16 or 24 <= day <= 30:
            itog = 0
        if 3 <= day <= 9 or 17 <= day <= 23:
            itog = 1

    if month == 5:
        if 8 <= day <= 14 or 22 <= day <= 28:
            itog = 0
        if 1 <= day <= 7 or 15 <= day <= 21 or 29 <= day <= 31:
            itog = 1

    if month == 6:
        if 5 <= day <= 11 or 19 <= day <= 25:
            itog = 0
        if 1 <= day <= 4 or 12 <= day <= 18 or 26 <= day <= 30:
            itog = 1

    if month == 7:
        if 2 < day:
            bot.send_message(message.chat.id, "Сегодня:" + "  " + str(day) + "  " + realmonth)
            bot.send_message(message.chat.id, "УРААААА! КАНИКУЛЫ :D")
        if 1 <= day <= 2:
            itog = 1

    if month == 8:
        bot.send_message(message.chat.id, "Сегодня:" + "  " + str(day) + "  " + realmonth)
        bot.send_message(message.chat.id, "УРААААА! КАНИКУЛЫ :D")

    if month == 9:
        if 1 <= day <= 4 or 12 <= day <= 18 or 26 <= day <= 30:
            itog = 0
        if 5 <= day <= 11 or 19 <= day <= 25:
            itog = 1

    if month == 10:
        if 1 <= day <= 2 or 10 <= day <= 16 or 24 <= day <= 30:
            itog = 0
        if 3 <= day <= 9 or 17 <= day <= 23 or day == 31:
            itog = 1

    if month == 11:
        if 7 <= day <= 13 or 21 <= day <= 27:
            itog = 0
        if 1 <= day <= 6 or 14 <= day <= 20 or 28 <= day <= 30:
            itog = 1

    if month == 12:
        if 5 <= day <= 11 or 19 <= day <= 25:
            itog = 0
        if 1 <= day <= 4 or 12 <= day <= 18 or 26 <= day <= 31:
            itog = 1


    if itog == 0:
        bot.send_message(message.chat.id, "Сегодня:" + "  " + str(day) + "  " + realmonth)
        bot.send_message(message.chat.id, "Сейчас Нечетная неделя")
    if itog == 1:
        bot.send_message(message.chat.id, "Сегодня:" + "  " + str(day) + "  " + realmonth)
        bot.send_message(message.chat.id, "Сейчас Четная неделя")

    if message.text == "Расписание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Расписание на текущую неделю")
        item2 = types.KeyboardButton("Расписание на следующую неделю")
        markup.add(item1)
        markup.add(item2)

        if message.text == "Расписание на текущую неделю":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Понедельник")
            item2 = types.KeyboardButton("Вторник")
            item3 = types.KeyboardButton("Среда")
            item4 = types.KeyboardButton("Четверг")
            item5 = types.KeyboardButton("Пятница")
            item6 = types.KeyboardButton("Суббота")
            item7 = types.KeyboardButton("Воскресенье")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            markup.add(item5)
            markup.add(item6)
            markup.add(item7)

            bot.send_message(message.chat.id, "Выберите расписание дня, который Вас интересует :)", reply_markup=markup)

            if itog == 0:
                id_week_thistime = str(2)
                cursor.execute("select * from raspisanie_week where id_week = " + " " + id_week_thistime + " " + ";")
                record = list(cursor.fetchall())

                limit = len(record)

                if 1 <= limit:
                    bot.send_message(message.chat.id, "<" + str(record[0][3]) + ">" + " " + "<" + str(
                        record[0][4]) + ">" + " " + "<" + str(record[0][5]) + ">" + " " + "<" + str(record[0][6]) + ">")
                if 2 <= limit:
                    bot.send_message(message.chat.id, "<" + str(record[1][3]) + ">" + " " + "<" + str(
                        record[1][4]) + ">" + " " + "<" + str(record[1][5]) + ">" + " " + "<" + str(record[1][6]) + ">")
                if 3 <= limit:
                    bot.send_message(message.chat.id, "<" + str(record[2][3]) + ">" + " " + "<" + str(
                        record[2][4]) + ">" + " " + "<" + str(record[2][5]) + ">" + " " + "<" + str(record[2][6]) + ">")
                if 4 <= limit:
                    bot.send_message(message.chat.id, "<" + str(record[3][3]) + ">" + " " + "<" + str(
                        record[3][4]) + ">" + " " + "<" + str(record[3][5]) + ">" + " " + "<" + str(record[3][6]) + ">")
                else:
                    bot.send_message(message.chat.id, "Вам интересно узнать расписание на другие дни? :3" "\r\n"
                                                      "\r\nЕсли да, то Вы можете выбрать другой день недели")

            if itog == 1:
                id_week_thistime = str(1)
                cursor.execute("select * from raspisanie_week where id_week = " + " " + id_week_thistime + " " + ";")
                record = list(cursor.fetchall())

                limit = len(record)

                if 1 <= limit:
                    bot.send_message(message.chat.id, "<" + str(record[0][3]) + ">" + " " + "<" + str(
                        record[0][4]) + ">" + " " + "<" + str(record[0][5]) + ">" + " " + "<" + str(record[0][6]) + ">")
                if 2 <= limit:
                    bot.send_message(message.chat.id, "<" + str(record[1][3]) + ">" + " " + "<" + str(
                        record[1][4]) + ">" + " " + "<" + str(record[1][5]) + ">" + " " + "<" + str(record[1][6]) + ">")
                if 3 <= limit:
                    bot.send_message(message.chat.id, "<" + str(record[2][3]) + ">" + " " + "<" + str(
                        record[2][4]) + ">" + " " + "<" + str(record[2][5]) + ">" + " " + "<" + str(record[2][6]) + ">")
                if 4 <= limit:
                    bot.send_message(message.chat.id, "<" + str(record[3][3]) + ">" + " " + "<" + str(
                        record[3][4]) + ">" + " " + "<" + str(record[3][5]) + ">" + " " + "<" + str(record[3][6]) + ">")
                else:
                    bot.send_message(message.chat.id, "Вам интересно узнать расписание на другие дни? :3" "\r\n"
                                                      "\r\nЕсли да, то Вы можете выбрать другой день недели")


@bot.message_handler(content_types='text')
def message_reply(message):

    if message.text == "Хочу" or message.text == "хочу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Авиамоторная")
        item2 = types.KeyboardButton("Октябрьское поле")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, "Вся информация хранится здесь: https://mtuci.ru/")
        bot.send_message(message.chat.id, "На данный момент у МТУСИ существуют два корпуса."
                                          "\r\nВыберите, какой Вас интересует.", reply_markup = markup)
        bot.send_message(message.chat.id, "Если Вы хотите узнать, что я могу вытворить, то воспользуйтесь командой /help")

    elif message.text == "Расписание" or message.text == "расписание":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Расписание на текущую неделю")
        item2 = types.KeyboardButton("Расписание на следующую неделю")
        markup.add(item1)
        markup.add(item2)

        bot.send_message(message.chat.id, "Выберите неделю, которая Вас интересует.", reply_markup=markup)

    elif message.text == "Расписание на текущую неделю":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Т--""Понедельник")
        item2 = types.KeyboardButton("Т--""Вторник")
        item3 = types.KeyboardButton("Т--""Среда")
        item4 = types.KeyboardButton("Т--""Четверг")
        item5 = types.KeyboardButton("Т--""Пятница")
        item6 = types.KeyboardButton("Т--""Суббота")
        item7 = types.KeyboardButton("Т--""Воскресенье")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)

        bot.send_message(message.chat.id, "Выберите расписание дня, который Вас интересует :)", reply_markup = markup)


    elif message.text == "Т--""Понедельник" or message.text == "Т--""Вторник" or message.text == "Т--""Среда" or message.text == "Т--""Четверг" or message.text == "Т--""Пятница" or message.text == "Т--""Суббота" or message.text == "Т--""Воскресенье":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Т--""Понедельник")
        item2 = types.KeyboardButton("Т--""Вторник")
        item3 = types.KeyboardButton("Т--""Среда")
        item4 = types.KeyboardButton("Т--""Четверг")
        item5 = types.KeyboardButton("Т--""Пятница")
        item6 = types.KeyboardButton("Т--""Суббота")
        item7 = types.KeyboardButton("Т--""Воскресенье")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)

        if message.text == "Т--""Среда" or message.text == "Т--""Пятница" or message.text == "Т--""Суббота":
            s = message.text
            d = len(s)
            s_i = s.replace('а', 'у')
            s_itog = s_i[3:d]
            bot.send_message(message.chat.id, "Вот расписание на" + " " + s_itog + " " + "текущей недели" + "   👇(._.)", reply_markup = markup)
        else:
            s = message.text
            d = len(s)
            s_itog = s[3:d]
            bot.send_message(message.chat.id, "Вот расписание на" + " " + s_itog + " " + "текущей недели" + "   👇(._.)", reply_markup = markup)

        current_date = datetime.now()
        day = current_date.day
        month = current_date.month

        if month == 1:
            if 2 <= day <= 8 or 16 <= day <= 22 or 30 <= day <= 31:
                itog = 0
            if 1 == day or 9 <= day <= 15 or 23 <= day <= 29:
                itog = 1

        if month == 2:
            if 1 <= day <= 5 or 13 <= day <= 19 or 27 <= day <= 28:
                itog = 0
            if 6 <= day <= 12 or 20 <= day <= 26:
                itog = 1

        if month == 3:
            if 1 <= day <= 5 or 13 <= day <= 19 or 27 <= day <= 31:
                itog = 0
            if 6 <= day <= 12 or 20 <= day <= 26:
                itog = 1

        if month == 4:
            if 1 <= day <= 2 or 10 <= day <= 16 or 24 <= day <= 30:
                itog = 0
            if 3 <= day <= 9 or 17 <= day <= 23:
                itog = 1

        if month == 5:
            if 8 <= day <= 14 or 22 <= day <= 28:
                itog = 0
            if 1 <= day <= 7 or 15 <= day <= 21 or 29 <= day <= 31:
                itog = 1

        if month == 6:
            if 5 <= day <= 11 or 19 <= day <= 25:
                itog = 0
            if 1 <= day <= 4 or 12 <= day <= 18 or 26 <= day <= 30:
                itog = 1

        if month == 7:
            if 2 < day:
                bot.send_message(message.chat.id, "УРААААА! КАНИКУЛЫ :D")
            if 1 <= day <= 2:
                itog = 1

        if month == 8:
            bot.send_message(message.chat.id, "УРААААА! КАНИКУЛЫ :D")

        if month == 9:
            if 1 <= day <= 4 or 12 <= day <= 18 or 26 <= day <= 30:
                itog = 0
            if 5 <= day <= 11 or 19 <= day <= 25:
                itog = 1

        if month == 10:
            if 1 <= day <= 2 or 10 <= day <= 16 or 24 <= day <= 30:
                itog = 0
            if 3 <= day <= 9 or 17 <= day <= 23 or day == 31:
                itog = 1

        if month == 11:
            if 7 <= day <= 13 or 21 <= day <= 27:
                itog = 0
            if 1 <= day <= 6 or 14 <= day <= 20 or 28 <= day <= 30:
                itog = 1

        if month == 12:
            if 5 <= day <= 11 or 19 <= day <= 25:
                itog = 0
            if 1 <= day <= 4 or 12 <= day <= 18 or 26 <= day <= 31:
                itog = 1

        if itog == 0:
            s = message.text
            d = len(s)
            s_itog = s[3:d]

            week = str(2)
            info = "'" + s_itog + "'"

            cursor.execute("select * from raspisanie_week where id_week = " + " " + week + " " + "and dayl = " + " " + info + " "  + ";")
            record = list(cursor.fetchall())

            limit = len(record)

            if 1 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[0][3]) + ">" + " " + "<" + str(record[0][4]) + ">" + " " + "<" + str(record[0][5]) + ">" + " " + "<" + str(record[0][6]) + ">")
            if 2 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[1][3]) + ">" + " " + "<" + str(record[1][4]) + ">" + " " + "<" + str(record[1][5]) + ">" + " " + "<" + str(record[1][6]) + ">")
            if 3 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[2][3]) + ">" + " " + "<" + str(record[2][4]) + ">" + " " + "<" + str(record[2][5]) + ">" + " " + "<" + str(record[2][6]) + ">")
            if 4 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[3][3]) + ">" + " " + "<" + str(record[3][4]) + ">" + " " + "<" + str(record[3][5]) + ">" + " " + "<" + str(record[3][6]) + ">")
            if 5 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[4][3]) + ">" + " " + "<" + str(record[4][4]) + ">" + " " + "<" + str(record[4][5]) + ">" + " " + "<" + str(record[4][6]) + ">")
            else:
                bot.send_message(message.chat.id, "Вам интересно узнать расписание на другие дни? :3" "\r\n"
                                                  "\r\nЕсли да, то Вы можете выбрать другой день недели")

        if itog == 1:
            s = message.text
            d = len(s)
            s_itog = s[3:d]

            week = str(1)
            info = "'" + s_itog + "'"

            cursor.execute("select * from raspisanie_week where id_week = " + " " + week + " " + "and dayl = " + " " + info + " " + ";")
            record = list(cursor.fetchall())

            limit = len(record)

            if 1 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[0][3]) + ">" + " " + "<" + str(record[0][4]) + ">" + " " + "<" + str(record[0][5]) + ">" + " " + "<" + str(record[0][6]) + ">")
            if 2 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[1][3]) + ">" + " " + "<" + str(record[1][4]) + ">" + " " + "<" + str(record[1][5]) + ">" + " " + "<" + str(record[1][6]) + ">")
            if 3 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[2][3]) + ">" + " " + "<" + str(record[2][4]) + ">" + " " + "<" + str(record[2][5]) + ">" + " " + "<" + str(record[2][6]) + ">")
            if 4 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[3][3]) + ">" + " " + "<" + str(record[3][4]) + ">" + " " + "<" + str(record[3][5]) + ">" + " " + "<" + str(record[3][6]) + ">")
            if 5 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[4][3]) + ">" + " " + "<" + str(record[4][4]) + ">" + " " + "<" + str(record[4][5]) + ">" + " " + "<" + str(record[4][6]) + ">")
            else:
                bot.send_message(message.chat.id, "Вам интересно узнать расписание на другие дни? :3" "\r\n"
                                                  "\r\nЕсли да, то Вы можете выбрать другой день недели")

    elif message.text == "Расписание на следующую неделю":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("С--""Понедельник")
        item2 = types.KeyboardButton("С--""Вторник")
        item3 = types.KeyboardButton("С--""Среда")
        item4 = types.KeyboardButton("С--""Четверг")
        item5 = types.KeyboardButton("С--""Пятница")
        item6 = types.KeyboardButton("С--""Суббота")
        item7 = types.KeyboardButton("С--""Воскресенье")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)

        bot.send_message(message.chat.id, "Выберите расписание дня, который Вас интересует :)", reply_markup=markup)

    elif message.text == "С--""Понедельник" or message.text == "С--""Вторник" or message.text == "С--""Среда" or message.text == "С--""Четверг" or message.text == "С--""Пятница" or message.text == "С--""Суббота" or message.text == "С--""Воскресенье":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("С--""Понедельник")
        item2 = types.KeyboardButton("С--""Вторник")
        item3 = types.KeyboardButton("С--""Среда")
        item4 = types.KeyboardButton("С--""Четверг")
        item5 = types.KeyboardButton("С--""Пятница")
        item6 = types.KeyboardButton("С--""Суббота")
        item7 = types.KeyboardButton("С--""Воскресенье")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)

        if message.text == "С--""Среда" or message.text == "С--""Пятница" or message.text == "С--""Суббота":
            s = message.text
            d = len(s)
            s_i = s.replace('а', 'у')
            s_itog = s_i[3:d]
            bot.send_message(message.chat.id, "Вот расписание на" + " " + s_itog + " " + "следующей недели" + "  👇(._.)", reply_markup=markup)
        else:
            s = message.text
            d = len(s)
            s_itog = s[3:d]
            bot.send_message(message.chat.id, "Вот расписание на" + " " + s_itog + " " + "следующей недели" + " 👇(._.)", reply_markup=markup)

        current_date = datetime.now()
        day = current_date.day
        month = current_date.month

        if month == 1:
            if 2 <= day <= 8 or 16 <= day <= 22 or 30 <= day <= 31:
                itog = 0
            if 1 == day or 9 <= day <= 15 or 23 <= day <= 29:
                itog = 1

        if month == 2:
            if 1 <= day <= 5 or 13 <= day <= 19 or 27 <= day <= 28:
                itog = 0
            if 6 <= day <= 12 or 20 <= day <= 26:
                itog = 1

        if month == 3:
            if 1 <= day <= 5 or 13 <= day <= 19 or 27 <= day <= 31:
                itog = 0
            if 6 <= day <= 12 or 20 <= day <= 26:
                itog = 1

        if month == 4:
            if 1 <= day <= 2 or 10 <= day <= 16 or 24 <= day <= 30:
                itog = 0
            if 3 <= day <= 9 or 17 <= day <= 23:
                itog = 1

        if month == 5:
            if 8 <= day <= 14 or 22 <= day <= 28:
                itog = 0
            if 1 <= day <= 7 or 15 <= day <= 21 or 29 <= day <= 31:
                itog = 1

        if month == 6:
            if 5 <= day <= 11 or 19 <= day <= 25:
                itog = 0
            if 1 <= day <= 4 or 12 <= day <= 18 or 26 <= day <= 30:
                itog = 1

        if month == 7:
            if 2 < day:
                bot.send_message(message.chat.id, "УРААААА! КАНИКУЛЫ :D")
            if 1 <= day <= 2:
                itog = 1

        if month == 8:
            bot.send_message(message.chat.id, "УРААААА! КАНИКУЛЫ :D")

        if month == 9:
            if 1 <= day <= 4 or 12 <= day <= 18 or 26 <= day <= 30:
                itog = 0
            if 5 <= day <= 11 or 19 <= day <= 25:
                itog = 1

        if month == 10:
            if 1 <= day <= 2 or 10 <= day <= 16 or 24 <= day <= 30:
                itog = 0
            if 3 <= day <= 9 or 17 <= day <= 23 or day == 31:
                itog = 1

        if month == 11:
            if 7 <= day <= 13 or 21 <= day <= 27:
                itog = 0
            if 1 <= day <= 6 or 14 <= day <= 20 or 28 <= day <= 30:
                itog = 1

        if month == 12:
            if 5 <= day <= 11 or 19 <= day <= 25:
                itog = 0
            if 1 <= day <= 4 or 12 <= day <= 18 or 26 <= day <= 31:
                itog = 1

        if itog == 0:
            s = message.text
            d = len(s)
            s_itog = s[3:d]

            week = str(1)
            info = "'" + s_itog + "'"

            cursor.execute(
                "select * from raspisanie_week where id_week = " + " " + week + " " + "and dayl = " + " " + info + " " + ";")
            record = list(cursor.fetchall())

            limit = len(record)

            if 1 <= limit:
                bot.send_message(message.chat.id,"<" + str(record[0][3]) + ">" + " " + "<" + str(record[0][4]) + ">" + " " + "<" + str(record[0][5]) + ">" + " " + "<" + str(record[0][6]) + ">")
            if 2 <= limit:
                bot.send_message(message.chat.id,"<" + str(record[1][3]) + ">" + " " + "<" + str(record[1][4]) + ">" + " " + "<" + str(record[1][5]) + ">" + " " + "<" + str(record[1][6]) + ">")
            if 3 <= limit:
                bot.send_message(message.chat.id,"<" + str(record[2][3]) + ">" + " " + "<" + str(record[2][4]) + ">" + " " + "<" + str(record[2][5]) + ">" + " " + "<" + str(record[2][6]) + ">")
            if 4 <= limit:
                bot.send_message(message.chat.id,"<" + str(record[3][3]) + ">" + " " + "<" + str(record[3][4]) + ">" + " " + "<" + str(record[3][5]) + ">" + " " + "<" + str(record[3][6]) + ">")
            if 5 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[4][3]) + ">" + " " + "<" + str(record[4][4]) + ">" + " " + "<" + str(record[4][5]) + ">" + " " + "<" + str(record[4][6]) + ">")
            else:
                bot.send_message(message.chat.id, "Вам интересно узнать расписание на другие дни? :3" "\r\n"
                                                  "\r\nЕсли да, то Вы можете выбрать другой день недели")

        if itog == 1:
            s = message.text
            d = len(s)
            s_itog = s[3:d]

            week = str(2)
            info = "'" + s_itog + "'"

            cursor.execute(
                "select * from raspisanie_week where id_week = " + " " + week + " " + "and dayl = " + " " + info + " " + ";")
            record = list(cursor.fetchall())

            limit = len(record)

            if 1 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[0][3]) + ">" + " " + "<" + str(record[0][4]) + ">" + " " + "<" + str(record[0][5]) + ">" + " " + "<" + str(record[0][6]) + ">")
            if 2 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[1][3]) + ">" + " " + "<" + str(record[1][4]) + ">" + " " + "<" + str(record[1][5]) + ">" + " " + "<" + str(record[1][6]) + ">")
            if 3 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[2][3]) + ">" + " " + "<" + str(record[2][4]) + ">" + " " + "<" + str(record[2][5]) + ">" + " " + "<" + str(record[2][6]) + ">")
            if 4 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[3][3]) + ">" + " " + "<" + str(record[3][4]) + ">" + " " + "<" + str(record[3][5]) + ">" + " " + "<" + str(record[3][6]) + ">")
            if 5 <= limit:
                bot.send_message(message.chat.id, "<" + str(record[4][3]) + ">" + " " + "<" + str(record[4][4]) + ">" + " " + "<" + str(record[4][5]) + ">" + " " + "<" + str(record[4][6]) + ">")
            else:
                bot.send_message(message.chat.id, "Вам интересно узнать расписание на другие дни? :3" "\r\n"
                                                  "\r\nЕсли да, то Вы можете выбрать другой день недели")



    elif message.text == "Авиамоторная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Октябрьское поле")
        markup.add(item1)

        m = requests.get('https://textarchive.ru/images/1049/2096106/m289c6b31.png')
        url = m.url
        bot.send_message(message.chat.id, "Вот местоположение Великого Института:)" "\r\n"
                                          "\r\n(Точное местоположение ГЛАВНОГО корпуса)")
        bot.send_photo(message.chat.id, url)
        bot.send_message(message.chat.id, "\r\nВыберите 'Октябрьское поле', если хотите узнать местоположение второго корпуса.",
                         reply_markup = markup)

    elif message.text == "Октябрьское поле":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Авиамоторная")
        markup.add(item1)

        m = requests.get('http://tatuage.org/wp-content/uploads/2014/06/1231.jpg')
        url = m.url
        bot.send_message(message.chat.id, "Вот местоположение Великого Института:)" "\r\n"
                                          "\r\n(Точное местоположение ВТОРОГО корпуса)")
        bot.send_photo(message.chat.id, url)
        bot.send_message(message.chat.id, "\r\nВыберите 'Октябрьское поле', если хотите узнать местоположение главного корпуса.",
                         reply_markup = markup)

    elif message.text == "Обо Мне":
        bot.send_message(message.chat.id, "Я - бот, хранящий информацию о МТУСИ, которого создали для выполнения лабораторной работы" "\r\n"
                                          "\r\nУ меня имеется несколько команд:"
                                          "\r\n1)  /help  --  эта команда нужна для того, чтобы Вы смогли разобраться в том, как со мной работать."
                                          "\r\n2)  /week  --  эта комнада покажет Вам, какая сейчас неделя."
                                          "\r\n3)  /mtuci  --  эта команда позволит вам более детально разобраться в вопросах, касающихся института 'МТУСИ'." "\r\n"
                                          "\r\n4)  /start  --  если Вы захотите вернуться к началу, то этот вариант как никогда вам пригодится))")

    elif message.text == "Моя Любимая Музыка":
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    elif message.text == "Любимая Игра":
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=VTzHj-R9McA&t=107s")
        bot.send_message(message.chat.id, "Обожаю играть в Тундру, кстати, она сделана Русскими Программистами)")

    elif message.text == "Спасибо, Товарищ":
        bot.send_message(message.chat.id, "☭  СЛУЖУ СОВЕСТСКОМУ СОЮЗУ!!!  ☭")

    else:
        bot.send_message(message.chat.id, "Извините, я Вас не совсем понял :(")
        bot.send_message(message.chat.id, "Вы можете узнать, что я могу, воспользовавшись командой /help")


bot.infinity_polling()