from asyncio.windows_events import NULL
from dataclasses import dataclass
import numpy as np
import os
import csv

# extract data from csv to matrxi and drop the error
def getMatrx():
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(suppress=True)
    input = find_csv()
    output = np.zeros((77,77), dtype = int)
    with open(input, "r") as csv_file:
        data = csv.reader(csv_file)
        next(data)
        for row in data:
            if (row[0] == '' or row[1] == ''or row[2] == ''):
                continue
            else:
                output[int(row[0]) - 1][int(row[1]) - 1] = int(row[2])
    #normalize the output matrix with weight
    sum_of_rows = output.sum(axis=1)
    M = output/sum_of_rows[:, np.newaxis]
    return M

def trafficRank():
    M = getMatrx()
    b = 0.85
    r0, r = np.zeros(77), np.ones(77)
    res = {}
    for i in range(100):
        r0 = r.copy()
        for j in range(77):
            Mi = np.array(M[:,j])
            N = 1 / 77
            r[j] = r0.dot(Mi * b) + N
        res[i + 1] = r
    re = res.get(64)
    re /= sum(re)
    temp = {}
    for k in range(len(re)):
       temp[k + 1] = re[k]
    sort_re = sorted(temp.items(), key=lambda x: x[1],reverse=True)
    print ('%s\n' % sort_re)
            
# grab the file locally
def find_csv():
    file_dir = os.path.dirname(__file__)
    csv_file = os.path.join(file_dir, 'chicago-taxi-rides.csv')

    return csv_file

trafficRank()