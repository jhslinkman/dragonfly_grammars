## Problems with the dragonfly package

- Need to add the following to `dragonfly/actions/typeables.py`:
```
    "semicolon":    keyboard.get_typeable(char=';'),
```
- Investigate why dragonfly doesn't recognize `Key('a-percent')`.