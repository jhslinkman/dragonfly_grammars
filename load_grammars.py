#! /usr/bin/env python2

import os
import shutil

MACRO_DIR = os.path.join('.','grammars')
NATLINK_MACROSYSTEM_DIR = os.path.join('C:\\','NatLink','NatLink','MacroSystem')

file_whitelist = [
    '_emacs.py',
    '_globals.py',
    '_multiedit.txt',
    '_multiedit_emacs.py',
    '_multiedit_emacs.txt',
    'grammar_loaders.py',
    'query_replace_mode.py',
    '_firefox.py',
    '_smartgit.py',
    '_dynamic_manager.py',
    
    'dynamics/__init__.py',
    'dynamics/javascript.py',
    'dynamics/d3.py',
    'dynamics/programming.py',
    # 'dynamics/python.py',
    
    'lib/__init__.py',
    'lib/config.py',
    'lib/sound.py',
    ]

class GrammarFile(object):

    def __init__(self, file_path):
        file_parts = file_path.split('/')
        if len(file_parts) > 1:
            self.sub_dir = os.path.join(*file_parts[:-1])
            self.dir = os.path.join(MACRO_DIR, self.sub_dir)
            self.file_name = file_parts[-1]
            self.dest_dir = os.path.join(NATLINK_MACROSYSTEM_DIR,
                                         self.sub_dir)
        else:
            self.sub_dir = None
            self.dir = MACRO_DIR
            self.file_name = file_path
            self.dest_dir = NATLINK_MACROSYSTEM_DIR
        self.full_file_path = os.path.join(self.dir, self.file_name)
        self.check_existence()
        self.copy()

    def check_existence(self):
        if not os.path.isdir(self.dir):
            raise Exception("The subdirectory %s does not exist." % self.dir)
        if not os.path.isfile(self.full_file_path):
            raise Exception("The file %s does not exist." % self.full_file_path)
        if self.sub_dir and not os.path.isdir(self.dest_dir):
            os.makedirs(self.dest_dir)

    def copy(self):
        print "Copying %s to %s . . ." % (self.full_file_path, self.dest_dir)
        shutil.copy(self.full_file_path, os.path.join(self.dest_dir, self.file_name))
                    
        
def copy_grammars(file_whitelist):
    for file_path in file_whitelist:
        GrammarFile(file_path)


if __name__ == '__main__':
    copy_grammars(file_whitelist)
