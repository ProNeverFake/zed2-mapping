import numpy as np

import matplotlib.pyplot as plt

def visualize_depth_npy(file_path):
    # Load the .npy file
    depth_data = np.load(file_path)
    
    # Display the depth data using matplotlib
    plt.imshow(depth_data, cmap='viridis')
    plt.colorbar(label='Depth')
    plt.title('Depth Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

if __name__ == "__main__":
    file_path = '/home/blackbird/zed2-mapping/depth.npy' 
    visualize_depth_npy(file_path)