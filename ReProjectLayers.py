# This script will re-project multiple datasets into a similar coordinate system then store all layers into the same folder.
# Author: Matt Crichton

# Import required modules.
import arcpy
import os

# Create variables from tool parameters.
targetFolder1 = arcpy.GetParameterAsText(0)
targetProjection = arcpy.GetParameterAsText(1)

# Set up a workspace and grant overwrite permissions.
arcpy.env.workspace = targetFolder1
arcpy.env.overwriteOutput = True

# Create a variable which stores the list of layers to be processed.
listLayer = arcpy.ListFeatureClasses()

# Get a count of feature classes in the Target Folder.
count = len(listLayer)

# Get properties of the Targer Layer projection.
tlProperties = arcpy.Describe(targetProjection)

# Get the spatial reference of the Target Layer.
spatialRef = tlProperties.SpatialReference
projectedLayers = []

# Create a for loop to check the projection of all layers in the target folder.
for x in range(len(listLayer)):
    if spatialRef.name != arcpy.Describe(listLayer[x]).SpatialReference.name:
        arcpy.Project_management(listLayer[x],listLayer[x].rstrip(".shp") + "_projected", spatialRef)
        projectedLayers.append(listLayer[x])
        print arcpy.AddMessage(listLayer[x])
if len(projectedLayers) > len(layerList):
    arcpy.AddMessage('You pojected the following layers:' + str(projectedList).strip('[]')) 
