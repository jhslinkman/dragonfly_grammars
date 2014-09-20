from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer, Function)


DYN_MODULE_TYPE = "programming_language"
DYN_MODULE_NAME = "javascript"
INCOMPATIBLE_MODULES = [
    # 'python',
]


grammar = Grammar('javascript mode')

rules = MappingRule(
    name = 'javascript',
    mapping = {
        # Keywords:
        "assign": Text(" = "),
        "equals (strict|strictly|exact|exactly)": Text(" === "),
        "greater than": Text(" > "),
        "greater equals": Text(" >= "),
        "((jquery|jay query) (variable|var)|dollar paren)": Text("$()") + Key("left"),  # @IgnorePep8
        "less than": Text(" < "),
        "less equals": Text(" <= "),
        "(line end|end line)": Key("end,semicolon"),
        "not (strict|strictly|exact|exactly) equals": Text(" !== "),
        "(variable|var)": Text("var "),
        "in line function": Key("i,l,f,tab"),
        "(jason | jace on| J S O N)": Key("s-j,s-s,s-o,s-n"),

    },    
    extras = [
        Dictation("text", format=False),
        Dictation("mark", format=False),
        Integer("n", 1, 20000),
        Integer("scroll_by", 1, 20000),
    ],

    defaults = {
        "text" : "", 
        "mark": "a",
        "n" : 1,
        "scroll_by" : 10
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
