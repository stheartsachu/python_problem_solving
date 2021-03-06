#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = []
    for i in s:
        time.append(i)
    var1 = time[-1]
    var2 = time[-2]
    pahar = "%s%s"%(var2,var1)
    st = "%s%s"%(time[0],time[1])
    st1 = "%s%s"%(time[3],time[4])
    st2 = "%s%s"%(time[6],time[7])
    new_time = []
    for i in range(len(s)-2):
        new_time.append(s[i])
    new_time_str = "".join(new_time)

    if pahar == "AM":
        if st == "12":
            return("00:%s:%s"%(st1,st2))
        else:
            return(new_time_str)

    if pahar == "PM":
        ar = [13,14,15,16,17,18,19,20,21,22,23,12]
        for i in range(1,10):
            t = "0%s"%(i)
            if st == t:
                return("%s:%s:%s"%(ar[i-1],st1,st2))
        if st == "10":
            return("%s:%s:%s"%(ar[9],st1,st2))
        if st == "11":
            return("%s:%s:%s"%(ar[10],st1,st2))
        if st == "12":
            return("%s:%s:%s"%(ar[11],st1,st2))

    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
