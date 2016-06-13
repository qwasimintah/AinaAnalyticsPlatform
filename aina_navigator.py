import sys
from PyQt4 import QtCore, QtGui, uic
import unicodecsv
import csv
import json
from collections import OrderedDict
from modules.aina_graphview import GraphView
from modules.aina_tableview import TableView
from modules.aina_report import Report
from modules.aina_chooseDataset import ChooseDataset
from modules.aina_select_feature import SelectFeature
from modules.aina_select_row import SelectRow
from modules.script import Script


qtCreatorFile = "aina_navigator.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle('AINA NAVIGATOR')
        self.setWindowIcon(QtGui.QIcon('C:/Users/DJAN DENNIS MINTAH/Desktop/work/ui/ico.png'))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint )
        self.setFixedSize(800,600)
        self.clearDataFile()
        self.fileview.clicked.connect(self.choose_data)
        self.tableview.clicked.connect(self.table_view)
        self.select_rows.clicked.connect(self.select_row)
        self.features.clicked.connect(self.select_features)
        self.bt_report.clicked.connect(self.generate_report)
        self.graph_view.clicked.connect(self.show_graph)
        self.bt_script.clicked.connect(self.open_script)


    def clearDataFile(self):
        writers =unicodecsv.writer(open("data.csv",'wb'),  delimiter=",")

        writers.writerow([])


    def choose_data(self):
        self.opendata=ChooseDataset()
        self.opendata.show()

    def table_view(self):
        self.opentableview=TableView()
        self.opentableview.show()

    def select_row(self):
        self.openselectRows=SelectRow()
        self.openselectRows.show()

    def select_features(self):
        self.openselectFeatures=SelectFeature()
        self.openselectFeatures.show()

    def generate_report(self):
        self.opengenerateReport=Report()
        self.opengenerateReport.show()

    def show_graph(self):
        self.opengraph=GraphView()
        self.opengraph.show()

    def open_script(self):
        self.openscript=Script()
        self.openscript.show()


def main():
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())





if __name__ == "__main__":
    main()
    
