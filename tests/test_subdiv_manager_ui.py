from mock import MagicMock
from Qt import QtCore
from pytestqt import qtbot

from arnold_subdiv_manager.SubDivUI import SubDivUI


def test_button_click_should_activate(qtbot):
    # type: (qtbot) -> None
    subdiv_manager = MagicMock()
    ui = SubDivUI(subdiv_manager)
    qtbot.addWidget(ui)

    qtbot.mouseClick(ui._btn_apply_subdiv, QtCore.Qt.LeftButton)

    subdiv_manager.apply_subdiv_to_selection.assert_called_once()

def test_button_click_should_deactivate(qtbot):
    # type: (qtbot) -> None
    subdiv_manager = MagicMock()
    ui = SubDivUI(subdiv_manager)
    qtbot.addWidget(ui)

    qtbot.mouseClick(ui._btn_remove_subdiv, QtCore.Qt.LeftButton)

    subdiv_manager.remove_subdiv_to_selection.assert_called_once()
