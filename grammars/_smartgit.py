from dragonfly import (Grammar,
                       FocusWindow,
                       MappingRule,
                       Integer,
                       Key,
                       AppContext)

smartgit = AppContext( title = 'smartgit')
grammar = Grammar('smartgit', context = (smartgit))


cs_down = Key('ctrl:down,shift:down')
cs_up = Key('ctrl:up,shift:up')

ca_down = Key('ctrl:down,alt:down')
ca_up = Key('ctrl:up,alt:up')

as_down = Key('alt:down,shift:down')
as_up = Key('alt:up,shift:up')

rules = MappingRule(
	name = "smartgit",
	mapping = {
        # Repository
        '(add | create) repository': Key('c-o'),
        'clone repository': cs_down + Key('o') + cs_up,
        'close repository': Key('c-f4'),
        'repository settings': Key('a-enter'),
        # 'exit': Key('a-x'),

        # Edit
        'filter files': Key('c-f'),
        'select commitable files': cs_down + Key('a') + cs_up,
        'copy path': Key('a-insert'),
        'copy relative path': as_down + Key('a-insert') + as_up,
        'clear output': Key('c-backspace'),
        'preferences': Key('c-comma'),

        # View
        'refresh view': Key('f5'),
        'view files from subdirectories': Key('c-0'),
        'show unchanged files': Key('c-1'),
        'show un versioned files': Key('c-2'),
        'show ignored files': Key('c-3'),
        'show staged files': Key('c-4'),
        'show assume unchanged files': Key('c-5'),

        # Remote
        'pull': Key('c-p'),
        'synchronize': Key('c-y'),
        'push': Key('c-u'),
        'push to': cs_down + Key('u') + cs_up,
        'push commits': ca_down + Key('u') + ca_up,

        # Local
        '(stage | add)': Key('c-t'),
        '(unstage | un-add)': cs_down + Key('t') + cs_up,
        'index editor': ca_down + Key('t') + ca_up,
        'ignore': Key('c-i'),
        'resolve': cs_down + Key('v') + cs_up,
        'commit': Key('c-k'),
        'undo last commit': cs_down + Key('k') + cs_up,
        'edit last commit message': Key('f2'),
        'edit commit message': Key('s-f2'),
        'discard': Key('c-z'),
        'remove': Key('c-minus'),
        'delete (file | directory | files | directories)': Key('f8'),
        'reset': Key('c-r'),
        'squash commits': Key('c-j'),
        'save stash': Key('c-s'),
        'apply stash': cs_down + Key('s') + cs_up,

        # Branch
        'check out': Key('c-g'),
        'merge': Key('c-m'),
        'cherry pick': cs_down + Key('m') + cs_up,
        'revert': ca_down + Key('m') + ca_up,
        'rebase head to': Key('c-d'),
        'rebase to head': cs_down + Key('d') + cs_up,
        'add branch': Key('f7'),
        'add tag': Key('s-f7'),

        # Query
        'show changes': Key('f4'),
        'conflict solver': Key('c-v'),
        'show log': Key('c-l'),
        'blame': cs_down + Key('l') + cs_up,

        # Changes
        'next change [<n>]': Key('f6:%(n)d'),
        '(prev | previous) change [<n>]': Key('s-f6:%(n)d'),

        # Windows
        'new window': Key('c-n'),
        'repositories': cs_down + Key('1') + cs_up,
        'files': cs_down + Key('2') + cs_up,
        'output': cs_down + Key('3') + cs_up,
        'changes': cs_down + Key('4') + cs_up,
        'outgoing': cs_down + Key('5') + cs_up,
        'commit messages': cs_down + Key('6') + cs_up,
        'branches': cs_down + Key('7') + cs_up,
        'main perspective': ca_down + Key('7') + ca_up,
        'review perspective': ca_down + Key('7') + ca_up,
        
	},
    
    extras = [
        Integer("n", 1, 20000),
    ],

    defaults = {
        "n" : 1,
    }
)

grammar.add_rule(rules)
grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
