change_list = []
class DiskConnector:
    def __init__(self):
        pass

    def upload_date(self, bot, message):
        total = []
        message_to_save_date = message.text
        for el in message_to_save_date:
            if el.isdigit():
                total.append(el)
        if len(total) == 3:
            total = total[0] + '.' + total[1] + total[2]
            return total
        elif len(total) == 4:
            total = total[0] + total[1] +'.' + total[2] + total[3]
            return total
        else:
            return False

    def upload_time(self, bot, message):
        total = []
        message_to_save_time = message.text
        for el in message_to_save_time:
            if el.isdigit():
                total.append(el)
        if len(total) == 3:
            total = total[0] + '-' + total[1] + total[2]
            return total
        elif len(total) == 4:
            total = total[0] + total[1] +'-' + total[2] + total[3]
            return total
        elif len(total) == 8:
            total = total[0] + total[1] + ':' + total[2] + total[3] + '-' + total[4] + total[5] + ':' + total[6] + total[7]
            return total
        else:
            return False

    def upload_number(self, bot, message):
        message_to_save_number = message.text
        if message_to_save_number.isdigit():
            return message_to_save_number
        else:
            return False

    def back(self, bot, message):
        message_to_back = message.text
        if message_to_back == 'Назад в меню':
            return message_to_back
        else:
            return False

    def upload_choose(self, bot, message):
        keyword = {1: 'Замена', 2: 'Изменение времени смены', 3: 'Установить выходной день'}
        message_to_save_choose = message.text
        if message_to_save_choose in keyword.values():
            print(message_to_save_choose)
            return message_to_save_choose
        else:
            return False

    def change_list(self, upload):
        change_list.append(upload)
        return change_list

    def change_list_clear(self):
        change_list.clear()
        return change_list

    def to_send_message(self, change_list_view):
        if len(change_list_view) == 4:
            date = change_list_view[0]
            number = change_list_view[1]
            fio = change_list_view[2]
            place = change_list_view[3]
            send_view =  f'Выходной\nДата: {date}\nБейдж: {number}\nСотрудник: {fio}\nМагазин: {place}\n'
            return send_view
        elif len(change_list_view) == 5:
            date = change_list_view[0]
            time = change_list_view[1]
            number = change_list_view[2]
            fio = change_list_view[3]
            place = change_list_view[4]
            send_view =  f'Изменение времени смены\nДата: {date}\nВремя: {time}\nБейдж: {number}\nСотрудник: {fio}\nМагазин: {place}\n'
            return send_view
        elif len(change_list_view) == 7:
            date = change_list_view[0]
            time = change_list_view[1]
            number = change_list_view[2]
            fio = change_list_view[3]
            number_work = change_list_view[4]
            fio_work = change_list_view[5]
            shop = change_list_view[6]
            send_view = f'Замена\nДата: {date}\nВремя: {time}\nБейдж сотрудника, у которого выходной: {number}\nСотрудник, у которого выходной: {fio}\nБейдж сотрудника, у которого выходной: {number_work}\nСотрудник, у которого выходной: {fio_work}\nМагазин: {shop}\n'
            return send_view
        else:
            return False

