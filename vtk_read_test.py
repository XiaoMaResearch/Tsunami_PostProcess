import meshio
import glob
import time

input_folder = 'E:\\Tsunami_3D\\100m\\disp_Z\\input_vtk'
output_folder = 'E:\\Tsunami_3D\\100m\\disp_Z\\output_new'
filename = 'hex8_100m-zpos_t8980000.vtk'
input_Path_list = glob.glob(input_folder + '\\' + '*.vtk')

def convert(input_Path):

    filename = input_Path.split('\\')
    output_Path = output_folder + '\\' + filename[-1]
    mesh = meshio.read(input_Path)
    meshio.write_points_cells(
        output_Path,
        mesh.points,
        mesh.cells,
        point_data=mesh.point_data,
        )



from multiprocessing import Pool, cpu_count


if __name__ == '__main__':
    print('num cpus = ',cpu_count())
    t0 = time.time()
    p = Pool()
    p.map(convert,input_Path_list)
    t1 = time.time()
    print('total time=', t1-t0)
# mesh.points -- np.ndarray
# mesh.cells -- dict
# mesh.point_data -- dict
# mesh.point_data['displacement'] -- np.ndarray
# mesh.point_data['velocity'] -- np.ndarray

# mesh.cell_data -- dict


# print('mesh\n',mesh)
# print('mesh point data\n',type(mesh.point_data))
# print('mesh cell data\n',type(mesh.cell_data))
# print('mesh cell data \n',mesh.cell_data)
#
#
# print('mesh point data -- displacement\n',type(mesh.point_data['displacement']))
# print('mesh point data -- velocity\n',type(mesh.point_data['velocity']))
#
# print('mesh_points\n',type(mesh.points))
# print('mesh_cells \n',type(mesh.cells))
