change_list = []
choose_list = []
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


