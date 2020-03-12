"""
    File for notes
"""
import pickle
import re


##################################
# Pickle for data Serialization  #
##################################

myList = ['a', 'b', 'c', 'd']

with open('datafile.pickle', 'w') as fh:
    pickle.dump(myList, fh)

with open('datafile.pickle') as fh:
    unpickledlist = pickle.load(fh)


##########
# Regex  #
##########

regex = re.compile('(?P<nums>[\d]+)(?P<none_nums>[\D]+)')

match = regex.search('1234abc')

print match.groupdict()             # {'none_nums': 'abc', 'nums': '1234'}
print match.groups()                # ('1234', 'abc')
print match.group('nums')           # 1234
print match.group('none_nums')      # abc
print match.group(0)                # 1234abc
print match.group(1)                # 1234
print match.group(2)                # abc


###################
# Format Strings  #
###################

print '{0} {1} {vehicle}'.format(0, 1, vehicle='car')   # 0 1 car
# with r'' escapes won't be translated
print r'a\nb'                                           # a\nb

############
#  Lambda  #
############

[attr for attr in dir({}) if '__' not in attr]
# Prints
# ['clear', 'copy', 'fromkeys', 'get', 'has_key',
# 'items', 'iteritems', 'iterkeys', 'itervalues',
# 'keys', 'pop', 'popitem', 'setdefault', 'update',
# 'values', 'viewitems', 'viewkeys', 'viewvalues']

#############
#  Classes  #
#############

class Square(object):
    
    def __init__(self, attr):
        self._attr = attr
    
    @property
    def attr(self):
        # Getter
        return self._attr
    
    @attr.setter
    def attr(self, attr):
        if attr <= 0:
            raise ValueError('Value must be positive and greater than 0.')
        else:
            self._attr = attr
    
    def __str__(self):
        # for 'str()'
        return 'Square: attr={0}'.format(self._attr)
    
    def __repr__(self):
        # for 'repr()'
        return 'Square({0})'.format(self._attr)
    
    def __eq__(self, other):
        # for '=='
        if isintance(other, Square):
            return self._attr == other.attr
        else:
            return False
    
###############
#  Interning  #
###############

"""
== compares values
is compares memory reference
"""

a = 'my string'
b = 'my string'
a is b # returns False, id(a) is not id(b)

# Creates shared memory object
a = sys.intern('my string')
b = sys.intern('my string')
a is b # returns True, same memory reference

####################
#  Dict: clearing  #
####################

d = { 'a': 1}

d.clear()   # Clears dictionary at pointer [other variables pointing to same dict will also reset]
d = {}      # Creates new dictionary and points d to it
