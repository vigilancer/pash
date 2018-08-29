initially was named after a friend from school, Pavel Hurgcheev - `pash`. then
`psh`. until free name was found - `pipeish`.

it's like pipes in shell but not exactly. hence `pipe-ish`.

[picture-of-python-looking-like-a-shell]

it is still raw and WIP but mostly behaves like you running commands in shell.

How to use
-----
for installed package:
```
from pipeish import Shell
```

for development (replace `os.getcwd()` with path to pipeish sources)
```
import os; import sys; sys.path.insert(0, os.getcwd())
from pipeish import Shell
```

Examples
-----

simple as it is:

```
_()('ls')
_()('ls -la | head -3')  # single string with '|' in shell-like way
```

it uses `str.split('|')` under the hood, so if your arguments contain `|`s you can feed comma separated list instead.

```
_()('gzcat stagedb.sql.gz', 'psql -U usermane pentagon_db')
```

if you need fancy redirections provide tuple (or list) with redirection options instead of string.
options are always two characters, first for `stdout` and second for `stderr`.
for example, 'nt' means "redirect stdout to /dev/null and don't redirect stderr".

there is a special variant for each stream, 'd', which means 'default behaviour'.
by default `pipeish` tryies to do what you expect from the same command when it runs in shell.


```
_()(
 ['ls -la', 'nt'],
 ('grep Pip', 'dd')
)
```

but none of these will cope with exit codes.
for this to work use `Shell` as context manager:

```
with Shell() as _:
    _('true | false')
```

now your python script will exits with the same exit code as bash script with same commands. but it will exit right after exiting `with` scope. nothing below context manager will be executed. to disable this behaviour there is `check` argument:

```
with Shell(check=False) as _:
    _('true | false')

print (_.last_retcode)
```

this way you can run different `Shell`s in one script which allows more complicated scenarios.


to capture outout of command you have to set 'i' option for stdout of last command:
```
with Shell() as _:
    out, err, exit_code = _(['uname -a', 'id'])
```

this looks a bit inconvenient, but this is best replacement for POSIX shell redirection syntax I came up so far.
in this example:
1. output will be captured into `out` and will not be printed in terminal.
similiar to when you do `out = $(uname -a)` in bash, but here you can capture all two streams along with exit code in one call.
2. errors will be printed into terminal and will not be captured. which is happening when you forget to set redirect `2>&1` or `2>/dev/null` in bash script.
you can totally do it by the way in `pipeish` with respective options `r` or `n` for stderr ('ir' or 'in' for this example).
3. `exit_code` will contain exit code of _last_ command. which is you kinda expect when running chain of commands.

more are comming!

feel free to open issues with common use cases, I'll try to prioritize
what seems important and integrate.


Links
-----

"Bash is the JavaScript of systems programming". Strongly agree.
https://github.com/progrium/bashstyle

"shell=True: Security Considerations"
https://docs.python.org/3/library/subprocess.html#security-considerations
