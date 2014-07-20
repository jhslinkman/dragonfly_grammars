from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer)
emacs = AppContext( title = 'emacs')
grammar = Grammar('emacs', context = (emacs))

rules = MappingRule(
    name = 'emacs',
    mapping = {
        'escape <text>'                      : Text('%(text)s'),

        # Movement
        'cent line': Key('c-l'),
        'bow [<n>]'                      : Key('c-left:%(n)d'),
        'fow [<n>]'                      : Key('c-right:%(n)d'),
        'sel bow [<n>]': Key('c-space, c-right:%(n)d, a-w'),
        'sel fow [<n>]': Key('c-space, c-right:%(n)d, a-w'),

        # Editing
        'undo'                      : Key('c-x, u'),
        'quote':  Text("''") + Key('left'),
        'double quote':  Text('""') + Key('left'),

        'yank line'                      : Key('c-a, c-space, c-e, a-w'),
        'paste [that]'                      : Key('c-y'),
#        'paste'                      : Key('c-y'),

        # Working with files and buffers
        'visit file': Key('c-x, c-f'),
        'file save':  Key('c-x, c-s'),
        
        'new window':  Key('c-x, 3'),
        'new window down':  Key('c-x, 2'),
        'previous window':  Key('c-minus, c-x, o'),
        'next window':  Key('c-x, o'),
        'kill window': Key('c-x, 0'),
        'kill other windows': Key('c-x, 1'),

        'buffer menu': Key('a-x') + Text('buffer-menu') + Key('enter'),
        'kill buffer': Key('c-x, k, enter'),

        # Working with Emacs itself
        'suspend Emacs': Key('c-z'),
        'minimize Emacs': Key('c-z'),
        'kill Emacs kill': Key('c-x, c-c'),
    },

    extras = [
        Dictation("text", format=False),
        Dictation("mark", format=False),
        Integer("n", 1, 20000),
        Integer("scroll_by", 1, 20000),
    ],

    defaults = {
        "text" : "", 
        "mark": "a",
        "n" : 1,
        "scroll_by" : 10
    }
)

grammar.add_rule(rules)
grammar.load()
def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
