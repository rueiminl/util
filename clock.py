#! /usr/bin/python
import threading
import datetime
import sys
import time
import kbhit

def show_toast(message):
    title = "Clock"
    subtitle = "Notification"
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

class TimeEvent:
    events = []
    se
    def count():
        return len(events)
    def add(message, timeout):
        TimeEvent.events.append(TimeEvent(inst, message, timeout))
    def delete(index):
        if index < 0 or index >= TimeEvent.count():
            raise IndexError()
        events[index].cancel()
        del events[index]
    def save():
        pass
    def load():
        pass
    def list():
        for index in range(count()):
            print("%d: %s" % (index, TimeEvent.events[index].message))
    def __init__(self, inst, message, timeout):
        self.disabled = False
        self.message = message
        self.timeout = time.time() + timeout
    def cancel(self):
        self.disabled = True
    def get_message(self):
        return self.message
    def get_timeout(self):
        res = self.timeout - time.time()
        if res < 0:
            res = 0
        return res
    def check_events():
        pass
    def __str__(self):
        return '{timeout:%s, message:"%s"}' % (self.get_timeout(), self.get_message())

# menu
def add_event():
    message = raw_input("message: ")
    timeout = int(raw_input("timeout (seconds): "))
    TimeEvent.add(message, timeout)
    return TimeEvent.count()

def del_event():
    index = int(raw_input("event index: "))
    TimeEvent.delete(index)

def save_events():
    TimeEvent.save()

def load_events():
    TimeEvent.load()

def print_events():
    TimeEvent.list()

def show_help():
    print("a: add an event")
    print("d: delete an event")
    print("l: load events")
    print("h: help")
    print("p: print events")
    print("q: quit")
    print("l: save events")

def thread_main():

def main():
    threading.Thread()
    try:
        while True:
            command = raw_input("command: ").lower()
            if command == "a":
                add_event()
            elif command == "d":
                del_event()
            elif command == "h":
                show_help()
            elif command == "l":
                load_events()
            elif command == "p":
                print_events()
            elif command == "q":
                return
            elif command == "s":
                save_events()
            else:
                print("unknown command: %s" % command)
    except:
        print(sys.exc_info()[0])

if __name__ == '__main__':
    main()
