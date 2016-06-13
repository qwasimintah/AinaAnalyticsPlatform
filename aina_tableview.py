

import sys
from PyQt4 import QtCore, QtGui, uic
import unicodecsv
import csv
import json
from collections import OrderedDict

tableview="aina_tableview.ui"

Table_View, TableClass=uic.loadUiType(tableview)



class TableView(QtGui.QMainWindow, Table_View):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Table_View.__init__(self)

        self.setupUi(self)
        self.setWindowTitle('Aina TableView')
        self.setWindowIcon(QtGui.QIcon('C:/Users/DJAN DENNIS MINTAH/Desktop/work/ui/ico.png'))
        self.showTable()
        

    def showTable(self):
        rows=[]
        fields=[]
        
        with open("data.csv",'rb') as f:
            reader=unicodecsv.DictReader(f)

            for row in reader:
                rows.append(row)

                for k, v in row.items():
                    if k not in fields:
                        fields.append(k)

        column=len(fields)
        row_length=len(rows)


        print(column,row_length)
        self.tableView.setRowCount(row_length)
        self.tableView.setColumnCount(column)
        
        #print(fields)     
        
        for row, data in enumerate(rows):

            for column, item in enumerate(fields):
                newitem=QtGui.QTableWidgetItem(data[item])
                self.tableView.setItem(row,column, newitem)
        
        self.tableView.setHorizontalHeaderLabels(fields)






