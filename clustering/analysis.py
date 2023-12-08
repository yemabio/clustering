from sklearn.decomposition import PCA

def get_pca_object(data, n_components=None):
    if n_components==None:
        n_components = data.shape[1]
    pca = PCA(n_components=n_components)
    pca.fit(data)
    return(pca)