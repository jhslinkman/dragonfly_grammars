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

        # Editing
        '(comment | uncomment)': Key('a-semicolon'),
        '(comment | uncomment) line': Key('a-m,c-space,end,a-semicolon'),
        'kill comment': Key('c-u,a-semicolon'),
        'set comment column': Key('c-x,semicolon'),
        'insert comment below': Key('a-j'),
        'comment region': Key('c-c,c-c'),

        # Code evaluation
        'eval expression':  Key('a-colon'),
        'eval last [sexp]':  Key('c-x,c-e'),
        'eval defun':  Key('ctrl:down,alt:down,x,alt:up,ctrl:up'),
        'eval region': Key('a-x,e,v,a,l,hyphen,r,e,g,i,o,n,enter'),
        'eval buffer': Key('a-x,e,v,a,l,hyphen,b,u,f,f,e,r,enter'),
                
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
        'file save as':  Key('c-x, c-w'),
        
        'new window':  Key('c-x, 3'),
        'new window down':  Key('c-x, 2'),
        'previous window':  Key('c-minus, c-x, o'),
        'next window':  Key('c-x, o'),
        'kill window': Key('c-x, 0'),
        'kill other windows': Key('c-x, 1'),

        'next buffer': Key('c-x,right'),
        'previous buffer': Key('c-x,right'),
        'buffer menu': Key('a-x') + Text('buffer-menu') + Key('enter'),
        'kill buffer': Key('c-x, k, enter'),

        # Working with Emacs itself
        'suspend Emacs': Key('c-z'),
        'minimize Emacs': Key('c-z'),
        'kill Emacs kill': Key('c-x, c-c'),
        
        # Shell specific commands
        'open shell': Key('a-x') + Text('shell') + Key('enter'),
        'last command [<n>]': Key('c-up:%(n)d'),
        'next command [<n>]': Key('c-down:%(n)d'),

        # Specific to simple-httpd.el
        'start server': Key('a-x') + Text('httpd-start') + Key('enter'),
        'stop server': Key('a-x') + Text('httpd-stop') + Key('enter'),
        'set server root': Key('a-x') + Text('set-server-root') + Key('enter'),

        # yasnippet commands
        'snip': Key('a-x,y,a,s,hyphen,e,x,p,a,n,d,enter'),
        'insert snippet': Key('a-x,y,a,s,hyphen,i,n,s,e,r,t,hyphen,s,n,i,p,p,e,t,enter'),
                
        # Some python specific commands, move these to another file
        'ipython shell': Key('a-x') + Text('ipython') + Key('enter'),
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
