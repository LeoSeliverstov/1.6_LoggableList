import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, elem):
        super(Loggable, self).append(elem)
        self.log(elem)


if __name__ == '__main__':
    a = LoggableList()
    a.append('msg 1')
    a.append('msg 2')
    print(a)
