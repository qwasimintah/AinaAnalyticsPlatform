from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
from PyQt4 import QtGui, QtCore,uic
import unicodecsv
import csv
import json
from collections import OrderedDict


class EmbedIPython(RichJupyterWidget):

    def __init__(self, **kwarg):
        super(RichJupyterWidget, self).__init__()
        self.kernel_manager = QtInProcessKernelManager()
        self.kernel_manager.start_kernel()
        self.kernel = self.kernel_manager.kernel
        self.kernel.gui = 'qt4'
        self.kernel.shell.push(kwarg)
        self.kernel_client = self.kernel_manager.client()
        self.kernel_client.start_channels()


ReportCreatorFile = "design/script_design.ui" # Enter file here.


Script_MainWindow, ReportBaseClass = uic.loadUiType(ReportCreatorFile)
class Script(QtGui.QMainWindow,Script_MainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        Script_MainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle('AINA SCRIPT')
        self.setWindowIcon(QtGui.QIcon('C:/Users/DJAN DENNIS MINTAH/Desktop/work/ui/ico.png'))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint )
        self.setFixedSize(730,641)
        self.rows=[]
        self.getData()
        self.console = EmbedIPython(in_data=self.rows)
        self.console.kernel.shell.run_cell('%pylab qt')
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.console)    
        self.widget.setLayout(vbox)
        self.run.clicked.connect(self.runScript)
        self.save.clicked.connect(self.saveScript)
        self.open.clicked.connect(self.openFile)

    def runScript(self):
        self.input_text=self.text_field.toPlainText()
        self.console.execute(self.input_text)

    def getData(self):

        with open("data.csv",'rb') as f:
            reader=unicodecsv.DictReader(f)

            for row in reader:
                self.rows.append(row)

    def saveScript(self):
        path = QtGui.QFileDialog.getSaveFileName(self,'Save file', '',"*.py")
        saved=self.text_field.toPlainText()

        if path:
            with open(path, "w") as f:
                f.write(saved)

    def openFile(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File','',"*.py")

        with open(name, "r") as f:
            text=f.read()
        self.text_field.setText(text)




