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


DYN_MODULE_TYPE = "utilities"
DYN_MODULE_NAME = "bash"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('')

rules = MappingRule(
    name = '',
    mapping = {
        "(change (directory|dir)|C D)": Key("c,d,space"),
        "list files": Key("l,s,space,hyphen,l,a,enter"),
        "make (directory|dir)": Key("m,k,d,i,r,space"),
        "move": Key("m,v,space"),
        "(R M|remove file)": Key("r,m,space"),
        "(R M D|remove directory)": Key("r,m,space,hyphen,r"),
        "W get ": Key("w,g,e,t,space"),

        # remote server commands
        "S S H": Key("f,a,k,e,c,y,g,p,t,y,space,s,s,h"),
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
