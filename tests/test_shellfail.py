# vim: set ts=4 sw=4 st=4 et:

# import os; import sys; sys.path.insert(0, os.getcwd())
import os; import sys; sys.path.insert(0, os.path.abspath('..'))
from pipeish import Shell

shell = Shell(pipefail=False, errexit=False, shellfail=False)

with shell as _:
    _("printf 'You will see this line. And next one\n'")
    _('false')

shell.shellfail = True
with shell as _:
    _("printf 'Yes, this one\n'")
    _('false')

with Shell() as _:
    _("printf 'But not this one\n'")

