# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mobisafe.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import feature_extraction
import process_message
import sms_controller


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 576)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setGeometry(QtCore.QRect(550, 210, 111, 31))
        self.btnSubmit.setStyleSheet("background-color:#FFD700")
        self.btnSubmit.setObjectName("btnSubmit")

        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(430, 210, 111, 31))
        self.btnClear.setStyleSheet("background-color:#FFD700")
        self.btnClear.setObjectName("btnclear")

        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(10, 10, 141, 61))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font2 = QtGui.QFont()
        font2.setFamily("Century Gothic")
        font2.setPointSize(12)
        font3 = QtGui.QFont()
        font3.setFamily("Open Sans")
        font3.setPointSize(11)


        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.cmbBoxSelectInputType = QtWidgets.QComboBox(self.centralwidget)

        self.cmbBoxSelectInputType.setGeometry(QtCore.QRect(200, 210, 131, 31))
        self.cmbBoxSelectInputType.setObjectName("cmbBoxSelectInputType")
        
        self.cmbBoxSelectInputType.addItem("")
        self.cmbBoxSelectInputType.addItem("")

        ## Output results ##
        self.lstShowResults = QtWidgets.QTextEdit(self.centralwidget)   
        self.lstShowResults.setGeometry(QtCore.QRect(200, 250, 601, 192))
        self.lstShowResults.setObjectName("lstShowResults")
    
        self.lstShowResults.setFont(font3)

        
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setObjectName("infoLabel")
        self.infoLabel.adjustSize()
        self.infoLabel.setGeometry(250, 400, 601, 192)
        self.infoLabel.setFont(font2)

        self.txtUserInput = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUserInput.setGeometry(QtCore.QRect(200, 100, 601, 91))
        
        self.txtUserInput.setObjectName("txtUserInput")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 70, 391, 16))


        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.btnSubmitFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmitFile.setGeometry(QtCore.QRect(670, 210, 111, 31))
        self.btnSubmitFile.setStyleSheet("background-color:#FFD700")
        self.btnSubmitFile.setObjectName("btnSubmitFile")

        MainWindow.setCentralWidget(self.centralwidget)
        self.File = QtWidgets.QMenuBar(MainWindow)
        self.File.setGeometry(QtCore.QRect(0, 0, 974, 21))
        self.File.setAutoFillBackground(False)
        self.File.setObjectName("File")

        self.menuFile = QtWidgets.QMenu(self.File)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.File)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.File)
        self.menuAbout.setObjectName("menuAbout")

        MainWindow.setMenuBar(self.File)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setShortcutVisibleInContextMenu(True)
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setShortcutVisibleInContextMenu(True)
        self.actionPaste.setObjectName("actionPaste")

        self.actionView_About_Page = QtWidgets.QAction(MainWindow)
        self.actionView_About_Page.setObjectName("actionView_About_Page")

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

       
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)

        self.menuAbout.addAction(self.actionView_About_Page)

        self.File.addAction(self.menuFile.menuAction())
        self.File.addAction(self.menuEdit.menuAction())
        self.File.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ACTIONS
        self.btnSubmit.clicked.connect(lambda: self.submit())
        self.btnSubmitFile.clicked.connect(lambda: self.submit_text_file())
        self.btnClear.clicked.connect(lambda: self.clear_edits())
        self.actionExit.triggered.connect(lambda: self.exit())

        self.update_label()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit Text"))
        self.btnClear.setText(_translate("MainWindow", "Clear Text"))
        self.lblTitle.setText(_translate("MainWindow", "MobiSafe"))
        self.infoLabel.setText(_translate("MainWindow","Thank you for using Mobi-Safe\nauthor - Danny Fitzgerald"))
        self.cmbBoxSelectInputType.setItemText(
            0, _translate("MainWindow", "SMS"))
        self.cmbBoxSelectInputType.setItemText(
            1, _translate("MainWindow", "URL"))
        self.label.setText(_translate(
            "MainWindow", "Please type the submission into the field below: "))
        self.btnSubmitFile.setText(_translate("MainWindow", "Submit File"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setStatusTip(_translate("MainWindow", "About Page"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionView_About_Page.setText(_translate("MainWindow", "View About Page"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


    # OPERATION LOGIC

    def submit(self):
        # If the user selects URL Input
        input_setting = str(self.cmbBoxSelectInputType.currentText())
        if input_setting == "URL":
            text = self.txtUserInput.text()
            obj = feature_extraction.Feature_Extraction(text)
            str1, str2 = obj.extract()
            self.lstShowResults.append("{} \n{}\n\n".format(str1, str2))
            label = "Classification Complete"
            self.infoLabel.setText(label)

        # If the user selects SMS Input
        if input_setting == "SMS":
            text = self.txtUserInput.text()

            if "https://" in str(text):

                print("\n\t Url Detection")

                obj2 = sms_controller.locate_url(text)
                str3 = obj2.split_url()
                print(str3)

                ###     URL Classification      ###

                classify_url = feature_extraction.Feature_Extraction(str3)
                str4, str5 = classify_url.extract()

                self.lstShowResults.append("{} \n{}\n\n".format(str4, str5))
                print("\nThe system has processed the url within the message\n")

            print("Begin analysis of sms")
            ###     SMS Classification      ###

            obj = process_message.Classify_Message(text)
            str1, str2 = obj.process()

            self.lstShowResults.append("{} \n{}\n\n".format(str1, str2))
            label = "Classification Complete"
            self.infoLabel.setText(label)




    def submit_text_file(self):
        input_setting = str(self.cmbBoxSelectInputType.currentText())
        self._results = []
        file_name = self.txtUserInput.text()
        input_setting = str(self.cmbBoxSelectInputType.currentText())
        if input_setting == "URL":
            try:
     
                with open(file_name, "r") as file:

                    for line in file:
                        text = str(line.split())
                        obj = feature_extraction.Feature_Extraction(text)
                        str1, str2 = obj.extract()

                        result = []
                        result.append("{} \n{}\n\n".format(str1, str2))
                        print("Prediction Result: \n", result)
                        self._results.append(text)
                        self._results.append(result)
                for item in self._results:
                        self.lstShowResults.append(str(item))
                label = "Classification Complete"
                self.infoLabel.setText(label)

        
            except:
                print("File Not found")
                self.no_file_found()
        


        
            print("File not found, please try again")

        
            
        if input_setting == "SMS":

            try:
                with open(file_name, "r") as file:

                    for line in file:
                        text = str(line.split())
                        self.infoLabel.setText = "Reading From Text File"

                        if "https://" in text:

                            print("\n\t Url Detection")

                            obj2 = sms_controller.locate_url(text)
                            str3 = obj2.split_url()
                            print(str3)

                            ###     URL Classification      ###

                            classify_url = feature_extraction.Feature_Extraction(
                                str3)
                            str4, str5 = classify_url.extract()

                            self.lstShowResults.append(
                                "{} \n{}\n\n".format(str4, str5))
                            print(
                                "\nThe system has processed the url within the message\n")
                            print("Prediction Result: \n", result)

                        print("Begin analysis of sms")
                        ###     SMS Classification      ###

                        obj = process_message.Classify_Message(text)
                        str1, str2 = obj.process()

                        result = []
                        result.append("{} \n{}\n\n".format(str1, str2))
                        print("Prediction Result: \n", result)
                        self._results.append(text)
                        self._results.append(result)
                   
 
            
                for item in self._results:
                    self.lstShowResults.append(str(item))
                self.infoLabel.setText(label)

                label = "Classification Complete"
                self.infoLabel.setText(label)

            except:
                print("File not found, please try again")
                self.no_file_found()
        


    def clear_edits(self):
    ## Clear data held within output and input edits ''
        self.lstShowResults.clear()
        self.txtUserInput.clear()

    def no_file_found(self):
        label = "No file found, check input and directory"
        self.infoLabel.setText(label)


    def update_label(self):

        label = "Please make a new submission"
        self.infoLabel.setText(label)

        

    def exit(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
