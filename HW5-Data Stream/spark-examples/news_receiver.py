#!/usr/bin/env python3
import math
import mmh3
from bitarray import bitarray
import os
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working thread and batch interval of 5 seconds
sc = SparkContext.getOrCreate()
ssc = StreamingContext(sc, 5)

def setup_stream():
    # Create a DStream that will connect to hostname:port, like localhost:9999
    news = ssc.socketTextStream("localhost", 9999)
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


    # Split each line into words
    words = news.flatMap(lambda line: line.split(" "))
    for word in words:
        if bloomf.check(word):
            pass
        else:
            word.pprint()

    # Print the first ten elements of each RDD generated in this DStream to the console
    # words.pprint()

def launch_stream(wait):
    ssc.start()                 # Start the computation
    ssc.awaitTermination(wait)  # Wait for the computation to terminate



 
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
        self.size = self.get_size(items_count, 0.05)
 
        # number of hash functions to use
        self.hash_count = self.get_hash_count(self.size, items_count) 
 
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




