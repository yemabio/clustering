import matplotlib.pyplot as plt
import numpy as np

def plot_data(data,pca=None, xmin=-5,ymin=-5,zmin=-5,xmax=5,ymax=5,zmax=5,pc_scale=4,s=1,three_d=False,figsize=(3,3)):
    fig = plt.figure(figsize=figsize)
    
    if three_d:
        ax = plt.axes(projection='3d')
        ax.scatter3D(data[:,0],data[:,1],data[:,2], s=s, color='k')
        ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), zlim=(zmin-1, zmax+1),aspect='equal')
        if pca:
            origin = np.array([0,0,0])
            for component, ev, perc_ev in zip(pca.components_, pca.explained_variance_, pca.explained_variance_ratio_):
                ax.quiver(*origin,component[0], component[1], component[2], color='r',scale=pc_scale/ev,label=perc_ev)
        ax.legend()
            
    else:
        ax = plt.axes()
        ax.scatter(data[:,0],data[:,1],s=s, color='k')
        if pca:
            origin = np.array([0,0])
            for component, ev, perc_ev in zip(pca.components_, pca.explained_variance_, pca.explained_variance_ratio_):
                ax.quiver(*origin,component[0], component[1], color='r',scale=pc_scale/ev, label=perc_ev)
        ax.legend()

        ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

        # Set bottom and left spines as x and y axes of coordinate system
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')

        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_xticklabels([])
        ax.set_yticklabels([])

    
    # fig.canvas.toolbar_visible = False
    fig.canvas.header_visible = False
    fig.canvas.footer_visible = False
    return fig, ax


