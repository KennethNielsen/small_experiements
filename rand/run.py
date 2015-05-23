from __future__ import division

from random import choice
import time

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

print 'making list'
random_words = []
for _ in xrange(10 ** 5):
    word = choice(WORDS)
    if len(word) < 3:
        continue
    random_words.append(word)

def make_tree(level=2):
    if level == 0:
        return [[] for _ in range(256)]
    else:
        return [make_tree(level-1) for _ in range(256)]

print 'make tree'
tree = make_tree(2)

print 'ordering words'
for word in random_words:
    tree[ord(word[0])][ord(word[1])][ord(word[2])].append(word)


test_words = [choice(WORDS) for _ in range(10)]
    
print 'test manual search'
timings = []
res1 = []
for word in test_words:
    t0 = time.time()
    res1.append(word in random_words)
    timings.append(time.time() - t0)

print sum(timings) / len(timings)
timing1 = sum(timings)

print 'tree search'
timings = []
res2 = []
for word in test_words:
    t0 = time.time()
    res2.append(word in tree[ord(word[0])][ord(word[1])][ord(word[2])])
    timings.append(time.time() - t0)

print sum(timings) / len(timings)
print timing1 / sum(timings)
print res1 == res2
