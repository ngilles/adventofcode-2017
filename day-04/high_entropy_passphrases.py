
from collections import Counter


# Count the words make sure there's only one copy of each
def is_valid1(p):
    return all(c == 1 for c in Counter(p.split()).values())

# anagram_key = a letter frequency count of the give word, made into a (hashable) set
anagram_key = lambda w: frozenset((l, c) for l, c in Counter(w).items())

# Count the anagram_keys for the words in the passphrase, make sure there's only 1
def is_valid2(p):
    return all(c == 1 for c in Counter(anagram_key(w) for w in p.split()).values())


with open('input.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]


assert(is_valid1('aa bb cc dd ee') == True)
assert(is_valid1('aa bb cc dd aa') == False)
assert(is_valid1('aa bb cc dd aaa') == True)

print(sum(1 for l in data if is_valid1(l)))

assert(is_valid2('abcde fghij') == True)
assert(is_valid2('abcde xyz ecdab') == False)
assert(is_valid2('a ab abc abd abf abj') == True)
assert(is_valid2('iiii oiii ooii oooi oooo') == True)
assert(is_valid2('oiii ioii iioi iiio') == False)

print(sum(1 for l in data if is_valid2(l)))


