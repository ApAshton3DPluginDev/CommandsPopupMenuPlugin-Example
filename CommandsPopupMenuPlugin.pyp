"""
Popup Menu GUI with Commands Example
Author: Asthon Rolle AKA AP Asthon
Cinema 4D Python Plugin For C4D
Compatible:
    - Win / Mac
    - R16, R17, R18, R19, R20, R21
"""
# Imports
import os
import sys
import c4d
from c4d import plugins, gui, bitmaps, documents, storage, utils
from c4d.gui import GeDialog as WindowDialog
from c4d.plugins import CommandData, TagData, ObjectData

iPath = os.path.join(os.path.dirname(__file__), 'res', "yourIcon.png")

def CustomCommandPopupMenu():
    """" Popup Commands Ids Only Menu """
    menu = c4d.BaseContainer()
    menu.InsData(0, '') # Append separator
    menu.InsData(PLUG_2['ID'], "CMD")           # eg: menu.InsData(00000000, "CMD")
    menu.InsData(0, '') # Append separator
    menu.InsData(PLUG_3['ID'], "CMD")
    result = gui.ShowPopupDialog(cd=None, bc=menu, x=c4d.MOUSEPOS, y=c4d.MOUSEPOS)
    return True    

class CMDTool(CommandData):

    def __init__(self, CMD):
        super(CMDTool, self).__init__()
        self.CMDTool = CMD

    def Init(self, op):
        return True
    def Message(self, type, data):
        return True
  
    def Execute(self, doc):

        if self.CMDTool == "PCT":
            CustomCommandPopupMenu()

        if self.CMDTool == "PCT1":
            gui.MessageDialog("PlugCafeTool2")

        if self.CMDTool == "PCT2":
            gui.MessageDialog("PlugCafeTool2")

    def RestoreLayout(self, sec_ref):
        return True
    def ExecuteOptionID(self, doc, plugid, subid):
        gui.MessageDialog("PlugCafeTool2 Options")
        return True

# ----------------------------------------------------
#               Plugin Registration
# ----------------------------------------------------
#  // Plugin Flags Tpyes  //
class PluginFlags:
    """ Register Info Plugin Flags Tpyes """
    # Plugin General Flags :
    HidePlugin = c4d.PLUGINFLAG_HIDE
    HideTool = c4d.PLUGINFLAG_HIDEPLUGINMENU
    RefreshPlugin = c4d.PLUGINFLAG_REFRESHALWAYS
    SmallNodePlugin = c4d.PLUGINFLAG_SMALLNODE
    # Command Plugin Flags:
    OptionGear = c4d.PLUGINFLAG_COMMAND_OPTION_DIALOG   # A info flag / Command has additional options. The user can access them through a small gadget.
    # Tag Plugin Flags :
    TagVis = c4d.TAG_VISIBLE                            # The tag can be seen in the object manager.
    TagMul = c4d.TAG_MULTIPLE                           # Multiple copies of the tag allowed on a single object.
    TagHier = c4d.TAG_HIERARCHICAL                      # The tag works hierarchical, so that sub-objects inherit its properties (e.g. the material tag).
    TagExp = c4d.TAG_EXPRESSION                         # The tag is an expression.
    TagTem = c4d.TAG_TEMPORARY                          # Private.
    # Object Plugin Flags:
    oMod = c4d.OBJECT_MODIFIER                          # Modifier object. Deforms the surrounding object. (E.g. bend.)
    oHier = c4d.OBJECT_HIERARCHYMODIFIER                # Hierarchical modifier. Deforms the surrounding objects together with other instances in a hierarchy chain. Only the top-most instance of the plugin in a chain is called. (E.g. bones.)Hierarchical modifier. Deforms the surrounding objects together with other instances in a hierarchy chain. Only the top-most instance of the plugin in a chain is called. (E.g. bones.)
    oGen = c4d.OBJECT_GENERATOR                         # Generator object. Produces a polygonal or spline representation on its own. (E.g. primitive cube.)
    oInput = c4d.OBJECT_INPUT                           # Used in combination with OBJECT_GENERATOR. Specifies that the generator uses builds a polygon or spline, using its subobjects as input. (E.g. Sweep Subdivision Surface, Boolean.)
    oPart = c4d.OBJECT_PARTICLEMODIFIER                 # Particle modifier.
    oSpline = c4d.OBJECT_ISSPLINE                       # The object is a spline.
    oCamera = c4d.OBJECT_CAMERADEPENDENT                # Camera dependent.
    oPointObj = c4d.OBJECT_POINTOBJECT                  # Point Object.
    oPolyObj = c4d.OBJECT_POLYGONOBJECT                 # Polygon object.
PF = PluginFlags()
# // Register Plugin Add-on Tool Tpyes to Cinema 4D //
def RegisterCommandData(id, str_name, infoflags, iconName, helpInfo, dataClass):
    """ A CommandData Tool Plugin Register """
    DESCRIPTIONS = "" #ToolInfo_Description(helpInfo)
    plugin_Icon = c4d.bitmaps.BaseBitmap()
    plugin_Icon.InitWith(iconName)
    result = plugins.RegisterCommandPlugin(id=id,                       # Plugin register ID.
                                        str=str_name,                   # This is for the Plugin Name to show in the Plugins lic4d.storage.
                                        info=infoflags,                 # If you want a option button once you have a ExecuteOptionID in Data Class, 
                                                                        # then put in Flags info=c4d.PLUGINFLAG_COMMAND_OPTION_DIALOG|c4d.PLUGINFLAG_COMMAND_HOTKEY,
                                        icon=plugin_Icon,               # Plugin Icon Image.
                                        help=DESCRIPTIONS,              # The plugin help info is on what the plugin does.
                                        dat=dataClass)                  # The plugin data class.
    return True
# // Register Tools // 
PLUG_1 = {'ID':1050002, 'Icon':iPath, 'Name':"CommandTools Menu",'flags':0, 'Data':CMDTool("PCT"), 'Info':""}
PLUG_2 = {'ID':1051421, 'Icon':iPath, 'Name':"PlugCafeTool-1", 'flags':PF.HideTool, 'Data':CMDTool("PCT1"), 'Info':""}
PLUG_3 = {'ID':1054336, 'Icon':iPath, 'Name':"PlugCafeTool-2", 'flags':PF.HideTool|PF.OptionGear, 'Data':CMDTool("PCT2"), 'Info':""}

if __name__ == '__main__':
    dir, file = os.path.split(__file__)
    RegisterCommandData(PLUG_1["ID"], PLUG_1["Name"], PLUG_1["flags"], PLUG_1["Icon"], PLUG_1["Info"], PLUG_1["Data"])
    RegisterCommandData(PLUG_2["ID"], PLUG_2["Name"], PLUG_2["flags"], PLUG_2["Icon"], PLUG_2["Info"], PLUG_2["Data"])
    RegisterCommandData(PLUG_3["ID"], PLUG_3["Name"], PLUG_3["flags"], PLUG_3["Icon"], PLUG_3["Info"], PLUG_3["Data"])