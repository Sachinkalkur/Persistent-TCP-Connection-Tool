#!/usr/bin/python
import os
from multiprocessing.dummy import Pool as ThreadPool

cmd = list()
for i in range(10000, 20001):
        port = str(i)
        cmd.append('nc -ld '+ port + ' &')

def threading_server(cmd):
        os.system(cmd)

if __name__ == '__main__':
        p = ThreadPool(5)
        result1 = p.map(threading_server, cmd)
        print "initiated"
