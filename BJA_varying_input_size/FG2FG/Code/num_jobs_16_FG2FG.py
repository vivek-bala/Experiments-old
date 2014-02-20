import pylab
import matplotlib.pyplot as mpl
import numpy as np
import math
import scipy.stats as stats
ip_size_256 = [35.4151896636,36.4344913165,42.4224785169,51.6331827641,61.1704343955]
ip_size_1024 = [32.5128986041,36.2178207239,39.8188836575,51.069422245,61.1353949706]
ip_size_262144 = [29.62083896,35.3153413932,45.7610719999,62.1266667048,70.8938852151]
ip_size_1048576 = [32.2011213303,44.9629050096,55.1185120742,70.0188814004,84.8367480437]
num_files = [1,2,3,4,5]
mpl.plot(num_files,ip_size_256,marker="*",linestyle="-",label = 'filesize = 256 B')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.2629337905,0.6722030294,1.8253925277,0.910852681,0.629174668])
pylab.hold(True)
mpl.plot(num_files,ip_size_1024,marker="*",linestyle="-",label = 'filesize = 1 KB')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[2.1009947769,0.9140018192,0.2015420728,0.1617901004,0.1059403392])
pylab.hold(True)
mpl.plot(num_files,ip_size_262144,marker="*",linestyle="-",label = 'filesize = 256 KB')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.0326613602,0.6441139267,0.1764312802,3.2477323482,0.5038373521])
pylab.hold(True)
mpl.plot(num_files,ip_size_1048576,marker="*",linestyle="-",label = 'filesize = 1 MB')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[1.8496871494,0.3963014509,0.3990244496,0.50148766,0.2161190766])
#mpl.ylim(5,350)
mpl.xticks([0,1,2,3,4,5,6],[0,1,2,3,4,5,6])
mpl.xlim(0,6)
pylab.legend(loc=2,prop={'size':8})
pylab.xlabel('No. of Files')
pylab.ylabel('Time for Completion (seconds)')
pylab.title('No. of Files vs Time for Completion -- Cores Reserved = 8, Number of Jobs = 4',fontsize = 10)
pylab.show()
