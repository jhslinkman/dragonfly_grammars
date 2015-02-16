#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#

"""
Command-module for cursor movement and **editing**
============================================================================

This module allows the user to control the cursor and 
efficiently perform multiple text editing actions within a 
single phrase.


Example commands
----------------------------------------------------------------------------

*Note the "/" characters in the examples below are simply 
to help the reader see the different parts of each voice 
command.  They are not present in the actual command and 
should not be spoken.*

Example: **"up 4 / down 1 page / home / space 2"**
   This command will move the cursor up 4 lines, down 1 page,
   move to the beginning of the line, and then insert 2 spaces.

Example: **"left 7 words / backspace 3 / insert hello Cap world"**
   This command will move the cursor left 7 words, then delete
   the 3 characters before the cursor, and finally insert
   the text "hello World".

Example: **"home / space 4 / down / 43 times"**
   This command will insert 4 spaces at the beginning of 
   of this and the next 42 lines.  The final "43 times" 
   repeats everything in front of it that many times.


Discussion of this module
----------------------------------------------------------------------------

This command-module creates a powerful voice command for 
editing and cursor movement.  This command's structure can 
be represented by the following simplified language model:

 - *CommandRule* -- top-level rule which the user can say
    - *repetition* -- sequence of actions (name = "sequence")
       - *KeystrokeRule* -- rule that maps a single 
         spoken-form to an action
    - *optional* -- optional specification of repeat count
       - *integer* -- repeat count (name = "n")
       - *literal* -- "times"

The top-level command rule has a callback method which is 
called when this voice command is recognized.  The logic 
within this callback is very simple:

1. Retrieve the sequence of actions from the element with 
   the name "sequence".
2. Retrieve the repeat count from the element with the name
   "n".
3. Execute the actions the specified number of times.

"""

try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

from dragonfly import *
import os

#---------------------------------------------------------------------------
# Here we globally defined the release action which releases all
#  modifier-keys used within this grammar.  It is defined here
#  because this functionality is used in many different places.
#  Note that it is harmless to release ("...:up") a key multiple
#  times or when that key is not held down at all.

release = Key("shift:up, ctrl:up, alt:up")


#---------------------------------------------------------------------------
# Set up this module's configuration.

def setup_config(config_file):
    config            = Config("multi edit")
    config.cmd        = Section("Language section")
    config.cmd.map    = Item(
        # Here we define the *default* command map.  If you would like to
        #  modify it to your personal taste, please *do not* make changes
        #  here.  Instead change the *config file* called "_multiedit.txt".
        {
         # Spoken-form    ->    ->    ->     Action object
         "up [<n>]":                         Key("up:%(n)d"),
         "down [<n>]":                       Key("down:%(n)d"),
         "left [<n>]":                       Key("left:%(n)d"),
         "right [<n>]":                      Key("right:%(n)d"),
         "page up [<n>]":                    Key("pgup:%(n)d"),
         "page down [<n>]":                  Key("pgdown:%(n)d"),
         "up <n> (page | pages)":            Key("pgup:%(n)d"),
         "down <n> (page | pages)":          Key("pgdown:%(n)d"),
         "left <n> (word | words)":          Key("c-left:%(n)d"),
         "right <n> (word | words)":         Key("c-right:%(n)d"),
         # "home":                             Key("home"),
         # "end":                              Key("end"),
         # "doc home":                         Key("c-home"),
         # "doc end":                          Key("c-end"),

         "space [<n>]":                      release + Key("space:%(n)d"),
         "enter [<n>]":                      release + Key("enter:%(n)d"),
         "tab [<n>]":                        Key("tab:%(n)d"),
         "delete [<n>]":                     release + Key("del:%(n)d"),
         "delete [<n> | this] (line|lines)": release + Key("home, s-down:%(n)d, del"),
         "backspace [<n>]":                  release + Key("backspace:%(n)d"),
         "pop up":                           release + Key("apps"),

         "paste":                            release + Key("c-v"),
         "duplicate <n>":                    release + Key("c-c, c-v:%(n)d"),
         "copy":                             release + Key("c-c"),
         "cut":                              release + Key("c-x"),
         # "select all":                       release + Key("c-a"),
         "[hold] shift":                     Key("shift:down"),
         "release shift":                    Key("shift:up"),
         "[hold] control":                   Key("ctrl:down"),
         "release control":                  Key("ctrl:up"),
         "release [all]":                    release,

         "say <text>":                       release + Text("%(text)s"),
         "mimic <text>":                     release + Mimic(extra="text"),
        },
        namespace={
         "Key":   Key,
         "Text":  Text,
        }
    )

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file)
    namespace = config.load(path = path)
    return config, namespace

