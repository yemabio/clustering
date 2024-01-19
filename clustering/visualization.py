import matplotlib.pyplot as plt
import numpy as np
#TODO: code for visualizing the PCs with the highest usage
#TODO: Move codeblocks to modules 
def plot_data(data,pca=None,color=[], pc_scale=4,s=1,three_d=False,figsize=(3,3)):
    fig = plt.figure(figsize=figsize)
    # if color == None:
    #     color='k'
    if three_d:
        ax = plt.axes(projection='3d')
        if len(color)>0:
            ax.scatter3D(data[:,0],data[:,1],data[:,2], s=s, c=color, cmap='Spectral')
        else:
            ax.scatter3D(data[:,0],data[:,1],data[:,2], s=s, color='k')
        # ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), zlim=(zmin-1, zmax+1),aspect='equal')
        if pca:
            origin = np.array([0,0,0])

            for component, ev, perc_ev in zip(pca.components_, pca.explained_variance_, pca.explained_variance_ratio_):
                ax.quiver(*origin,component[0], component[1], component[2], color='r',length=perc_ev*pc_scale,label=perc_ev)
            
    else:
        ax = plt.axes()
        if len(color)>0:
            ax.scatter(data[:,0],data[:,1], s=s, c=color, cmap='Spectral')
        else:
            ax.scatter(data[:,0],data[:,1], s=s, color='k')
        if pca:
            origin = np.array([0,0])
            for component, ev, perc_ev in zip(pca.components_, pca.explained_variance_, pca.explained_variance_ratio_):
                ax.quiver(*origin,component[0], component[1], color='r',scale=pc_scale/ev, label=perc_ev)
        # ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

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


