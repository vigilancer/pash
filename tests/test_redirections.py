# vim: set ts=4 sw=4 st=4 et:

# import os; import sys; sys.path.insert(0, os.getcwd())
import os; import sys; sys.path.insert(0, os.path.abspath('..'))
from pipeish import Shell

with Shell(shellfail=False) as _:
    _(
        'printf Stdout1',
        ('xargs -I{} echo {}', 'dn')
    )

    _(
        'printf Stdout2',
        ('xargs -I{} echo {}', 'nd')
    )
