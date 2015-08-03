from dragonfly import (Grammar,
                       AppContext,
                       MappingRule,
                       Key,
                       Text,
                       Dictation,
                       Integer,
                       Function,
                       Mimic)


DYN_MODULE_TYPE = "utilities"
DYN_MODULE_NAME = "find replace"
INCOMPATIBLE_MODULES = [
    '',
]

grammar = Grammar('find replace')

unload_grammar_action = Mimic('disable', 'find', 'replace', 'mode')

rules = MappingRule(
    name = 'find replace',
    mapping = {
        "toggle regex": Key("a-r"),
        "toggle case": Key("a-c"),
        '(rep | replace) [<n>]':
            Key('ctrl:down,shift:down,h:%(n)d,shift:up,ctrl:up'),
        'skip [<n>]':
            Key('f3:%(n)d'),
        'find all':
            Key('exclamation') + unload_grammar_action,
        '(rep | replace) all':
            Key('ctrl:down,shift:down,enter,shift:up,ctrl:up') + unload_grammar_action,
        'quit (Q | query | regex | regexp) (rep | replace)':
            Key('escape') + unload_grammar_action,
    },
    extras = [Integer('n', 1, 100)],
    defaults = {'n': 1}
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
