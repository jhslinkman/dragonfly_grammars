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
DYN_MODULE_NAME = "Q rep"
INCOMPATIBLE_MODULES = [
    '',
]

grammar = Grammar('')

unload_grammar_action = Mimic('disable', 'Q', 'rep', 'mode')

rules = MappingRule(
    name = 'query replace',
    mapping = {
        '(rep | replace) [<n>]':
            Key('space:%(n)d'),
        'skip [<n>]':
            Key('backspace:%(n)d'),
        '(rep | replace) [and] hold':
            Key('comma'),
        '(rep | replace) quit':
            Key('dot') + unload_grammar_action,
        'Q (rep | replace) all':
            Key('exclamation') + unload_grammar_action,
        'Q back':
            Key('caret'),
        'Q edit':
            Key('e'),
        '(rec | recursive) edit':
            Key('c-r'),
        '(rec | recursive) edit [and] (del | delete)':
            Key('c-w'),
        'quit (rec | recursive) edit':
            Key('ctrl:down, alt:down, c, ctrl:up, alt:up'),
        'quit (Q | query | regex | regexp) (rep | replace)':
            Key('c-g:2') + unload_grammar_action,
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
