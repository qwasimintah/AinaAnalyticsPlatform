import sys
from PyQt4 import QtCore, QtGui, uic
import unicodecsv
import csv
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


File = "design/graphview.ui" # Enter file here.


GraphView_MainWindow, GraphViewBaseClass = uic.loadUiType(File)

class GraphView(QtGui.QMainWindow, GraphView_MainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        GraphView_MainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle('AINA GRAPHVIEW')
        self.setWindowIcon(QtGui.QIcon('C:/Users/DJAN DENNIS MINTAH/Desktop/work/ui/ico.png'))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint )
        self.setFixedSize(739,598)
        self.rows=[]
        self.fields=[]

        self.plotGraph()
        self.generateCombo()
        self.graph.clicked.connect(self.drawGraph)
        self.save.clicked.connect(self.save_plot)


    def save_plot(self):
        file_choices = "PNG (*.png)|*.png"
        
        path = QtGui.QFileDialog.getSaveFileName(self, 
                        'Save file', '', 
                        file_choices)
        if path:
            self.canvas.print_figure(path, dpi=self.dpi)


    def generateCombo(self):

        with open("data.csv",'rb') as f:
            reader=unicodecsv.DictReader(f)

            for row in reader:
                self.rows.append(row)

                for k, v in row.items():
                    if k not in self.fields:
                        self.fields.append(k)

        final_fields=[]
        for field in self.fields:
            result=self.occurence(field)
            len_result=len(result.keys())
            if len_result<= 6:
                final_fields.append(field)


        self.x.addItems(final_fields)

    def occurence(self, chosen):
        chosen_data=[]
        for row in self.rows:
            chosen_data.append(row[chosen])

        frequency={}

        for row in chosen_data:
            frequency[row]=frequency.get(row,0) +1

        return frequency


    def drawGraph(self):
        chosen=self.x.currentText();
        chosen_data=[]
        for row in self.rows:
            chosen_data.append(row[chosen])

        frequency={}

        for row in chosen_data:
            frequency[row]=frequency.get(row,0) +1


        
        labels=[]
        values=[]
        for keys, value in frequency.items():
            labels.append(str(keys))
            values.append(int(value))

        self.maindraw(labels,values)

        

    def plotGraph(self):
        self.dpi = 100
        self.fig = Figure((5.0, 4.6), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.plot_widget)
        self.axes = self.fig.add_subplot(111)


    def maindraw(self,l,values):
        self.axes.clear()
        x = range(len(l))
        print(x)
        self.axes.bar(
            left=x, 
            height=values, 
            width=0.5, 
            align='center', 
            alpha=0.44,
            picker=5)

        self.axes.set_xticks(x)
        self.axes.set_xlabel(self.x.currentText())
        self.axes.set_ylabel("frequency")
        xtickNames = self.axes.set_xticklabels(l)
        plt.setp(xtickNames,fontsize=8)
        self.canvas.draw()
