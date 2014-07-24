# Vision for Dragonfly Soar

Want to wrap `_multiedit.py` around a dynamic rule loader so the following can be possible:

1. Saying "programming mode on" loads a set of rules specific to programming, and integrates them with the already existing multi-edit grammar.
2. Rules can be context specific, so that, e.g., the rules for multi-edit differ between Emacs and other programs.

## Rough layout for the project

```
_base.py                    # The base grammar, modeled after _multiedit.py.
_loaders.py
static_rules/		    # Directory containing rules that are always loaded.
dynamic_rules/              # Directory containing rules to be dynamically loaded.
    programming_mode.py	    # Rules to be integrated with the grammar _base.py
    			    #  when the command "programming mode on " is spoken.
```