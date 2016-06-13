import sys
from PyQt4 import QtCore, QtGui, uic
import unicodecsv
import csv
import json
from collections import OrderedDict


ReportCreatorFile = "design/general_reporter.ui" # Enter file here.


Report_MainWindow, ReportBaseClass = uic.loadUiType(ReportCreatorFile)

class Report(QtGui.QMainWindow, Report_MainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Report_MainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle('AINA GENERAL REPORT GENERATOR')
        self.setWindowIcon(QtGui.QIcon('C:/Users/DJAN DENNIS MINTAH/Desktop/work/ui/ico.png'))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint )
        self.setFixedSize(500,550)
        self.report.clicked.connect(self.write_report)



    def write_report(self):

        title=self.title.toPlainText()
        content=self.content.toPlainText()
        try:
            content_json=json.loads(content, object_pairs_hook=OrderedDict)
            
        except:
            accept=content.replace("'","\"")
            content_json=json.loads(accept, object_pairs_hook=OrderedDict)


        self.report_generator(content_json, [title])




    def report_generator(self,data,perm):
        headers=[]
        value=[]

        header=data.keys()
        for i in header:
            headers.append(i)
        values=data.values()
        for i in values:
            value.append(i)

        #print(header)
        #print(values)
        filename=str(self.filename.toPlainText())+".csv"

        limit=len(headers)
        writers =unicodecsv.writer(open(filename,'ab'),  delimiter=",")

        writers.writerow(perm)
        writers.writerow([])

        for row in range(0,limit):
            writers.writerow([headers[row],"","","","","",value[row]])
