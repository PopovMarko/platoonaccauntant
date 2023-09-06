# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_supervisorSeMphL.ui'
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

class Ui_add_supervisor(object):
    def setupUi(self, add_supervisor):
        if not add_supervisor.objectName():
            add_supervisor.setObjectName(u"add_supervisor")
        add_supervisor.resize(377, 240)
        self.verticalLayout_2 = QVBoxLayout(add_supervisor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(add_supervisor)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.le_position = QLineEdit(add_supervisor)
        self.le_position.setObjectName(u"le_position")

        self.horizontalLayout.addWidget(self.le_position)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(add_supervisor)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.le_rank = QLineEdit(add_supervisor)
        self.le_rank.setObjectName(u"le_rank")

        self.horizontalLayout_2.addWidget(self.le_rank)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(add_supervisor)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.le_name = QLineEdit(add_supervisor)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout_3.addWidget(self.le_name)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(add_supervisor)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.le_surname = QLineEdit(add_supervisor)
        self.le_surname.setObjectName(u"le_surname")

        self.horizontalLayout_4.addWidget(self.le_surname)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(add_supervisor)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.le_lastname = QLineEdit(add_supervisor)
        self.le_lastname.setObjectName(u"le_lastname")

        self.horizontalLayout_5.addWidget(self.le_lastname)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.cancel = QPushButton(add_supervisor)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_6.addWidget(self.cancel)

        self.save = QPushButton(add_supervisor)
        self.save.setObjectName(u"save")

        self.horizontalLayout_6.addWidget(self.save)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(add_supervisor)

        QMetaObject.connectSlotsByName(add_supervisor)
    # setupUi

    def retranslateUi(self, add_supervisor):
        add_supervisor.setWindowTitle(QCoreApplication.translate("add_supervisor", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("add_supervisor", u"\u041f\u043e\u0441\u0430\u0434\u0430", None))
        self.label_2.setText(QCoreApplication.translate("add_supervisor", u"\u0417\u0432\u0430\u043d\u043d\u044f", None))
        self.label_3.setText(QCoreApplication.translate("add_supervisor", u"\u0406\u043c\u02bc\u044f", None))
        self.label_4.setText(QCoreApplication.translate("add_supervisor", u"\u041f\u043e\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456", None))
        self.label_5.setText(QCoreApplication.translate("add_supervisor", u"\u041f\u0440\u0438\u0437\u0432\u0438\u0449\u0435", None))
        self.cancel.setText(QCoreApplication.translate("add_supervisor", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.save.setText(QCoreApplication.translate("add_supervisor", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
    # retranslateUi


