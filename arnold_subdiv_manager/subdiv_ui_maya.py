from shiboken2 import wrapInstance
import maya.OpenMayaUI as OpenMayaUI
from Qt import QtWidgets
from arnold_subdiv_manager.maya_abstraction_implementation import MayaAbstractionImplementation
from arnold_subdiv_manager.subdiv_manager import SubDivManager
from arnold_subdiv_manager.subdiv_ui import SubDivUI


def _maya_main_window():
    main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


def run():
    maya_abstraction_implementation = MayaAbstractionImplementation()
    subdiv_manager = SubDivManager(maya_abstraction_implementation)
    ui = SubDivUI(subdiv_manager, parent=_maya_main_window())
    ui.show()
    return ui
