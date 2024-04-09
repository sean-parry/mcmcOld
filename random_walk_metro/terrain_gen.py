import numpy as np
from scipy.ndimage import convolve
from noise import pnoise2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_perlin_noise(width:int,
                          height:int,
                          scale: int = 100,
                          octaves: int = 6,
                          persistence: float = 0.5,
                          lacunarity: float = 2.0,
                          seed: int = 1 
                          ) -> list[list[float]]:
    
    grid = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            grid[i][j] = pnoise2( i / scale,
                                  j / scale,
                                  octaves=octaves,
                                  persistence=persistence,
                                  lacunarity=lacunarity,
                                  repeatx=1024,
                                  repeaty=1024,
                                  base=seed)
    return grid


def erode(grid: list[float], iterations: int = 100) -> list[list[float]]:
    kernel = np.array([[0.05, 0.2, 0.05],
                       [0.2, 0.2, 0.2],
                       [0.05, 0.2, 0.05]])

    for _ in range(iterations):
        erosion = convolve(grid, kernel, mode='constant', cval=0.0)
        grid -= erosion
    return grid


def plot_grid(result: list[list[float]]) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.arange(result.shape[0])
    y = np.arange(result.shape[1])
    X, Y = np.meshgrid(x, y)

    ax.plot_surface(X, Y, result, cmap='terrain')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
    return None


def get_grid(n: int = 100,
             scale: int = 100,
             octaves: int = 8,
             persistence: float = 0.6,
             lacunarity: float = 2.0,
             erosion_iterations: int = 1000,
             erosion_seed: int = 1
             ) -> list[float]:
    
    noise_grid = generate_perlin_noise(height=n, width= n, scale=scale, octaves=octaves, 
                                       persistence=persistence, lacunarity=lacunarity, 
                                       seed=erosion_seed)
    eroded_grid = erode(noise_grid, iterations=erosion_iterations)
    return abs(eroded_grid)


def main():
    result = get_grid()
    plot_grid(result)


if __name__ == '__main__':
    main()