from dragonfly import (Grammar,
                       FocusWindow,
                       MappingRule,
                       Mimic,
                       Text,
                       Dictation,
                       Integer,
                       Key)

rules = MappingRule(
	name = "general",
	mapping = {
        '(escape | scape) <text>' : Text('%(text)s'),
		"slap": Key("enter"),
		"max (when | win | window)": Key("w-up"),
		"left (when | win | window) [<n>]": Key("w-left:%(n)d"),
		"right (when | win | window) [<n>]": Key("w-right:%(n)d"),
		"min (when | win | window)": Key("w-down"),
        "switch apps": Key("alt:down, tab"),
		"switch app": Key("a-tab"),
        "code mode": Mimic("\\no-caps-on") + Mimic("\\no-space-on"),
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
