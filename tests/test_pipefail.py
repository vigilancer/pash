#!/usr/bin/env python3
# vim: set ts=4 sw=4 st=4 et:

# import os; import sys; sys.path.insert(0, os.getcwd())
import os; import sys; sys.path.insert(0, os.path.abspath('..'))
from pipeish import Pipe as _

_('ls | false', pipefail=False)
print('pipe failed but you see me')

print('will not see next line')
_('ls | false', pipefail=True)
print('123')

