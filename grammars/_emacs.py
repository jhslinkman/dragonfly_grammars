from dragonfly import (Grammar,
                       AppContext,
                       MappingRule,
                       Key,
                       Text,
                       Dictation,
                       Integer,
                       Function,
                       Mimic)

emacs = AppContext( title = 'emacs')
grammar = Grammar('emacs', context = (emacs))

load_query_replace = Mimic('enable', 'Q', 'rep', 'mode')

num_args =  Key('alt:down') + Text('%(n)d') + Key('alt:up')

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
        'eval (fun | function)':  Key('a-x'),
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
            Key('a-x,l,i,s,t,hyphen,c,o,m,m,a,n,d,hyphen,h,i,s,t,o,r,y,enter'),

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
        'shrink window horizontally [<n>]': Key('c-minus') + num_args + Key('c-x,rbrace'),
        'enlarge window horizontally [<n>]': num_args + Key('c-x,rbrace'),
        'shrink window [<n>]': Key('c-minus') + num_args + Key('c-x,caret'),
        'enlarge window [<n>]': num_args + Key('c-x,caret'),
        "switch to scratch": Key("a-x,s,w,i,t,c,h,hyphen,t,o,hyphen,b,u,f,f,e,r,enter/50") + Key("asterisk,s,c,r,a,t,c,h,asterisk"),

        'next buffer': Key('c-x,right'),
        'previous buffer': Key('c-x,right'),
        'buffer menu': Key('a-x,b,u,f,f,e,r,hyphen,m,e,n,u,enter'),
        'kill buffer': Key('c-x, k, enter'),

        # Open HTML preview of current buffer (requires html-preview function)
        "html preview": Key("a-x,h,t,m,l,hyphen,p,r,e,v,i,e,w,enter"),

        # Working with Emacs itself
        'suspend Emacs': Key('c-z'),
        'minimize Emacs': Key('c-z'),
        'close Emacs close': Key('c-x, c-c'),

        # Shell specific commands
        'open shell': Key('a-x,s,h,e,l,l,enter'),
        'open cygwin shell': Key('a-x,c,y,g,w,i,n,hyphen,s,h,e,l,l,enter'),
        'last command [<n>]': Key('c-up:%(n)d'),
        'next command [<n>]': Key('c-down:%(n)d'),

        # Specific to simple-httpd.el
        'start server': Key('a-x,h,t,t,p,d,hyphen,s,t,a,r,t,enter'),
        'stop server': Key('a-x,h,t,t,p,d,hyphen,s,t,o,p,enter'),
        'set server root': Key('a-x,s,e,t,hyphen,s,e,r,v,e,r,hyphen,r,o,o,t,enter'),

        # yasnippet commands
        'snip': Key('a-x,y,a,s,hyphen,e,x,p,a,n,d,enter'),
        'insert snippet': Key('a-x,y,a,s,hyphen,i,n,s,e,r,t,hyphen,s,n,i,p,p,e,t,enter'),

        # Dired commands
        'open ( dire | dired )': Key('c-x,d'),
        'quit ( dire | dired )': Key('q'),
        '( dire | dired ) update': Key('g'),
        '( dire | dired ) flag': Key('d'),
        '( dire | dired ) mark': Key('m'),
        '( dire | dired ) toggle marks': Key('t'),
        '( dire | dired ) (unmark | unflag)': Key('u'),
        '( dire | dired ) (unmark | unflag) all': Key('s-u'),
        '( dire | dired ) delete': Key('x'),
        '( dire | dired ) flag auto save': Key('hash'),
        '( dire | dired ) flag backup': Key('tilde'),
        '( dire | dired ) clean directory': Key('dot'),
        '( dire | dired ) flag garbage files': Key('percent,ampersand'),
        '( dire | dired ) flag files regex': Key('percent,d'),
        # '( dire | dired ) visit': Key('f'),
        '( dire | dired ) visit other': Key('o'),
        '( dire | dired ) view [file]': Key('v'),
        '( dire | dired ) visit parent': Key('caret'),
        '( dire | dired ) copy': Key('s-c'),
        '( dire | dired ) rename': Key('s-r'),
        '( dire | dired ) make (dir | directory)': Key('plus'),
        '( dire | dired ) shell': Key('exclamation'),
        '( dire | dired ) async shell': Key('ampersand'),

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
