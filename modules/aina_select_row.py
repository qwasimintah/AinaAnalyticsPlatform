import sys
from PyQt4 import QtCore, QtGui, uic
import unicodecsv
import csv
import json
from collections import OrderedDict



selectCreatorFile = "design/aina_select_rows.ui" # Enter file here.


SelectRow_MainWindow, SelectClass = uic.loadUiType(selectCreatorFile)


class SelectRow(QtGui.QMainWindow, SelectRow_MainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        SelectRow_MainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle('AINA ROW SELECTIONS')
        self.setWindowIcon(QtGui.QIcon('C:/Users/DJAN DENNIS MINTAH/Desktop/work/ui/ico.png'))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint )
        self.setFixedSize(580,482)
        self.rows=[]
        self.fields=[]
        self.getFile()
        self.commit.clicked.connect(self.commitChanges)


    def clearAll(self):

        self.fields_box.clear()
        self.fields_box2.clear()
        self.conditions.clear()
        self.condition2.clear()
        self.rows=[]
        self.fields=[]
        self.description.setText("Description")




    def getFile(self):
        filename="data.csv"
        
        self.clearAll()
        print(self.fields_box.count())
        
        with open(filename,'rb') as f:
            reader=unicodecsv.DictReader(f)

            for row in reader:
                self.rows.append(row)

                for k, v in row.items():
                    if k not in self.fields:
                        self.fields.append(k)

        conditionals=["Equal","Not Equal","Greater Than","Less Than","Contains","Less or Equal To","Greater or Equal To"]

        self.fields_box.addItems(self.fields)
        self.fields_box2.addItems(self.fields)
        self.conditions.addItems(conditionals)
        self.condition2.addItems(conditionals)



    def commitChanges(self):

        field_chosen=self.fields_box.currentText()
        value_chosen=self.value.toPlainText()
        dependent=self.conditions.currentText()

        matched=[]

        if self.add.isChecked()==True:
            field_chosen2=self.fields_box2.currentText()
            value_chosen2=self.value2.toPlainText()
            dependent2=self.condition2.currentText()

            if self.and_bt.isChecked()==True:

                for i in self.rows:
                    if dependent=="Equal":
                        if dependent2=="Equal":
                            if i[field_chosen]==value_chosen and i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if i[field_chosen]==value_chosen and float(i[field_chosen2])>float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Contains":
                            if i[field_chosen]==value_chosen and i[field_chosen2].find(value_chosen2)!= -1:
                                print(field_chosen2, value_chosen2)
                                matched.append(i)
                        if dependent2=="Not Equal":
                            if i[field_chosen]==value_chosen and i[field_chosen2]!=value_chosen2:
                                matched.append(i)
                        if dependent2=="Less Than":
                            if i[field_chosen]==value_chosen and float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)  
                        if dependent2=="Less or Equal To":
                            if i[field_chosen]==value_chosen and float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Greater or Equal To":
                            if i[field_chosen]==value_chosen and float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)                      

                    if dependent=="Greater Than":
                        if dependent2=="Equal":
                            if float(i[field_chosen])>float(value_chosen) and i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if float(i[field_chosen])>float(value_chosen) and  float(i[field_chosen2])>float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Contains":
                            if float(i[field_chosen])>float(value_chosen) and i[field_chosen2].find(value_chosen2)!= -1:
                                matched.append(i)

                        if dependent2=="Not Equal":
                            if float(i[field_chosen])>float(value_chosen) and i[field_chosen2]!=value_chosen2:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if float(i[field_chosen])>float(value_chosen) and float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Less or Equal To":
                            if float(i[field_chosen])>float(value_chosen) and float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Greater or Equal To":
                            if float(i[field_chosen])>float(value_chosen) and float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)                        


                    if dependent=="Contains":
                        if dependent2=="Equal":
                            if i[field_chosen].find(value_chosen)!=-1 and i[field_chosen2]==value_chosen2:
                                matched.append(i)

                        if dependent2=="Greater Than":
                            if i[field_chosen].find(value_chosen)!=-1 and float(i[field_chosen2])>float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Contains":
                            if i[field_chosen].find(value_chosen)!=-1 and  i[field_chosen2].find(value_chosen2)!=-1:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if i[field_chosen].find(value_chosen)!=-1 and float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Less or Equal To":
                            if i[field_chosen].find(value_chosen)!=-1 and float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Greater or Equal To":
                            if i[field_chosen].find(value_chosen)!=-1 and float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)




                    if dependent=="Not Equal":
                        if dependent2=="Equal":
                            if i[field_chosen]!=value_chosen and i[field_chosen2]==value_chosen2:
                                matched.append(i)

                        if dependent2=="Greater Than":
                            if i[field_chosen]!=value_chosen and float(i[field_chosen2])<=float(value_chosen2) :
                                matched.append(i)

                        if dependent2=="Contains":
                            if i[field_chosen]!=value_chosen and i[field_chosen2].find(value2)!=-1:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if i[field_chosen]!=value_chosen and float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Less or Equal To":
                            if i[field_chosen]!=value_chosen and float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Greater or Equal To":
                            if i[field_chosen]!=value_chosen and float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)


                    if dependent=="Less Than":

                        if dependent2=="Equal":
                            if float(i[field_chosen])< float(value_chosen) and i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if float(i[field_chosen])< float(value_chosen) and  float(i[field_chosen2])> float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Contains":
                            if float(i[field_chosen])< float(value_chosen) and i[field_chosen2].find(value_chosen2)!=-1:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if float(i[field_chosen])< float(value_chosen) and  float(i[field_chosen2])< float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Less or Equal To":
                            if float(i[field_chosen])< float(value_chosen) and float(i[field_chosen2])<= float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Greater or Equal To":
                            if float(i[field_chosen])< float(value_chosen) and  float(i[field_chosen2])>= float(value_chosen2):
                                matched.append(i)


                    if dependent=="Less or Equal To":
                        if dependent2=="Equal":
                            if float(i[field_chosen])<= float(value_chosen) and i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if float(i[field_chosen])<= float(value_chosen) and  float(i[field_chosen2])> float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Contains":
                            if float(i[field_chosen])<= float(value_chosen) and i[field_chosen2].find(value_chosen2)!=-1:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if float(i[field_chosen])<= float(value_chosen) and  float(i[field_chosen2])< float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Less or Equal To":
                            if float(i[field_chosen])<= float(value_chosen) and float(i[field_chosen2])<= float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Greater or Equal To":
                            if float(i[field_chosen])<= float(value_chosen) and  float(i[field_chosen2])>= float(value_chosen2):
                                matched.append(i)

                    if dependent=="Greater or Equal To":
                        if dependent2=="Equal":
                            if float(i[field_chosen])>=float(value_chosen) and i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if float(i[field_chosen])>=float(value_chosen) and  float(i[field_chosen2])>float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Contains":
                            if float(i[field_chosen])>=float(value_chosen) and i[field_chosen2].find(value_chosen2)!= -1:
                                matched.append(i)

                        if dependent2=="Not Equal":
                            if float(i[field_chosen])>=float(value_chosen) and i[field_chosen2]!=value_chosen2:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if float(i[field_chosen])>=float(value_chosen) and float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Less or Equal To":
                            if float(i[field_chosen])>=float(value_chosen) and float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Greater or Equal To":
                            if float(i[field_chosen])>=float(value_chosen) and float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)                        


            else:


                for i in self.rows:
                    if dependent=="Equal":
                        if dependent2=="Equal":
                            if i[field_chosen]==value_chosen or i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if i[field_chosen]==value_chosen or float(i[field_chosen2])>float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Contains":
                            if i[field_chosen]==value_chosen or i[field_chosen2].find(value_chosen2)!= -1:
                                print(field_chosen2, value_chosen2)
                                matched.append(i)
                        if dependent2=="Not Equal":
                            if i[field_chosen]==value_chosen or i[field_chosen2]!=value_chosen2:
                                matched.append(i)
                        if dependent2=="Less Than":
                            if i[field_chosen]==value_chosen or float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)  
                        if dependent2=="Less or Equal To":
                            if i[field_chosen]==value_chosen or float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Greater or Equal To":
                            if i[field_chosen]==value_chosen or float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)                      

                    if dependent=="Greater Than":
                        if dependent2=="Equal":
                            if float(i[field_chosen])>float(value_chosen) or i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if float(i[field_chosen])>float(value_chosen) or  float(i[field_chosen2])>float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Contains":
                            if float(i[field_chosen])>float(value_chosen) or i[field_chosen2].find(value_chosen2)!= -1:
                                matched.append(i)

                        if dependent2=="Not Equal":
                            if float(i[field_chosen])>float(value_chosen) or i[field_chosen2]!=value_chosen2:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if float(i[field_chosen])>float(value_chosen) or float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Less or Equal To":
                            if float(i[field_chosen])>float(value_chosen) or float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Greater or Equal To":
                            if float(i[field_chosen])>float(value_chosen) or float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)                        


                    if dependent=="Contains":
                        if dependent2=="Equal":
                            if i[field_chosen].find(value_chosen)!=-1 or i[field_chosen2]==value_chosen2:
                                matched.append(i)

                        if dependent2=="Greater Than":
                            if i[field_chosen].find(value_chosen)!=-1 or float(i[field_chosen2])>float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Contains":
                            if i[field_chosen].find(value_chosen)!=-1 or  i[field_chosen2].find(value_chosen2)!=-1:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if i[field_chosen].find(value_chosen)!=-1 or float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Less or Equal To":
                            if i[field_chosen].find(value_chosen)!=-1 or float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Greater or Equal To":
                            if i[field_chosen].find(value_chosen)!=-1 or float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)




                    if dependent=="Not Equal":
                        if dependent2=="Equal":
                            if i[field_chosen]!=value_chosen or i[field_chosen2]==value_chosen2:
                                matched.append(i)

                        if dependent2=="Greater Than":
                            if i[field_chosen]!=value_chosen or float(i[field_chosen2])<=float(value_chosen2) :
                                matched.append(i)

                        if dependent2=="Contains":
                            if i[field_chosen]!=value_chosen or i[field_chosen2].find(value2)!=-1:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if i[field_chosen]!=value_chosen or float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Less or Equal To":
                            if i[field_chosen]!=value_chosen or float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Greater or Equal To":
                            if i[field_chosen]!=value_chosen or float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)


                    if dependent=="Less Than":

                        if dependent2=="Equal":
                            if float(i[field_chosen])< float(value_chosen) or i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if float(i[field_chosen])< float(value_chosen) or  float(i[field_chosen2])> float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Contains":
                            if float(i[field_chosen])< float(value_chosen) or i[field_chosen2].find(value_chosen2)!=-1:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if float(i[field_chosen])< float(value_chosen) or  float(i[field_chosen2])< float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Less or Equal To":
                            if float(i[field_chosen])< float(value_chosen) or float(i[field_chosen2])<= float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Greater or Equal To":
                            if float(i[field_chosen])< float(value_chosen) or  float(i[field_chosen2])>= float(value_chosen2):
                                matched.append(i)


                    if dependent=="Less or Equal To":
                        if dependent2=="Equal":
                            if float(i[field_chosen])<= float(value_chosen) or i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if float(i[field_chosen])<= float(value_chosen) or  float(i[field_chosen2])> float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Contains":
                            if float(i[field_chosen])<= float(value_chosen) or i[field_chosen2].find(value_chosen2)!=-1:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if float(i[field_chosen])<= float(value_chosen) or  float(i[field_chosen2])< float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Less or Equal To":
                            if float(i[field_chosen])<= float(value_chosen) or float(i[field_chosen2])<= float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Greater or Equal To":
                            if float(i[field_chosen])<= float(value_chosen) or  float(i[field_chosen2])>= float(value_chosen2):
                                matched.append(i)

                    if dependent=="Greater or Equal To":
                        if dependent2=="Equal":
                            if float(i[field_chosen])>=float(value_chosen) or i[field_chosen2]==value_chosen2:
                                matched.append(i)
                        if dependent2=="Greater Than":
                            if float(i[field_chosen])>=float(value_chosen) or  float(i[field_chosen2])>float(value_chosen2):
                                matched.append(i)

                        if dependent2=="Contains":
                            if float(i[field_chosen])>=float(value_chosen) or i[field_chosen2].find(value_chosen2)!= -1:
                                matched.append(i)

                        if dependent2=="Not Equal":
                            if float(i[field_chosen])>=float(value_chosen) or i[field_chosen2]!=value_chosen2:
                                matched.append(i)

                        if dependent2=="Less Than":
                            if float(i[field_chosen])>=float(value_chosen) or float(i[field_chosen2])<float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Less or Equal To":
                            if float(i[field_chosen])>=float(value_chosen) or float(i[field_chosen2])<=float(value_chosen2):
                                matched.append(i)
                        if dependent2=="Greater or Equal To":
                            if float(i[field_chosen])>=float(value_chosen) or float(i[field_chosen2])>=float(value_chosen2):
                                matched.append(i)


        else:
            for i in self.rows:
                if dependent=="Equal":
                    if i[field_chosen]==value_chosen:
                        matched.append(i)

                if dependent=="Greater Than":
                    if float(i[field_chosen])>float(value_chosen):
                        matched.append(i)

                if dependent=="Contains":
                    if i[field_chosen].find(value_chosen)!=-1:
                        matched.append(i)
                if dependent=="Not Equal":
                    if i[field_chosen]!=value_chosen:
                        matched.append(i)

                if dependent=="Less Than":
                    if float(i[field_chosen])< float(value_chosen):
                        matched.append(i)

                if dependent=="Less or Equal To":
                    if float(i[field_chosen])<= float(value_chosen):
                        matched.append(i)
                if dependent=="Greater or Equal To":
                    if float(i[field_chosen]) >= float(value_chosen):
                        matched.append(i)

        num_rows=len(matched)
        des="Matched Occurences: "+ str(num_rows)
        self.description.setText(des)


        self.writeRows("data.csv",self.fields,matched)

    def writeRows(self,filename,header, rows):
        writers =unicodecsv.writer(open(filename,'wb'),  delimiter=",")

        writers.writerow(header)
        
        for result in rows:
            row=[]
            for field in header:
                if field in result.keys():
                    row.append(result[field])
                else:
                    row.append("")
            writers.writerow(row)


