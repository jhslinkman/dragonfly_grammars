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


DYN_MODULE_TYPE = "utility"
DYN_MODULE_NAME = "pivotal tracker"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('pivotal tracker')

rules = MappingRule(
    name = 'pivotal tracker',
    mapping = {
        "toggle backlog": Key("s-b"),
        "toggle [charts | graphs]": Key("s-g"),
        "toggle done": Key("s-d"),
        "toggle history": Key("s-h"),
        "toggle icebox": Key("s-i"),
        "toggle my work": Key("s-w"),
        "toggle (labels | searches)": Key("s-l"),
        "toggle current": Key("s-c"),
        "toggle notifications": Key("s-n"),
        "toggle epic": Key("s-e"),
        "toggle help":  Key("question"),
        "add story":  Key("a"),
        "add epic":  Key("e"),
        "search":  Key("slash"),
        "save story":  Key("c-s"),
        "save comment":  Key("s-enter"),
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
