import os
import signal
import subprocess
import time
import itertools
import atexit
import sys

global all_processes
all_processes=list()
def cleanup():
    global run
    run=False
    timeout_sec = 5
    for p in all_processes: # list of your processes
        print("cleaning")
        p_sec = 0
        for _ in range(timeout_sec):
            if p.poll() == None:
                time.sleep(1)
                p_sec += 1
        if p_sec >= timeout_sec:
            p.killpg()
            # os.killpg(os.getpgid(p.pid), signal.SIGTERM)  # Send the signal to all the process groups

    print('cleaned up!')

args=""

for arg in sys.argv[1:]:
    args+="'"+arg+"' "

cmd = "python3 depthai.py " + args
print(cmd)

atexit.register(cleanup)
run = True
while(run):
    p = subprocess.run(cmd, shell=True)
    all_processes.append(p)
    return_code = p.returncode
    print("Return code:"+str(return_code))
    all_processes.clear()
    if(return_code == 2): #wrong arguments
        exit(2)