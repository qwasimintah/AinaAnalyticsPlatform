
import sys
from PyQt4 import QtCore, QtGui, uic
import unicodecsv
import csv
import json
from collections import OrderedDict

SelectFeatureCreatorFile = "design/aina_select_feature.ui" # Enter file here.


SelectFeature_MainWindow, FeatureBaseClass = uic.loadUiType(SelectFeatureCreatorFile)



class SelectFeature(QtGui.QMainWindow, SelectFeature_MainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        SelectFeature_MainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle('AINA FEATURE SELECTION')
        self.setWindowIcon(QtGui.QIcon('C:/Users/DJAN DENNIS MINTAH/Desktop/work/ui/ico.png'))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint )
        self.setFixedSize(367,530)
        self.directory=""
        self.vbox=QtGui.QVBoxLayout()
        self.checks=[]
        self.selected=[]
        self.widget=QtGui.QWidget()
        self.rows=[]
        self.fields=[]
        self.getFile()
        self.accept.clicked.connect(self.writeRows)

    def clearLayout(self,layout):
        while layout.count()>0:

            item=layout.takeAt(0)
            if not item:
                continue
            w=item.widget()
            if w:
                w.deleteLater()

    def reset(self):
        self.row=[]
        self.fields=[]
        self.rows=[]
        self.selected=[]
        self.checks=[]
        



    def getFile(self):

        self.reset()

  
        
        with open("data.csv",'rb') as f:
            reader=unicodecsv.DictReader(f)

            for row in reader:
                self.rows.append(row)

                for k, v in row.items():
                    if k not in self.fields:
                        self.fields.append(k)
        
    
        self.getFeatures()
        



    def getFeatures(self):
        #self.scrol=QtGui.QScrollArea()

        self.clearLayout(self.vbox)

        for i in self.fields:
            c=QtGui.QCheckBox("%s"%i)
            c.setChecked(True)

            self.vbox.addWidget(c)
            self.checks.append(c)

        self.widget.setLayout(self.vbox)
        self.scrol.setWidget(self.widget)




    def getSelected(self):

        for row in self.checks:
            if row.isChecked():
                self.selected.append(row.text())

        #print(self.selected)


    def writeRows(self):
        
        self.getSelected()

        writers =unicodecsv.writer(open("data.csv",'wb'),  delimiter=",")

        writers.writerow(self.selected)
        
        for result in self.rows:
            row=[]
            for field in self.selected:
                if field in result.keys():
                    row.append(result[field])
                else:
                    row.append("")
                
            writers.writerow(row)