from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer, Function, CompoundRule,
                       RuleRef, Alternative, Choice)
grammar = Grammar('programming mode')

key_rules = MappingRule(
    name = 'key rules',
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
        # '(equals | eek)':
        'eek':
            Key('equal'),
        '( bar | pipe )':
            Key('bar'),
        
        }
    )

class FormattingRule(CompoundRule):
    spec = '[<padding>] [<double>] <rule>'
    extras = [
        RuleRef(key_rules, name = 'rule'),
        Choice('padding', {
            'pad': 1,
            'pad (L | left)': 2,
            'pad (R | right)': 3,
            }),
        Choice('double', {
            '(dub | double)': True
            })]

    def _process_recognition(self, node, extras):
        rule = extras['rule']
        double = extras.get('double', False)
        padding = extras.get('padding', 0)
        if padding == 1 or padding == 2:
            Key('space').execute()
        rule.execute()
        if double:
            rule.execute()
        if padding == 1 or padding == 3:
            Key('space').execute()

rules = MappingRule(
    name = "programming rules",
    mapping = {
        "dot <text>": Key("dot") + Text("%(text)s"),
        },
    extras = [
        Dictation("text", format=False),
        ]
    )

grammar.add_rule(rules)
grammar.add_rule(FormattingRule())
grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
