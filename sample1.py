import sys
import bpy


f_path = "/home/darshan/Mesh_C2M_DIST_DELAUNAY.stl"
file1 = "Mesh_C2M_DIST_DELAUNAY.stl"
bpy.ops.import_mesh.stl(filepath=f_path)



#bpy.ops.import_mesh.stl(filepath="/home/darshan/Mesh_C2M_DIST_DELAUNAY.stl", filter_glob="*.stl", files=None, directory="/home/darshan")
#bpy.ops.import_mesh.stl(filepath=f_path, filter_glob="*.stl",  files=[{"name":file1, "name":file1}], directory="/home/darshan")
