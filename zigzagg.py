import time, sys
indent=0
indentIncreasing=True

try:
    while True:
        print(' ' * indent,end='')
        print('********')
        time.sleep(0.1) #Pause for 1/10th seconds

        if indentIncreasing:
            indent=indent+1
            if indent == 10: # time to decrease indent
                indentIncreasing = False

        else:
            indent=indent-1
            if indent == 0: # time to increase indent
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()