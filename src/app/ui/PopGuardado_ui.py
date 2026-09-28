# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopGuardado.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
    QSizePolicy, QWidget)
import resources_rc
import resources_rc

class Ui_PopG(object):
    def setupUi(self, PopG):
        if not PopG.objectName():
            PopG.setObjectName(u"PopG")
        PopG.resize(237, 97)
        font = QFont()
        font.setBold(False)
        PopG.setFont(font)
        self.horizontalLayout = QHBoxLayout(PopG)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(PopG)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/bombilla/images/bombilla.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(PopG)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(PopG)

        QMetaObject.connectSlotsByName(PopG)
    # setupUi

    def retranslateUi(self, PopG):
        PopG.setWindowTitle(QCoreApplication.translate("PopG", u"Guardado", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("PopG", u"Registro Guardado", None))
    # retranslateUi

