#!/usr/bin/env python3
# vim: set ts=4 sw=4 st=4 et:

# import os; import sys; sys.path.insert(0, os.getcwd())
import os; import sys; sys.path.insert(0, os.path.abspath('..'))
from pipeish import Pipe as _

description = ' \
Just smoke semi-auto test to check if anything was broken. \
'

print(f'{description}')


def __test_single_string(cmd):
    print(f"\np$ {cmd}")
    _(cmd)


def __test_array_of_commands(cmd):
    print(f"\np$ {cmd}")
    cmds = [c.strip() for c in cmd.split('|') if c]
    _(*cmds)


cmd = 'ls'
__test_single_string(cmd)

cmd = 'ls -la | head -3'
__test_single_string(cmd)

cmd = "ls -1 | wc -l | tr -d ' '"
__test_single_string(cmd)


print('\n---\n')


cmd = 'ls -la | head -3'
__test_array_of_commands(cmd)

cmd = "ls -1 | wc -l | tr -d ' '"
__test_array_of_commands(cmd)
