from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer, Function)
grammar = Grammar('programming mode')

rules = MappingRule(
    name = 'Programming rules',
    mapping = {
        '(ampersand | amp)':
            Key('ampersand'),
        'bang':
            Key('exclamation'),
        'hash':
            Key('hash'),
        '(dash | hyphen)':
            Key('hyphen'),
        'minus':
            Key('minus'),
        'percent':
            Key('percent'),
        'plus':
            Key('plus'),
        '(semicolon | semicol)':
            Key('semicolon'),
        'S quote':
            Key('squote'),
        'D quote':
            Key('dquote'),
        '(underscore | U score)':
            Key('underscore'),
        'dot':
            Key('dot'),
        '(colon | col)':
            Key('colon'),
        'dollar':
            Key('dollar'),
        'at':
            Key('at'),
        '(asterisk | star)':
            Key('asterisk'),
        'slash':
            Key('slash'),
        'backslash':
            Key('backslash'),
        '(equals | eek)':
            Key('equal'),
        '( bar | pipe )':
            Key('bar'),
        
        }
    )


grammar.add_rule(rules)
grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
