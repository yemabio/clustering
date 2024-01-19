from sklearn.decomposition import PCA
import numpy as np

def get_pca_object(data, n_components=None):
    if n_components==None:
        n_components = data.shape[1]
    pca = PCA(n_components=n_components)
    pca.fit(data)
    return(pca)

def get_participation_ratio(pca_object):
    variance = pca_object.explained_variance_
    return np.sum(variance)**2/np.sum(variance**2)

def get_top_pcs(pca_object, data, topk=3):
    top_k_pcs = np.argsort(np.mean(pca_object.transform(data),axis=0))[-topk:]
    return top_k_pcs[::-1]