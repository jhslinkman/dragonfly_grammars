from dragonfly import (Grammar, AppContext, MappingRule, Key, Text,
                       Dictation, Integer, Function, CompoundRule,
                       RuleRef, Alternative, Choice)

DYN_MODULE_TYPE = "programming_language"
DYN_MODULE_NAME = "programming"
INCOMPATIBLE_MODULES = []

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
        'caret':
            Key('caret'),
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
        "dash <text>": Key("hyphen") + Text("%(text)s"),
        "quote": Key("dquote"),

        "dot C S V": Key("dot,c,s,v"),
        "dot (jason | jace on | J S O N)": Key("dot,j,s,o,n"),
        "dot J S": Key("dot,j,s"),
        "dot (M D | markdown)": Key("dot,m,d"),
        "dot S Q L": Key("dot,s,q,l"),
        "dot (tex | tech)": Key("dot,t,e,x"),
        "dot T X T": Key("dot,t,x,t"),
        
        "(pail | (L | left) paren)": Key("lparen"),
        "(pair | (R | right) paren)": Key("rparen"),
        "(bale | (L | left) bracket)": Key("lbracket"),
        "(bare | (R | right) bracket)": Key("rbracket"),
        "(braille | (L | left) brace)": Key("lbrace"),
        "(briar | (R | right) brace)": Key("rbrace"),
        "(lang | (L | left) angle)": Key("langle"),
        "(rang | (R | right) angle)": Key("rangle"),
        },
    extras = [
        Dictation("text", format=False),
        ]
    )



grammar.add_rule(rules)
grammar.add_rule(FormattingRule())
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
