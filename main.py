import re
import telebot
from telebot import types
from config import id_chanel, token
bot = telebot.TeleBot(token)

change_list = []
change_time_list = []
up_date_weekend = []

@bot.message_handler(commands=['start'])
def start(message):
    menu = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard=True)
    change_button = types.KeyboardButton(text='Замена')
    change_time_button = types.KeyboardButton(text='Изменение времени смены')
    up_date_weekend_button = types.KeyboardButton(text='Установить выходной день')
    menu.add(change_button, change_time_button,up_date_weekend_button)
    bot.send_message(message.chat.id, 'Выберите параметр!', reply_markup=menu)

@bot.message_handler(func=lambda m: m.text == 'Назад в меню')
def back(message):
    start(message)

@bot.message_handler(func=lambda m: m.text == 'Замена')
def change(message):
    catalog_keyboard = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard=True)
    back_button = types.KeyboardButton(text='Назад в меню')
    catalog_keyboard.add(back_button)
    sent_1 = bot.reply_to(message, 'Пожалуйста, оставьте дату замены. 01.01', reply_markup=catalog_keyboard)
    bot.register_next_step_handler(sent_1, date)
@bot.message_handler(func=lambda m: m.text == 'Назад в меню')
def back(message):
    start(message)

def date(message):
    total = []
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_date = message.text
        for el in message_to_save_date:
            if el.isdigit():
                total.append(el)
        if len(total) == 3:
            total = total[0] + '.' + total[1] + total[2]
            change_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, введите время смены. 10:00-23:00 с указанием часов и минут')
            bot.register_next_step_handler(sent_2, time)
        elif len(total) == 4:
            total = total[0] + total[1] +'.' + total[2] + total[3]
            change_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, введите время смены. 10:00-23:00 с указанием часов и минут')
            bot.register_next_step_handler(sent_2, time)
        else:
            sent_5 = bot.reply_to(message, 'Пожалуйста, введите корректно корректно даты! 01.01')
            bot.register_next_step_handler(sent_5, date)

def time(message):
    total = []
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_time = message.text
        for el in message_to_save_time:
            if el.isdigit():
                total.append(el)
        if len(total) == 3:
            total = total[0] + '-' + total[1] + total[2]
            change_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, свой бейдж сотрудника! 01234')
            bot.register_next_step_handler(sent_2, number_myself)
        elif len(total) == 4:
            total = total[0] + total[1] +'-' + total[2] + total[3]
            change_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, свой бейдж сотрудника! 01234')
            bot.register_next_step_handler(sent_2, number_myself)
        elif len(total) == 8:
            total = total[0] + total[1] + ':' + total[2] + total[3] + '-' + total[4] + total[5] + ':' + total[6] + total[7]
            change_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, свой бейдж сотрудника! 01234')
            bot.register_next_step_handler(sent_2, number_myself)
        else:
            sent_5 = bot.reply_to(message, 'Пожалуйста, введите корректно время! 10:00-23:00')
            bot.register_next_step_handler(sent_5, time)

def number_myself(message):
     if message.text == 'Назад в меню':
        start(message)
     else:
        message_to_save_number = message.text
        if message_to_save_number.isdigit():
            change_list.append(message_to_save_number)
            sent_3 = bot.reply_to(message, 'Пожалуйста, укажите свою Фамилию и Имя! Иванова Анна')
            bot.register_next_step_handler(sent_3, fio_no_work)
        else:
            sent_3 = bot.reply_to(message, 'Пожалуйста, введите корректно табельный номер. 012345')
            bot.register_next_step_handler(sent_3, number_myself)

