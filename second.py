import time
import datetime
import os

def Copy_File(fp_of_tlog, fp_of_log):

    print("\n\nCurrent Time is")
    print(datetime.datetime.now())
    pre_time = time.time()
    
    try:
        while True:
            line = fp_of_log.readline()
            fp_of_tlog.write(line)
            if((time.time() - pre_time) > 2 and (time.time() - pre_time) <= 3 ):
                fp_of_tlog.close()
                print("Current file line no ", (fp_of_log.tell()))
                if line is None:
                    return "EOF"
                return time.time()
    except EOFError :
        return "EOF"
