#!/usr/bin/python
import os
from multiprocessing.dummy import Pool as ThreadPool

cmd = list()
for i in range(10000, 20001):
        dst_port = str(i)
        src_port = str(i + 31000)
        ip = '172.16.100.11'
        cmd.append('nc -d '+ '-p ' + src_port + ' ' + ip + ' ' + dst_port + ' &')

def threading_client(cmd):
        os.system(cmd)

if __name__=='__main__':
        p = ThreadPool(5)
        result1 = p.map(threading_client, cmd)
        print "initiated"
