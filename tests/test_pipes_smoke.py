# vim: set ts=4 sw=4 st=4 et:

# import os; import sys; sys.path.insert(0, os.getcwd())
import os; import sys; sys.path.insert(0, os.path.abspath('..'))
from pipeish import Pipe as _

_()(
    'date +%m'
)

_()(
    'uname -a',
    'awk \'BEGIN { RS=" " }; { print $1; }\'',
    'sort',
    'head -3',
)

_()("ls -1 | wc -l | tr -d ' '")
