import laspy
from laspy.file import File
import scipy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn import preprocessing
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import path

from pprint import pprint

# file_path = 'data/Job480220_2014_olc_four_rivers/Job480220_2014_olc_four_rivers.las'
file_path = 'data/Job480209_2014_olc_four_rivers/Job480209_2014_olc_four_rivers.las'

inFile = File(file_path, mode='r')
dataset = np.vstack([inFile.x, inFile.y, inFile.z]).transpose()

def reset_z_o(v):
    v = np.array(v)
    v_min = np.min(v)
    v_max = np.max(v)
    return (v - v_min)/(v_max - v_min)

sp_dataset = np.vstack([inFile.x, inFile.y, inFile.z]).T
col_dataset = np.vstack([
    reset_z_o(inFile.red),
    reset_z_o(inFile.green),
    reset_z_o(inFile.blue),
    reset_z_o(inFile.intensity)
]).T

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# pprint(col_dataset)
# pprint(sp_dataset[:,0])
# for sp, col in zip(sp_dataset, col_dataset):
#     pprint(col)
ax.scatter(sp_dataset[:,0],sp_dataset[:,1], sp_dataset[:,2], c=col_dataset, marker=".")
plt.show()
