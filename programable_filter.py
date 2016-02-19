input =self.GetInput() 
output=self.GetOutput()

output.DeepCopy(input)

points = output.GetPoints()

x= [0.0,0.0,0.0]
for i in range(points.GetNumberOfPoints()):
    points.GetPoint(i,x)
    x[1]=-x[1]
    points.SetPoint(i,x)

output.GetPointData().DeepCopy(input.GetPointData())
output.GetCellData().DeepCopy(input.GetCellData())
