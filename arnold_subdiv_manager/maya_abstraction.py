from abc import ABCMeta, abstractmethod

from typing import List

from arnold_subdiv_manager.mesh import Mesh


class MayaAbstraction(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def load_arnold_plugin(self):
        # type: () -> None
        pass

    @abstractmethod
    def is_arnold_plugin_loaded(self):
        # type: () -> bool
        pass

    @abstractmethod
    def get_meshes_in_selection(self):
        # type: () -> List[Mesh]
        pass

    @abstractmethod
    def apply_subdiv_attr(self, mesh):
        # type: (Mesh) -> None
        pass
