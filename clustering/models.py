import numpy as np

def generate_gaussian(mean, cov, n_points, seed=None):
    if seed:
        np.random.seed(seed=seed)
    data = np.random.multivariate_normal(mean,cov, n_points)
    return(data)

def generate_noisy_sine(A=1, xmin=-5, xmax=5, n_points=100, T=10, y_noise_scale=1):
    x = np.linspace(xmin,xmax,n_points)
    noise = [np.random.normal(scale=y_noise_scale) for _ in range(len(x))]
    y = A*np.sin(2*np.pi/T*x) + noise
    #TODO: TUNE FREQUENCY
    # y = A*np.sin(x)+noise
    return np.column_stack([x,y])

def generate_3d_sine(A=1, xmin=-5, xmax=5, n_points=100, T=10, y_noise_scale=1):
    twod_sine = generate_noisy_sine(A=A, xmin=xmin, xmax=xmax, n_points=n_points, T=T, y_noise_scale=y_noise_scale)
    z = np.ones((len(twod_sine),1))
    return np.column_stack((twod_sine,z))