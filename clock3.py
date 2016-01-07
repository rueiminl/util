#! /usr/bin/python
import threading
import datetime
import sys
import time
import math
import traceback

def show_toast(message):
    title = "Clock"
    subtitle = "Notification"
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

class TimeEvent:
    events = []
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

def save_events():
    TimeEvent.save()

def load_events():
    TimeEvent.load()

def print_events():
    TimeEvent.list()

class Event:
    def __init__(self, message, timeout):
        self.message = message
        self.abs = timeout + time.time()
    def get_timeout(self):
        return self.abs - time.time()
    def get_abs(self):
        return self.abs
    def __str__(self):
        return '{message:%s, timeout:%d}' % (self.message, self.get_timeout())

class EventManager(threading.Thread):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
        self.events = []
        self.timeout = math.inf
    def run(self):
        pass
    def update(self):
        pass
    # invoked by main thread
    def addEvent(self, message, timeout):
        event = Event(message, timeout)
        with self.lock:
            self.events.append(event)
            if event.timeout < self.timeout:
                self.timeout = event.timeout
        self.update()
    def delEvent(self, index):
        with self.lock:
            if index < 0 or index >= len(self.events):
                raise IndexError()
            del self.events[index]
    def listEvents(self):
        with self.lock:
            for i in range(len(self.events)):
                print("%d: %s" % (i, self.events[i]))

def showHelp():
    print("a: add an event")
    print("d: delete an event")
    print("l: load events")
    print("h: help")
    print("p: print events")
    print("q: quit")
    print("l: save events")

def main():
    manager = EventManager()
    manager.start()
    try:
        while True:
            command = input("command: ").lower()
            if command == "a":
                message = input("message: ")
                timeout = int(input("timeout (seconds): "))
                manager.addEvent(message, timeout)
            elif command == "d":
                index = int(input("event index: "))
                manager.delEvent(index)
            elif command == "h":
                showHelp()
            elif command == "l":
                #TODO
                pass
            elif command == "p":
                manager.listEvents()
            elif command == "q":
                return
            elif command == "s":
                #TODO
                pass
            else:
                print("unknown command: %s" % command)
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print "*** print_tb:"
        traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
        print "*** print_exception:"
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                                  limit=2, file=sys.stdout)
        print "*** print_exc:"
        traceback.print_exc()
        print "*** format_exc, first and last line:"
        formatted_lines = traceback.format_exc().splitlines()
        print (formatted_lines[0])
        print (formatted_lines[-1])
        print ("*** format_exception:")
        print (repr(traceback.format_exception(exc_type, exc_value,
                                              exc_traceback)))
        print ("*** extract_tb:")
        print (repr(traceback.extract_tb(exc_traceback)))
        print ("*** format_tb:")
        print (repr(traceback.format_tb(exc_traceback)))
        print ("*** tb_lineno:", exc_traceback.tb_lineno)
if __name__ == '__main__':
    main()
