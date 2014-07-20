#! /usr/bin/env python2

import os
import shutil

MACRO_DIR = os.path.join('.','grammars')
NATLINK_MACROSYSTEM_DIR = os.path.join('C:\\','NatLink','NatLink','MacroSystem')

def copy_grammars():
    src_files = os.listdir(MACRO_DIR)
    for file_name in src_files:
        full_file_name = os.path.join(MACRO_DIR, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, NATLINK_MACROSYSTEM_DIR)



if __name__ == '__main__':
    copy_grammars()
