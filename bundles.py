"""
    File for notes
"""
import pickle
import re


##################################
# Pickle for data Serialization  #
##################################

myList = ['a', 'b', 'c', 'd']

with open('datafile.txt', 'w') as fh:
    pickle.dump(myList, fh)

with open('datafile.txt') as fh:
    unpickledlist = pickle.load(fh)


##########
# Regex  #
##########

regex = re.compile('(?P<nums>[\d]+)(?P<none_nums>[\D]+)')

match = regex.search('1234abc 567')

print match.groupdict()             # {'letters': 'abc', 'none_nums': '1234'}
print match.groups()                # ('1234', 'abc')
print match.group('nums')           # 1234
print match.group('none_nums')      # abc
print match.group(0)                # 1234abc
print match.group(1)                # 1234
print match.group(2)                # abc
