from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer, Function)
firefox = AppContext( title = 'firefox')
grammar = Grammar('firefox', context = (firefox))


rules = MappingRule(
    name = 'firefox',
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
        "link": Key("squote"),

        "close tab": Key("c-w"),
        "move tab left [<n>]": Key('ctrl:down,shift:down,pgup:%(n)d,shift:up,ctrl:up'),
        "move tab right [<n>]": Key('ctrl:down,shift:down,pgdown:%(n)d,shift:up,ctrl:up'),
        "new tab": Key("c-t"),
        "new window": Key("c-n"),
        "next tab [<n>]": Key("c-tab:%(n)d"),
        "(prev | previous) tab [<n>]": Key("c-pgup:%(n)d"),
        "undo close tab": Key('ctrl:down,shift:down,t,shift:up,ctrl:up'),
        "tab <n>":  Key('c-%(n)d'),

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
def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
