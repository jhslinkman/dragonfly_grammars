from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer, Function)
from grammar_loaders import unload_grammar
emacs = AppContext( title = 'emacs')
grammar = Grammar('query-replace mode', context = (emacs))

unload_grammar_action = Function(unload_grammar(grammar))

rules = MappingRule(
    name = 'query replace',
    mapping = {
        '(rep | replace)':
            Key('space'),
        'skip':
            Key('backspace'),
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
    }
)

grammar.add_rule(rules)
