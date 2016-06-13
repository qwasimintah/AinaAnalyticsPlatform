import sys
from PyQt4 import QtCore, QtGui, uic
import unicodecsv
import csv
import json
from collections import OrderedDict


chooseDataset="design/choose_dataset.ui"


Choose_Window, ChooseClass=uic.loadUiType(chooseDataset)




class ChooseDataset(QtGui.QMainWindow, Choose_Window):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Choose_Window.__init__(self)

        self.setupUi(self)
        self.setWindowTitle('Choose Dataset')
        self.setWindowIcon(QtGui.QIcon('C:/Users/DJAN DENNIS MINTAH/Desktop/work/ui/ico.png'))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint )
        self.setFixedSize(389,215)

        self.fields=[]
        self.rows=[]
        self.loadData.clicked.connect(self.openfile)

    def openfile(self):
        filepath=QtGui.QFileDialog.getOpenFileName(self,'Single File','~/Desktop/','*.csv')
        self.filename.setText(filepath)
        
        with open(filepath,'rb') as f:
            reader=unicodecsv.DictReader(f)

            for row in reader:
                self.rows.append(row)

                for k, v in row.items():
                    if k not in self.fields:
                        self.fields.append(k)


        writers =unicodecsv.writer(open("data.csv",'wb'),  delimiter=",")

        writers.writerow(self.fields)
        
        for result in self.rows:
            row=[]
            for field in self.fields:
                if field in result.keys():
                    row.append(result[field])
                else:
                    row.append("")
            writers.writerow(row)
        

        
        self.des.setText("Dataset contains %d rows and %d features" %(len(self.rows),len(self.fields)))
