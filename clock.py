#! /usr/bin/python
import datetime
import kbhit
import os
import sys
import thread
import threading
import time
import traceback

def show_toast(title, subtitle, message):
  title = "Clock"
  subtitle = "Notification"
  t = '-title {!r}'.format(title)
  s = '-subtitle {!r}'.format(subtitle)
  m = '-message {!r}'.format(message)
  os.system('/Users/rueiminl/tool/terminal-notifier_1.4.2/terminal-notifier.app/Contents/MacOS/terminal-notifier {} > null'.format(' '.join([m, t, s])))

class TimeEvent:
  events = []
  lock = threading.Lock()
  @staticmethod
  def add(message, timeout):
    with TimeEvent.lock:
      TimeEvent.events.append(TimeEvent(message, timeout))
  @staticmethod
  def delete(index):
    with TimeEvent.lock:
      if index < 0 or index >= len(TimeEvent.events):
        raise IndexError()
      del TimeEvent.events[index]
  @staticmethod
  def list():
    with TimeEvent.lock:
      for index in range(len(TimeEvent.events)):
        print("%d: %s" % (index, TimeEvent.events[index]))
  @staticmethod
  def save():
    with TimeEvent.lock:
      pass
  @staticmethod
  def load():
    with TimeEvent.lock:
      pass
  @staticmethod
  def check_events():
    with TimeEvent.lock:
      for event in TimeEvent.events:
        event.check()
  def __init__(self, message, timeout):
    self.disabled = False
    self.message = message
    self.timeout = time.time() + timeout
  def check(self):
    if not self.disabled:
      if self.get_timeout() == 0:
        show_toast("Warning", "Time's up", self.get_message())
        self.disabled = True
  def cancel(self):
    self.disabled = True
  def get_message(self):
    return self.message
  def get_timeout(self):
    res = self.timeout - time.time()
    if res < 0:
      res = 0
    return res
  def __str__(self):
    return '{timeout:%s, message:"%s"}' % (self.get_timeout(), self.get_message())

# menu
def add_event():
  message = raw_input("message: ")
  timeout = int(raw_input("timeout (seconds): "))
  TimeEvent.add(message, timeout)

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

def counter_down():
  try:
    while True:
      time.sleep(1)
      TimeEvent.check_events()
  except:
    print traceback.print_exc()

def main():
  try:
    thread.start_new_thread(counter_down, () )
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
    print traceback.print_exc()

if __name__ == '__main__':
  main()
