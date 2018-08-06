#!/usr/bin/env python3
# vim: set ts=4 sw=4 st=4 et:

# import os; import sys; sys.path.insert(0, os.getcwd())
import os; import sys; sys.path.insert(0, os.path.abspath('..'))
from pipeish import Pipe as _

description = ' \
Test for one, two and three commands in pipe. \
'

_(f'echo {description}')


def __test(cmd):
    print(f"\np$ {cmd}")
    cmds = [c.strip() for c in cmd.split('|') if c]
    _(*cmds)


cmd = 'ls'
__test(cmd)

cmd = 'ls -la | head -3'
__test(cmd)

cmd = "ls -1 | wc -l | tr -d ' '"
__test(cmd)
