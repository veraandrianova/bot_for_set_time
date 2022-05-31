import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from user import UserState
import keyboards as kb
from config import id_chanel, token
from loader import bot, dp, test, storage
from messages import MESSAGES

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(MESSAGES['start'], reply_markup=kb.menu)

@dp.message_handler()
async def client_choose(message: types.Message):
    if message.text == 'Замена':
        await message.answer(MESSAGES['choose_day_change'], reply_markup=kb.catalog_keyboard)
        await UserState.date_to_change.set()
    elif message.text == 'Изменение времени смены':
        catalog_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        back_button = types.KeyboardButton(text='Назад в меню')
        catalog_keyboard.add(back_button)
        await message.answer(MESSAGES['choose_day_change'], reply_markup=kb.catalog_keyboard)
        await UserState.date_to_change_time.set()
    elif message.text == 'Установить выходной день':
        catalog_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        back_button = types.KeyboardButton(text='Назад в меню')
        catalog_keyboard.add(back_button)
        await message.answer(MESSAGES['choose_day_change'], reply_markup=kb.catalog_keyboard)
        await UserState.date_to_day_off.set()


@dp.message_handler(state=UserState.date_to_change)
async def get_date(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    elif test.upload_date(bot, message):
        upload_result = test.upload_date(bot, message)
        await state.update_data(date_to_change=upload_result)
        await message.answer(MESSAGES['choose_time_change'])
        await UserState.time_to_change.set()
    else:
        await message.answer(MESSAGES['choose_day_change_correct'])
        await UserState.date_to_change.set()


@dp.message_handler(state=UserState.time_to_change)
async def get_time(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    elif test.upload_time(bot, message):
        upload_result = test.upload_time(bot, message)
        await state.update_data(time_to_change=upload_result)
        await message.answer(MESSAGES['choose_number_change'])
        await UserState.number_to_change.set()
    else:
        await message.answer(MESSAGES['choose_time_change'])
        await UserState.time_to_change.set()


@dp.message_handler(state=UserState.number_to_change)
async def get_number(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    elif test.upload_number(bot, message):
        upload_result = test.upload_number(bot, message)
        await state.update_data(number_to_change=upload_result)
        await message.answer(MESSAGES['choose_fio_change'])
        await UserState.fio_to_change.set()
    else:
        await message.answer(MESSAGES['choose_number_change'])
        await UserState.number_to_change.set()

@dp.message_handler(state=UserState.fio_to_change)
async def get_fio(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    else:
        await state.update_data(fio_to_change=message.text)
        await message.answer(MESSAGES['choose_number_to_work_change'])
        await UserState.number_to_work.set()

@dp.message_handler(state=UserState.number_to_work)
async def get_number_to_work(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    elif test.upload_number(bot, message):
        upload_result = test.upload_number(bot, message)
        await state.update_data(number_to_work=upload_result)
        await message.answer(MESSAGES['choose_fio_to_work_change'])
        await UserState.fio_to_work.set()
    else:
        await message.answer(MESSAGES['choose_number_to_work_change'])
        await UserState.number_to_work.set()


@dp.message_handler(state=UserState.fio_to_work)
async def get_fio_to_work(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    else:
        await state.update_data(fio_to_work=message.text)
        await message.answer(MESSAGES['choose_place'])
        await UserState.place_to_change.set()

@dp.message_handler(state=UserState.place_to_change)
async def get_place(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    else:
        await state.update_data(place_to_work=message.text)
        await message.answer(MESSAGES['get_comments'])
        await UserState.comments_to_change.set()

@dp.message_handler(state=UserState.comments_to_change)
async def get_comments(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    else:
        await state.update_data(comments=message.text)
        data = await state.get_data()
        await message.answer(MESSAGES['to_chat_send_message'])
        await bot.send_message(id_chanel, f"Замена\n"
                             f"Дата: {data['date_to_change']}\n"
                             f"Время: {data['time_to_change']}\n"
                             f"Бейдж сотрудника, у которого выходной: {data['number_to_change']}\n"
                             f"Сотрудник, у которого выходной: {data['fio_to_change']}\n"
                             f"Бейдж сотрудника, который будет работать: {data['number_to_work']}\n"
                             f"Сотрудник, который будет работать: {data['fio_to_work']}\n"
                             f"Магазин: {data['place_to_work']}\n"
                             f"Комментарии: {data['comments']}\n")
        await state.finish()
        await start(message)

@dp.message_handler(state=UserState.date_to_change_time)
async def get_date(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    elif test.upload_date(bot, message):
        upload_result = test.upload_date(bot, message)
        await state.update_data(date_to_change_time=upload_result)
        await message.answer(MESSAGES['choose_time_change'])
        await UserState.time_to_change_time.set()
    else:
        await message.answer(MESSAGES['choose_day_change_correct'])
        await UserState.date_to_change_time.set()

@dp.message_handler(state=UserState.time_to_change_time)
async def get_time(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    elif test.upload_time(bot, message):
        upload_result = test.upload_time(bot, message)
        await state.update_data(time_to_change_time=upload_result)
        await message.answer(MESSAGES['choose_number_change'])
        await UserState.number_to_change_time.set()
    else:
        await message.answer(MESSAGES['choose_time_change'])
        await UserState.time_to_change_time.set()

@dp.message_handler(state=UserState.number_to_change_time)
async def get_number(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    elif test.upload_number(bot, message):
        upload_result = test.upload_number(bot, message)
        await state.update_data(number_to_change_time=upload_result)
        await message.answer(MESSAGES['choose_fio_change'])
        await UserState.fio_to_change_time.set()
    else:
        await message.answer(MESSAGES['choose_number_change'])
        await UserState.number_to_change_time.set()


@dp.message_handler(state=UserState.fio_to_change_time)
async def get_fio(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    else:
        await state.update_data(fio_to_change_time=message.text)
        await message.answer(MESSAGES['choose_place'])
        await UserState.place_to_change_time.set()

@dp.message_handler(state=UserState.place_to_change_time)
async def get_place(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    else:
        await state.update_data(place_to_work_time=message.text)
        await message.answer(MESSAGES['get_comments'])
        await UserState.comments_to_change_time.set()

@dp.message_handler(state=UserState.comments_to_change_time)
async def get_comments(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    else:
        await state.update_data(comments_time=message.text)
        data = await state.get_data()
        await message.answer(MESSAGES['to_chat_send_message'])
        await bot.send_message(id_chanel, f"Изменение времени смены\n"
                             f"Дата: {data['date_to_change_time']}\n"
                             f"Время: {data['time_to_change_time']}\n"
                             f"Бейдж сотрудника: {data['number_to_change_time']}\n"
                             f"Сотрудник: {data['fio_to_change_time']}\n"
                             f"Магазин: {data['place_to_work_time']}\n"
                             f"Комментарии: {data['comments_time']}\n")
        await state.finish()
        await start(message)



@dp.message_handler(state=UserState.date_to_day_off)
async def get_time(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    elif test.upload_date(bot, message):
        upload_result = test.upload_date(bot, message)
        await state.update_data(date_to_day_off=upload_result)
        await message.answer(MESSAGES['choose_number_change'])
        await UserState.number_to_day_off.set()
    else:
        await message.answer(MESSAGES['choose_day_change_correct'])
        await UserState.date_to_day_off.set()


@dp.message_handler(state=UserState.number_to_day_off)
async def get_number(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    elif test.upload_number(bot, message):
        upload_result = test.upload_number(bot, message)
        await state.update_data(number_to_day_off=upload_result)
        await message.answer(MESSAGES['choose_fio_change'])
        await UserState.fio_to_day_off.set()
    else:
        await message.answer(MESSAGES['choose_number_change'])
        await UserState.number_to_day_off.set()

@dp.message_handler(state=UserState.fio_to_day_off)
async def get_fio(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    else:
        await state.update_data(fio_to_day_off=message.text)
        await message.answer(MESSAGES['choose_place'])
        await UserState.place_to_day_off.set()

@dp.message_handler(state=UserState.place_to_day_off)
async def get_place(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)
        await state.finish()
    else:
        await state.update_data(place_to_day_off=message.text)
        await message.answer(MESSAGES['get_comments'])
        await UserState.comments_to_day_off.set()

@dp.message_handler(state=UserState.comments_to_day_off)
async def get_comments_day_off(message: types.Message, state: FSMContext):
    if message.text == 'Назад в меню':
        await start(message)

    else:
        await state.update_data(comments_to_day_off=message.text)
        data = await state.get_data()
        await message.answer(MESSAGES['to_chat_send_message'])
        await bot.send_message(id_chanel, f"Выходной\n"
                             f"Дата: {data['date_to_day_off']}\n"
                             f"Бейдж сотрудника: {data['number_to_day_off']}\n"
                             f"Сотрудник: {data['fio_to_day_off']}\n"
                             f"Магазин: {data['place_to_day_off']}\n"
                             f"Комментарии: {data['comments_to_day_off']}\n")



        await start(message)
        await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp)

