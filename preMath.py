# -*- coding: utf_8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os, sys
import random
import pickle
app = QApplication(sys.argv)
func="add"
# 2 nrs random int
n1=random.randint(1,9)
n2=random.randint(1,9)
#
filew=open("files/1.sav","wb")
pickle.dump(n1,filew)
filew.close()
filew=open("files/2.sav","wb")
pickle.dump(n2,filew)
filew.close()
tot=n1+n2
eq=QLabel()
eq.setText(str(n1)+ " + "+str(n2))
eq.setFont(QFont("Arial",18,QFont.Bold))
#imagem
imgi=QPixmap("img/apple.jpg").scaledToWidth(48)
#operator
oper=QLabel()
oper.setText('+')
oper.setFont(QFont("Arial",18,QFont.Bold))
#total
total=QLabel()
total.setText('Total :')
instot=QLineEdit()
instot.resize(64,32)
#butao
button1 = QPushButton()
button1.setIcon(QIcon('img/search.png'))
#layout
layout = QGridLayout()

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayout(layout)
        global imgi
        # create menu
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        menu = menubar.addMenu("Menu")
        action=menu.addAction("+++++")
        action.triggered.connect(self.adi)
        action=menu.addAction("-----")
        action.triggered.connect(self.subt)
        menu.addSeparator()
        action=menu.addAction("Quit")
        action.triggered.connect(self.close)
        menu = menubar.addMenu("Info")
        action=menu.addAction("Credits")
        action.triggered.connect(self.showdialog)
        button1.clicked.connect(self.showw)
        img=QLabel()
        img.setPixmap(imgi)
        if(n1>n2):
            layout.addWidget(eq,1,0,1,n1)
            layout.addWidget(instot,5,1,1,n1)
            layout.addWidget(button1,6,0,1,n1+1)
            layout.addWidget(oper,3,1,1,n1)
        else:
            layout.addWidget(eq,1,0,1,n2)
            layout.addWidget(instot,5,1,1,n2)
            layout.addWidget(button1,6,0,1,n2+1)
            layout.addWidget(oper,3,1,1,n2)
        i=1
        while i<=n1:
            img=QLabel()
            img.setPixmap(imgi)
            layout.addWidget(img,2,i)
            i=i+1
        i=1
        while i<=n2:
            img=QLabel()
            img.setPixmap(imgi)
            layout.addWidget(img,4,i)
            i=i+1
        layout.addWidget(total,5,0)
    def showw(self):
        global tot,instot,func
        filer=open("files/1.sav","rb")
        n1=pickle.load(filer)
        filer.close()
        filer=open("files/2.sav","rb")
        n2=pickle.load(filer)
        filer.close()
        if func=="subt":
            tot=n1-n2
        else:
            tot=n1+n2
        if str(tot)==instot.text():
            answer=QLabel()
            answeri=QPixmap("img/checked.png").scaledToWidth(48)
            answer.setPixmap(answeri)
            layout.addWidget(answer,7,0,1,n2+1)
        else:
            answer=QLabel()
            answeri=QPixmap("img/error.png").scaledToWidth(48)
            answer.setPixmap(answeri)
            layout.addWidget(answer,7,0,1,n2+1)
    def clearLayout(self):
            global layout
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
    def adi(self):
        self.clearLayout()        
        global instot,imgi,layout,func
        func="add"
        # 2 nrs random int
        n1=random.randint(1,9)
        n2=random.randint(1,9)
        filew=open("files/1.sav","wb")
        pickle.dump(n1,filew)
        filew.close()
        filew=open("files/2.sav","wb")
        pickle.dump(n2,filew)
        filew.close()
        eq=QLabel()
        eq.setText(str(n1)+ " + "+str(n2))
        eq.setFont(QFont("Arial",18,QFont.Bold))
        #operator
        oper=QLabel()
        oper.setText('+')
        oper.setFont(QFont("Arial",18,QFont.Bold))
        #total
        total=QLabel()
        total.setText('Total :')
        instot=QLineEdit()
        instot.resize(64,32)
        #butao
        button1 = QPushButton()
        button1.setIcon(QIcon('img/search.png'))
        # create menu
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        menu = menubar.addMenu("Menu")
        action=menu.addAction("+++++")
        action.triggered.connect(self.adi)
        action=menu.addAction("-----")
        action.triggered.connect(self.subt)
        menu.addSeparator()
        action=menu.addAction("Quit")
        action.triggered.connect(self.close)
        menu = menubar.addMenu("Info")
        action=menu.addAction("Credits")
        action.triggered.connect(self.showdialog)
        button1.clicked.connect(self.showw)
        img=QLabel()
        img.setPixmap(imgi)
        if(n1>n2):
            layout.addWidget(eq,1,0,1,n1)
            layout.addWidget(instot,5,1,1,n1)
            layout.addWidget(button1,6,0,1,n1+1)
            layout.addWidget(oper,3,1,1,n1)
        else:
            layout.addWidget(eq,1,0,1,n2)
            layout.addWidget(instot,5,1,1,n2)
            layout.addWidget(button1,6,0,1,n2+1)
            layout.addWidget(oper,3,1,1,n2)
        i=1
        while i<=n1:
            img=QLabel()
            img.setPixmap(imgi)
            layout.addWidget(img,2,i)
            i=i+1
        i=1
        while i<=n2:
            img=QLabel()
            img.setPixmap(imgi)
            layout.addWidget(img,4,i)
            i=i+1
        layout.addWidget(total,5,0)
    def subt(self):
        self.clearLayout()        
        global layout,instot,func
        func="subt"
        z=0
        # 2 nrs random int
        n1=random.randint(1,9)
        n2=random.randint(1,9)
        while(z==0):
            if(n1<n2):
                n1=random.randint(1,9)
                n2=random.randint(1,9)
            else:
                z=1
        filew=open("files/1.sav","wb")
        pickle.dump(n1,filew)
        filew.close()
        filew=open("files/2.sav","wb")
        pickle.dump(n2,filew)
        filew.close()
        eq=QLabel()
        eq.setText(str(n1)+ " - "+str(n2))
        eq.setFont(QFont("Arial",18,QFont.Bold))
        #operator
        oper=QLabel()
        oper.setText('-')
        oper.setFont(QFont("Arial",18,QFont.Bold))
        #total
        total=QLabel()
        total.setText('Total :')
        instot=QLineEdit()
        instot.resize(64,32)
        #butao
        button1 = QPushButton()
        button1.setIcon(QIcon('img/search.png'))
        # create menu
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        menu = menubar.addMenu("Menu")
        action=menu.addAction("+++++")
        action.triggered.connect(self.adi)
        action=menu.addAction("-----")
        action.triggered.connect(self.subt)
        menu.addSeparator()
        action=menu.addAction("Quit")
        action.triggered.connect(self.close)
        menu = menubar.addMenu("Info")
        action=menu.addAction("Credits")
        action.triggered.connect(self.showdialog)
        button1.clicked.connect(self.showw)
        #imagem
        imgi=QPixmap("img/fish.png").scaledToWidth(64)
        img=QLabel()
        img.setPixmap(imgi)
        if(n1>n2):
            layout.addWidget(eq,1,0,1,n1)
            layout.addWidget(instot,5,1,1,n1)
            layout.addWidget(button1,6,0,1,n1+1)
            layout.addWidget(oper,3,1,1,n1)
        else:
            layout.addWidget(eq,1,0,1,n2)
            layout.addWidget(instot,5,1,1,n2)
            layout.addWidget(button1,6,0,1,n2+1)
            layout.addWidget(oper,3,1,1,n2)
        i=1
        while i<=n1:
            img=QLabel()
            img.setPixmap(imgi)
            layout.addWidget(img,2,i)
            i=i+1
        i=1
        while i<=n2:
            img=QLabel()
            img.setPixmap(imgi)
            layout.addWidget(img,4,i)
            i=i+1
        layout.addWidget(total,5,0)
    def showdialog(self):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Information)

       msg.setText("Copyright (c) 2020, Oscar Monteiro All rights reserved.")
       texti="""Redistribution and use in source and binary forms, with or without
                 modification, are permitted provided that the following conditions are met:"""
       msg.setInformativeText(texti)
       msg.setWindowTitle("Credits")
       text="""* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
                * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
                * Neither the name of the <organization> nor thenames of its contributors may be used to endorse or promote productsderived from this software without specific prior written permission.
                THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" ANDANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIEDWARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE AREDISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANYDIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED ANDON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THISSOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE
                """
       msg.setDetailedText(text)
       msg.exec_()        
screen = Window()
screen.show()
sys.exit(app.exec_())
