# vim: set ts=2 sw=2 st=2 et:

[x] create github repo
[x] exec with subprocess
[x] collect output in array with os-specific line-end as separator
[] redirect > to file and /dev/null
[] redirect >> to file and /dev/null
[] handle commands with params
[x] stub not implemented operators
[x] override truth (__bool__) based on return code (nonzero == False)
[x] emulate `set -e` and/or `set -o pipefail`
[x] implement 'pipefail' somehow.
#       maybe with `|=` (__ior__)
#       _('ls') | _('grep') |= ('xargs')
#       if `grep` fails, whole chain will fail and xargs will not be executed
[x] maybe pipe by default should work in `pipefail` mode, and __ior__ override it
#       but without __ior__
[] redirect stdout and stderror
[] redirect to file descriptors and filenames
[] write tests
[x] create package to install with pip
[] override __copy__ to create new fresh copy of command
[] implement __repr__ (recreate python object) (need it?)
[x] implement __str__ (what should go there?)
[] add examples for && and || (with 'and' and 'or')
[] make gif with all usecases
[x] research alternative implementation: https://stackoverflow.com/questions/15008807/overriding-or-operator-on-python-classes
[] add to readme 'restrictions' chapter
