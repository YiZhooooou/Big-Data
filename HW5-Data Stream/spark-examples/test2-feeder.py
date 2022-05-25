#!/usr/bin/env python3
import sys
import feedparser, time, datetime
import pandas as pd
import math
import mmh3
from bitarray import bitarray
import os

class BloomFilter(object):
 
    '''
    Class for Bloom filter, using murmur3 hash function
    '''
 
    def __init__(self, items_count):
        '''
        items_count : int
            Number of items expected to be stored in bloom filter
        fp_prob : float
            False Positive probability in decimal
        '''
        # False possible probability in decimal
        self.fp_prob = 0.05
 
        # Size of bit array to use
        self.size = int(8 * n)
 
        # number of hash functions to use
        self.hash_count = int(8 * math.log(2))
 
        # Bit array of given size
        self.bit_array = bitarray(self.size)
 
        # initialize all bits as 0
        self.bit_array.setall(0)
 
    def add(self, item):
        '''
        Add an item in the filter
        '''
        digests = []
        for i in range(self.hash_count):
 
            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)
 
            # set the bit True in bit_array
            self.bit_array[digest] = True
 
    def check(self, item):
        '''
        Check for existence of an item in filter
        '''
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
 
                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return False
        return True
 
    @classmethod
    def get_size(self, n, p):
        '''
        Return the size of bit array(m) to used using
        following formula
        m = -(n * lg(p)) / (lg(2)^2)
        n : int
            number of items expected to be stored in filter
        p : float
            False Positive probability in decimal
        '''
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)
 
    @classmethod
    def get_hash_count(self, m, n):
        '''
        Return the hash function(k) to be used using
        following formula
        k = (m/n) * lg(2)
 
        m : int
            size of bit array
        n : int
            number of items expected to be stored in filter
        '''
        k = (m/n) * math.log(2)
        return int(k)

class Feed:
    name = ''
    url = None
    max_delay = None
    def __init__(self, name, url, max_delay):
        self.name = name
        self.url  = url
        self.max_delay = max_delay

    def __str__(self):
        return '%s: %s' % (self.name, self.url)

    def getHeadline(self):
        d = feedparser.parse (self.url)
        for post in d.entries:
            time.sleep(1.0)
            ret = (datetime.datetime.now().time(), self.name, post.title, post.link)
            yield ret

#

feeds = (
    Feed('nyt-home', 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', 1),
    Feed('nyt-sun', 'https://rss.nytimes.com/services/xml/rss/nyt/sunday-review.xml', 1),
    Feed('nyt-hlth', 'https://rss.nytimes.com/services/xml/rss/nyt/Health.xml', 1),
    Feed('nyt-wrld', 'https://www.nytimes.com/section/world/rss.xml', 1),
    Feed('nyt-bsns', 'http://feeds.nytimes.com/nyt/rss/Business', 1),
    Feed('nyt-tech', 'http://feeds.nytimes.com/nyt/rss/Technology', 1),
    Feed('nyt-sprt', 'https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml', 1),
    Feed('nyt-scnc', 'http://www.nytimes.com/services/xml/rss/nyt/Science.xml', 1),
    Feed('nyt-arts', 'https://rss.nytimes.com/services/xml/rss/nyt/Arts.xml', 1),
    Feed('nyt-trvl', 'https://rss.nytimes.com/services/xml/rss/nyt/Travel.xml', 1),
    Feed('nyt-usa',  'http://www.nytimes.com/services/xml/rss/nyt/US.xml', 1),
    Feed('bbc-hlth', 'http://feeds.bbci.co.uk/news/health/rss.xml', 1),
    Feed('bbc-brkn', 'https://bbcbreakingnews.com/feed', 1),
    Feed('bbc-bsns', 'http://feeds.bbci.co.uk/news/business/rss.xml', 1),
    Feed('bbc-pltc', 'http://feeds.bbci.co.uk/news/politics/rss.xml', 1),
    Feed('bbc-educ', 'http://feeds.bbci.co.uk/news/education/rss.xml', 1),
    Feed('bbc-scnc', 'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml', 1),
    Feed('bbc-tech', 'http://feeds.bbci.co.uk/news/technology/rss.xml', 1),
    Feed('bbc-arts', 'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 1),
)

'''
# Used for testing, now commented out
titles = []
for feed in feeds:
    for (tt, name, title, link) in feed.getHeadline():
        words = pre_process(title).split()

        if all([x in understood_words for x in words]):
            # print('i know this: ', title)
            pass
        else:
            print(title)
'''

titles = []
bloom_list = []

with open('Moving-Averages_data_headline_words.txt') as f:
    line = f.readlines()
    for word in line:
        new_word = word.strip()
        bloom_list.append(new_word)

n = len(bloom_list)
bloomf = BloomFilter(n)

for word in bloom_list:
    bloomf.add(word)

for feed in feeds:
    for (tt, name, title, link) in feed.getHeadline():
        allnews = title.split()
        for item in allnews:
            if bloomf.check(item.lower()):
                pass
            else:
                print(item, flush = True)

        # print (title, flush = True)

