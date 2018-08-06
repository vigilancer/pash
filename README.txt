initially was named after a friend from school, Pavel Hurgcheev - `pash`. then
`psh`. until free name was found - `pipeish`.

it's like pipes in shell but not exactly. hence `pipe-ish`.

[picture-of-python-looking-like-a-shell]

# Examples:
# pattern = 'Pip'
# (_('ls') | _(f'grep {pattern}')).stdout

```
from pipeish.commands import Command as _
print(_('ls -la')() | _('grep pipeish') | _('grep 20'))
```

