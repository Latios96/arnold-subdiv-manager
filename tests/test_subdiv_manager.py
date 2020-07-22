from mock import MagicMock

from arnold_subdiv_manager.mesh import Mesh
from arnold_subdiv_manager.subdiv_manager import SubDivManager
from arnold_subdiv_manager.subdiv_mode import SubDivMode


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
    maya_abstraction.apply_subdiv_attr.assert_any_call(
        Mesh("pCube1"), SubDivMode.CATCLARK
    )
    maya_abstraction.apply_subdiv_attr.assert_any_call(
        Mesh("pCube2"), SubDivMode.CATCLARK
    )


def test_should_load_arnold_plugin_before_applying_subdiv():
    # type: () -> None
    maya_abstraction = MagicMock()
    maya_abstraction.is_arnold_plugin_loaded.return_value = False
    subdiv_manager = SubDivManager(maya_abstraction)

    subdiv_manager.apply_subdiv_to_selection()

    maya_abstraction.load_arnold_plugin.assert_called_once()


def test_should_not_load_arnold_plugin_again_before_applying_subdiv():
    # type: () -> None
    maya_abstraction = MagicMock()
    maya_abstraction.is_arnold_plugin_loaded.return_value = True
    subdiv_manager = SubDivManager(maya_abstraction)

    subdiv_manager.apply_subdiv_to_selection()

    maya_abstraction.load_arnold_plugin.assert_not_called()


def test_should_not_load_arnold_plugin_if_no_meshes_are_selected_before_applying_subdiv():
    # type: () -> None
    maya_abstraction = MagicMock()
    maya_abstraction.get_meshes_in_selection.return_value = []
    maya_abstraction.is_arnold_plugin_loaded.return_value = True
    subdiv_manager = SubDivManager(maya_abstraction)

    subdiv_manager.apply_subdiv_to_selection()

    maya_abstraction.load_arnold_plugin.assert_not_called()


def test_should_remove_subdiv_to_selection():
    # type: () -> None
    maya_abstraction = MagicMock()
    maya_abstraction.get_meshes_in_selection.return_value = [
        Mesh("pCube1"),
        Mesh("pCube2"),
    ]
    subdiv_manager = SubDivManager(maya_abstraction)

    subdiv_manager.remove_subdiv_to_selection()

    maya_abstraction.get_meshes_in_selection.assert_called_once()
    maya_abstraction.apply_subdiv_attr.assert_any_call(Mesh("pCube1"), SubDivMode.NONE)
    maya_abstraction.apply_subdiv_attr.assert_any_call(Mesh("pCube2"), SubDivMode.NONE)


def test_should_remove_arnold_plugin_before_removing_subdiv():
    # type: () -> None
    maya_abstraction = MagicMock()
    maya_abstraction.is_arnold_plugin_loaded.return_value = False
    subdiv_manager = SubDivManager(maya_abstraction)

    subdiv_manager.remove_subdiv_to_selection()

    maya_abstraction.load_arnold_plugin.assert_called_once()


def test_should_not_load_arnold_plugin_again_before_removing_subdiv():
    # type: () -> None
    maya_abstraction = MagicMock()
    maya_abstraction.is_arnold_plugin_loaded.return_value = True
    subdiv_manager = SubDivManager(maya_abstraction)

    subdiv_manager.remove_subdiv_to_selection()

    maya_abstraction.load_arnold_plugin.assert_not_called()


def test_should_not_load_arnold_plugin_if_no_meshes_are_selected_before_removing_subdiv():
    # type: () -> None
    maya_abstraction = MagicMock()
    maya_abstraction.get_meshes_in_selection.return_value = []
    maya_abstraction.is_arnold_plugin_loaded.return_value = True
    subdiv_manager = SubDivManager(maya_abstraction)

    subdiv_manager.remove_subdiv_to_selection()

    maya_abstraction.load_arnold_plugin.assert_not_called()
