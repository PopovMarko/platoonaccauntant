# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_goodsFQNTKG.ui'
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

class Ui_add_goods(object):
    def setupUi(self, add_goods):
        if not add_goods.objectName():
            add_goods.setObjectName(u"add_goods")
        add_goods.resize(729, 117)
        self.horizontalLayout_3 = QHBoxLayout(add_goods)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.goodsNameLabel = QLabel(add_goods)
        self.goodsNameLabel.setObjectName(u"goodsNameLabel")

        self.verticalLayout.addWidget(self.goodsNameLabel)

        self.goodsNameLine = QLineEdit(add_goods)
        self.goodsNameLine.setObjectName(u"goodsNameLine")

        self.verticalLayout.addWidget(self.goodsNameLine)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.goodsUnitsLabel = QLabel(add_goods)
        self.goodsUnitsLabel.setObjectName(u"goodsUnitsLabel")

        self.verticalLayout_2.addWidget(self.goodsUnitsLabel)

        self.goodsUnitsLine = QLineEdit(add_goods)
        self.goodsUnitsLine.setObjectName(u"goodsUnitsLine")

        self.verticalLayout_2.addWidget(self.goodsUnitsLine)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.goodsPriceLabel = QLabel(add_goods)
        self.goodsPriceLabel.setObjectName(u"goodsPriceLabel")

        self.verticalLayout_3.addWidget(self.goodsPriceLabel)

        self.goodsPriceLine = QLineEdit(add_goods)
        self.goodsPriceLine.setObjectName(u"goodsPriceLine")

        self.verticalLayout_3.addWidget(self.goodsPriceLine)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(add_goods)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_2.addWidget(self.cancel)

        self.save = QPushButton(add_goods)
        self.save.setObjectName(u"save")

        self.horizontalLayout_2.addWidget(self.save)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.retranslateUi(add_goods)

        QMetaObject.connectSlotsByName(add_goods)
    # setupUi

    def retranslateUi(self, add_goods):
        add_goods.setWindowTitle(QCoreApplication.translate("add_goods", u"Add goods", None))
        self.goodsNameLabel.setText(QCoreApplication.translate("add_goods", u"\u041d\u0430\u0437\u0432\u0430 \u0422\u041c\u0426", None))
        self.goodsUnitsLabel.setText(QCoreApplication.translate("add_goods", u"\u041e\u0434\u0438\u043d\u0438\u0446\u0456 \u0432\u0438\u043c\u0456\u0440\u0443", None))
        self.goodsPriceLabel.setText(QCoreApplication.translate("add_goods", u"\u0426\u0456\u043d\u0430", None))
        self.cancel.setText(QCoreApplication.translate("add_goods", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.save.setText(QCoreApplication.translate("add_goods", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
    # retranslateUi

