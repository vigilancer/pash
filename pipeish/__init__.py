# vim: set ts=4 sw=4 st=4 et:

import shlex
# from subprocess import DEVNULL, PIPE, STDOUT, Popen
from subprocess import DEVNULL, PIPE, STDOUT, Popen
import subprocess
import sys


class Shell:

    out_pipes = {
        't': None,
        'n': DEVNULL,
    }
    err_pipes = {
        't': None,
        'n': DEVNULL,
        'r': STDOUT,
    }

    def __init__(self, check=True, *args):
        self.check = check

    def __update_cmds(self, *args):
        self.cmds = []

        # maybe it is a single string with pipes
        if len(args) == 1:
            args = [c.strip() for c in args[0].split('|') if c]

        for a in args:
            if isinstance(a, str):
                self.cmds.append((a, 'dd'))
            elif isinstance(a, list) or isinstance(a, tuple):
                self.cmds.append(a)
            else:
                raise ValueError("Unsupported command type: %s" % a)

    def __call__(self, *args):
        self.__update_cmds(*args)

        if len(self.cmds) == 0:
            return
        elif len(self.cmds) == 1:
            self.__exec_single()
        else:
            self.__exec_multiple()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self.check and self.retcode is not 0:
            sys.exit(self.retcode)

    def __exec_multiple(self):
        proc = None
        stdin = None

        for idx, cmd in enumerate(self.cmds):
            o, e = self.__parse_cmd_opts(cmd[1], idx < len(self.cmds) - 1)

            prev_proc = proc
            proc = subprocess.Popen(
                shlex.split(cmd[0]),
                stdin=stdin,
                stdout=o, stderr=e,
                universal_newlines=True,
            )
            stdin = proc.stdout

            if prev_proc and prev_proc.stdout:
                # https://docs.python.org/3.6/library/subprocess.html#replacing-shell-pipeline
                # Allow 'prev_proc' to receive a SIGPIPE if 'proc' exits.
                prev_proc.stdout.close()

            self.retcode = proc.returncode

        proc.wait()
        self.retcode = proc.returncode

    def __exec_single(self):
        c = self.cmds[0]
        o, e = self.__parse_cmd_opts(c[1], False)

        proc = subprocess.Popen(
            shlex.split(c[0]),
            stdin=None,
            stdout=o, stderr=e,
            universal_newlines=True,
        )
        proc.wait()
        self.retcode = proc.returncode

    def __parse_cmd_opts(self, opts, have_next_command):
        if opts[0] == 'd':
            if have_next_command:
                o = PIPE
            else:
                o = None
        else:
            o = self.out_pipes[opts[0]]

        if opts[1] == 'd':
            e = None
        else:
            e = self.err_pipes[opts[1]]

        return o, e

