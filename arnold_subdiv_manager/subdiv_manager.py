from arnold_subdiv_manager.maya_abstraction import MayaAbstraction


class SubDivManager(object):
    def __init__(self, maya_abstraction):
        # type: (MayaAbstraction) -> None
        self._maya_abstraction = maya_abstraction

    def apply_subdiv_to_selection(self):
        # type: () -> None
        meshes = self._maya_abstraction.get_meshes_in_selection()

        if self._should_load_arnold_plugin(meshes):
            self._maya_abstraction.load_arnold_plugin()

        for mesh in meshes:
            self._maya_abstraction.apply_subdiv_attr(mesh)

    def _should_load_arnold_plugin(self, meshes):
        return meshes and not self._maya_abstraction.is_arnold_plugin_loaded()
