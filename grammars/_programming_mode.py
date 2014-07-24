from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer, Function, CompoundRule,
                       RuleRef)
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

class PaddingRule(CompoundRule):
    spec = 'pad <rule>'
    extras = [RuleRef(rules, name = 'rule')]

    def _process_recognition(self, node, extras):
        rule = extras['rule']
        Key('space').execute()
        rule.execute()
        Key('space').execute()

class DoubleRule(CompoundRule):
    spec = '(dub | double) <rule>'
    extras = [RuleRef(rules, name = 'rule')]

    def _process_recognition(self, node, extras):
        rule = extras["rule"]
        rule.execute()
        rule.execute()



grammar.add_rule(rules)
grammar.add_rule(DoubleRule())
grammar.add_rule(PaddingRule())
grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
