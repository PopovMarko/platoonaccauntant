## -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowlSHpKt.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(776, 404)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.horizontalLayout = QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.goodsButton = QPushButton(self.mainFrame)
        self.goodsButton.setObjectName(u"goodsButton")

        self.verticalLayout_2.addWidget(self.goodsButton)

        self.invoicesButton = QPushButton(self.mainFrame)
        self.invoicesButton.setObjectName(u"invoicesButton")

        self.verticalLayout_2.addWidget(self.invoicesButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.addInvoiceButton = QPushButton(self.mainFrame)
        self.addInvoiceButton.setObjectName(u"addInvoiceButton")

        self.verticalLayout_2.addWidget(self.addInvoiceButton)

        self.addGoodsButton = QPushButton(self.mainFrame)
        self.addGoodsButton.setObjectName(u"addGoodsButton")

        self.verticalLayout_2.addWidget(self.addGoodsButton)

        self.addServiceButton = QPushButton(self.mainFrame)
        self.addServiceButton.setObjectName(u"addServiceButton")

        self.verticalLayout_2.addWidget(self.addServiceButton)

        self.addSupervisorButton = QPushButton(self.mainFrame)
        self.addSupervisorButton.setObjectName(u"addSupervisorButton")

        self.verticalLayout_2.addWidget(self.addSupervisorButton)

        self.addInvoiceTypeButton = QPushButton(self.mainFrame)
        self.addInvoiceTypeButton.setObjectName(u"addInvoiceTypeButton")

        self.verticalLayout_2.addWidget(self.addInvoiceTypeButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableLabel = QLabel(self.mainFrame)
        self.tableLabel.setObjectName(u"tableLabel")
        self.tableLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.tableLabel)

        self.tableView = QTableView(self.mainFrame)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"platoon accauntant", None))
        self.goodsButton.setText(QCoreApplication.translate("MainWindow", u"\u0422\u041c\u0426", None))
        self.invoicesButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0456", None))
        self.addInvoiceButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043d\u0430\u043a\u043b\u0430\u0434\u043d\u0443", None))
        self.addGoodsButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0422\u041c\u0426", None))
        self.addServiceButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0441\u043b\u0443\u0436\u0431\u0443", None))
        self.addSupervisorButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043a\u043e\u043c\u0430\u043d\u0434\u0438\u0440\u0430", None))
        self.addInvoiceTypeButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0442\u0438\u043f \u043d\u0430\u043a\u043b\u0430\u0434\u043d\u043e\u0457", None))
        self.tableLabel.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043f\u0438\u0441\u043e\u043a \u0442\u043e\u0432\u0430\u0440\u0456\u0432", None))
    # retranslateUi


