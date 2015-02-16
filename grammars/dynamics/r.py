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


DYN_MODULE_TYPE = "programming language"
DYN_MODULE_NAME = "R"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('R rules')

rules = MappingRule(
    name = 'r_rules',
    mapping = {
        "assign": Key("space,langle,hyphen,space"),
        "caret pack": Key("c,a,r,e,t"),

        # basic functions
        "cat": Key("c,a,t,lparen"),
        "seek": Key("s,e,q,lparen"),
        "write [dot] table": Key("w,r,i,t,e,dot,t,a,b,l,e,lparen"),
        "read [dot] table": Key("r,e,a,d,dot,t,a,b,l,e,lparen"),
        "write [dot] csv": Key("w,r,i,t,e,dot,c,s,v,lparen"),
        "read [dot] csv": Key("r,e,a,d,dot,c,s,v,lparen"),

        # R modules
        "R MySQL": Key("s-r,s-m,y,s-s,s-q,s-l"),
        "sis": Key("s-s,y,s"),

        # Emacs specific
        "start R": Key("a-x,s-r"),
        "send": Key("ctrl:down,a-x,ctrl:up"),
        "send line": Key("c-c,c-j"),

        # ESS + noweb
        "s narrow": Key("a-n,n"),
        "s widen": Key("c-x,n,w"),
        "to PDF": Key("a-n,s-p"),
        "knit": Key("a-n,r"),
        "tangle": Key("a-n,s-t"),
                
        # workarounds for Windows/Emacs specific issues
        "turn off graphics": Key("o,p,t,i,o,n,s,lparen,dquote,m,e,n,u,dot,g,r,a,p,h,i,c,s,dquote,equal,s-f,s-a,s-l,s-s,s-e,rparen"),
                
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
