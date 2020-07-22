from mock import MagicMock

from arnold_subdiv_manager.mesh import Mesh
from arnold_subdiv_manager.subdiv_manager import SubDivManager


def test_should_apply_subdiv_to_selection():
    # type: () -> None
    maya_abstraction = MagicMock()
    maya_abstraction.get_meshes_in_selection.return_value = [
        Mesh("pCube1"),
        Mesh("pCube2"),
    ]
    subdiv_manager = SubDivManager(maya_abstraction)

    subdiv_manager.apply_subdiv_to_selection()

    maya_abstraction.get_meshes_in_selection.assert_called_once()
    maya_abstraction.apply_subdiv_attr.assert_any_call(Mesh("pCube1"))
    maya_abstraction.apply_subdiv_attr.assert_any_call(Mesh("pCube2"))
