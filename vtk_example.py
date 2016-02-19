#!/usr/bin/env python

from vtk import*
 
#Create a source
textSource = vtkVectorText();
textSource.SetText("Hello AMCG!");
#textSource.SetForegroundColor(1.0, 0.0, 0.0);
#textSource.SetBackgroundColor(0.0, 0.0, 1.0);
#textSource.BackingOn();
textSource.Update();
 
#Create a mapper and actor
mapper = vtkPolyDataMapper();
mapper.SetInputConnection(textSource.GetOutputPort());
 
actor = vtkActor();
actor.SetMapper(mapper);
actor.GetProperty().SetColor(1, 0, 0)

 
#Create a renderer, render window, and interactor
renderer = vtkRenderer();
renderWindow = vtkRenderWindow();
renderWindow.AddRenderer(renderer);
renderWindowInteractor = vtkRenderWindowInteractor();
renderWindowInteractor.SetRenderWindow(renderWindow);
 
#Add the actor to the scene
renderer.AddActor(actor);
renderer.SetBackground(1,1,1); # Background color white
 
#Render and interact
renderWindow.Render();
renderWindowInteractor.Start();
