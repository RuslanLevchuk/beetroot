CHANNELS = ["BBC", "Discovery", "УТ-1", "PornHUB", "ICTV"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.actual_channel = 0


    def first_channel(self):
        self.actual_channel = 0

    def turn_channel(self, turn):
        turn = int(turn) - 1
        if turn >= 0 and turn < len(self.channels):
            self.actual_channel = turn
            return f'{self.actual_channel}'

    def last_channel(self):
        self.actual_channel = len(self.channels) - 1

    def next_channel(self):
        self.actual_channel += 1
        if self.actual_channel >= len(self.channels):
            self.actual_channel = 0

    def previous_channel(self):
        self.actual_channel -= 1
        if self.actual_channel < 0:
            self.actual_channel = len(self.channels) - 1

    def current_channel(self):
        return f'{self.actual_channel + 1} - {self.channels[self.actual_channel]}'

    def is_exist(self, is_in_list):
        if is_in_list.isalpha():
            for i in self.channels:
                if is_in_list.casefold() == i.casefold():
                    return f'Yes, {is_in_list} is exist'
            return f'No, {is_in_list} is not  exist'

        elif is_in_list.isdigit():
            is_in_list = int(is_in_list)
            if is_in_list <= len(self.channels) and is_in_list > 0:
                return f'Yes, {is_in_list} is exist'
            else:
                return f'No, {is_in_list} is not  exist'
        else:
            pass
