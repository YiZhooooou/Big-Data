#!/usr/bin/env python3

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import numpy as np

# Create a local StreamingContext with two working thread and batch interval of 5 seconds
sc = SparkContext.getOrCreate()
ssc = StreamingContext(sc, 5)

def setup_stream():
    # Create a DStream that will connect to hostname:port, like localhost:9999
    lines = ssc.socketTextStream("localhost", 9999)
    # dj30sum = 0
    # price_data = np.array([])
    # output = []

    # Split each line into words
    words = lines.flatMap(lambda line: line.split(" "))


    # price_data = np.append(price_data, float(row['Close']))
    # dj30sum += float(row['Close'])
    # date = row['Long Date']
    # # print(i, dj30sum, flush = True)
    
    # if len(price_data) >= 10:
    #     temp = np.convolve(price_data, np.ones(10), 'valid')/10
    #     # print('10daysMA: ', temp[-1])
    
    # if len(price_data) >= 40:
    #     temp = np.convolve(price_data, np.ones(40), 'valid')/40
    #     # print('40daysMA: ', temp[-1])

    # if len(price_data) > 40:
    #     ten_MA =  np.convolve(price_data, np.ones(10), 'valid')/10
    #     fourty_MA = np.convolve(price_data, np.ones(40), 'valid')/40
    #     if (ten_MA[-2] > fourty_MA[-2]) != (ten_MA[-1] > fourty_MA[-1]):
    #         if ten_MA[-1] > fourty_MA[-1]:
                
    #             output.append((date, 'buy'))
    #         else:
    #             output.append((date, 'sell'))

    words.pprint()


def launch_stream(wait):
    ssc.start()                 
    ssc.awaitTermination(wait)