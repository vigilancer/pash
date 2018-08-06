# vim: set ts=4 sw=4 st=4 et:

import shlex
# from subprocess import DEVNULL, PIPE, STDOUT, Popen
import subprocess


class Pipe:
    '''
    pipe
    _('ls', 'grep p')
    _('ls', 'grep p', 'grep Pip')
    _('gzcat tests/stagedb.sql.gz', "grep ISO", 'wc -l', "tr -d ' '")
    '''

    def __init__(self, *args):
        if len(args) == 0:
            return

        self.cmds = args

        if len(self.cmds) == 1:
            self.__exec_single()
        else:
            self.__exec_multiple()

    def __exec_multiple(self):
        proc = subprocess.Popen(
            shlex.split(self.cmds[0]),
            stdout=subprocess.PIPE,
        )

        for cmd in self.cmds[1:-1]:
            proc = subprocess.Popen(
                shlex.split(cmd),
                stdin=proc.stdout,
                stdout=subprocess.PIPE,
            )

        subprocess.Popen(
            shlex.split(self.cmds[-1]),
            stdin=proc.stdout,
        ).wait()

    def __exec_single(self):
        subprocess.run(shlex.split(self.cmds[0]))
