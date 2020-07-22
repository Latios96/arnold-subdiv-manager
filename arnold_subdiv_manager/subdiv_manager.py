from typing import List

from arnold_subdiv_manager.maya_abstraction import MayaAbstraction
from arnold_subdiv_manager.mesh import Mesh
from arnold_subdiv_manager.subdiv_mode import SubDivMode


class SubDivManager(object):
    def __init__(self, maya_abstraction):
        # type: (MayaAbstraction) -> None
        self._maya_abstraction = maya_abstraction

    def apply_subdiv_to_selection(self):
        # type: () -> None
        self._apply_subdiv_mode(SubDivMode.CATCLARK)

    def remove_subdiv_to_selection(self):
        # type: () -> None
        self._apply_subdiv_mode(SubDivMode.NONE)

    def _should_load_arnold_plugin(self, meshes):
        # type: (List[Mesh]) -> bool
        return bool(meshes) and not self._maya_abstraction.is_arnold_plugin_loaded()

    def _apply_subdiv_mode(self, subdiv_mode):
        # type: (SubDivMode) -> None
        meshes = self._maya_abstraction.get_meshes_in_selection()
        if self._should_load_arnold_plugin(meshes):
            self._maya_abstraction.load_arnold_plugin()
        for mesh in meshes:
            self._maya_abstraction.apply_subdiv_attr(mesh, subdiv_mode)
