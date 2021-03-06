
# -------------------------------------------------
# shortcut_LogToLinSwitcher.py
# Version: 1.0.0
# Author: Lu Anh Tuan
#
# Last Modified by: Lu Anh Tuan
# Last Update: August 4th, 2019
# -------------------------------------------------

# -------------------------------------------------
# USAGE:
#
# - Ctrl+Alt+D toggle between log2lin/lin2log, lin2log/log2lin.
# -------------------------------------------------

import nuke

def shortcut_LogToLinSwitcher():

    node = nuke.selectedNode()

    LogToLin_ops = {'log2lin': 'lin2log', 'lin2log': 'log2lin'}

    if node.Class() == "Log2Lin":

	current_oop = node['operation'].value()

	if current_oop in LogToLin_ops.keys():

	    node['operation'].setValue(LogToLin_ops[node['operation'].value()])

	elif current_oop in LogToLin_ops.values():
		
            node['operation'].setValue(LogToLin_ops.keys()[node['operation'].value().index(current_oop)])




# Add menu item
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Toggle Operation to log2lin', 'shortcut_LogToLinSwitcher.shortcut_LogToLinSwitcher()', 'ctrl+shift+d')		    	
