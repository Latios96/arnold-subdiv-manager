from arnold_subdiv_manager.subdiv_manager import SubDivManager
from Qt import QtWidgets


class SubDivUI(QtWidgets.QWidget):
    def __init__(self, subdiv_manager):
        # type: (SubDivManager) -> None
        super(SubDivUI, self).__init__()
        self._subdiv_manager = subdiv_manager
        self._setup_ui()

    def _setup_ui(self):
        # type: () -> None
        self.setWindowTitle("Arnold SubDiv Manager")
        self._layout = QtWidgets.QVBoxLayout()
        self.setLayout(self._layout)
        self._btn_apply_subdiv = QtWidgets.QPushButton("Active Subdivision")
        self._btn_apply_subdiv.clicked.connect(
            self._subdiv_manager.apply_subdiv_to_selection
        )
        self._layout.addWidget(self._btn_apply_subdiv)
        self._btn_remove_subdiv = QtWidgets.QPushButton("Deactivate Subdivision")
        self._btn_remove_subdiv.clicked.connect(
            self._subdiv_manager.remove_subdiv_to_selection
        )
        self._layout.addWidget(self._btn_remove_subdiv)


if __name__ == "__main__":
    from mock import MagicMock
    import sys

    app = QtWidgets.QApplication(sys.argv)

    ui = SubDivUI(MagicMock())
    ui.show()

    app.exec_()
