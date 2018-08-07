# vim: set ts=4 sw=4 st=4 et:

import shlex
# from subprocess import DEVNULL, PIPE, STDOUT, Popen
import subprocess


class Pipe:

    def __init__(self, *args, pipefail=True):
        if len(args) == 0:
            return

        self.cmds = args
        self.pipefail = pipefail

        # maybe it's single string with pipes
        if len(self.cmds) == 1:
            self.cmds = [c.strip() for c in self.cmds[0].split('|') if c]

        if len(self.cmds) == 1:
            self.__exec_single()
        else:
            self.__exec_multiple()

    def __fail_if_pipefail(self, retcode):
        if self.pipefail:
            if retcode is not None and retcode != 0:
                exit(retcode)

    def __exec_multiple(self):
        proc = subprocess.Popen(
            shlex.split(self.cmds[0]),
            stdout=subprocess.PIPE,
        )
        self.__fail_if_pipefail(proc.returncode)

        for cmd in self.cmds[1:-1]:
            proc = subprocess.Popen(
                shlex.split(cmd),
                stdin=proc.stdout,
                stdout=subprocess.PIPE,
            )
            self.__fail_if_pipefail(proc.returncode)

        proc = subprocess.Popen(
            shlex.split(self.cmds[-1]),
            stdin=proc.stdout,
        )
        proc.wait()
        self.__fail_if_pipefail(proc.returncode)

    def __exec_single(self):
        proc = subprocess.run(shlex.split(self.cmds[0]))
        if proc.returncode != 0:
            exit(proc.returncode)
