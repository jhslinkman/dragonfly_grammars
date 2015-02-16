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


DYN_MODULE_TYPE = "programming_language"
DYN_MODULE_NAME = "SQL"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('SQL')

rules = MappingRule(
    name = 'SQL',
    mapping = {
        "my (s q l | sequel)": Key("m,y,s,q,l"),
        "select": Key("s,e,l,e,c,t"),
        "select star": Key("s,e,l,e,c,t,space,asterisk,space"),
        "descending": Key("d,e,s,c"),
        "ascending": Key("a,s,c"),
        "start (s q l | sequel) server": Key("a-x,s,q,l,hyphen,m,y,s,q,l,enter"),
        "char": Key("C,H,A,R"),
        "var char": Key("V,A,R,C,H,A,R"),

        "send (par | paragraph)": Key("c-c,c-c"),
        "send region": Key("c-c,c-r"),
        "send buffer": Key("c-c,c-b"),
        "send string": Key("c-c,c-s"),
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
