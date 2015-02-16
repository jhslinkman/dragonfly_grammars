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


DYN_MODULE_TYPE = "Emacs mode"
DYN_MODULE_NAME = "org"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('org mode')

rules = MappingRule(
    name = 'org mode',
    mapping = {
        "to do": Key("c-c,c-t"),
        "sparse tree": Key("c-c,slash"),
        "show global to do": Key("c-c,a,t"),
        "insert to do": Key("shift:down,a-enter,shift:up"),
        "visit link": Key("c-c,c-o"),
        "insert link": Key("c-c,c-l"),
        "fold document": Key("s-tab"),
        "scheduled task": Key("c-c,c-s"),
        "show agenda": Key("c-c,a,a")
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
