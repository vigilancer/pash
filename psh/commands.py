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

    # def __repr__(self):
    #     raise NotImplemented('not decided what should go there just yet')

    # def __str__(self):
    #     raise NotImplemented('not decided what should go there just yet')


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
        else:
            p = Popen(self._args,
                      shell=False,
                      universal_newlines=True,
                      stdout=PIPE, stderr=PIPE)


        # import pudb; pudb.set_trace()

        if self.stdin:
            self.stdout, self.stderr = p \
                .communicate(input=self.stdin, timeout=self._timeout)
        else:
            self.stdout, self.stderr = p \
                .communicate(timeout=self._timeout)

        self.code = p.returncode



        # self.stdout = p.stdout
        # self.stderr = p.stderr
        # self.code = p.returncode



        # self.stdout = f'Std out string from {self.command}'
        # self.stderr = f'Std err string from {self.command}'
        # self.code = 22
        return self

    def __or__(self, other):
        # import pudb; pudb.set_trace()

        self()

        other.stdin = self.stdout
        return other()

    # def __str__(self):
    #     r = self.stderr
    #     if self.stdout:
    #         r += self.stdout
    #     return r

    # __repr__ = __str__
