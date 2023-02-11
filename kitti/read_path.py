import os, sys
# import numpy

# Get the path to the text file
file_path = "D:/studio/Blender/txt"
# Read the text file and store the point data in a list
points = []

with open(os.path.join(file_path, "curve_points.txt")) as f:
    for line in f:
#        x, y, z, a = map(float, line.strip().split())
#        points.append((x, y, z, a))
        x, y, z = map(float, line.strip().split())
        points.append((x, y, z))

import bpy

# Create a curve object and set the points as nodes of the curve
curve = bpy.data.curves.new("Curve", "CURVE")
curve.dimensions = '3D'
spline = curve.splines.new("BEZIER")
#spline = curve.splines.new("POLY")
spline.bezier_points.add(len(points) - 1)
#spline.points.add(len(points) - 1)
for i, coord in enumerate(points):
    spline.bezier_points[i].co = coord
#    spline.points[i].co = coord

#spline.type = 'POLY'
# Create an object to hold the curve and add it to the scene
curve_obj = bpy.data.objects.new("CurveObj", curve)
bpy.context.collection.objects.link(curve_obj)

#This script assumes that the text file curve_points.txt is located in the same directory as the Blender file and contains one point per line, with the x, y, and z values separated by spaces. You can modify this script to fit the format of your text file.

#bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