config, namespace = setup_config('_multiedit.txt')
emacs_config, emacs_namespace = setup_config('_multiedit_emacs.txt')
sublime_config, sublime_namespace = setup_config('_multiedit_sublime.txt')
terminal_config, terminal_namespace = setup_config('_mintty.txt')

#---------------------------------------------------------------------------
# Here we prepare the list of formatting functions from the config file.

# Retrieve text-formatting functions from this module's config file.
#  Each of these functions must have a name that starts with "format_".

def setup_format_rule(namespace):
    format_functions = {}
    if namespace:
        for name, function in namespace.items():
         if name.startswith("format_") and callable(function):
            spoken_form = function.__doc__.strip()

            # We wrap generation of the Function action in a function so
            #  that its *function* variable will be local.  Otherwise it
            #  would change during the next iteration of the namespace loop.
            def wrap_function(function):
                def _function(dictation):
                    formatted_text = function(dictation)
                    Text(formatted_text).execute()
                return Function(_function)

            action = wrap_function(function)
            format_functions[spoken_form] = action

    # Here we define the text formatting rule.
    # The contents of this rule were built up from the "format_*"
    #  functions in this module's config file.
    if format_functions:
        class FormatRule(MappingRule):

            mapping  = format_functions
            extras   = [Dictation("dictation")]

    else:
        FormatRule = None

    return FormatRule

FormatRule = setup_format_rule(namespace)
EmacsFormatRule = setup_format_rule(emacs_namespace)
SublimeFormatRule = setup_format_rule(sublime_namespace)
TerminalFormatRule = setup_format_rule(terminal_namespace)

#---------------------------------------------------------------------------
# Here we define the keystroke rule.

# This rule maps spoken-forms to actions.  Some of these 
#  include special elements like the number with name "n" 
#  or the dictation with name "text".  This rule is not 
#  exported, but is referenced by other elements later on.
#  It is derived from MappingRule, so that its "value" when 
#  processing a recognition will be the right side of the 
#  mapping: an action.
# Note that this rule does not execute these actions, it
#  simply returns them when it's value() method is called.
#  For example "up 4" will give the value Key("up:4").
# More information about Key() actions can be found here:
#  http://dragonfly.googlecode.com/svn/trunk/dragonfly/documentation/actionkey.html
def setup_keystroke_rule(config):
    class KeystrokeRule(MappingRule):

        exported = False

        mapping  = config.cmd.map
        extras   = [
                    IntegerRef("n", 1, 100),
                    Dictation("text"),
                    Dictation("text2"),
                   ]
        defaults = {
                    "n": 1,
                   }
        # Note: when processing a recognition, the *value* of 
        #  this rule will be an action object from the right side 
        #  of the mapping given above.  This is default behavior 
        #  of the MappingRule class' value() method.  It also 
        #  substitutes any "%(...)." within the action spec
        #  with the appropriate spoken values.

    return KeystrokeRule

KeystrokeRule = setup_keystroke_rule(config)
EmacsKeystrokeRule = setup_keystroke_rule(emacs_config)
SublimeKeystrokeRule = setup_keystroke_rule(sublime_config)
TerminalKeystrokeRule = setup_keystroke_rule(terminal_config)

#---------------------------------------------------------------------------
# Here we create an element which is the sequence of keystrokes.

