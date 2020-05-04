import os
import sys
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
#sys.path.append(os.path.join(ROOT_DIR, 'data'))

name = input('enter file: ')
name= os.path.join(BASE_DIR, 'data\\23\\',name)
handle = open(name,encoding='utf')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)