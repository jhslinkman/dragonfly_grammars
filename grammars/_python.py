from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer)
neemacs = AppContext( title = 'emacs')
grammar = Grammar('emacs', context = (emacs))
