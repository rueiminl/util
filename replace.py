#! /usr/bin/python
"""
motivation: replace space with underscore for all files
"""
import sys
import os
import subprocess

def usage(execfile):
    print 'Usage:', execfile, 'target', 'replacement' 

def main():
    """
    up filename
    """
    if len(sys.argv) < 3:
        Usage()
        return
    for filename in os.listdir('.'):
        subprocess.call(['mv', filename, filename.replace(sys.argv[1], sys.argv[2])])

if __name__ == '__main__':
    main()
