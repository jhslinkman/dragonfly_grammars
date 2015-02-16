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


DYN_MODULE_TYPE = "programming"
DYN_MODULE_NAME = "skewer"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('skewer mode')

rules = MappingRule(
    name = 'skewer rules',
    mapping = {
        "skewer form": Key("c-x,c-e"),
        "skewer top form": Key("ctrl:down,a-x,ctrl:up"),
        "skewer (buffer | buff)": Key("c-c,c-k"),
        "skewer repple": Key("c-c,c-z"),
        "skewer log": Key("s,k,e,w,e,r,dot,l,o,g,lparen")
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
