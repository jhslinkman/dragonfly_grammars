from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer, Function)
firefox = AppContext( title = 'firefox')
grammar = Grammar('firefox', context = (firefox))

mapping = {
    "back": Key('backspace'),
    "forward": Key('s-backspace'),
    "reload": Key('c-r'),
    "force reload": Key('ctrl:down,shift:down,r,shift:up,ctrl:up'),
    "stop": Key('escape'),


    "zoom in [<n>]": Key("c-plus:%(n)d"),
    "zoom out [<n>]": Key("c-minus:%(n)d"),
    "zoom reset": Key("c-0"),

    "find": Key("c-f"),
    "find again [<n>]": Key("c-g:%(n)d"),
    "find (prev | previous) [<n>]": Key('ctrl:down,shift:down,g:%(n)d,shift:up,ctrl:up'),
    "link [<text>]": Key("squote") + Text("%(text)s"),

    "close tab": Key("c-w"),
    "move tab left [<n>]": Key('ctrl:down,shift:down,pgup:%(n)d,shift:up,ctrl:up'),
    "move tab right [<n>]": Key('ctrl:down,shift:down,pgdown:%(n)d,shift:up,ctrl:up'),
    "new tab": Key("c-t"),
    "new window": Key("c-n"),
    "next tab [<n>]": Key("c-tab:%(n)d"),
    "(prev | previous) tab [<n>]": Key("c-pgup:%(n)d"),
    "undo close tab": Key('ctrl:down,shift:down,t,shift:up,ctrl:up'),
    # "tab <n>":  Key('c-%(n)d'),

    "show history": Key('ctrl:down,shift:down,h,shift:up,ctrl:up'),
    "show bookmarks": Key('ctrl:down,shift:down,b,shift:up,ctrl:up'),
    "bookmark page": Key("c-d"),

    "(dev | developer) tools": Key("f12"),
    "web console": Key("ctrl:down,shift:down,k,shift:up,ctrl:up"),
    "inspector": Key("ctrl:down,shift:down,c,shift:up,ctrl:up"),
    "debugger": Key("ctrl:down,shift:down,s,shift:up,ctrl:up"),
    "style editor": Key("s-f7"),
    "profiler": Key("s-f5"),
    "network": Key("ctrl:down,shift:down,q,shift:up,ctrl:up"),
    "developer toolbar": Key("s-f2"),
    "responsive design view": Key("ctrl:down,shift:down,m,shift:up,ctrl:up"),
    "scratchpad": Key("s-f4"),
    "page source": Key("c-u"),
    "browser console": Key("ctrl:down,shift:down,j,shift:up,ctrl:up"),

    "next page": Key("right"),
    "(prev | previous) page": Key("left"),
    "rotate": Key("r"),
    "rotate (counter | counterclockwise)": Key("s-r"),
    "presentation mode": Key("ctrl:down,alt:down,p,alt:up,ctrl:up"),
    "go to page": Key("ctrl:down,alt:down,g,alt:up,ctrl:up"),
}

cs = lambda k: Key("ctrl:down,shift:down") + k + Key("ctrl:up,shift:up")

mapping.update({

    # Global
    "help": Key("f1"),
    "show command history": Key("c-h"),
    "toggle firebug": Key("f12"),
    "deactivate firebug": Key("s-f12"),
    "open firebug [in] window": Key("c-f12"),
    "switch [to previous] panel": Key("c-backtick"),
    "toggle command line [popup]": cs(Key("l")),
    "toggle inspect mode": cs(Key("c")),
    "toggle javascript profiler": cs(Key("p")),
    "execute last command": cs(Key("e")),
    "finish editing": Key("s-enter"),
    "next field": Key("enter"),
    "(prev | previous) field": Key("s-tab"),
    "next panel": cs(Key("pgup")),
    "(prev | previous) panel": cs(Key("pgdown")),

    # console panel
    "clear console": Key("a-r"),
    "focus command line": cs(Key("l")),
    "inspect result": Key("s-enter"),
    "show completion": Key("c-space"),
    "execute": Key("c-enter"),

    # HTML
    "next node": Key("c-dot"),
    "(prev | previous) node": Key("c-comma"),
    # "finish editing":  Key("c-enter")  # conflicts with console command
    "inspect element": cs(Key("c")),
    "inspect parent": Key("c-up"),
    "inspect child": Key("c-down"),

    # script panel
    "rerun": Key("s-f8"),
    "continue": Key("f8"),
    "step over": Key("f10"),
    "step into": Key("f11"),
    "step out": Key("s-f11"),
    "next function": Key("c-dot"),
    "(prev | previous) function": Key("c-comma"),
    "focus scripts location": Key("c-space"),
    "focus watch side panel": cs(Key("n")),
    "go to line number": Key("c-l"),

    # DOM panel
    "next object": Key("c-dot"),
    "(prev | previous) object ": Key("c-comma"),

    })

rules = MappingRule(
    name = 'firefox',
    mapping = mapping,

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
def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
