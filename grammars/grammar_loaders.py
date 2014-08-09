#! /usr/bin/env python2

def load_grammar(grammar):
    print "Loading grammar %s" % grammar
    return lambda grammar = grammar: grammar.load()

def unload_grammar(grammar):
    print "Unloading grammar %s" % grammar
    return lambda grammar = grammar: grammar.unload()
