# vim: set ts=4 sw=4 st=4 et:

# import os; import sys; sys.path.insert(0, os.getcwd())
import os; import sys; sys.path.insert(0, os.path.abspath('..'))
from pipeish import Shell

shell = Shell(errexit=False, shellfail=False)

'''
WARNING: this test works like 50% of a time.
mostly because of bad timing. in second snippet sometimes
'false' not return fast enough. it is something to do with proc.poll().
need to check how pipes are implemented in bash for example.
of in OpenBSD's ksh, it's code should be cleaner.

disabling in for now

'''

shell.pipefail = False
with shell as _:
    o, e, x = _('false | true')

    if x is not None and x == 0:
        pass
    else:
        # should never happen because of 'pipefail = False'
        exit(x)
    _("printf 'Heyho\n'")

shell.pipefail = True
with shell as _:
    # import pudb; pudb.set_trace()
    o, e, x = _('false | true')

    _("printf 'Invisible Heyho\n'")

    if x is not None and x == 0:
        pass
    else:
        # now this will happen
        exit(x)
