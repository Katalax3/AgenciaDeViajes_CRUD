# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ingresar_Registro.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_NueReg(object):
    def setupUi(self, NueReg):
        if not NueReg.objectName():
            NueReg.setObjectName(u"NueReg")
        NueReg.resize(216, 278)
        self.verticalLayout_2 = QVBoxLayout(NueReg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.Guardar = QPushButton(NueReg)
        self.Guardar.setObjectName(u"Guardar")

        self.verticalLayout_2.addWidget(self.Guardar)


        self.retranslateUi(NueReg)

        QMetaObject.connectSlotsByName(NueReg)
    # setupUi

    def retranslateUi(self, NueReg):
        NueReg.setWindowTitle(QCoreApplication.translate("NueReg", u"Nuevo Registro", None))
        self.Guardar.setText(QCoreApplication.translate("NueReg", u"Guardar", None))
    # retranslateUi

