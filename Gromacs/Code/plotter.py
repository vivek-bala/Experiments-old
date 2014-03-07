import pylab
import matplotlib.pyplot as mpl
import numpy as np
import math
import scipy.stats as stats
_core1 = [16.5199999809,33.2000000477,67.1900000572,130.809999943,261.789999962,532.730000019]
_core2 = [16.8499999046,33.379999876,66.8499999046,130.870000124,260.850000143,527.789999962]
_core4 = [0,33.7300000191,67.129999876,130.830000162,260.429999828,525.289999962]
_core8 = [0,0,66.0599999428,130.370000124,259.550000191,522.380000114]
_core16 = [0,0,0,73.2000000477,138.560000181,272.930000067]
_core32 = [0,0,0,0,91.4100000858,159.25999999]
_core64 = [0,0,0,0,0,144.00999999]
no_tasks = [2,4,8,16,32,64]
x = np.exp2(np.arange(7))
pylab.plot(no_tasks,_core1,marker='o',linestyle="-",label = 'Pilot size = 1')
pylab.hold(True)
pylab.plot(no_tasks,_core2,marker='o',linestyle="-",label = 'Pilot size = 2')
pylab.hold(True)
pylab.plot(no_tasks,_core4,marker='o',linestyle="-",label = 'Pilot size = 4')
pylab.hold(True)
pylab.plot(no_tasks,_core8,marker='o',linestyle="-",label = 'Pilot size = 8')
pylab.hold(True)
pylab.plot(no_tasks,_core16,marker='o',linestyle="-",label = 'Pilot size = 16')
pylab.hold(True)
pylab.plot(no_tasks,_core32,marker='o',linestyle="-",label = 'Pilot size = 32')
pylab.hold(True)
pylab.plot(no_tasks,_core64,marker='o',linestyle="-",label = 'Pilot size = 64')
#mpl.xticks(x,x)
#mpl.xlim(0,64)
pylab.legend(loc=2,prop={'size':8})
pylab.xlabel('Total number of tasks')
pylab.ylabel('Execution Time (seconds)')
pylab.title('Gromacs performance test on Sierra Futuregrid using BJA -- PYP Molecule',fontsize = 10)
pylab.show()
