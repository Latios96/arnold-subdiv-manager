import os

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
    return file_path + ".png"


def assert_images_are_equal(image1, image2):
    # type: (str, str) -> None
    assert os.path.exists(image1), "image1 does not exists!"
    assert os.path.exists(image2), "image1 does not exists!"

    from Qt import QtGui

    image_left = QtGui.QImage()
    image_left.load(image1)
    image_right = QtGui.QImage()
    image_right.load(image2)

    assert image_left.width() == image_right.width(), "Images are different in width!"
    assert image_left.height() == image_right.height(), "Images are different in height!"

    for x in range(image_left.width()):
        for y in range(image_left.height()):
            color_left = QtGui.QColor(image_left.pixel(x, y))
            color_right = QtGui.QColor(image_right.pixel(x, y))
            red_diff = (color_left.red() - color_right.red()) >= 50
            green_diff = color_left.green() - color_right.green() >= 50
            blue_diff = color_left.blue() - color_right.blue() >= 50
            assert not red_diff and not green_diff and not blue_diff, "Pixel {}x{} does not match!".format(x,y)


@maya_only
def test_integration_render_test(tmpdir):
    import pymel.core as pm
    from arnold_subdiv_manager.maya_abstraction_implementation import (
        MayaAbstractionImplementation,
    )

    maya_abstraction = MayaAbstractionImplementation()
    subdiv_manager = SubDivManager(maya_abstraction)
    pm.openFile(get_resource("cubes.ma"), f=True)

    before_render = render_to(str(tmpdir.join("before")))
    assert_images_are_equal(get_resource("before.png"), before_render)

    pm.select("SUBDIV_CATCLARK")
    subdiv_manager.apply_subdiv_to_selection()

    after_render = render_to(str(tmpdir.join("after")))
    assert_images_are_equal(get_resource("after.png"), after_render)

    pm.select("SUBDIV_CATCLARK")
    subdiv_manager.remove_subdiv_to_selection()

    before_render = render_to(str(tmpdir.join("before")))
    assert_images_are_equal(get_resource("before.png"), before_render)

