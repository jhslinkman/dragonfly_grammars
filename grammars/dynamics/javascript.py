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
        # "and": Text(" && "),
        "assign": Text(" = "),
        "break": Text("break"),
        "case": Text("case "),
        #"case <text>": SCText("case %(text)s"),
        # "catch": Text("catch () {") + Key("left:3"),
        # "comment": Text("// "),
        # "comment <text>": SCText("// %(text)s"),
        # "continue": Text("continue"),
        "close comment": Text(" */"),
        "debugger": Text("debugger"),
        "default": Text("default"),
#         "delete": Text("delete "),  # Messes with ordinary delete command.
        # "do": Text("do {"),
        "equals": Text(" == "),
        "equals (strict|strictly|exact|exactly)": Text(" === "),
        "else": Text("else"),
        # "else if": Text("else if () {") + Key("left:3"),
        "extends ": Text("extends "),
        # "for": Text("for () {") + Key("left:3"),
        #"for <text>": SCText("for (%(text)s) {") + Key("left:3"),
        "false": Text("false"),
        # "finally": Text("finally {") + Key("enter"),
        "function": Text("function "),
        # "function <text>": Function(define_function),
        "greater than": Text(" > "),
        "greater equals": Text(" >= "),
        # "if": Text("if ("),
        # "if <text>": Text("if (%(text)s) {") + Key("left:3"),
        "instanceof": Text("instanceof "),
        "(int|I N T)": Text("int "),
        #"(int|I N T) <text>": SCText("int %(text)s"),
        "in": Text("in "),
        #"in <text>": SCText("in %(text)s"),
        "((jquery|jay query) (variable|var)|dollar paren)": Text("$()") + Key("left"),  # @IgnorePep8
        "less than": Text(" < "),
        "less equals": Text(" <= "),
        "(line end|end line)": Key("end,semicolon"),
        #"(minus|subtract|subtraction)": Text(" - "),
        "(minus|subtract|subtraction) equals": Text(" -= "),
        "modulo": Key("space") + Key("percent") + Key("space"),
        "new": Text("new "),
        "not equals": Text(" != "),
        "not (strict|strictly|exact|exactly) equals": Text(" !== "),
        "open comment": Text("/* "),
        "or": Text(" || "),
        "object": Text("Object "),
        #"(plus|add|addition)": Text(" + "),
        "(plus|add|addition) equals": Text(" += "),
        "reg exp": Text("RegExp"),
        "return": Text("return"),
        #"return <text>": SCText("return %(text)s"),
        "string": Text("String"),
        # "switch": Text("switch () {") + Key("left:3"),
        #"switch <text>": SCText("switch (%(text)s) {") + Key("left:3"),
        "this": Text("this"),
        "throw": Text("throw "),
        "true": Text("true"),
        "try": Text("try {") + Key("enter"),
        "typeof": Text("typeof "),
        "toString": Text("toString()") + Key("left"),
        "(variable|var)": Text("var "),
        #"(variable|var) <text>": SCText("var %(text)s"),
        # "while": Text("while () {") + Key("left:3"),
        #"while <text>": SCText("while (%(text)s) {") + Key("left:3"),
        # "with": Text("with () {") + Key("left:3"),
        #"with <text>": SCText("with (%(text)s) {") + Key("left:3"),
        # Global variables and objects.
        "window": Text("window"),
        "undefined": Text("undefined"),
        "(jason | jace on| J S O N)": Text("s-j,s-s,s-o,s-n"),

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
