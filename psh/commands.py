# vim: set ts=2 sw=2 st=2 et:


import shlex
from subprocess import PIPE, Popen


class BaseCommandException(Exception):
    pass


class AlreadyCalled(BaseCommandException):
    pass


class NeverCalled(BaseCommandException):
    pass


class BaseCommand():

    command_line = None

    stdin = None
    stdout = None
    stderr = None
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


class Command(BaseCommand):

    _args = None
    _timeout = 0

    def __init__(self, cmd, timeout=1):
        self.command_line = cmd
        self._args = shlex.split(cmd)
        self._timeout = timeout

    def __call__(self):
        super().__call__()

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
