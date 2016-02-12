from dragonfly import (Grammar,
                       FocusWindow,
                       MappingRule,
                       Mouse,
                       Mimic,
                       Text,
                       Dictation,
                       Integer,
                       Key,
                       Function)

release = Mouse("left:up")

rules = MappingRule(
  name = "general",
  mapping = {
    "pause": Key("f9"),
    "precise": Key("f8"),
    "click": Mouse("left"),
    "control click": Key("ctrl:down") + Mouse("left") + Key("ctrl:up"),
    "control dub click": Key("ctrl:down") + Mouse("left:2") + Key("ctrl:up"),
    "shift click": Key("shift:down") + Mouse("left") + Key("shift:up"),
    "shift dub click": Key("shift:down") + Mouse("left:2") + Key("shift:up"),
    "drag start": Mouse("left:down"),
    "drag stop": release,
    "dub click": Mouse("left:2"),
    "right click": Mouse("right"),
    "dub right click": Mouse("right:2"),
    "mouse release": release,
    "scroll start": Key("f11:down"),
    "scroll stop": Key("f11:up"),
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

grammar = Grammar("general")
grammar.add_rule(rules)
grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
