from paraview.simple import *
import vtk 

image = vtk.vtkPNGReader()
image.SetFileName('/Users/origimbo/Software/ParaviewPlugins/Macros/AMCGLogo.png')
image.Update()

rep = vtk.vtkLogoRepresentation()
rep.SetImage(image.GetOutput())

widget = vtk.vtkLogoWidget()
widget.SetRepresentation(rep)
widget.SetInteractor(GetRenderView().GetInteractor())
widget.On()
