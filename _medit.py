from natlink import setMicState
from aenea import (
    Grammar,
    MappingRule,
    Text,
    Key,
    Function,
    Dictation,
    Choice,
    Window,
    Config,
    Section,
    Item,
    IntegerRef,
    Alternative,
    RuleRef,
    Repetition,
    CompoundRule,
    AppContext,
)

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')

from format import (
    format_text,
    FormatTypes as ft,
)

RELEASE = Key("shift:up, ctrl:up, alt:up")

formatMap = {
    "(sentence|sense|since) case": ft.sentenceCase,
    "cam": ft.camelCase,
    "big cam": ft.pascalCase,
    "score": ft.snakeCase,
    "uppercase": ft.upperCase,
    "lowercase": ft.lowerCase,
    "squash": ft.squash,
    "lowercase squash": [ft.squash, ft.lowerCase],
    "uppercase squash": [ft.squash, ft.upperCase],
    "squash lowercase": [ft.squash, ft.lowerCase],
    "squash uppercase": [ft.squash, ft.upperCase],
    "dashy": ft.dashify,
    "lowercase dashy": [ft.dashify, ft.lowerCase],
    "uppercase dashy": [ft.dashify, ft.upperCase],
    "dashy lowercase": [ft.dashify, ft.lowerCase],
    "dashy uppercase": [ft.dashify, ft.upperCase],
    "dottie": ft.dotify,
    "lowercase dottie": [ft.dotify, ft.lowerCase],
    "uppercase dottie": [ft.dotify, ft.upperCase],
    "dottie lowercase": [ft.dotify, ft.lowerCase],
    "dottie uppercase": [ft.dotify, ft.upperCase],
    "say": ft.spokenForm,
    "(as env | environment variable)": [ft.snakeCase, ft.upperCase],
}

