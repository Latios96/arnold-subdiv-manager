from arnold_subdiv_manager.mesh import Mesh
from tests import maya_only


@maya_only
def test_get_meshes_in_selection_should_only_return_meshes():
    import pymel.core as pm
    from arnold_subdiv_manager.maya_abstraction_implementation import (
        MayaAbstractionImplementation,
    )

    pm.newFile(f=True)
    pm.camera()
    pm.polyCube()
    pm.select(["pCube1", "camera1"])
    maya_abstraction = MayaAbstractionImplementation()

    meshes = maya_abstraction.get_meshes_in_selection()

    assert meshes == [Mesh("|pCube1")]


@maya_only
def test_get_meshes_in_selection_should_handle_shapes_correctly():
    import pymel.core as pm
    from arnold_subdiv_manager.maya_abstraction_implementation import (
        MayaAbstractionImplementation,
    )

    pm.newFile(f=True)
    pm.camera()
    pm.polyCube()
    pm.select(["|pCube1|pCubeShape1", "|pCube1"])
    maya_abstraction = MayaAbstractionImplementation()

    meshes = maya_abstraction.get_meshes_in_selection()

    assert meshes == [Mesh("|pCube1|pCubeShape1"), Mesh("|pCube1")]
