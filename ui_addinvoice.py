# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_invoicejwJrRd.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_add_invoice(object):
    def setupUi(self, add_invoice):
        if not add_invoice.objectName():
            add_invoice.setObjectName(u"add_invoice")
        add_invoice.resize(799, 586)
        self.horizontalLayout_8 = QHBoxLayout(add_invoice)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_11 = QLabel(add_invoice)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.cb_invoice_type = QComboBox(add_invoice)
        self.cb_invoice_type.setObjectName(u"cb_invoice_type")

        self.horizontalLayout_3.addWidget(self.cb_invoice_type)


        self.verticalLayout_12.addLayout(self.horizontalLayout_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, 5, -1)
        self.label = QLabel(add_invoice)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.le_reg_number = QLineEdit(add_invoice)
        self.le_reg_number.setObjectName(u"le_reg_number")

        self.verticalLayout.addWidget(self.le_reg_number)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, -1, -1)
        self.label_2 = QLabel(add_invoice)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.le_sh_number = QLineEdit(add_invoice)
        self.le_sh_number.setObjectName(u"le_sh_number")

        self.verticalLayout_2.addWidget(self.le_sh_number)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, -1, -1)
        self.label_3 = QLabel(add_invoice)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.le_doc_number = QLineEdit(add_invoice)
        self.le_doc_number.setObjectName(u"le_doc_number")

        self.verticalLayout_3.addWidget(self.le_doc_number)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, -1, -1)
        self.label_4 = QLabel(add_invoice)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.de_doc_date = QDateEdit(add_invoice)
        self.de_doc_date.setObjectName(u"de_doc_date")

        self.verticalLayout_4.addWidget(self.de_doc_date)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, -1, -1)
        self.label_5 = QLabel(add_invoice)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.le_op_aime = QLineEdit(add_invoice)
        self.le_op_aime.setObjectName(u"le_op_aime")

        self.verticalLayout_5.addWidget(self.le_op_aime)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, -1, -1)
        self.label_6 = QLabel(add_invoice)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.de_op_date = QDateEdit(add_invoice)
        self.de_op_date.setObjectName(u"de_op_date")

        self.verticalLayout_6.addWidget(self.de_op_date)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, -1, -1)
        self.label_7 = QLabel(add_invoice)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.cb_serv_name = QComboBox(add_invoice)
        self.cb_serv_name.setObjectName(u"cb_serv_name")

        self.verticalLayout_7.addWidget(self.cb_serv_name)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, -1, -1)
        self.label_8 = QLabel(add_invoice)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.le_sender = QLineEdit(add_invoice)
        self.le_sender.setObjectName(u"le_sender")

        self.verticalLayout_8.addWidget(self.le_sender)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_9.setSpacing(-1)
#endif
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, -1, -1)
        self.label_9 = QLabel(add_invoice)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)

        self.le_reciver = QLineEdit(add_invoice)
        self.le_reciver.setObjectName(u"le_reciver")

        self.verticalLayout_9.addWidget(self.le_reciver)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, -1, -1)
        self.label_10 = QLabel(add_invoice)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_10)

        self.le_rec_supervisor = QLineEdit(add_invoice)
        self.le_rec_supervisor.setObjectName(u"le_rec_supervisor")

        self.verticalLayout_10.addWidget(self.le_rec_supervisor)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.tableView = QTableView(add_invoice)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_11.addWidget(self.tableView)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(add_invoice)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.cb_sender_supervisor = QComboBox(add_invoice)
        self.cb_sender_supervisor.setObjectName(u"cb_sender_supervisor")

        self.horizontalLayout_5.addWidget(self.cb_sender_supervisor)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_13 = QLabel(add_invoice)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.cb_rec_supervisor = QComboBox(add_invoice)
        self.cb_rec_supervisor.setObjectName(u"cb_rec_supervisor")

        self.horizontalLayout_6.addWidget(self.cb_rec_supervisor)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(add_invoice)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_4.addWidget(self.cancel)

        self.save = QPushButton(add_invoice)
        self.save.setObjectName(u"save")

        self.horizontalLayout_4.addWidget(self.save)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)


        self.retranslateUi(add_invoice)

        QMetaObject.connectSlotsByName(add_invoice)
    # setupUi

    def retranslateUi(self, add_invoice):
        add_invoice.setWindowTitle(QCoreApplication.translate("add_invoice", u"Add invoice", None))
        self.label_11.setText(QCoreApplication.translate("add_invoice", u"\u043d\u0430\u043a\u043b\u0430\u0434\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("add_invoice", u"\u0420\u0435\u0435\u0441\u0442\u0440\u0430\u0446\u0456\u0439\u043d\u0438\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.label_2.setText(QCoreApplication.translate("add_invoice", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u0440\u043a\u0443\u0448\u0430", None))
        self.label_3.setText(QCoreApplication.translate("add_invoice", u"\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.label_4.setText(QCoreApplication.translate("add_invoice", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("add_invoice", u"\u041f\u0456\u0434\u0441\u0442\u0430\u0432\u0430 (\u043c\u0435\u0442\u0430) \u043e\u043f\u0435\u0440\u0430\u0446\u0456\u0457", None))
        self.label_6.setText(QCoreApplication.translate("add_invoice", u"\u0414\u0430\u0442\u0430 \u043e\u043f\u0435\u0440\u0430\u0446\u0456\u0457", None))
        self.label_7.setText(QCoreApplication.translate("add_invoice", u"\u0421\u043b\u0443\u0436\u0431\u0430 \u0437\u0430\u0431\u0435\u0437\u043f\u0435\u0447\u0435\u043d\u043d\u044f", None))
        self.label_8.setText(QCoreApplication.translate("add_invoice", u"\u0412\u0430\u043d\u0442\u0430\u0436\u043e\u0432\u0456\u0434\u043f\u0440\u0430\u0432\u043d\u0438\u043a", None))
        self.label_9.setText(QCoreApplication.translate("add_invoice", u"\u0412\u0430\u043d\u0442\u0430\u0436\u043e\u043e\u0434\u0435\u0440\u0436\u0443\u0432\u0430\u0447", None))
        self.label_10.setText(QCoreApplication.translate("add_invoice", u"\u0412\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u0430\u043b\u044c\u043d\u0438\u0439 \u043e\u0434\u0435\u0440\u0436\u0443\u0432\u0430\u0447", None))
        self.label_12.setText(QCoreApplication.translate("add_invoice", u"\u0412\u0438\u0434\u0430\u0432", None))
        self.label_13.setText(QCoreApplication.translate("add_invoice", u"\u041e\u0442\u0440\u0438\u043c\u0430\u0432", None))
        self.cancel.setText(QCoreApplication.translate("add_invoice", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.save.setText(QCoreApplication.translate("add_invoice", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
    # retranslateUi

