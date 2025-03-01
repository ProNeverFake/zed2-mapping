import open3d as o3d
import numpy as np
import ipdb

def read_obj_file(file_path):
    vertices = []
    colors = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                parts = line.split()
                vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
                color = [float(parts[4]), float(parts[5]), float(parts[6])]
                vertices.append(vertex)
                colors.append(color)
    return np.array(vertices), np.array(colors)

def save_to_pcd(vertices, colors, output_path):
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(vertices)
    point_cloud.colors = o3d.utility.Vector3dVector(colors)
    o3d.io.write_point_cloud(output_path, point_cloud)

if __name__ == "__main__":
    obj_file_path = "/home/blackbird/zed2-mapping/svo_file/map.obj"
    pcd_file_path = "/home/blackbird/zed2-mapping/svo_file/map.pcd"
    
    vertices, colors = read_obj_file(obj_file_path)
    # ipdb.set_trace()
    save_to_pcd(vertices, colors, pcd_file_path)
    print(f"PCD file saved to {pcd_file_path}")