class MultiEditBuilder:
    def __init__( self, name, context=None):
        self._name = name
        self._context = context

        self._alphabet = {}
        self.update_alphabet({
            "air": "a",
            "bat": "b",
            "cap": "c",
            "drum": "d",
            "each": "e",
            "fine": "f",
            "gust": "g",
            "harp": "h",
            "sit": "i",
            "jury": "j",
            "crunch": "k",
            "look": "l",
            "made": "m",
            "near": "n",
            "odd": "o",
            "pit": "p",
            "quench": "q",
            "red": "r",
            "sun": "s",
            "trap": "t",
            "urge": "u",
            "vest": "v",
            "whale": "w",
            "plex": "x",
            "yank": "y",
            "zip": "z",
        })

        self._numbers = {}

        self._symbols = {}
        self.update_symbols({
            "pale": "lparen",
            "pair": "rparen",
            "bail": "[",
            "bear": "]",
            "braille": "{",
            "br'er": "}",
            "lang": "<",
            "rang": ">",
            "comma": "comma",
            "dot": ".",
            "dash": "-",
            "minus": "-",
            "eek": "=",
            "equals": "=",
            "plus": "+",
            "tiled": "~",
            "tilde": "~",
            "backtick": "`",
            "tick": "`",
            "bang": "!",
            "at": "@",
            "hash": "#",
            "doll": "$",
            "dollar": "$",
            "purse": "percent",
            "percent": "percent",
            "care": "^",
            "caret": "caret",
            "amp": "ampersand",
            "star": "*",
            "cole": ":",
            "colon": ":",
            "semi": ";",
            "semicolon": ";",
            "D quote": "\"",

            # TODO quote is sent as text
            "quote": "'",
            "S quote": "'",
            "backslash": "\\",
            "slash": "/",
            "quest": "?",
            "you score": "_",

            "slap": "enter",
            "enter": "enter",
            "space": "space",
            "tab": "tab",
        })

        self._navigation = {}
        self.update_navigation({
            "up [<n>]": Key("up:%(n)d"),
            "down [<n>]": Key("down:%(n)d"),
            "left [<n>]": Key("left:%(n)d"),
            "right [<n>]": Key("right:%(n)d"),
            "page up [<n>]": Key("pgup:%(n)d"),
            "pup [<n>]": Key("pgup:%(n)d"),
            "page down [<n>]": Key("pgdown:%(n)d"),
            "drop [<n>]": Key("pgdown:%(n)d"),
            "home": Key("home"),
            "end": Key("end"),
            "doc home": Key("c-home/3"),
            "doc end": Key("c-end/3"),
        })

        self._control = {}
        self.update_control({
            "cape": Key("escape"),
            "dub cape": Key("escape") * 2,
        })

        self._editing = {}
        self.update_editing({
            "paste": Key('c-v'),
            "copy": Key('c-c'),
            "cut": Key('c-x'),
            "backspace [<n>]": Key('backspace:%(n)d'),
            "back [<n>]": Key('backspace:%(n)d'),
            "delete [<n>]": Key('del:%(n)d'),
            "dell [<n>]": Key('del:%(n)d'),
        })

        self._formatters = {}
        self.update_formatters({
            "(sentence|sense|since) case": ft.sentenceCase,
            "cam": ft.camelCase,
            "big cam": ft.pascalCase,
            "pass": ft.pascalCase,
            "score": ft.snakeCase,
            "uppercase": ft.upperCase,
            "lowercase": ft.lowerCase,
            "squash": ft.squash,
            "lowercase squash": [ft.squash, ft.lowerCase],
            "uppercase squash": [ft.squash, ft.upperCase],
            "squash lowercase": [ft.squash, ft.lowerCase],
            "squash uppercase": [ft.squash, ft.upperCase],
            "dashy": ft.dashify,
            "lowercase dashy": [ft.dashify, ft.lowerCase],
            "uppercase dashy": [ft.dashify, ft.upperCase],
            "dashy lowercase": [ft.dashify, ft.lowerCase],
            "dashy uppercase": [ft.dashify, ft.upperCase],
            "dottie": ft.dotify,
            "lowercase dottie": [ft.dotify, ft.lowerCase],
            "uppercase dottie": [ft.dotify, ft.upperCase],
            "dottie lowercase": [ft.dotify, ft.lowerCase],
            "dottie uppercase": [ft.dotify, ft.upperCase],
            "say": ft.spokenForm,
            "(as env | environment variable)": [ft.snakeCase, ft.upperCase],
        })

    def update_alphabet(self, updates):
        self._alphabet.update(updates)

    def update_numbers(self, updates):
        self._numbers.update(updates)

    def update_symbols(self, updates):
        self._symbols.update(updates)

    def update_navigation(self, updates):
        self._navigation.update(updates)

    def update_control(self, updates):
        self._control.update(updates)

    def update_editing(self, updates):
        self._editing.update(updates)

    def update_formatters(self, updates):
        self._formatters.update(updates)

    def update_mapping(self, mapping, updates):
        for key, value in updates.iteritems():
            if not mapping.get(key, None):
                mapping[key] = value
            else:
                raise KeyError('command "{0}" already defined'.format(key))

    def build_keystroke_rule(self):
        atoms = {}

        for sound, letter in self._alphabet.iteritems():
            atoms[sound] =  Key(letter)
            atoms['dub {0}'.format(sound)] =  Key(letter) * 2
            atoms['big {0}'.format(sound)] =  Key('s-{0}'.format(letter))

        for sound, number in self._numbers.iteritems():
            atoms[sound] =  Key(number)

        space = Key('space')

        for sound, symbol in self._symbols.iteritems():
            sounds = [
                    (sound, Key(symbol)),
                    ('dub {0}'.format(sound), Key(symbol) * 2),
                    ('trip {0}'.format(sound), Key(symbol) * 3),
                    ]
            for _sound, action in sounds:
                atoms[_sound] = action
                atoms['pad {0}'.format(_sound)] = space + action + space
                atoms['pad left {0}'.format(_sound)] = space + action
                atoms['pad right {0}'.format(_sound)] = action + space

        atoms['<formatType> <text>'] = Function(format_text)

        for partial in [
             self._editing,
             self._navigation,
             self._control,
             ]:
            self.update_mapping(atoms, partial)

        return MappingRule(
                mapping=atoms,
                extras=[
                    IntegerRef('n', 1, 100),
                    Choice("formatType", self._formatters),
                    Dictation("text"),
                ],
                defaults={
                    'n': 1
                }
            )

    def build_repeat_rule(self, keystroke_rule):
        alternatives = []
        alternatives.append(RuleRef(rule=keystroke_rule))
        single_action = Alternative(alternatives)

        sequence = Repetition(single_action, min=1, max=16, name="sequence")

        class RepeatRule(CompoundRule):
            # Here we define this rule's spoken-form and special elements.
            spec = "<sequence> [[[and] do [that]] <n> [times]]"
            extras = [
                sequence,  # Sequence of actions defined above.
                IntegerRef("n", 1, 100),  # Times to repeat the sequence.
            ]
            defaults = {
                "n": 1,  # Default repeat count.
            }

            def _process_recognition(self, node, extras):  # @UnusedVariable
                sequence = extras["sequence"]  # A sequence of actions.
                count = extras["n"]  # An integer repeat count.
                for i in range(count):  # @UnusedVariable
                    for action in sequence:
                        action.execute()
                RELEASE.execute()
        return RepeatRule()

    def build_grammar(self):
        grammar = Grammar(self._name, context=self._context)
        keystroke_rule = self.build_keystroke_rule()
        repeat_rule = self.build_repeat_rule(keystroke_rule)
        grammar.add_rule(repeat_rule)  # Add the top-level rule.
        return grammar


grammar = MultiEditBuilder('generic').build_grammar()
grammar.load()


def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