def setup_repeat_rule(KeystrokeRule, FormatRule):
    # First we create an element that references the keystroke rule.
    #  Note: when processing a recognition, the *value* of this element
    #  will be the value of the referenced rule: an action.
    alternatives = []
    alternatives.append(RuleRef(rule=KeystrokeRule()))
    if FormatRule:
        alternatives.append(RuleRef(rule=FormatRule()))
    single_action = Alternative(alternatives)

    # Second we create a repetition of keystroke elements.
    #  This element will match anywhere between 1 and 16 repetitions
    #  of the keystroke elements.  Note that we give this element
    #  the name "sequence" so that it can be used as an extra in
    #  the rule definition below.
    # Note: when processing a recognition, the *value* of this element
    #  will be a sequence of the contained elements: a sequence of
    #  actions.
    sequence = Repetition(single_action, min=1, max=16, name="sequence")


    #---------------------------------------------------------------------------
    # Here we define the top-level rule which the user can say.

    # This is the rule that actually handles recognitions. 
    #  When a recognition occurs, it's _process_recognition() 
    #  method will be called.  It receives information about the 
    #  recognition in the "extras" argument: the sequence of 
    #  actions and the number of times to repeat them.
    class RepeatRule(CompoundRule):

        # Here we define this rule's spoken-form and special elements.
        spec     = "<sequence> [[[and] repeat [that]] <n> times]"
        extras   = [
                    sequence,                 # Sequence of actions defined above.
                    IntegerRef("n", 1, 100),  # Times to repeat the sequence.
                   ]
        defaults = {
                    "n": 1,                   # Default repeat count.
                   }

        # This method gets called when this rule is recognized.
        # Arguments:
        #  - node -- root node of the recognition parse tree.
        #  - extras -- dict of the "extras" special elements:
        #     . extras["sequence"] gives the sequence of actions.
        #     . extras["n"] gives the repeat count.
        def _process_recognition(self, node, extras):
            sequence = extras["sequence"]   # A sequence of actions.
            count = extras["n"]             # An integer repeat count.
            for i in range(count):
                for action in sequence:
                    action.execute()
            release.execute()
    return RepeatRule

RepeatRule = setup_repeat_rule(KeystrokeRule, FormatRule)
EmacsRepeatRule = setup_repeat_rule(EmacsKeystrokeRule, EmacsFormatRule)
SublimeRepeatRule = setup_repeat_rule(SublimeKeystrokeRule, SublimeFormatRule)
TerminalRepeatRule = setup_repeat_rule(TerminalKeystrokeRule, TerminalFormatRule)

#---------------------------------------------------------------------------
# Create and load this module's grammar.
#  This module contains Emacs specific multi-edit commands.

emacs = AppContext( title = 'emacs')
sublime = AppContext( executable = 'sublime_text')
terminal = AppContext( executable = 'mintty')
not_emacs = ~emacs & ~sublime & ~terminal

grammar = Grammar('multi edit', context = (not_emacs))   # Create this module's grammar.
grammar.add_rule(RepeatRule())    # Add the top-level rule.
grammar.load()                    # Load the grammar.

emacs_grammar = Grammar('emacs multi edit', context = (emacs))   # Create this module's grammar.
emacs_grammar.add_rule(EmacsRepeatRule())    # Add the top-level rule.
emacs_grammar.load()                    # Load the grammar.

sublime_grammar = Grammar('sublime multi edit', context = (sublime))   # Create this module's grammar.
sublime_grammar.add_rule(SublimeRepeatRule())    # Add the top-level rule.
sublime_grammar.load()                    # Load the grammar.

terminal_grammar = Grammar('terminal multi edit', context = (terminal))   # Create this module's grammar.
terminal_grammar.add_rule(TerminalRepeatRule())    # Add the top-level rule.
terminal_grammar.load()                    # Load the grammar.



# Unload function which will be called at unload time.
def unload():
    global grammar
    global emacs_grammar
    global sublime_grammar
    global terminal_grammar
    if grammar: grammar.unload()
    if emacs_grammar: emacs_grammar.unload()
    if sublime_grammar: sublime_grammar.unload()
    if terminal_grammar: terminal_grammar.unload()
    grammar = None
    emacs_grammar = None
    sublime_grammar = None
    terminal_grammar = None
