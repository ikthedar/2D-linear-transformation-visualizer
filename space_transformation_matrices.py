import numpy as np
import matplotlib.pyplot as plt

def apply_transformation(matrix, points):
    """Applies a transformation matrix to a set of points."""
    return np.dot(points, matrix.T)

def plot_transformation(matrix):
    """Plots original and transformed vectors and grid."""
    # Original grid
    grid_x, grid_y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
    grid_points = np.column_stack([grid_x.flatten(), grid_y.flatten()])
    
    # Transform grid
    transformed_grid = apply_transformation(matrix, grid_points)
    
    # Plot
    plt.figure(figsize=(8, 8))
    plt.quiver(*grid_points.T, color="blue", alpha=0.5, scale=1, scale_units='xy', angles='xy', width=0.0025, label="Original Grid")
    plt.quiver(*transformed_grid.T, color="red", alpha=0.5, scale=1, scale_units='xy', angles='xy', width=0.0025, label="Transformed Grid")
    
    # Formatting
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Linear Transformation Visualization")
    plt.show()

if __name__ == "__main__":
    # Get user input for 2x2 matrix
    print("Enter a 2x2 transformation matrix:")
    matrix = []
    for i in range(2):
        row = input(f"Row {i + 1} (space-separated): ").split()
        matrix.append([float(x) for x in row])
    
    matrix = np.array(matrix)
    plot_transformation(matrix)
