from dragonfly import (Grammar, FocusWindow, MappingRule, Key, Config, Section, Item, Playback, Mimic)

rules = MappingRule(
	name = "general",
	mapping = { 
		"slap": Key("enter"),
		"max (when | win | window)": Key("w-up"),
		"left (when | win | window)": Key("w-left"),
		"right (when | win | window)": Key("w-right"),
		"min (when | win | window)": Key("w-down"),
    "switch apps": Key("alt:down, tab"),
		"switch app": Key("a-tab"),
    "termi": Key("w-b/10, s-tab/10, enter"),
    "foxy": Key("w-b/10, s-tab/10, right:1/10, enter"),
    "foxy reload": Key("w-b/10, s-tab/10, right:1/10, enter/10, f5"),
    "Jimmy": Key("w-b/10, s-tab/10, right:2/10, enter"), 
    "Heidi": Key("w-b/10, s-tab/10, right:3/10, enter"),
    "chrome": Key("w-b/10, s-tab/10, right:4/10, enter"),
    "chrome reload": Key("w-b/10, s-tab/10, right:4/10, enter/10, f5"),
    "bashing": Key("w-b/10, s-tab/10, right:5/10, enter"),
    "code mode": Mimic("\\no-caps-on") + Mimic("\\no-space-on"),
	}
)

grammar = Grammar("general")
grammar.add_rule(rules)
grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
