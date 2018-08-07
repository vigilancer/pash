initially was named after a friend from school, Pavel Hurgcheev - `pash`. then
`psh`. until free name was found - `pipeish`.

it's like pipes in shell but not exactly. hence `pipe-ish`.

[picture-of-python-looking-like-a-shell]

it is still raw and WIP but mostly behaves like you running commands in shell.

How to use
-----
for installed package:
```
from pipeish import Pipe as _
```

for development (replace `os.getcwd()` with path to pipeish sources)
```
import os; import sys; sys.path.insert(0, os.getcwd())
from pipeish import Pipe as _
```

Examples
-----

```
_('ls')
_('gzcat stagedb.sql.gz', 'psql -U usermane pentagon_db')
```

can we do '|'s? yes, we can!

```
_('ls -la | head -3')  # single string with '|' in shell-like-way
```
it uses `str.split('|')` under the hood, so if your arguments contain `|`s you can feed comma separated list instead.

more are comming!

feel free to open issues with common use cases, I'll try to prioritize
what seems important and integrate.


Links
-----

"Bash is the JavaScript of systems programming". Strongly agree.
https://github.com/progrium/bashstyle

"shell=True: Security Considerations"
https://docs.python.org/3/library/subprocess.html#security-considerations
