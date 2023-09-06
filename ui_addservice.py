# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_servicessrNEHE.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_add_service(object):
    def setupUi(self, add_service):
        if not add_service.objectName():
            add_service.setObjectName(u"add_service")
        add_service.resize(549, 166)
        self.horizontalLayout_5 = QHBoxLayout(add_service)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(add_service)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_name = QLineEdit(add_service)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout.addWidget(self.le_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(add_service)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_red_name = QLineEdit(add_service)
        self.le_red_name.setObjectName(u"le_red_name")

        self.horizontalLayout_2.addWidget(self.le_red_name)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(add_service)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.cb_supervisor = QComboBox(add_service)
        self.cb_supervisor.setObjectName(u"cb_supervisor")

        self.horizontalLayout_3.addWidget(self.cb_supervisor)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(add_service)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_4.addWidget(self.cancel)

        self.save = QPushButton(add_service)
        self.save.setObjectName(u"save")

        self.horizontalLayout_4.addWidget(self.save)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.retranslateUi(add_service)

        QMetaObject.connectSlotsByName(add_service)
    # setupUi

    def retranslateUi(self, add_service):
        add_service.setWindowTitle(QCoreApplication.translate("add_service", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("add_service", u"\u041d\u0430\u0437\u0432\u0430 \u0441\u043b\u0443\u0436\u0431\u0438", None))
        self.label_2.setText(QCoreApplication.translate("add_service", u"\u0437\u043c\u0435\u043d\u0448\u0435\u043d\u0430 \u043d\u0430\u0437\u0432\u0430", None))
        self.label_3.setText(QCoreApplication.translate("add_service", u"\u043a\u0435\u0440\u0456\u0432\u043d\u0438\u043a", None))
        self.cancel.setText(QCoreApplication.translate("add_service", u"\u0412\u0456\u0434\u043c\u0456\u0442\u0438\u0442\u0438", None))
        self.save.setText(QCoreApplication.translate("add_service", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
    # retranslateUi

