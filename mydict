#! /usr/bin/python
"""One-line documentation for mydict module.

A detailed description of mydict.
"""

import os
import re
import copy
import sys
from subprocess import call
sys.path.append('/Users/rueiminl/Desktop/Project/PyLib')
from appcommands import AppCommands as appcommands
from flags import Flags as flags
import path

FLAGS = flags.FLAGS
flags.DEFINE_string('dict', os.path.join(path.Path.GetHome(), 'dict.txt'),
                    'Path to the dictionary file')

FAILURE = 1
SUCCESS = 0


class Util:

  @staticmethod
  def LoadDict(filename):
    d = Dict()
    try:
      with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
          w = Util.LoadWord(line)
          d.AddWord(w)
    except Exception as e:
      print e
    return d

  @staticmethod
  def SaveDict(filename, d):
    try:
      with open(filename, 'w') as f:
        for w in d.Words():
          Util.SaveWord(f, w)
        return SUCCESS
    except Exception as e:
      print e
    return FAILURE

  @staticmethod
  def LoadWord(line):
    return Word(*line.split('\t'))

  @staticmethod
  def SaveWord(fh, word):
    fh.write(word.word + '\t' + str(word.count))
    if word.desc:
      fh.write('\t' + word.desc)
    fh.write('\n')

  @staticmethod
  def ListDict(d):
    try:
      for w in d.Words():
        print w
      print d.Length()
      return SUCCESS
    except Exception as e:
      print e
    return FAILURE

  @staticmethod
  def LoadDictFromArticle(filename):
    d = Dict()
    try:
      with open(filename, 'r') as f:
        for line in f:
          for word in re.split('[^a-zA-Z]', line):
            if word:
              d.AddWord(Word(word, 1, line))
    except Exception as e:
      print e
    return d


class Word:

  def __init__(self, w, count=1, desc=None):
    self.word = w.lower()
    self.count = int(count)
    self.desc = desc
    if self.desc:
      self.desc = self.desc.strip()

  def __str__(self):
    s = 'Word('
    s += self.word
    s += ', '
    s += str(self.count)
    if self.desc:
      s += ', '
      s += self.desc
    s += ')'
    return s

  def __repr__(self):
    return self.word + '(' + str(self.count) + '): ' + self.desc


class Dict:

  def __init__(self, d=None):
    if d:
      self.words = copy.deepcopy(d.words)
    else:
      self.words = {}

  def Contains(self, word):
    return word in self.words

  def Words(self):
    return self.words.values()

  def Length(self):
    return len(self.words)

  def AddWord(self, word):
    if word.word in self.words:
      self.words[word.word].count += word.count
      if word.desc:
        self.words[word.word].desc = word.desc
    else:
      self.words[word.word] = word

  def RemoveWord(self, word):
    if word in self.words:
      del self.words[word]

  def Diff(self, d):
    for w in d.Words():
      self.RemoveWord(w)

  def Import(self, d):
    for w in d.Words():
      self.AddWord(w)


class MyCmd(appcommands.Cmd):

  def __init__(self, name, flag_values, **kwargs):
    super(MyCmd, self).__init__(name, flag_values, **kwargs)


class AddWordCmd(MyCmd):
  """Add a word

  Usage: add word [ count[ 'description']]
  """

  def Run(self, argv):
    w = Word(*argv)
    d = Util.LoadDict(FLAGS.dict)
    d.AddWord(w)
    return Util.SaveDict(FLAGS.dict, d)


class ImportCmd(MyCmd):
  """Import all words from an article

  Usage: import file
  """

  def Run(self, argv):

    d1 = Util.LoadDict(FLAGS.dict)
    d2 = Util.LoadDictFromArticle(argv[0])
    d3 = Dict(d1)
    d1.Import(d2)
    d2.Diff(d3)
    Util.ListDict(d2)
    return Util.SaveDict(FLAGS.dict, d1)


class BackupCmd(MyCmd):
  """Backup the dict.txt to dict.txt.bak

  Usage: backup
  """

  def Run(self, argv):
    return call(['cp', FLAGS.dict, FLAGS.dict + '.bak'])


class ListCmd(MyCmd):
  """List all words

  Usage: ls
  """

  def Run(self, argv):
    d = Util.LoadDict(FLAGS.dict)
    return Util.ListDict(d)

def main(argv):
  appcommands.AddCmd('add', AddWordCmd)
  appcommands.AddCmd('import', ImportCmd)
  appcommands.AddCmd('ls', ListCmd)
  appcommands.AddCmd('backup', BackupCmd)

if __name__ == '__main__':
  appcommands.Run()
