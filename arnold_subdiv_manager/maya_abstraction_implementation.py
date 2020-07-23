from typing import List

from arnold_subdiv_manager.maya_abstraction import MayaAbstraction
import pymel.core as pm

from arnold_subdiv_manager.mesh import Mesh
from arnold_subdiv_manager.subdiv_mode import SubDivMode


class MayaAbstractionImplementation(MayaAbstraction):
    def load_arnold_plugin(self):
        # type: () -> None
        pm.loadPlugin("mtoa")

    def is_arnold_plugin_loaded(self):
        # type: () -> bool
        return pm.pluginInfo("mtoa", query=True, loaded=True)

    def get_meshes_in_selection(self):
        # type: () -> List[Mesh]
        def is_mesh(candidate):
            is_mesh_shape = candidate.type() == "mesh"
            has_mesh_shape = (
                candidate.type() == "transform"
                and candidate.getShape().type() == "mesh"
            )
            return is_mesh_shape or has_mesh_shape

        meshes = filter(is_mesh, pm.selected())
        return list(map(lambda x: Mesh(x.fullPath()), meshes))

    def apply_subdiv_attr(self, mesh, subdiv_mode):
        # type: (Mesh, SubDivMode) -> None
        pm.PyNode(mesh.name).aiSubdivType.set(self._to_ai_subdiv_type(subdiv_mode))

    def _to_ai_subdiv_type(self, subdiv_mode):
        # type: (SubDivMode) -> int
        if subdiv_mode == SubDivMode.NONE:
            return 0
        return 1
