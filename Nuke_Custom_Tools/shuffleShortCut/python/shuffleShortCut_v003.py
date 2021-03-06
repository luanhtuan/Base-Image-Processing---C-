
# -------------------------------------------------
# shuffleShortcuts.py
# Version: 0.2.1
# Author: Ben McEwan
#
# Last Modified by: Lu Anh Tuan
# Last Update: June 2th, 2019
# -------------------------------------------------

# -------------------------------------------------
# USAGE:
#
# Create a shuffle node that shuffle RGBA channles into the Green channel.
# -------------------------------------------------

import nuke

# Define the function 
def createCustomShuffle(in_channel, out_channel, set_channel, rColor, gColor, bColor):

    # Create a new shuffle node, and assign it to variable so we can change somethings...
    myShuffle = nuke.createNode("Shuffle")

    # change the input & output channels to what is define in the in_channel and out_channel argument 

    myShuffle["in"].setValue(in_channel)
    myShuffle["out"].setValue(out_channel)
    
    
    # Change the relevant knob to shuffle the RGBA channels to the green channel. 
    myShuffle["red"].setValue(set_channel)
    myShuffle["green"].setValue(set_channel)
    myShuffle["blue"].setValue(set_channel)
    myShuffle["alpha"].setValue(set_channel)
    
    # Change the node color to green( we have to convert Nuke's weird to hex colour values to RGB to be a bit more human-readable)
    myShuffle["tile_color"].setValue(int("%02x%02x%02x%02x" % (rColor*255, gColor*255, bColor*255, 1),16))
    
    # Other way create __tile color__
    #myShuffle["tile_color"].setValue(0xff000ff)
    #nuke.selectedNode()["tile_color"].setValue(0xff000ff)
    
    # Add a node label
    myShuffle["label"].setValue("[value green] > [value out]")



def shuffleRGBchannels():
    
    # Create a variable for the selected node, before creating any shuffle nodes.
    selectedNode = nuke.selectedNode()

    # Get the X-Position and y-Position of the selected node.
    selectedNode_xPos = selectedNode['xpos'].value()
    selectedNode_yPos = selectedNode['ypos'].value()

    # Create our Red, Green & Blue Shuffle nodes, and assign them to a variable after creation.
    createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)
    redShuffle = nuke.selectedNode()
    createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)
    greenShuffle = nuke.selectedNode()
    createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)
    blueShuffle = nuke.selectedNode()

    # Set the input of the Red Shuffle node to the selected node, and Transform the Red Shuffle node down and to the left.
    redShuffle.setInput(0, selectedNode)
    redShuffle['xpos'].setValue(selectedNode_xPos-150)
    redShuffle['ypos'].setValue(selectedNode_yPos+150)

    # Set the input of the Green Shuffle node to the selected node, and Transform the Green Shuffle node down.
    greenShuffle.setInput(0, selectedNode)
    greenShuffle['xpos'].setValue(selectedNode_xPos)
    greenShuffle['ypos'].setValue(selectedNode_yPos+150)

    # Set the input of the Blue Shuffle node to the selected node, and Transform the Blue Shuffle node down and to the right.
    blueShuffle.setInput(0, selectedNode)
    blueShuffle['xpos'].setValue(selectedNode_xPos+150)
    blueShuffle['ypos'].setValue(selectedNode_yPos+150)


 def MergRGBChannel():

    # Create Merge RGB Channel
	MergeRGB = nuke.createNode("Merge2", inpanel = False)
	MergeRGB['operation'].setValue('max')
	MergeRGB = nuke.selectConnectedNodes()
	for MergeRGB in nuke.selectedNodes():
	    nuke.autoplace(MergeRGB)
	nuke.selectAll()

	
# Add menu
nuke.menu("Nodes").addCommand("Channel/Shuffle (Red to All)", "shuffleShortCut_v003.createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)", "ctrl+shift+r", icon="redShuffle.png", shortcutContext=2)
nuke.menu("Nodes").addCommand("Channel/Shuffle (Green to All)", "shuffleShortCut_v003.createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)", "ctrl+shift+g", icon="greenShuffle.png", shortcutContext=2)
nuke.menu("Nodes").addCommand("Channel/Shuffle (Blue to All)", "shuffleShortCut_v003.createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)", "ctrl+shift+b", icon="blueShuffle.png", shortcutContext=2)
nuke.menu("Nodes").addCommand("Channel/Shuffle (Alpha to All)", "shuffleShortCut_v003.createCustomShuffle('alpha', 'rgba', 'alpha', 1, 1, 1)", "ctrl+shift+a", icon="alphaToAll.png", shortcutContext=2)
nuke.menu("Nodes").addCommand("Channel/Shuffle (Alpha to 0)", "shuffleShortCut_v003.createCustomShuffle('alpha', 'alpha', 'black', 0, 0, 0)", "ctrl+shift+`", icon="alpha0Shuffle.png", shortcutContext=2)
nuke.menu("Nodes").addCommand("Channel/Shuffle (Alpha to 1)", "shuffleShortCut_v003.createCustomShuffle('alpha', 'alpha', 'white', 1, 1, 1)", "ctrl+shift+1", icon="alpha1Shuffle.png", shortcutContext=2)



nuke.menu("Nodes").addCommand("Channel/Shuffle (Split RGB Channels)", "shuffleShortCut_v003.shuffleRGBchannels()", "ctrl+shift+s", icon="ShuffleSplitRGB.png",  shortcutContext=2)
nuke.menu("Nodes").addCommand("Channel/Shuffle (Merge RGB Channels)", "shuffleShortCut_v003.MergRGBChannel()", "ctrl+shift+s", icon="ShuffleSplitRGB.png", shortcutContext=2)
