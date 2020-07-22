from arnold_subdiv_manager.maya_abstraction import MayaAbstraction


class SubDivManager(object):
    def __init__(self, maya_abstraction):
        # type: (MayaAbstraction) -> None
        self._maya_abstraction = maya_abstraction

    def apply_subdiv_to_selection(self):
        # type: () -> None
        pass
