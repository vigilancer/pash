initially was named after a friend from school, Pavel Hurgcheev - `pash`. then
`psh`. until free name was found - `pipeish`.

it's like pipes in shell but not exactly. hence `pipe-ish`.

[picture-of-python-looking-like-a-shell]

it is still raw and WIP but mostly behaves like you running commands in shell.
# Examples:

```
from pipeish import Pipe as _
_('ls')
_('gzcat stagedb.sql.gz', 'psql -U usermane pentagon_db')
```

can we do '|'s? yes, we can!

```
from pipeish import Pipe as _
cmd = 'ls -la | head -3'
_(*[c.strip() for c in cmd.split('|') if c])
```

yeah... looking at it seems like we can support syntax with '|'s internally.
more are comming!
most likely.

feel free to open issues with common use cases, I'll try to prioritize
what seems important and integrate.


Links
-----

"Bash is the JavaScript of systems programming". Strongly agree.
https://github.com/progrium/bashstyle

"shell=True: Security Considerations"
https://docs.python.org/3/library/subprocess.html#security-considerations
