import os

from arnold_subdiv_manager.mesh import Mesh
from arnold_subdiv_manager.subdiv_manager import SubDivManager
from tests import maya_only


def get_resource(name):
    # type: (str) -> str
    file_dir = os.path.dirname(__file__)
    return os.path.join(file_dir, "data", "integration_test", name)


def render_to(file_path):
    from mtoa.cmds.arnoldRender import arnoldRender
    import pymel.core as pm

    pm.setAttr("defaultArnoldDriver.pre", file_path, type="string")
    arnoldRender(960, 540, True, True, "rendercam", " -layer defaultRenderLayer")
    return file_path + "'_1.png"


def assert_images_are_equal(image1, image2):
    pass


@maya_only
def test_integration_render_test(tmpdir):
    import pymel.core as pm
    from arnold_subdiv_manager.maya_abstraction_implementation import (
        MayaAbstractionImplementation,
    )

    maya_abstraction = MayaAbstractionImplementation()
    subdiv_manager = SubDivManager(maya_abstraction)
    pm.openFile(get_resource("cubes.ma"), f=True)

    before_render = render_to(tmpdir.join("before"))
    assert_images_are_equal(get_resource("before.png"), before_render)

    pm.select("SUBDIV_CATCLARK")
    subdiv_manager.apply_subdiv_to_selection()

    after_render = render_to(tmpdir.join("after"))
    assert_images_are_equal(get_resource("after.png"), after_render)

    pm.select("SUBDIV_CATCLARK")
    subdiv_manager.remove_subdiv_to_selection()

    before_render = render_to(tmpdir.join("before"))
    assert_images_are_equal(get_resource("before.png"), before_render)
