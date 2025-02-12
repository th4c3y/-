# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ziui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)
import newpo_rc

class Ui_iii(object):
    def setupUi(self, iii):
        if not iii.objectName():
            iii.setObjectName(u"iii")
        iii.resize(261, 318)
        icon = QIcon()
        icon.addFile(u":/im/WhhAlertpay.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        iii.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(iii)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bbg = QTableWidget(iii)
        if (self.bbg.columnCount() < 1):
            self.bbg.setColumnCount(1)
        if (self.bbg.rowCount() < 13):
            self.bbg.setRowCount(13)
        self.bbg.setObjectName(u"bbg")
        self.bbg.setStyleSheet(u"")
        self.bbg.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.bbg.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.bbg.setRowCount(13)
        self.bbg.setColumnCount(1)
        self.bbg.horizontalHeader().setCascadingSectionResizes(False)
        self.bbg.horizontalHeader().setDefaultSectionSize(102)
        self.bbg.horizontalHeader().setHighlightSections(True)
        self.bbg.horizontalHeader().setProperty("showSortIndicator", False)
        self.bbg.horizontalHeader().setStretchLastSection(True)
        self.bbg.verticalHeader().setMinimumSectionSize(18)
        self.bbg.verticalHeader().setDefaultSectionSize(18)

        self.verticalLayout.addWidget(self.bbg)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton = QToolButton(iii)
        self.toolButton.setObjectName(u"toolButton")
        icon1 = QIcon()
        icon1.addFile(u":/im/UimLockOpenAlt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setAutoRaise(False)

        self.horizontalLayout.addWidget(self.toolButton)

        self.toolButton_3 = QToolButton(iii)
        self.toolButton_3.setObjectName(u"toolButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/im/MageFileCrossFill.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setAutoRaise(False)

        self.horizontalLayout.addWidget(self.toolButton_3)

        self.toolButton_4 = QToolButton(iii)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButton_4)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.go_win = QToolButton(iii)
        self.go_win.setObjectName(u"go_win")
        self.go_win.setMaximumSize(QSize(65, 25))
        self.go_win.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(26, 167, 255);")
        self.go_win.setIconSize(QSize(12, 12))
        self.go_win.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.go_win.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.go_win)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label = QLabel(iii)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))
        self.label.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label)

        QWidget.setTabOrder(self.toolButton, self.toolButton_3)

        self.retranslateUi(iii)
        self.toolButton_3.clicked.connect(self.bbg.clearContents)

        QMetaObject.connectSlotsByName(iii)
    # setupUi

    def retranslateUi(self, iii):
        iii.setWindowTitle(QCoreApplication.translate("iii", u"\u6587\u672c\u9884\u89c8", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("iii", u"<html><head/><body><p>\u9501\u5b9a\u5faa\u73af</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolButton.setWhatsThis(QCoreApplication.translate("iii", u"<html><head/><body><p>\u9501\u5b9a\u5faa\u73af</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolButton.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_3.setToolTip(QCoreApplication.translate("iii", u"<html><head/><body><p>\u6e05\u9664\u6240\u6709</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolButton_3.setWhatsThis(QCoreApplication.translate("iii", u"<html><head/><body><p>\u6e05\u9664\u6240\u6709</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_4.setToolTip(QCoreApplication.translate("iii", u"<html><head/><body><p>\u663e\u793a\u8fb9\u6846</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolButton_4.setWhatsThis(QCoreApplication.translate("iii", u"<html><head/><body><p>\u663e\u793a\u7a97\u53e3\u8fb9\u6846</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolButton_4.setText("")
        self.go_win.setText(QCoreApplication.translate("iii", u"\u4e3b", None))
        self.label.setText("")
    # retranslateUi

