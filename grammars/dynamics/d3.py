from dragonfly import (
    Grammar,
    AppContext,
    MappingRule,
    Key,
    Text, 
    Dictation,
    Integer,
    Function
)


DYN_MODULE_TYPE = "programming_language"
DYN_MODULE_NAME = "D3"
INCOMPATIBLE_MODULES = [
    # 'python',
]
SUGGESTED_MODULES = [
    'javascript'
    ]


grammar = Grammar('d3 mode')

rules = MappingRule(
    name = '',
    mapping = {
        
        # d3 specific
        "D three": Key("d,3"),
        "S V G": Key("s,v,g"),

        # Selections
        "dot select": Key("dot,s,e,l,e,c,t,lparen"),
            # d3.select - select an element from the current document.
        "dot select all": Key("dot,s,e,l,e,c,t,s-a,l,l,lparen"),
            # d3.selectAll - select multiple elements from the current document.
        "dot (A T T R | attribute)": Key("dot,a,t,t,r,lparen"),
            # selection.attr - get or set attribute values.
        "dot classed": Key("dot,c,l,a,s,s,e,d,lparen"),
            # selection.classed - add or remove CSS classes.
        "dot style": Key("dot,s,t,y,l,e,lparen"),
            # selection.style - get or set style properties.
        "dot property": Key("dot,p,r,o,p,e,r,t,y,lparen"),
            # selection.property - get or set raw properties.
        "dot text": Key("dot,t,e,x,t,lparen"),
            # selection.text - get or set text content.
        "dot html": Key("dot,h,t,m,l,lparen"),
            # selection.html - get or set inner HTML content.
        "dot append": Key("dot,a,p,p,e,n,d,lparen"),
            # selection.append - create and append new elements.
        "dot insert": Key("dot,i,n,s,e,r,t,lparen"),
            # selection.insert - create and insert new elements before existing elements.
        "dot remove": Key("dot,r,e,m,o,v,e,lparen"),
            # selection.remove - remove elements from the document.
        "dot data": Key("dot,d,a,t,a,lparen"),
            # selection.data - get or set data for a group of elements, while computing a relational join.
        "dot enter": Key("dot,e,n,t,e,r,lparen"),
            # selection.enter - returns placeholders for missing elements.
        "dot exit": Key("dot,e,x,i,t,lparen"),
            # selection.exit - returns elements that are no longer needed.
        "dot datum": Key("dot,d,a,t,u,m,lparen"),
            # selection.datum - get or set data for individual elements, without computing a join.
        "dot filter": Key("dot,f,i,l,t,e,r,lparen"),
            # selection.filter - filter a selection based on data.
        "dot sort": Key("dot,s,o,r,t,lparen"),
            # selection.sort - sort elements in the document based on data.
        "dot order": Key("dot,o,r,d,e,r,lparen"),
            # selection.order - reorders elements in the document to match the selection.
        "dot on": Key("dot,o,n,lparen"),
            # selection.on - add or remove event listeners for interaction.
        "dot transition": Key("dot,t,r,a,n,s,i,t,i,o,n,lparen"),
            # selection.transition - start a transition on the selected elements.
        "dot interrupt": Key("dot,i,n,t,e,r,r,u,p,t,lparen"),
            # selection.interrupt - immediately interrupt the current transition, if any.
        "dot each": Key("dot,e,a,c,h,lparen"),
            # selection.each - call a function for each selected element.
        "dot call": Key("dot,c,a,l,l,lparen"),
            # selection.call - call a function passing in the current selection.
        "dot empty": Key("dot,e,m,p,t,y,lparen"),
            # selection.empty - returns true if the selection is empty.
        "dot node": Key("dot,n,o,d,e,lparen"),
            # selection.node - returns the first node in the selection.
        "dot size": Key("dot,s,i,z,e,lparen"),
            # selection.size - returns the number of elements in the selection.
        "dot select": Key("dot,s,e,l,e,c,t,lparen"),
            # selection.select - subselect a descendant element for each selected element.
        "dot select all": Key("dot,s,e,l,e,c,t,s-a,l,l,lparen"),
            # selection.selectAll - subselect multiple descendants for each selected element.
        "dot selection": Key("dot,s,e,l,e,c,t,i,o,n,lparen"),
            # d3.selection - augment the selection prototype, or test instance types.
        "dot event": Key("dot,e,v,e,n,t,lparen"),
            # d3.event - access the current user event for interaction.
        "dot mouse": Key("dot,m,o,u,s,e,lparen"),
            # d3.mouse - gets the mouse position relative to a specified container.
        "dot touch": Key("dot,t,o,u,c,h,lparen"),
            # d3.touch - gets a touch position relative to a specified container.
        "dot touches": Key("dot,t,o,u,c,h,e,s,lparen"),
            # d3.touches - gets the touch positions relative to a specified container.

        # Arrays
        "dot ascending": Key("dot,a,s,c,e,n,d,i,n,g,lparen"),
            # d3.ascending - compare two values for sorting.
        "dot descending": Key("dot,d,e,s,c,e,n,d,i,n,g,lparen"),
            # d3.descending - compare two values for sorting.
        "dot min": Key("dot,m,i,n,lparen"),
            # d3.min - find the minimum value in an array.
        "dot max": Key("dot,m,a,x,lparen"),
            # d3.max - find the maximum value in an array.
        "dot extent": Key("dot,e,x,t,e,n,t,lparen"),
            # d3.extent - find the minimum and maximum value in an array.
        "dot sum": Key("dot,s,u,m,lparen"),
            # d3.sum - compute the sum of an array of numbers.
        "dot mean": Key("dot,m,e,a,n,lparen"),
            # d3.mean - compute the arithmetic mean of an array of numbers.
        "dot median": Key("dot,m,e,d,i,a,n,lparen"),
            # d3.median - compute the median of an array of numbers (the 0.5-quantile).
        "dot quantile": Key("dot,q,u,a,n,t,i,l,e,lparen"),
            # d3.quantile - compute a quantile for a sorted array of numbers.
        "dot bisect": Key("dot,b,i,s,e,c,t,lparen"),
            # d3.bisect - search for a value in a sorted array.
        "dot bisect right": Key("dot,b,i,s,e,c,t,s-r,i,g,h,t,lparen"),
            # d3.bisectRight - search for a value in a sorted array.
        "dot bisect left": Key("dot,b,i,s,e,c,t,s-l,e,f,t,lparen"),
            # d3.bisectLeft - search for a value in a sorted array.
        "dot bisector": Key("dot,b,i,s,e,c,t,o,r,lparen"),
            # d3.bisector - bisect using an accessor or comparator.
        "dot shuffle": Key("dot,s,h,u,f,f,l,e,lparen"),
            # d3.shuffle - randomize the order of an array.
        "dot permute": Key("dot,p,e,r,m,u,t,e,lparen"),
            # d3.permute - reorder an array of elements according to an array of indexes.
        "dot zip": Key("dot,z,i,p,lparen"),
            # d3.zip - transpose a variable number of arrays.
        "dot transpose": Key("dot,t,r,a,n,s,p,o,s,e,lparen"),
            # d3.transpose - transpose an array of arrays.
        "dot pairs": Key("dot,p,a,i,r,s,lparen"),
            # d3.pairs - returns an array of adjacent pairs of elements.
        "dot keys": Key("dot,k,e,y,s,lparen"),
            # d3.keys - list the keys of an associative array.
        "dot values": Key("dot,v,a,l,u,e,s,lparen"),
            # d3.values - list the values of an associated array.
        "dot entries": Key("dot,e,n,t,r,i,e,s,lparen"),
            # d3.entries - list the key-value entries of an associative array.
        "dot merge": Key("dot,m,e,r,g,e,lparen"),
            # d3.merge - merge multiple arrays into one array.
        "dot range": Key("dot,r,a,n,g,e,lparen"),
            # d3.range - generate a range of numeric values.
        "dot nest": Key("dot,n,e,s,t,lparen"),
            # d3.nest - group array elements hierarchically.
        "dot key": Key("dot,k,e,y,lparen"),
            # nest.key - add a level to the nest hierarchy.
        "dot sort keys": Key("dot,s,o,r,t,s-k,e,y,s,lparen"),
            # nest.sortKeys - sort the current nest level by key.
        "dot sort values": Key("dot,s,o,r,t,s-v,a,l,u,e,s,lparen"),
            # nest.sortValues - sort the leaf nest level by value.
        "dot rollup": Key("dot,r,o,l,l,u,p,lparen"),
            # nest.rollup - specify a rollup function for leaf values.
        "dot map": Key("dot,m,a,p,lparen"),
            # nest.map - evaluate the nest operator, returning an associative array.
        "dot entries": Key("dot,e,n,t,r,i,e,s,lparen"),
            # nest.entries - evaluate the nest operator, returning an array of key-values tuples.
        "dot map": Key("dot,m,a,p,lparen"),
            # d3.map - a shim for ES6 maps, since objects are not hashes!
        "dot has": Key("dot,h,a,s,lparen"),
            # map.has - returns true if the map contains the specified key.
        "dot get": Key("dot,g,e,t,lparen"),
            # map.get - returns the value for the specified key.
        "dot set": Key("dot,s,e,t,lparen"),
            # map.set - sets the value for the specified key.
        "dot remove": Key("dot,r,e,m,o,v,e,lparen"),
            # map.remove - removes the entry for specified key.
        "dot keys": Key("dot,k,e,y,s,lparen"),
            # map.keys - returns the map's array of keys.
        "dot values": Key("dot,v,a,l,u,e,s,lparen"),
            # map.values - returns the map's array of values.
        "dot entries": Key("dot,e,n,t,r,i,e,s,lparen"),
            # map.entries - returns the map's array of entries (key-values objects).
        "dot for each": Key("dot,f,o,r,s-e,a,c,h,lparen"),
            # map.forEach - calls the specified function for each entry in the map.
        "dot empty": Key("dot,e,m,p,t,y,lparen"),
            # map.empty - returns false if the map has at least one entry.
        "dot size": Key("dot,s,i,z,e,lparen"),
            # map.size - returns the number of entries in the map.
        "dot set": Key("dot,s,e,t,lparen"),
            # d3.set - a shim for ES6 sets, since objects are not hashes!
        # "dot has": Key("dot,h,a,s,lparen"),
            # set.has - returns true if the set contains the specified value.
        "dot add": Key("dot,a,d,d,lparen"),
            # set.add - adds the specified value.
        # "dot remove": Key("dot,r,e,m,o,v,e,lparen"),
            # set.remove - removes the specified value.
        # "dot values": Key("dot,v,a,l,u,e,s,lparen"),
            # set.values - returns the set's array of values.
        # "dot for each": Key("dot,f,o,r,s-e,a,c,h,lparen"),
            # set.forEach - calls the specified function for each value in the set.
        # "dot empty": Key("dot,e,m,p,t,y,lparen"),
            # set.empty - returns true if the set has at least one value.
        # "dot size": Key("dot,s,i,z,e,lparen"),
            # set.size - returns the number of values in the set.

                        
        # Shapes
        "rectangle": Key("r,e,c,t"),

        # Scales
        "dot scale":  Key("dot,s,c,a,l,e"),
        "dot linear":  Key("dot,l,i,n,e,a,r,lparen"),
        "dot domain":  Key("dot,d,o,m,a,i,n,lparen"),
        "dot range":  Key("dot,r,a,n,g,e,lparen"),
        
    },    
    extras = [
        Dictation("text", format=False),
        Integer("n", 1, 20000),
    ],

    defaults = {
        "text" : "", 
        "n" : 1,
    }
)



grammar.add_rule(rules)
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
