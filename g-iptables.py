from PyQt5 import QtCore, QtGui, QtWidgets
from main_form import Ui_Main_Form
from root_check_form import Ui_Root_Check_Form
from creator_form import Ui_Creator_Form
from error_form import Ui_Error_Form
import resource
import os

class main_w(Ui_Main_Form):
    def setupUi(self, Main_Form):
        super().setupUi(Main_Form)
        Main_Form.setWindowTitle("g-iptables")
        self.header = self.tableWidget.horizontalHeader()                               # resize option for columns
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.pushButton_1.clicked.connect(self.open_creator)
        self.pushButton_2.clicked.connect(lambda: self.addRule(rowPosition=True))       # addrule buttons
        self.tableWidget.cellClicked.connect(self.removeRule)                           # remove rule
        self.tabWidget_main.currentChanged.connect(self.index)                          # tab currentChanged
        self.tabWidget_1.currentChanged.connect(self.index)
        self.tabWidget_2.currentChanged.connect(self.index)
        self.tabWidget_3.currentChanged.connect(self.index)
        self.tabWidget_4.currentChanged.connect(self.index)
        self.tabWidget_5.currentChanged.connect(self.index)
        self.index()

    def open_creator(self):
        c_Form.show()

    def index(self):
        chainIndex = self.tabWidget_main.currentIndex()                                 # tab index
        self.chain = self.tabWidget_main.tabText(chainIndex)
        if chainIndex == 0:
            tableIndex = self.tabWidget_1.currentIndex()
            self.table = self.tabWidget_1.tabText(tableIndex)
            self.listRule(self.table, self.chain)
        if chainIndex == 1:
            tableIndex = self.tabWidget_2.currentIndex()
            self.table = self.tabWidget_2.tabText(tableIndex)
            self.listRule(self.table, self.chain)
        if chainIndex == 2:
            tableIndex = self.tabWidget_3.currentIndex()
            self.table = self.tabWidget_3.tabText(tableIndex)
            self.listRule(self.table, self.chain)
        if chainIndex == 3:
            tableIndex = self.tabWidget_4.currentIndex()
            self.table = self.tabWidget_4.tabText(tableIndex)
            self.listRule(self.table, self.chain)
        if chainIndex == 4:
            tableIndex = self.tabWidget_5.currentIndex()
            self.table = self.tabWidget_5.tabText(tableIndex)
            self.listRule(self.table, self.chain)
        self.lineEdit.setText("iptables -t " + self.table + " -A " + self.chain)

    def listRule(self, table, chain):
        cmd = "iptables -t " + table + " -S " + chain
        res = os.popen(cmd).read()
        rules = res.splitlines()
        self.tableWidget.setRowCount(0)
        for rule in rules:
            self.addRule(rule)

    def addRule(self, rule=False, rowPosition=False):
        if rule == False:
            rule = self.lineEdit.text()
            os.popen(rule)
        if rule != "":
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(rowPosition, item)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(rowPosition)))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(rule))
            item = QtWidgets.QTableWidgetItem()
            if rowPosition != 0:
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap(":/delete_img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon3)
                self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(item))

    def removeRule(self, row, column):
        if (column == 2) & (row != 0):
            self.tableWidget.removeRow(row)
            rowPosition = self.tableWidget.rowCount()
            cmd = "iptables -t " + self.table + " -D " + self.chain + " " + str(row)
            os.popen(cmd)
            for id in range(row, rowPosition):
                self.tableWidget.setItem(id, 0, QtWidgets.QTableWidgetItem(str(id)))

class root_w(Ui_Root_Check_Form):
    def setupUi(self, Root_Check_Form):
        super().setupUi(Root_Check_Form)
        self.pushButton.clicked.connect(Root_Check_Form.close)
        self.pushButton.clicked.connect(Main_Form.close)

class creator_w(Ui_Creator_Form):
    def setupUi(self, Creator_Form):
        super().setupUi(Creator_Form)
        self.pushButton_1.clicked.connect(self.reset)
        self.pushButton_2.clicked.connect(self.create)

    def create(self):
        self.dict = {
            ' -p ': '',
            ' -i ': '',
            ' -o ': '',
            ' -d ': '',
            'dest_from': '',
            'dest_to': '',
            ' -s ': '',
            'source_from': '',
            'source_to': '',
            'state': '',
            'limit': '',
            ' - j ': '',
        }

        self.dict[' -p '] = self.comboBox_1.currentText()
        if self.dict[' -p '] == 'None':
            self.dict[' -p '] = ""
        self.dict[' -i '] = self.lineEdit_1.text()
        self.dict[' -o '] = self.lineEdit_2.text()
        self.dict[' -d '] = self.lineEdit_3.text()
        self.dict['dest_from'] = self.lineEdit_6.text()
        self.dict['dest_to'] = self.lineEdit_8.text()
        self.dict[' -s '] = self.lineEdit_4.text()
        self.dict['source_from'] = self.lineEdit_7.text()
        self.dict['source_to'] = self.lineEdit_9.text()
        self.dict['state'] = self.comboBox_2.currentText()
        if self.dict['state'] == 'None':
            self.dict['state'] = ""
        self.dict['limit'] = self.lineEdit_5.text()
        self.dict[' -j '] = self.comboBox_3.currentText()
        creator = ""
        for key in self.dict.keys():
            if self.dict[key] != "":
                if key == ' -d ':
                    creator += " -d {} --dport {}:{}".format(self.dict[key], self.dict['dest_from'], self.dict['dest_to'])
                    self.dict['dest_from'] = ""
                    self.dict['dest_to'] = ""
                elif key == ' -s ':
                    creator += " -s {} --sport {}:{}".format(self.dict[key], self.dict['source_from'], self.dict['source_to'])
                    self.dict['source_from'] = ""
                    self.dict['source_to'] = ""
                elif key == 'state':
                    creator += " -m state --state {}".format(self.dict[key])
                elif key == 'limit':
                    creator += " -m limit --limit {}".format(self.dict[key])
                else:
                    creator += "{}{}".format(key, self.dict[key])

        rule = "iptables -t " + main_ui.table + " -A " + main_ui.chain
        creator_rule = rule + creator
        main_ui.lineEdit.setText(creator_rule)
        c_Form.close()

    def reset(self):
        self.comboBox_1.setCurrentIndex(0)
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_6.clear()
        self.lineEdit_8.clear()
        self.lineEdit_4.clear()
        self.lineEdit_7.clear()
        self.lineEdit_9.clear()
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_5.clear()
        self.comboBox_3.setCurrentIndex(0)

class error_w(Ui_Error_Form):
        def setupUi(self, Creator_Form):
            super().setupUi(Creator_Form)
            self.textBrowser.setText("help")

if __name__ == "__main__":
    def root_check():
        if os.getuid() != 0:
            Main_Form.setEnabled(False)
            rc_Form = QtWidgets.QWidget()
            check_ui = root_w()
            check_ui.setupUi(rc_Form)
            rc_Form.show()
            sys.exit(app.exec_())

    import sys
    app = QtWidgets.QApplication(sys.argv)
    c_Form = QtWidgets.QWidget()
    c_ui = creator_w()
    c_ui.setupUi(c_Form)
    e_Form = QtWidgets.QWidget()
    e_ui = creator_w()
    e_ui.setupUi(e_Form)
    Main_Form = QtWidgets.QWidget()
    main_ui = main_w()
    main_ui.setupUi(Main_Form)
    Main_Form.show()

    if os.name == "posix":
        root_check()
    sys.exit(app.exec_())
