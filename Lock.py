#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:55:12 2022

@author: alejandro
"""

from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import Lock

N = 8

def task(lock, common, tid):
    a = 0
    for i in range(100):
        print(f"{tid}−{i}: Non−critical Section", flush = True)
        a += 1
        print(f"{tid}−{i}: End of non−critical Section", flush = True)
        lock.acquire()
        try:
            print(f"{tid}−{i}: Critical section", flush = True)
            v = common.value + 1
            print(f"{tid}−{i}: Inside critical section", flush = True)
            common.value = v
            print(f"{tid}−{i}: End of critical section", flush = True)
        finally:
            lock.release()
    
        
def main():
    lock = Lock()
    lp = []
    common = Value("i", 0)
    for tid in range(N):
        lp.append(Process(target=task, args=(lock, common, tid)))
    print (f"Valor inicial del contador {common.value}", flush = True)
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}", flush = True)
    print ("fin", flush = True)

if __name__ == "__main__":
    main()