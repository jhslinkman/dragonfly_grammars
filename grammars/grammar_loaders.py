#! /usr/bin/env python2

def load_grammar(grammar):
    return lambda grammar = grammar: grammar.load()

def unload_grammar(grammar):
    return lambda grammar = grammar: grammar.unload()
