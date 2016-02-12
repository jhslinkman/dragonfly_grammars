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


DYN_MODULE_TYPE = "programming_environment"
DYN_MODULE_NAME = "notebook"
INCOMPATIBLE_MODULES = [
    '',
]


grammar = Grammar('notebook mode')

rules = MappingRule(
    name = 'notebook',
    mapping = {
        "next input": Key("c-c,c-n"),
        "back input": Key("c-c,c-p"),
        "execute": Key("c-c,c-c"),
        "toggle output": Key("c-c,c-e"),
        "show all": Key("c-c,c-v"),
        "kill cell": Key("c-c,c-k"),
        "yank cell": Key("c-c,a-w"),
        "paste cell": Key("c-c,c-y"),
        "back worksheet": Key("c-c,a-lbrace"),
        "next worksheet": Key("c-c,a-rbrace"),
        "new worksheet next": Key("c-c,a-plus"),
        "insert cell above": Key("c-c,c-a"),
        "insert cell below": Key("c-c,c-b"),
        "toggle cell type": Key("c-c,c-t"),
        "set cell type": Key("c-c,c-u"),
        "split cell": Key("c-c,c-s"),
        "merge cell": Key("c-c,c-m"),
        "move cell up": Key("c-c,up"),
        "move cell down": Key("c-c,down"),
        "request help": Key("c-c,c-f"),
        "complete": Key("c-c,c-i"),
        "show trace back": Key("c-c,c-x"),
        "restart kernel": Key("c-c,c-r"),
        "interrupt kernel": Key("c-c,c-z"),
        "close notebook": Key("c-c,c-hash"),
        "console open": Key("c-c,c-o"),
        "jump to source": Key("c-c,c-dot"),
        "jump back": Key("c-c,c-comma"),
        "open scratch": Key("c-c,c-slash"),
        "rename sheet": Key("c-c,exclamation"),
        "open last worksheet": Key("c-c,lbrace"),
        "open next worksheet": Key("c-c,rbrace"),
        "open worksheet <n>": Key("c-c,%(n)d"),
        "execute next": Key("a-enter"),
        "back input history [<n>]": Key("a-p:%(n)d"),
        "next input history [<n>]": Key("a-n:%(n)d")
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
