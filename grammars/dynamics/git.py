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
DYN_MODULE_NAME = "git"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('')

git = Key("g,i,t,space")

rules = MappingRule(
    name = '',
    mapping = {
        "git pull [<text>]": git + Key("p,u,l,l,space") + Text("%(text)s"),
        "git fetch [<text>]": git + Key("f,e,t,c,h,space") + Text("%(text)s"),
        "git push [<text>]": git + Key("p,u,s,h,space") + Text("%(text)s"),
        "git clone [<text>]": git + Key("c,l,o,n,e,space") + Text("%(text)s"),
        "git status": git + Key("s,t,a,t,u,s,space") + Text("%(text)s"),
        "git branch": git + Key("b,r,a,n,c,h,space") + Text("%(text)s"),
        "git commit all": git + Key("c,o,m,m,i,t,space,hyphen,a,space,hyphen,m,space") + Text("%(text)s"),
        "git commit": git + Key("c,o,m,m,i,t,space,hyphen,m,space") + Text("%(text)s"),
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
