# vim: set ts=2 sw=2 st=2 et:

[] create github repo
[] exec with subprocess
[] redirect > to file and /dev/null
[] redirect >> to file and /dev/null
[] handle commands with params
[] stub not implemented operators
[] override truth (__bool__) based on return code (nonzero == False)
[] implement 'pipefail' somehow.
#       maybe with `|=` (__ior__)
#       _('ls') | _('grep') |= ('xargs')
#       if `grep` fails, whole chain will fail and xargs will not be executed
[] maybe pipe by default should work in `pipefail` mode, and __ior__ override it
[] redirect stdout and stderror
[] write tests
[] create package to install with pip
[] emulate `set -e` and/or `set -o pipefail`

