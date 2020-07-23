import sys
from Qt import QtWidgets
from mock import MagicMock

from arnold_subdiv_manager.subdiv_ui import SubDivUI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = SubDivUI(MagicMock())
    ui.show()

    app.exec_()
