import numpy as np

a = np.loadtxt('YearPredictionMSD')
mi = a.min(0)
ma = a.max(0)
res = (a-mi) / (ma-mi)
np.savetxt('YearPrediction_normalized', res, fmt="%.6g")
