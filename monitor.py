import sys
import time
import psutil

last_idle = last_total = 0

while True:
    f = open('system_stats.txt','w')

    mem_usage = psutil.virtual_memory().percent
    print 'mem_usage'
    print mem_usage
    # import IPython
    # IPython.embed()    

    swap_usage = psutil.swap_memory().percent
    print 'swap_usage'
    print swap_usage

    cpu_usage = psutil.cpu_percent()
    print 'cpu_usage'
    print cpu_usage

    # import IPython
    # IPython.embed()
    f.write('MEM: ' + repr(mem_usage) + '\nSwap:' + repr(swap_usage) + '\nCPU:' + repr(cpu_usage) + '\n')
    f.close()
    call(['cp', 'system_stats.txt', '/var/www/html/system_stats.txt'])
    time.sleep(5)