def fio_no_work(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_fio_no_work = message.text.lower()
        change_list.append(message_to_save_fio_no_work)
        sent_2 = bot.reply_to(message, 'Пожалуйста, бейдж сотрудника, КОТОРЫЙ БУДЕТ РАБОТАТЬ! 012345')
        bot.register_next_step_handler(sent_2, number_to_change)

def number_to_change(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_number_to_change = message.text
        if message_to_save_number_to_change.isdigit():
            change_list.append(message_to_save_number_to_change)
            sent_3 = bot.reply_to(message, 'Пожалуйста, укажите Фамилию и Имя сотрудника, КОТОРЫЙ БУДЕТ РАБОТАТЬ! Иванова Анна')
            bot.register_next_step_handler(sent_3, fio_to_work)
        else:
            sent_3 = bot.reply_to(message, 'Пожалуйста, введите корректно табельный номер, сотрудника КОТОРЫЙ БУДЕТ РАБОТАТЬ. 123456')
            bot.register_next_step_handler(sent_3, number_to_change)

def fio_to_work(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_fio_to_work = message.text.lower()
        change_list.append(message_to_save_fio_to_work)
        sent_3 = bot.reply_to(message, 'Пожалуйста, напишите магазин! Мега Теплый стан')
        bot.register_next_step_handler(sent_3, place)

def place(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_place = message.text
        change_list.append(message_to_save_place)
        bot.send_message(message.chat.id, 'Обращение создано. Статус можно проверить перейдя по ссылке https://t.me/testpython100')
        date = change_list[0]
        time = change_list[1]
        number = change_list[2]
        fio = change_list[3]
        number_work = change_list[4]
        fio_work = change_list[5]
        shop = change_list[6]
        bot.send_message(id_chanel, f'Замена\nДата: {date}\nВремя: {time}\n'
                                          f'Бейдж сотрудника, у которого выходной: {number}\nСотрудник, у которого выходной: {fio}\n'
                                          f'Бейдж сотрудника, у которого выходной: {number_work}\n'
                                          f'Сотрудник, у которого выходной: {fio_work}\nМагазин: {shop}\n')
        start(message)


@bot.message_handler(func=lambda m: m.text == 'Изменение времени смены')
def change(message):
    catalog_keyboard = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard=True)
    back_button = types.KeyboardButton(text='Назад в меню')
    catalog_keyboard.add(back_button)
    sent_1 = bot.reply_to(message, 'Пожалуйста, оставьте дату замены. 01.01', reply_markup=catalog_keyboard)
    bot.register_next_step_handler(sent_1, date_1)

def date_1(message):
    total = []
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_date = message.text
        for el in message_to_save_date:
            if el.isdigit():
                total.append(el)
        if len(total) == 3:
            total = total[0] + '.' + total[1] + total[2]
            change_time_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, введите время смены. 10:00-23:00 с указанием часов и минут')
            bot.register_next_step_handler(sent_2, time_1)
        elif len(total) == 4:
            total = total[0] + total[1] +'.' + total[2] + total[3]
            change_time_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, введите время смены. 10:00-23:00 с указанием часов и минут')
            bot.register_next_step_handler(sent_2, time_1)
        else:
            sent_5 = bot.reply_to(message, 'Пожалуйста, введите корректно корректно даты! 01.01')
            bot.register_next_step_handler(sent_5, date_1)

def time_1(message):
    total = []
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_time = message.text
        for el in message_to_save_time:
            if el.isdigit():
                total.append(el)
        if len(total) == 3:
            total = total[0] + '-' + total[1] + total[2]
            change_time_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, свой бейдж сотрудника! 01234')
            bot.register_next_step_handler(sent_2, number_myself_1)
        elif len(total) == 4:
            total = total[0] + total[1] +'-' + total[2] + total[3]
            change_time_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, свой бейдж сотрудника! 01234')
            bot.register_next_step_handler(sent_2, number_myself_1)
        elif len(total) == 8:
            total = total[0] + total[1] + ':' + total[2] + total[3] + '-' + total[4] + total[5] + ':' + total[6] + total[7]
            change_time_list.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, свой бейдж сотрудника! 01234')
            bot.register_next_step_handler(sent_2, number_myself_1)
        else:
            sent_5 = bot.reply_to(message, 'Пожалуйста, введите корректно время! 10:00-23:00')
            bot.register_next_step_handler(sent_5, time_1)

def number_myself_1(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_number = message.text
        if message_to_save_number.isdigit():
            change_time_list.append(message_to_save_number)
            sent_3 = bot.reply_to(message, 'Пожалуйста, укажите свою Фамилию и Имя! Иванова Анна')
            bot.register_next_step_handler(sent_3, fio_1)
        else:
            sent_3 = bot.reply_to(message, 'Пожалуйста, введите корректно табельный номер. 123456')
            bot.register_next_step_handler(sent_3, number_myself_1)

def fio_1(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_fio_no_work = message.text.lower()
        change_time_list.append(message_to_save_fio_no_work)
        sent_3 = bot.reply_to(message, 'Пожалуйста, напишите магазин! Мега Теплый стан')
        bot.register_next_step_handler(sent_3, place_1)

def place_1(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_place = message.text
        change_time_list.append(message_to_save_place)
        date = change_time_list[0]
        time = change_time_list[1]
        number = change_time_list[2]
        fio = change_time_list[3]
        place = change_time_list[4]
        bot.send_message(message.chat.id, 'Обращение создано. Статус можно проверить перейдя по ссылке https://t.me/testpython100')
        bot.send_message(id_chanel, f'Дата: {date}\nВремя: {time}\nБейдж: {number}\nСотрудник: {fio}\nМагазин: {place}\n')
        # bot.send_message(message.chat.id, f'Дата: {date}\nВремя: {time}\nБейдж: {number}\nСотрудник: {fio}\nМагазин: {place}\n')
        start(message)
@bot.message_handler(func=lambda m: m.text == 'Установить выходной день')
def change(message):
    catalog_keyboard = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard=True)
    back_button = types.KeyboardButton(text='Назад в меню')
    catalog_keyboard.add(back_button)
    sent_1 = bot.reply_to(message, 'Пожалуйста, оставьте дату выходного. 01.01', reply_markup=catalog_keyboard)
    bot.register_next_step_handler(sent_1, date_2)

def date_2(message):
    total = []
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_date = message.text
        for el in message_to_save_date:
            if el.isdigit():
                total.append(el)
        if len(total) == 3:
            total = total[0] + '.' + total[1] + total[2]
            up_date_weekend.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, свой бейдж сотрудника! 123456')
            bot.register_next_step_handler(sent_2, number_myself_2)
        elif len(total) == 4:
            total = total[0] + total[1] +'.' + total[2] + total[3]
            up_date_weekend.append(total)
            sent_2 = bot.reply_to(message, 'Пожалуйста, свой бейдж сотрудника! 123456')
            bot.register_next_step_handler(sent_2, number_myself_2)
        else:
            sent_5 = bot.reply_to(message, 'Пожалуйста, введите корректно корректно даты! 01.01')
            bot.register_next_step_handler(sent_5, date_2)

def number_myself_2(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_number = message.text
        if message_to_save_number.isdigit():
            up_date_weekend.append(message_to_save_number)
            sent_3 = bot.reply_to(message, 'Пожалуйста, укажите свою Фамилию и Имя! Иванова Анна')
            bot.register_next_step_handler(sent_3, fio_2)
        else:
            sent_3 = bot.reply_to(message, 'Пожалуйста, введите корректно табельный номер. 123456')
            bot.register_next_step_handler(sent_3, number_myself_2)

def fio_2(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_fio_no_work = message.text.lower()
        up_date_weekend.append(message_to_save_fio_no_work)
        sent_3 = bot.reply_to(message, 'Пожалуйста, напишите магазин! Мега Теплый Cтан')
        bot.register_next_step_handler(sent_3, place_2)

def place_2(message):
    if message.text == 'Назад в меню':
        start(message)
    else:
        message_to_save_place = message.text
        up_date_weekend.append(message_to_save_place)

        date = up_date_weekend[0]
        number = up_date_weekend[1]
        fio = up_date_weekend[2]
        place = up_date_weekend[3]
        bot.send_message(message.chat.id, 'Обращение создано. Статус можно проверить перейдя по ссылке https://t.me/testpython100')
        bot.send_message(id_chanel, f'Дата: {date}\nБейдж: {number}\nСотрудник: {fio}\nМагазин: {place}\n')
        # bot.send_message(message.chat.id, f'Дата: {date}\nБейдж: {number}\nСотрудник: {fio}\nМагазин: {place}\n')
        start(message)

bot.polling()


