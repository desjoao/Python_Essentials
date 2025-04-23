class Timer:
    def __init__(self, hora, minuto, segundo):
        self.hour = hora
        self.minute = minuto
        self.second = segundo

    def __str__(self):
        hour = f'{self.hour:02}'
        minute = f'{self.minute:02}'
        second = f'{self.second:02}'
        return f'{hour}:{minute}:{second}'

    def next_second(self):
        if self.second == 59:
            self.second = 0
            if self.minute == 59:
                self.minute = 0
                if self.hour == 23:
                    self.hour = 0
                else:
                    self.hour += 1
            else:
                self.minute += 1
        else:
            self.second += 1

    def prev_second(self):
        if self.second == 0:
            self.second = 59
            if self.minute == 0:
                self.minute = 59
                if self.hour == 0:
                    self.hour = 23
                else:
                    self.hour -= 1
            else:
                self.minute -= 1
        else:
            self.second -= 1


# Test the class
timer = Timer(23, 59, 59)
print(timer)         # 23:59:59
timer.next_second()
print(timer)         # 00:00:00
timer.prev_second()
print(timer)         # 23:59:59
