from telebot import TeleBot, types

from config import id_chanel, token
from connector import DiskConnector

bot = TeleBot(token)
test = DiskConnector()


@bot.message_handler(commands=['start'])
def start(message):
    test.change_list_clear()
    menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    change_button = types.KeyboardButton(text='Замена')
    change_time_button = types.KeyboardButton(text='Изменение времени смены')
    up_date_weekend_button = types.KeyboardButton(text='Установить выходной день')
    menu.add(change_button, change_time_button, up_date_weekend_button)
    bot.send_message(message.chat.id, 'Выберите параметр!', reply_markup=menu)


@bot.message_handler(func=lambda m: True)
def change(message):
    if not test.upload_choose(bot, message):
        test.back(bot, message)
        start(message)
    elif test.upload_choose(bot, message):
        upload_result = test.upload_choose(bot, message)
        test.change_list(upload_result)
        catalog_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        back_button = types.KeyboardButton(text='Назад в меню')
        catalog_keyboard.add(back_button)
        sent_1 = bot.reply_to(message, 'Пожалуйста, укажите дату замены: 01.01', reply_markup=catalog_keyboard)
        bot.register_next_step_handler(sent_1, date)


@bot.message_handler(func=lambda m: m.text == 'Назад в меню')
def back(message):
    test.back(bot, message)
    start(message)


def date(message):
    if test.back(bot, message):
        start(message)
    else:
        if test.upload_date(bot, message):
            upload_result = test.upload_date(bot, message)
            test.change_list(upload_result)
            if test.for_change_list_1():
                sent_2 = bot.reply_to(message, 'Пожалуйста, введите время смены с указанием часов и минут: 10:00-23:00')
                bot.register_next_step_handler(sent_2, time)
            else:
                sent_2 = bot.reply_to(message, 'Пожалуйста, укажите свой бейдж сотрудника! 123456')
                bot.register_next_step_handler(sent_2, number_myself)
        else:
            sent_5 = bot.reply_to(message, 'Пожалуйста, введите корректно дату замены! 01.01')
            bot.register_next_step_handler(sent_5, date)


def time(message):
    if test.back(bot, message):
        start(message)
    else:
        if test.upload_time(bot, message):
            upload_result = test.upload_time(bot, message)
            test.change_list(upload_result)
            if test.for_change_list_1():
                sent_2 = bot.reply_to(message, 'Пожалуйста, укажите свой бейдж сотрудника! 01234')
                bot.register_next_step_handler(sent_2, number_myself)
            else:
                sent_2 = bot.reply_to(message, 'Пожалуйста, укажите свою Фамилию и Имя! Иванова Анна')
                bot.register_next_step_handler(sent_2, fio_no_work)

        else:
            sent_5 = bot.reply_to(message, 'Пожалуйста, введите корректно время! 10:00-23:00')
            bot.register_next_step_handler(sent_5, time)


def number_myself(message):
    if test.back(bot, message):
        start(message)
    else:
        if test.upload_number(bot, message):
            upload_result = test.upload_number(bot, message)
            test.change_list(upload_result)
            if test.for_change_list_1():
                sent_3 = bot.reply_to(message, 'Пожалуйста, укажите свою Фамилию и Имя! Иванова Анна')
                bot.register_next_step_handler(sent_3, fio_no_work)
            else:
                sent_2 = bot.reply_to(message, 'Пожалуйста, укажите свою Фамилию и Имя! Иванова Анна')
                bot.register_next_step_handler(sent_2, fio_no_work)

        else:
            sent_3 = bot.reply_to(message, 'Пожалуйста, введите корректно бейдж сотрудника. 012345')
            bot.register_next_step_handler(sent_3, number_myself)


def fio_no_work(message):
    if test.back(bot, message):
        start(message)
    else:
        upload_result = message.text
        test.change_list(upload_result)
        if test.for_change_list_2():
            sent_2 = bot.reply_to(message, 'Пожалуйста, укажите бейдж сотрудника, КОТОРЫЙ БУДЕТ РАБОТАТЬ! 012345')
            bot.register_next_step_handler(sent_2, number_to_change)
        else:
            sent_2 = bot.reply_to(message, 'Пожалуйста, укажите магазин! Мега Теплый стан')
            bot.register_next_step_handler(sent_2, place)


def number_to_change(message):
    if test.back(bot, message):
        start(message)
    else:
        if test.upload_number(bot, message):
            upload_result = test.upload_number(bot, message)
            test.change_list(upload_result)
            sent_3 = bot.reply_to(message,
                                  'Пожалуйста, укажите Фамилию и Имя сотрудника, КОТОРЫЙ БУДЕТ РАБОТАТЬ! Иванова Анна')
            bot.register_next_step_handler(sent_3, fio_to_work)
        else:
            sent_3 = bot.reply_to(message,
                                  'Пожалуйста, введите корректно бейдж сотрудника, КОТОРЫЙ БУДЕТ РАБОТАТЬ. 123456')
            bot.register_next_step_handler(sent_3, number_to_change)


def fio_to_work(message):
    if test.back(bot, message):
        start(message)
    else:
        upload_result = message.text
        test.change_list(upload_result)
        sent_3 = bot.reply_to(message, 'Пожалуйста, укажите магазин! Мега Теплый стан')
        bot.register_next_step_handler(sent_3, place)


def place(message):
    if test.back(bot, message):
        start(message)
    else:
        upload_result = message.text
        test.change_list(upload_result)
        sent_3 = bot.reply_to(message, 'Пожалуйста, укажите комментарий к изменениям в графике, если комментариев нет - напишите "нет"')
        bot.register_next_step_handler(sent_3, comments)

def comments(message):
    if test.back(bot, message):
        start(message)
    else:
        upload_result = message.text
        change_list_view = test.change_list(upload_result)
        bot.send_message(message.chat.id,
                         'Обращение создано. Статус можно проверить перейдя по ссылке https://t.me/testpython100')
        if test.to_send_message(change_list_view):
            send = test.to_send_message(change_list_view)
            bot.send_message(id_chanel, send)
        test.change_list_clear()
        start(message)

if __name__ == '__main__':
    bot.polling(none_stop=True)
