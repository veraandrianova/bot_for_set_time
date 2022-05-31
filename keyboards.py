from aiogram import types

menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
change_button = types.KeyboardButton(text='Замена')
change_time_button = types.KeyboardButton(text='Изменение времени смены')
up_date_weekend_button = types.KeyboardButton(text='Установить выходной день')
menu.add(change_button, change_time_button, up_date_weekend_button)


catalog_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
back_button = types.KeyboardButton(text='Назад в меню')
catalog_keyboard.add(back_button)
