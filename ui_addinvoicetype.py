# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_invoice_typegkSETh.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_add_invoicetype(object):
    def setupUi(self, add_invoicetype):
        if not add_invoicetype.objectName():
            add_invoicetype.setObjectName(u"add_invoicetype")
        add_invoicetype.resize(429, 91)
        self.verticalLayout_2 = QVBoxLayout(add_invoicetype)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(add_invoicetype)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_type = QLineEdit(add_invoicetype)
        self.le_type.setObjectName(u"le_type")

        self.horizontalLayout.addWidget(self.le_type)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(add_invoicetype)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_2.addWidget(self.cancel)

        self.save = QPushButton(add_invoicetype)
        self.save.setObjectName(u"save")

        self.horizontalLayout_2.addWidget(self.save)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(add_invoicetype)

        QMetaObject.connectSlotsByName(add_invoicetype)
    # setupUi

    def retranslateUi(self, add_invoicetype):
        add_invoicetype.setWindowTitle(QCoreApplication.translate("add_invoicetype", u"Add invoice type", None))
        self.label.setText(QCoreApplication.translate("add_invoicetype", u"TextLabel", None))
        self.cancel.setText(QCoreApplication.translate("add_invoicetype", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.save.setText(QCoreApplication.translate("add_invoicetype", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
    # retranslateUi

