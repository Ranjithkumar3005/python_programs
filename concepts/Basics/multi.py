from multiprocessing import Process,cpu_count
import time

def counter(num):
    count=0
    while count<num:
        count+=1
   
def main():     
    a=Process(target=counter,args=(100000,)) 
    a.start()
    a.join()
    print(time.perf_counter())
    
if __name__=="__main__":
    main()