import os
import time
if __name__ == "__main__":
    t1=time.time()
    os.system('/bin/bash -l -c "module load gromacs"')
    os.system('/bin/bash -l -c "grompp -n index.ndx"')
    os.system('/bin/bash -l -c "mdrun"')
    t2=time.time()
    f1=open('/home1/02734/vivek91/output/exectime.txt','a')
    f1.write(str(t1)+'\n'+str(t2)+'\n')
    f1.close()