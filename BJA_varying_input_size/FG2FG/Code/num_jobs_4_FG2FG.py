import pylab
import matplotlib.pyplot as mpl
import numpy as np
import math
import scipy.stats as stats
ip_size_256 = [25.3920142651,26.1357589563,25.293721358,25.3976306915,26.2484043439]
ip_size_1024 = [25.552486976,25.8897699515,25.2185330391,26.5546876589,25.9388730526]
ip_size_262144 = [25.2378062407,26.7423673471,25.3531062603,25.3829102516,24.7021216551]
ip_size_1048576 = [25.3194386959,25.4880398909,26.1573813756,24.8844320774,29.1084096432]
num_files = [1,2,3,4,5]
mpl.plot(num_files,ip_size_256,marker="*",linestyle="-",label = 'filesize = 256 B')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.2573052925,1.479418264,0.6700185602,0.4713267328,0.6043294998])
pylab.hold(True)
mpl.plot(num_files,ip_size_1024,marker="*",linestyle="-",label = 'filesize = 1 KB')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.3560274503,0.1974192077,0.3094805261,0.1789326601,0.506410393])
pylab.hold(True)
mpl.plot(num_files,ip_size_262144,marker="*",linestyle="-",label = 'filesize = 256 KB')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.3222690813,0.7794620831,0.27288038,0.5161363321,0.424571685])
pylab.hold(True)
mpl.plot(num_files,ip_size_1048576,marker="*",linestyle="-",label = 'filesize = 1 MB')
#mpl.errorbar(num_files,ip_size_256,xerr=None,yerr=[0.262567186,0.3358515242,0.7289714074,0.2202385572,0.0523080702])
mpl.ylim(20,30)
mpl.xticks([0,1,2,3,4,5,6],[0,1,2,3,4,5,6])
mpl.xlim(0,6)
pylab.legend(loc=2,prop={'size':8})
pylab.xlabel('No. of Files')
pylab.ylabel('Time for Completion (seconds)')
pylab.title('No. of Files vs Time for Completion -- Cores Reserved = 8, Number of Jobs = 4',fontsize = 10)
pylab.show()
