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
DYN_MODULE_NAME = "html"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('')

rules = MappingRule(
    name = 'html',
    mapping = {
        "fold": Key("c-c,c-f"),
        "element close": Key("c-c,slash"),
        "element child": Key("c-c,c-e,d"),
        "element parent": Key("c-c,c-e,u"),
        "element next": Key("c-c,c-e,n"),
        "element last": Key("c-c,c-e,p"),
        "element select": Key("c-c,c-e,s"),
        "element kill": Key("c-c,c-e,k"),
        "element home": Key("c-c,c-e,d"),
        "element end": Key("c-c,c-e,e"),
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
