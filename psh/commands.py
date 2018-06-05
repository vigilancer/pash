# vim: set ts=2 sw=2 st=2 et:


import shlex
from subprocess import PIPE, Popen
import os
import sys


class BaseCommandException(Exception):
    pass


class AlreadyCalled(BaseCommandException):
    pass


class NeverCalled(BaseCommandException):
    pass


class StdinMissing(BaseCommandException):
    pass


class StdoutMissing(BaseCommandException):
    pass


class StderrMissing(BaseCommandException):
    pass


class BaseCommand():

    command_line = None

    _stdin = None
    _stdout = None
    _stderr = None

    code = None

    def __call__(self):
        ''' execute command.
            should change self.code after command execution
        '''
        if self.code is not None:
            raise AlreadyCalled()

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
        if self.code is None:
            raise NeverCalled()
        return self.code == 0

    def __str__(self):
        try:
            return self.stderr
        except StderrMissing:
            return self.stdout

    @property
    def stdin(self):
        if self._stdin is None:
            raise StdinMissing()
        return self._stdin

    @stdin.setter
    def stdin(self, value):
        self._stdin = value

    @property
    def stdout(self):
        if self._stdout is None:
            raise StdoutMissing()
        return self._stdout

    @stdout.setter
    def stdout(self, value):
        self._stdout = value

    @property
    def stderr(self):
        if self._stderr is None:
            raise StderrMissing()
        return self._stderr

    @stderr.setter
    def stderr(self, value):
        self._stderr = value

    @property
    def stdin_formatted(self):
        return list(filter(
            lambda x: len(x) > 0,
            self.stdin.split(os.linesep)
        ))

    @property
    def stdout_formatted(self):
        return list(filter(
            lambda x: len(x) > 0,
            self.stdout.split(os.linesep)
        ))

    @property
    def stderr_formatted(self):
        return list(filter(
            lambda x: len(x) > 0,
            self.stderr.split(os.linesep)
        ))


class Command(BaseCommand):

    _args = None
    _timeout = 0

    def __init__(self, cmd, timeout=1):
        self.command_line = cmd
        self._args = shlex.split(cmd)
        self._timeout = timeout

    def __call__(self):
        super().__call__()

        try:
            stdin = self.stdin
            p = Popen(self._args,
                      shell=False,
                      universal_newlines=True,
                      stdin=PIPE,
                      stdout=PIPE, stderr=PIPE)
            self.stdout, self.stderr = p \
                .communicate(input=stdin, timeout=self._timeout)
        except StdinMissing:
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
