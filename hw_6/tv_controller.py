CHANNELS = ["BBC", "Discovery", "TV1000", "PornHUB", "ICTV"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.actual_channel = 0
        self.draw_tv()


    def first_channel(self):
        self.actual_channel = 0
        self.draw_tv()

    def turn_channel(self, turn):
        turn = int(turn) - 1
        if turn >= 0 and turn < len(self.channels):
            self.actual_channel = turn
            print(self.actual_channel)
            self.draw_tv()


    def last_channel(self):
        self.actual_channel = len(self.channels) - 1
        self.draw_tv()

    def next_channel(self):
        self.actual_channel += 1
        if self.actual_channel >= len(self.channels):
            self.actual_channel = 0
        self.draw_tv()

    def previous_channel(self):
        self.actual_channel -= 1
        if self.actual_channel < 0:
            self.actual_channel = len(self.channels) - 1
        self.draw_tv()

    def current_channel(self):
        print(self.actual_channel+1, '-', self.channels[self.actual_channel])

    def is_exist(self, is_in_list):
        if is_in_list.isalpha():
            for i in self.channels:
                if is_in_list.casefold() == i.casefold():
                    return "Yes"
            return "No"

        elif is_in_list.isdigit():
            is_in_list = int(is_in_list)
            if is_in_list <= len(self.channels) and is_in_list > 0:
                return "Yes"
            else:
                return "No"
        else:
            pass

    def draw_tv(self):
        if len(self.channels[self.actual_channel]) > 3:
            logo = ''.join(list(self.channels[self.actual_channel])[:3]).upper()
        else:
            logo = self.channels[self.actual_channel].upper()

        borders = ['╔', '╚', '╗', '╝', '═', '║']
        print('       \  /')
        print('        \/')
        print(borders[0], borders[4]*15, borders[2], sep='')
        print(borders[-1], end='')
        print(' '*(15-len(logo)),logo, borders[-1], sep='')
        print(borders[-1], '               ', borders[-1], sep='')
        print(borders[-1], '               ', borders[-1], sep='')
        print(borders[1], borders[4]*15, borders[3], sep='')
        pass


controller = TVController(CHANNELS)
while 1:
    command = input('Input command: "first", "last", "next", "prev", "curr" "is N (or Name)" to know is exist '
                    'or "N" change channel: ')

    if command.casefold() == 'first':
        controller.first_channel()
    elif command.casefold() == 'last':
        controller.last_channel()
    elif command.casefold() == 'next':
        controller.next_channel()
    elif command.casefold() == 'prev':
        controller.previous_channel()
    elif command.casefold() == 'curr':
        controller.current_channel()
    elif command.isdigit():
        controller.turn_channel(command)
    else:
        command = command.split()
        if len(command) == 1:
            print('Unknown command')
            pass
        elif command[0].casefold() == 'is':
            print(controller.is_exist(command[1]))
        else:
            print('Unknown command')

