# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:17:00 2015

@author: A30123
"""
from matplotlib.mlab import PCA as mlabPCA
import numpy as np
import time
       
def PCA_module(training_data,testing_data):
#    from matplotlib.mlab import PCA as mlabPCA
#    import numpy as np
#    import time
    tstart = time.time()
    mlab_pca=mlabPCA(training_data)
#    scores=mlab_pca.Y
    loadings=mlab_pca.Wt
    training_mean=np.mean(training_data, axis=0)
    training_std=np.std(training_data,axis=0)

    normalized_testing=(testing_data-training_mean)/training_std
    print('PCA TIME: %.2f secs' % (time.time()-tstart))
    return np.dot(normalized_testing,loadings)
    
    
X=np.asarray([173,155,175,171,166,167,163,155,159,168,166,169,159,154,160,66,49,72,68,63,64,61,52,55,65,61,73,57,49,60])
X=np.transpose(np.reshape(X,(2,15)))

x_test=np.asarray([[173,54]])

transformed_data=PCA_module(X,x_test)