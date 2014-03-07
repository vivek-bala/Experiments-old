import pylab
import matplotlib.pyplot as mpl
import numpy as np
import math
import scipy.stats as stats
exectime = [9.8800001144,16.2300000191,26.5199999809,56.2300000191,68.4900000095,127.940000057,228.829999924,496.849999905,903.899999857]
no_tasks = [2,4,8,16,32,64,128,256,512]
x = np.exp2(np.arange(10))
pylab.loglog(no_tasks,exectime,marker='o',linestyle="-",label = 'Pilot size = Number of tasks')
pylab.hold(True)
#mpl.xticks(x,x)
#mpl.xlim(0,512)
pylab.legend(loc=2,prop={'size':8})
pylab.xlabel('Total number of tasks')
pylab.ylabel('Execution Time (seconds)')
pylab.title('Gromacs performance test on Stampede XSEDE using BJA -- PYP Molecule',fontsize = 10)
pylab.show()
