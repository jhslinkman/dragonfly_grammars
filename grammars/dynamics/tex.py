from dragonfly import (
    Grammar,
    AppContext,
    MappingRule,
    Key,
    Text, 
    Dictation,
    Integer,
    Function
)


DYN_MODULE_TYPE = "typesetting_language"
DYN_MODULE_NAME = "tex"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('')

rules = MappingRule(
    name = '',
    mapping = {
        'insert section': Key('c-c,c-s'),
        'macro': Key('c-c,enter'),
        'end macro': Key('ctrl:down,a-i,ctrl:up'),
        'insert (environment | environ)': Key('c-c,c-e'),
        'change (environment | environ)': Key('c-u,c-c,c-e'),
        'end (environment | environ)': Key('c-c,rparen'),
        'insert item': Key('c-c,c-j'),

        'emphasize': Key('c-c,c-f,c-e'),
        'bold': Key('c-c,c-f,c-b'),
        'typewriter': Key('c-c,c-f,c-t'),
        'small caps': Key('c-c,c-f,c-c'),
        'sans serif': Key('c-c,c-f,c-f'),
        'italicize': Key('c-c,c-f,c-i'),
        'slant': Key('c-c,c-f,c-s'),
        'roman': Key('c-c,c-f,c-r'),
        'calligraphic': Key('c-c,c-f,c-a'),
        'change emphasize': Key('c-u,c-c,c-f,c-e'),
        'change bold': Key('c-u,c-c,c-f,c-b'),
        'change typewriter': Key('c-u,c-c,c-f,c-t'),
        'change small caps': Key('c-u,c-c,c-f,c-c'),
        'change sans serif': Key('c-u,c-c,c-f,c-f'),
        'change italicize': Key('c-u,c-c,c-f,c-i'),
        'change slant': Key('c-u,c-c,c-f,c-s'),
        'change roman': Key('c-u,c-c,c-f,c-r'),
        'change calligraphic': Key('c-u,c-c,c-f,c-a'),
        'delete font': Key('c-c, c-f,c-d'),

        'comment (paragraph | par)': Key('c-c,percent'),
        'format (environment | environ)': Key('c-c,c-q,c-e'),
        'format (paragraph | par)': Key('c-c,c-q,c-p'),
        'format region': Key('c-c,c-q,c-r'),
        'format section': Key('c-c,c-q,c-s'),
        'mark (environment | environ)': Key('c-c,dot'),
        'mark section': Key('c-c,asterisk'),
        'go to (environment | environ) start': Key('ctrl:down,a-a,ctrl:up'),
        'go to (environment | environ) end': Key('ctrl:down,a-e,ctrl:up'),

        'fold mode': Key('c-c,c-o,c-f'),
        'hide buffer': Key('c-c,c-o,c-b'),
        'hide region': Key('c-c,c-o,c-r'),
        'hide (paragraph | par)': Key('c-c,c-o,c-p'),
        'hide macro': Key('c-c,c-o,enter'),
        'hide (environment | environ)': Key('c-c,c-o,c-e'),
        'hide comment': Key('c-c,c-o,c-c'),
        'show buffer': Key('c-c,c-o,b'),
        'show region': Key('c-c,c-o,r'),
        'show (paragraph | par)': Key('c-c,c-o,p'),
        'show item': Key('c-c,c-o,i'),
        'hide item': Key('c-c, c-o, c-o'),
                
    },    
    extras = [
        Dictation("text", format=False),
        Integer("n", 1, 20000),
    ],

    defaults = {
        "text" : "", 
        "n" : 1,
    }
)



grammar.add_rule(rules)
grammar.load()
grammar.disable()


def dynamic_enable():
    global grammar
    if grammar.enabled:
        return False
    else:
        grammar.enable()
        return True


def dynamic_disable():
    global grammar
    if grammar.enabled:
        grammar.disable()
        return True
    else:
        return False


def is_enabled():
    global grammar
    if grammar.enabled:
        return True
    else:
        return False


def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
