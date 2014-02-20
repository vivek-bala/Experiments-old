import pylab
import matplotlib.pyplot as mpl
import numpy as np
import math
import scipy.stats as stats
ip_size_256 = [27.373970747,26.7419006824,27.0097935994,32.3023366928,37.7996940613]
ip_size_1024 = [26.5225246747,27.9485737483,29.134759744,32.5670633316,37.6683170001]
ip_size_262144 = [27.5648813248,27.3826256593,31.8109149933,33.8164929549,42.5575597286]
ip_size_1048576 = [26.7629903158,26.9637416204,33.8624753157,41.3394823869,46.6167813937]
num_files = [1,2,3,4,5]
mpl.plot(num_files,ip_size_256,marker="*",linestyle="-",label = 'filesize = 256 B')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.8800468218,0.1465218593,0.2876207617,0.0861185611,0.8583357873])
pylab.hold(True)
mpl.plot(num_files,ip_size_1024,marker="*",linestyle="-",label = 'filesize = 1 KB')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.0585800985,0.3343926723,1.2688827657,0.5539400855,0.7972848424])
pylab.hold(True)
mpl.plot(num_files,ip_size_262144,marker="*",linestyle="-",label = 'filesize = 256 KB')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.4913818966,0.2172806974,0.5814970787,1.6553159909,4.2499492099])
pylab.hold(True)
mpl.plot(num_files,ip_size_1048576,marker="*",linestyle="-",label = 'filesize = 1 MB')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.1916601525,0.454035331,2.335634082,0.6042267469,0.1008148981])
#mpl.ylim(5,350)
mpl.xticks([0,1,2,3,4,5,6],[0,1,2,3,4,5,6])
mpl.xlim(0,6)
pylab.legend(loc=2,prop={'size':8})
pylab.xlabel('No. of Files')
pylab.ylabel('Time for Completion (seconds)')
pylab.title('No. of Files vs Time for Completion -- Cores Reserved = 8, Number of Jobs = 4',fontsize = 10)
pylab.show()
