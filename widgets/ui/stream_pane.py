# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stream_pane.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(763, 111)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ipLabel = QLabel(Form)
        self.ipLabel.setObjectName(u"ipLabel")

        self.horizontalLayout_2.addWidget(self.ipLabel)

        self.ipAdressLineEdit = QLineEdit(Form)
        self.ipAdressLineEdit.setObjectName(u"ipAdressLineEdit")

        self.horizontalLayout_2.addWidget(self.ipAdressLineEdit)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.portLabel = QLabel(Form)
        self.portLabel.setObjectName(u"portLabel")

        self.horizontalLayout.addWidget(self.portLabel)

        self.portLineEdit = QLineEdit(Form)
        self.portLineEdit.setObjectName(u"portLineEdit")

        self.horizontalLayout.addWidget(self.portLineEdit)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.enableStreamCheckBox = QCheckBox(Form)
        self.enableStreamCheckBox.setObjectName(u"enableStreamCheckBox")

        self.horizontalLayout_3.addWidget(self.enableStreamCheckBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ipLabel.setText(QCoreApplication.translate("Form", u"ip: ", None))
        self.portLabel.setText(QCoreApplication.translate("Form", u"port: ", None))
        self.enableStreamCheckBox.setText(QCoreApplication.translate("Form", u"enable stream", None))
    # retranslateUi

