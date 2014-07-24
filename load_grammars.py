#! /usr/bin/env python2

import os
import shutil

MACRO_DIR = os.path.join('.','grammars')
NATLINK_MACROSYSTEM_DIR = os.path.join('C:\\','NatLink','NatLink','MacroSystem')

file_whitelist = set([
    '_emacs.py',
    '_globals.py',
    '_multiedit.txt',
    '_multiedit_emacs.py',
    '_multiedit_emacs.txt',
    'grammar_loaders.py',
    '_programming_mode.py',
    'query_replace_mode.py',
    '_test.py'
    ])

def copy_grammars():
    src_files = set(os.listdir(MACRO_DIR)) & file_whitelist
    for file_name in src_files:
        full_file_name = os.path.join(MACRO_DIR, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, NATLINK_MACROSYSTEM_DIR)



if __name__ == '__main__':
    copy_grammars()
