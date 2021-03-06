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
        "push directory": Key("p,u,s,h,d"),
        "pop directory": Key("p,o,p,d"),
        "list files": Key("l,s,space,hyphen,l,a,enter"),
        "make (directory|dir)": Key("m,k,d,i,r,space"),
        "move": Key("m,v,space"),
        "(R M|remove file)": Key("r,m,space"),
        "(R M D|remove directory)": Key("r,m,space,hyphen,r"),
        "W get ": Key("w,g,e,t,space"),
        "slash user": Key("slash,u,s,r"),
        "slash opt": Key("slash,o,p,t"),
        "slash et cetera": Key("slash,e,t,c"),
        "slash win root": Key("slash,c,y,g,d,r,i,v,e,slash,c"),
        "vim": Key("v,i,m,space"),
        "kill process": Key("c-c"),
        "diff": Key("d,i,f,f,space"),

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
