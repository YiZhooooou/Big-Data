#!/usr/bin/env python3

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working thread and batch interval of 5 seconds
sc = SparkContext.getOrCreate()
ssc = StreamingContext(sc, 5)

def setup_stream():
    # Create a DStream that will connect to hostname:port, like localhost:9999
    lines = ssc.socketTextStream("localhost", 9999)

    # Split each line into words
    words = lines.flatMap(lambda line: line.split(" "))
    for item in words.collect():
        item.pprint()
    # word2 = words.collect()

    # Count each word in each batch
    # pairs = words.map(lambda word: (word, 1))
    # wordCounts = pairs.reduceByKey(lambda x, y: x + y)

    # Print the first ten elements of each RDD generated in this DStream to the console
    # words.pprint()

def launch_stream(wait):
    ssc.start()                 # Start the computation
    ssc.awaitTermination(wait)  # Wait for the computation to terminate






