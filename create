#! /usr/bin/python
import sys
import os
from subprocess import call
def main():
    """
    cd $REPO
    mkdir TAG
    touch TAG/TAG.txt
    open TAG/TAG.txt
    """
    if len(sys.argv) < 2:
        print 'Usage: %s TAG' % sys.argv[0]
        return
    repo = os.environ['REPO']
    path = '%s/%s' % (repo, sys.argv[1])
    call(['mkdir', path])
    file = '%s/%s.txt' % (path, sys.argv[1])
    call(['touch', file])
    call(['open', file])

if __name__ == '__main__':
    main()