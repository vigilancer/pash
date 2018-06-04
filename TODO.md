# vim: set ts=2 sw=2 st=2 et:

[x] create github repo
[x] exec with subprocess
[] collect output in array with os-specific line-end as separator
[] redirect > to file and /dev/null
[] redirect >> to file and /dev/null
[] handle commands with params
[] stub not implemented operators
[] override truth (__bool__) based on return code (nonzero == False)
[] emulate `set -e` and/or `set -o pipefail`
[] implement 'pipefail' somehow.
#       maybe with `|=` (__ior__)
#       _('ls') | _('grep') |= ('xargs')
#       if `grep` fails, whole chain will fail and xargs will not be executed
[] maybe pipe by default should work in `pipefail` mode, and __ior__ override it
[] redirect stdout and stderror
[] write tests
[x] create package to install with pip

