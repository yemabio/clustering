from sklearn.decomposition import PCA

def get_pca_object(data):
    pca = PCA(n_components=data.shape[1])
    pca.fit(data)
    return(pca)