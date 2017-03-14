import vtk

tabPoints = [
    (0.5, 0.5, -0.5),
    (0.5, 0.5, 0.5),
    (0.5, -0.5, 0.5),
    (0.5, -0.5, -0.5),
    (-0.5, 0.5, -0.5),
    (-0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5),
    (-0.5, -0.5, -0.5),
]

cubeFaces = [
    (0, 1, 2, 3),
    (4, 5, 1, 0),
    (7, 4, 0, 3),
    (7, 6, 5, 4),
    (3, 2, 6, 7),
    (2, 1, 5, 6)
]

triangleFaces = [
    (0, 1, 2),
    (0, 2, 3),
    (4, 5, 1),
    (4, 1, 0),
    (7, 4, 0),
    (7, 0, 3),
    (7, 6, 5),
    (7, 5, 4),
    (3, 2, 6),
    (3, 6, 7),
    (2, 1, 5),
    (2, 5, 6)
]

triangleStrip = [7, 4, 3, 0, 1, 4, 5, 6, 1, 2, 3, 6, 7, 4]


def write(polydata, file):
    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName(file)
    writer.SetInputData(polydata)
    writer.Write()


# Cube with square
points = vtk.vtkPoints()
poly = vtk.vtkCellArray()
scalars = vtk.vtkFloatArray()
cube = vtk.vtkPolyData()
cube.SetPoints(points)

for i in range(0, 8):
    points.InsertPoint(i, tabPoints[i])

for face in cubeFaces:
    poly.InsertNextCell(4, face)

for i in range(0, 8):
    scalars.InsertTuple1(i, i)

cube.SetPolys(poly)
cube.GetPointData().SetScalars(scalars)

write(cube, 'cubeSquare.vtk')

# Cube with triangle
poly = vtk.vtkCellArray()

for face in triangleFaces:
    poly.InsertNextCell(3, face)

cube.SetPolys(poly)

write(cube, 'cubeTriangle.vtk')

# Cube with triangle strip
strip = vtk.vtkCellArray()
strip.InsertNextCell(len(triangleStrip))
for point in triangleStrip:
    strip.InsertCellPoint(point)

cube = vtk.vtkPolyData()
cube.SetPoints(points)
cube.SetStrips(strip)
cube.GetPointData().SetScalars(scalars)

write(cube, 'cubeStrip.vtk')
