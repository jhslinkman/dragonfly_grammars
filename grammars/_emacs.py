from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer, Function)
from grammar_loaders import load_grammar
from query_replace_mode import grammar as query_replace_grammar
emacs = AppContext( title = 'emacs')
grammar = Grammar('emacs', context = (emacs))

load_query_replace = Function(load_grammar(query_replace_grammar))

rules = MappingRule(
    name = 'emacs',
    mapping = {
        '(escape | scape) <text>' : Text('%(text)s'),

        # Editing
        'quote':  Text("''") + Key('left'),
        'double quote':  Text('""') + Key('left'),

        # Search and replace
        '( (fore | forward) search | (S | search) next ) [<n>]':
            Key('c-s:%(n)d'),
        '( (back | backward) search | (S | search) back ) [<n>]':
            Key('c-r:%(n)d'),
        'replace all':
            Key('a-x') + Text('replace-string') + Key('enter'),
        '(Q | query) (rep | replace)':
            Key('alt:down') + Key('percent') + Key('alt:up') +\
            load_query_replace,
#            Key('a-percent'),
        '(regex | regexp) [(Q | query)] (rep | replace)':
            Key('ctrl:down, alt:down') + Key('percent') + Key('alt:up, ctrl:up') +\
            load_query_replace,
#            Key('c-a-percent'),

        # Minibuffer
        'repeat command': Key('c-x, escape, escape'),
        'command history':
            Key('a-x') + Text('list-command-history') + Key('enter'),

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
