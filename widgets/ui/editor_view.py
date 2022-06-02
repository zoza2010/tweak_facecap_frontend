# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editor_view.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListView, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(424, 598)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.filterLabel = QLabel(Form)
        self.filterLabel.setObjectName(u"filterLabel")

        self.horizontalLayout_2.addWidget(self.filterLabel)

        self.filterLineEdit = QLineEdit(Form)
        self.filterLineEdit.setObjectName(u"filterLineEdit")

        self.horizontalLayout_2.addWidget(self.filterLineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.listView = QListView(Form)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_5.addWidget(self.listView)

        self.currentItemlabel = QLabel(Form)
        self.currentItemlabel.setObjectName(u"currentItemlabel")

        self.verticalLayout_5.addWidget(self.currentItemlabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.clampMaxLineEdit = QLineEdit(Form)
        self.clampMaxLineEdit.setObjectName(u"clampMaxLineEdit")

        self.verticalLayout.addWidget(self.clampMaxLineEdit)

        self.clampMaxSlider = QSlider(Form)
        self.clampMaxSlider.setObjectName(u"clampMaxSlider")
        self.clampMaxSlider.setFocusPolicy(Qt.StrongFocus)
        self.clampMaxSlider.setLayoutDirection(Qt.LeftToRight)
        self.clampMaxSlider.setAutoFillBackground(False)
        self.clampMaxSlider.setOrientation(Qt.Vertical)
        self.clampMaxSlider.setTickPosition(QSlider.NoTicks)

        self.verticalLayout.addWidget(self.clampMaxSlider, 0, Qt.AlignHCenter)

        self.clampMaxLabel = QLabel(Form)
        self.clampMaxLabel.setObjectName(u"clampMaxLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clampMaxLabel.sizePolicy().hasHeightForWidth())
        self.clampMaxLabel.setSizePolicy(sizePolicy)
        self.clampMaxLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.clampMaxLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.clampMinLineEdit = QLineEdit(Form)
        self.clampMinLineEdit.setObjectName(u"clampMinLineEdit")

        self.verticalLayout_2.addWidget(self.clampMinLineEdit)

        self.clampMinSlider = QSlider(Form)
        self.clampMinSlider.setObjectName(u"clampMinSlider")
        self.clampMinSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_2.addWidget(self.clampMinSlider, 0, Qt.AlignHCenter)

        self.clampMinLabel = QLabel(Form)
        self.clampMinLabel.setObjectName(u"clampMinLabel")
        self.clampMinLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.clampMinLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.offsetLineEdit = QLineEdit(Form)
        self.offsetLineEdit.setObjectName(u"offsetLineEdit")

        self.verticalLayout_3.addWidget(self.offsetLineEdit)

        self.offsetSlider = QSlider(Form)
        self.offsetSlider.setObjectName(u"offsetSlider")
        self.offsetSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.offsetSlider, 0, Qt.AlignHCenter)

        self.offsetLabel = QLabel(Form)
        self.offsetLabel.setObjectName(u"offsetLabel")
        self.offsetLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.offsetLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scaleLineEdit = QLineEdit(Form)
        self.scaleLineEdit.setObjectName(u"scaleLineEdit")

        self.verticalLayout_4.addWidget(self.scaleLineEdit)

        self.scaleSlider = QSlider(Form)
        self.scaleSlider.setObjectName(u"scaleSlider")
        self.scaleSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_4.addWidget(self.scaleSlider, 0, Qt.AlignHCenter)

        self.scaleLabel = QLabel(Form)
        self.scaleLabel.setObjectName(u"scaleLabel")
        self.scaleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.scaleLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.goBackPushButton = QPushButton(Form)
        self.goBackPushButton.setObjectName(u"goBackPushButton")

        self.verticalLayout_5.addWidget(self.goBackPushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.filterLabel.setText(QCoreApplication.translate("Form", u"filter: ", None))
        self.currentItemlabel.setText(QCoreApplication.translate("Form", u"current item", None))
        self.clampMaxLabel.setText(QCoreApplication.translate("Form", u"Clamp Max", None))
        self.clampMinLabel.setText(QCoreApplication.translate("Form", u"Clamp Min", None))
        self.offsetLabel.setText(QCoreApplication.translate("Form", u"Offset", None))
        self.scaleLabel.setText(QCoreApplication.translate("Form", u"Scale", None))
        self.goBackPushButton.setText(QCoreApplication.translate("Form", u"go back", None))
    # retranslateUi

