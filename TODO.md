
- [x] create github repo
- [x] exec with subprocess
- [] collect output in variable
- [] redirect to file and /dev/null
- [] redirect to file and /dev/null
- [x] handle commands with params
- [] override truth (__bool__) based on return code (nonzero == False)
- [] emulate `set -e` and/or `set -o pipefail`
- [] implement 'pipefail' somehow.
     maybe with `|=` (__ior__)
     _('ls') | _('grep') |= ('xargs')
     if `grep` fails, whole chain will fail and xargs will not be executed
- [] maybe pipe by default should work in `pipefail` mode, and __ior__ override it
      but without __ior__
- [] redirect stdout and stderror
- [] add default behaviour - redirect stderr to terminal even when stdout redirected to next commanad in pipe
- [] redirect to file descriptors and filenames
- [x] create package to install with pip
- [] implement __repr__ (recreate python object) (need it?)
- [] implement __str__ (what should go there?)
- [] add examples for && and || (with 'and' and 'or')
- [] make gif with all usecases
- [x] research alternative implementation: https://stackoverflow.com/questions/15008807/overriding-or-operator-on-python-classes
- [] add to readme 'restrictions' chapter
- [] simplify env variable access (os.environ- ['HOME'] etc)
- [] maybe it's worth to reimplement 'test' command (-z seems neat)


tests
- [x] smoke: one command
- [x] smoke: pipe two commands
- [x] smoke: pipe three commands
- [x] check execution order in pipe
- [] context manager to set 'cwd' for commands executed in the same context
- [x] check that 'gunzip' works okay with pipe
