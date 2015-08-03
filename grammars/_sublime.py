from dragonfly import (Grammar,
                       AppContext,
                       MappingRule,
                       Key,
                       Text,
                       Dictation,
                       Integer,
                       Function,
                       Mimic)

sublime = AppContext( executable = 'sublime_text')
grammar = Grammar('sublime text', context = (sublime))

load_query_replace = Mimic('enable', 'find', 'replace', 'mode')

num_args =  Key('alt:down') + Text('%(n)d') + Key('alt:up')

rules = MappingRule(
    name = 'sublime',
    mapping = {

        # Editing
        '(comment | uncomment)': Key('c-slash'),

        # Search and replace
        "Q rep": Key("c-f") + load_query_replace,
        "regex Q rep": Key("c-h") + load_query_replace,


        # Working with files and buffers
        "new file": Key("c-n"),
        "open file": Key("c-o"),
        "new window": Key("ctrl:down,s-n,ctrl:up"),
        "kill window": Key("ctrl:down,s-w,ctrl:up"),
        'visit file': Key('c-p'),
        'file save':  Key('c-s'),
        'file save as':  Key('ctrl:down,s-s,ctrl:up'),        
        'layout none':  Key('alt:down,s-1'),
        'layout columns':  Key('alt:down,s-2'),
        'layout row':  Key('alt:down,s-8'),
        'layout grid':  Key('alt:down,s-5'),
        "new group": Key("c-k,ctrl:down,s-up,ctrl:up"),
        "kill group": Key("c-k,c-down,c-w"),
        "next group": Key("c-k,c-right"),
        "last group": Key("c-k,c-left"),
        "send to next group": Key("c-k,ctrl:down,s-right,ctrl:up"),
        "send to last group": Key("c-k,ctrl:down,s-left,ctrl:up"),

        'previous tab [<n>]':  Key('c-pgup:%(n)d'),
        'next tab [<n>]':  Key('c-pgdown:%(n)d'),
        'kill tab': Key('c-w'),
        "go to tab <n>": Key("a-%(n)d"),

        "go to line": Key("c-g"),
        "go to word": Key("c-semicolon"),
        
        # Shell specific commands
        'open shell': Key('ctrl:down,s-t,ctrl:up'),
        "(show | open) console": Key("c-backtick"),
        "command prompt": Key("ctrl:down,s-p,ctrl:up"),

        # Dired commands
        'open ( dire | dired )': Key('f1'),
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
        "( dire | dired ) open": Key("space"),

        ## IJulia commands
        "send": Key("s-enter"),
        "send par": Key("ctrl:down,s-g,ctrl:up,s-enter"),
        "send file": Key("ctrl:down,s-enter,ctrl:up"),
        
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
