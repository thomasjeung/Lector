# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listView.setMovement(QtWidgets.QListView.Static)
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setLayoutMode(QtWidgets.QListView.Batched)
        self.listView.setViewMode(QtWidgets.QListView.IconMode)
        self.listView.setUniformItemSizes(True)
        self.listView.setWordWrap(True)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.LibraryToolBar = QtWidgets.QToolBar(MainWindow)
        self.LibraryToolBar.setMovable(False)
        self.LibraryToolBar.setIconSize(QtCore.QSize(22, 22))
        self.LibraryToolBar.setFloatable(False)
        self.LibraryToolBar.setObjectName("LibraryToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.LibraryToolBar)
        self.BookToolBar = QtWidgets.QToolBar(MainWindow)
        self.BookToolBar.setMovable(False)
        self.BookToolBar.setFloatable(False)
        self.BookToolBar.setObjectName("BookToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.BookToolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lector"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Library"))
        self.LibraryToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.BookToolBar.setWindowTitle(_translate("MainWindow", "toolBar_2"))

