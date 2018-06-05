# vim: set ts=2 sw=2 st=2 et:


import shlex
from subprocess import PIPE, Popen


class AlreadyCalled(Exception):
    pass


class AbsCommand():

    command_line = None

    stdin = None
    stdout = None
    stderr = None
    code = None

    def __call__(self):
        ''' execute command '''
        raise NotImplemented()

    def __or__(self, other):
        ''' | '''
        raise NotImplemented()

    def __gt__(self, other):
        ''' > '''
        raise NotImplemented()

    def __rshift__(self, other):
        ''' >> '''
        raise NotImplemented()

    def __bool__(self):
        return self.code == 0


class Command(AbsCommand):

    _args = None
    _timeout = 0
    _called = False

    def __init__(self, cmd, timeout=1):
        self.command_line = cmd
        self._args = shlex.split(cmd)
        self._timeout = timeout

    def __call__(self):
        if self._called:
            raise AlreadyCalled()
        self._called = True

        if self.stdin:
            p = Popen(self._args,
                      shell=False,
                      universal_newlines=True,
                      stdin=PIPE,
                      stdout=PIPE, stderr=PIPE)

            self.stdout, self.stderr = p \
                .communicate(input=self.stdin, timeout=self._timeout)
        else:
            p = Popen(self._args,
                      shell=False,
                      universal_newlines=True,
                      stdout=PIPE, stderr=PIPE)

            self.stdout, self.stderr = p \
                .communicate(timeout=self._timeout)

        self.code = p.returncode

        return self

    def __or__(self, other):
        self()
        other.stdin = self.stdout
        return other()
