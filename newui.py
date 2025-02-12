# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import newpo_rc

class Ui_Newui(object):
    def setupUi(self, Newui):
        if not Newui.objectName():
            Newui.setObjectName(u"Newui")
        Newui.resize(542, 392)
        Newui.setMaximumSize(QSize(542, 392))
        Newui.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/im/WhhAlertpay.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Newui.setWindowIcon(icon)
        self.layoutWidget = QWidget(Newui)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(15, 7, 521, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))
        self.pushButton.setMaximumSize(QSize(72, 16777215))
        self.pushButton.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.horizontalLayout.addWidget(self.pushButton)

        self.line_5 = QFrame(self.layoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 31))
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(80, 25))
        font = QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(80, 25))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setMaxLength(100)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(92, 25))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"")
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(6)

        self.horizontalLayout.addWidget(self.comboBox)

        self.line_6 = QFrame(Newui)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 0, 551, 16))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget = QTabWidget(Newui)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(4, 58, 541, 311))
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setAcceptDrops(True)
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-2, -2, 511, 311))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(520, 320))
        self.frame.setAcceptDrops(False)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 261, 511, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(3, 273, 421, 31))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(371, 76, 37, 189))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.layoutWidget2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u":/im/MaterialSymbolsLightShadowMinusSharp.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(25, 25))
        self.toolButton.setAutoRaise(True)

        self.verticalLayout_6.addWidget(self.toolButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.toolButton_2 = QToolButton(self.layoutWidget2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/im/MageFileCrossFill.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QSize(25, 25))
        self.toolButton_2.setAutoRaise(True)

        self.verticalLayout_6.addWidget(self.toolButton_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.toolButton_3 = QToolButton(self.layoutWidget2)
        self.toolButton_3.setObjectName(u"toolButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/im/UimLockOpenAlt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setIconSize(QSize(25, 25))
        self.toolButton_3.setAutoRaise(True)

        self.verticalLayout_6.addWidget(self.toolButton_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.toolButton_switch = QToolButton(self.layoutWidget2)
        self.toolButton_switch.setObjectName(u"toolButton_switch")
        self.toolButton_switch.setStyleSheet(u"font: 8pt \"Microsoft YaHei UI\";")
        icon4 = QIcon()
        icon4.addFile(u":/im/FluentToggleMultiple20Filled.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_switch.setIcon(icon4)
        self.toolButton_switch.setIconSize(QSize(25, 25))
        self.toolButton_switch.setAutoRaise(True)

        self.verticalLayout_6.addWidget(self.toolButton_switch, 0, Qt.AlignmentFlag.AlignHCenter)

        self.toolButton_4 = QToolButton(self.layoutWidget2)
        self.toolButton_4.setObjectName(u"toolButton_4")
        icon5 = QIcon()
        icon5.addFile(u":/im/MdiBorderRadius.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_4.setIcon(icon5)
        self.toolButton_4.setIconSize(QSize(25, 25))
        self.toolButton_4.setAutoRaise(True)

        self.verticalLayout_6.addWidget(self.toolButton_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(1, 0, 371, 261))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setStyleSheet(u"\n"
"QTableWidget::item:selected { background-color: rgb(255, 227, 181); }\n"
"QTableWidget::item:selected { color: black; }\n"
"QTableWidget QLineEdit { color: black; }")
        self.tableWidget.setLineWidth(18)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScrollMargin(25)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(22)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setDefaultSectionSize(24)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.layoutWidget3 = QWidget(self.frame)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(374, 7, 32, 61))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 1))
        self.label_12.setMaximumSize(QSize(3, 15))
        self.label_12.setStyleSheet(u"font: 18pt \"Microsoft YaHei UI\";\n"
"color: rgb(85, 170, 127);")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.page_input = QLineEdit(self.layoutWidget3)
        self.page_input.setObjectName(u"page_input")
        self.page_input.setEnabled(True)
        self.page_input.setMinimumSize(QSize(0, 3))
        self.page_input.setStyleSheet(u"color: rgba(40, 40, 40, 150);\n"
"font: 7pt \"Microsoft YaHei UI\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.page_input.setMaxLength(2000)
        self.page_input.setCursorPosition(0)
        self.page_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_input.setDragEnabled(False)
        self.page_input.setReadOnly(True)
        self.page_input.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.page_input.setClearButtonEnabled(False)

        self.horizontalLayout_7.addWidget(self.page_input)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.label_page = QLabel(self.layoutWidget3)
        self.label_page.setObjectName(u"label_page")
        self.label_page.setStyleSheet(u"font: 7pt \"Microsoft YaHei UI\";")
        self.label_page.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_page)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.toolButton_up = QToolButton(self.layoutWidget3)
        self.toolButton_up.setObjectName(u"toolButton_up")
        self.toolButton_up.setEnabled(False)
        self.toolButton_up.setMaximumSize(QSize(14, 16777215))
        self.toolButton_up.setStyleSheet(u"")
        self.toolButton_up.setAutoRaise(True)
        self.toolButton_up.setArrowType(Qt.ArrowType.LeftArrow)

        self.horizontalLayout_6.addWidget(self.toolButton_up)

        self.toolButton_down = QToolButton(self.layoutWidget3)
        self.toolButton_down.setObjectName(u"toolButton_down")
        self.toolButton_down.setEnabled(False)
        self.toolButton_down.setMaximumSize(QSize(14, 16777215))
        self.toolButton_down.setStyleSheet(u"")
        self.toolButton_down.setAutoRaise(True)
        self.toolButton_down.setArrowType(Qt.ArrowType.RightArrow)

        self.horizontalLayout_6.addWidget(self.toolButton_down)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.layoutWidget4 = QWidget(self.frame)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(407, -1, 101, 271))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.layoutWidget4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAcceptDrops(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy3)
        self.doubleSpinBox.setMinimumSize(QSize(75, 18))
        self.doubleSpinBox.setStyleSheet(u"")
        self.doubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMaximum(99999.000000000000000)
        self.doubleSpinBox.setSingleStep(50.000000000000000)
        self.doubleSpinBox.setValue(100.000000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox = QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout.addWidget(self.checkBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout.addWidget(self.checkBox_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_enter = QCheckBox(self.groupBox_3)
        self.checkBox_enter.setObjectName(u"checkBox_enter")
        self.checkBox_enter.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout.addWidget(self.checkBox_enter, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_force = QCheckBox(self.groupBox_3)
        self.checkBox_force.setObjectName(u"checkBox_force")
        self.checkBox_force.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout.addWidget(self.checkBox_force, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_13.addLayout(self.verticalLayout)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.layoutWidget4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_1 = QCheckBox(self.groupBox_4)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(False)
        self.checkBox_1.setStyleSheet(u"font: 8pt \"Microsoft YaHei UI\";")
        self.checkBox_1.setTristate(False)

        self.verticalLayout_9.addWidget(self.checkBox_1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMinimumSize(QSize(75, 18))
        self.doubleSpinBox_2.setStyleSheet(u"")
        self.doubleSpinBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_2.setMaximum(3600.000000000000000)
        self.doubleSpinBox_2.setSingleStep(1.000000000000000)
        self.doubleSpinBox_2.setValue(3.000000000000000)

        self.verticalLayout_9.addWidget(self.doubleSpinBox_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_3 = QCheckBox(self.groupBox_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_9.addWidget(self.checkBox_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_4 = QCheckBox(self.groupBox_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_9.addWidget(self.checkBox_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSlider = QSlider(self.groupBox_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(70, 12))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_9.addWidget(self.horizontalSlider, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_14.addLayout(self.verticalLayout_9)


        self.verticalLayout_8.addWidget(self.groupBox_4)

        self.layoutWidget4.raise_()
        self.layoutWidget4.raise_()
        self.layoutWidget4.raise_()
        self.layoutWidget4.raise_()
        self.line.raise_()
        self.tableWidget.raise_()
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, 0, 521, 341))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(5, 1, 391, 179))
        self.layoutWidget5 = QWidget(self.groupBox)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(28, 98, 331, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.lineEdit_5 = QLineEdit(self.layoutWidget5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_5)

        self.pushButton_7 = QPushButton(self.layoutWidget5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.layoutWidget6 = QWidget(self.groupBox)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(29, 27, 291, 61))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.schedule_checkBox = QCheckBox(self.layoutWidget6)
        self.schedule_checkBox.setObjectName(u"schedule_checkBox")

        self.horizontalLayout_3.addWidget(self.schedule_checkBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_10 = QLabel(self.layoutWidget6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.time_Val = QDoubleSpinBox(self.layoutWidget6)
        self.time_Val.setObjectName(u"time_Val")
        self.time_Val.setMinimumSize(QSize(112, 25))
        self.time_Val.setMaximumSize(QSize(176, 16777215))
        self.time_Val.setWrapping(False)
        self.time_Val.setDecimals(0)
        self.time_Val.setMinimum(1.000000000000000)
        self.time_Val.setMaximum(360.000000000000000)
        self.time_Val.setValue(10.000000000000000)

        self.horizontalLayout_3.addWidget(self.time_Val)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.checkBox_5 = QCheckBox(self.layoutWidget6)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_4.addWidget(self.checkBox_5)

        self.down_button = QPushButton(self.groupBox)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setGeometry(QRect(280, 142, 75, 25))
        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(22, 140, 75, 25))
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(5, 182, 391, 121))
        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(168, 94, 75, 24))
        self.layoutWidget7 = QWidget(self.groupBox_2)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(24, 20, 351, 71))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.layoutWidget7)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.horizontalSpacer_3 = QSpacerItem(9, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.pushButton_8 = QPushButton(self.layoutWidget7)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_8.addWidget(self.pushButton_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.layoutWidget7)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.lineEdit_4 = QLineEdit(self.layoutWidget7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_4)

        self.pushButton_5 = QPushButton(self.layoutWidget7)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_5.addWidget(self.pushButton_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.layoutWidget8 = QWidget(self.frame_2)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(400, 130, 101, 91))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.checkBox_image = QCheckBox(self.layoutWidget8)
        self.checkBox_image.setObjectName(u"checkBox_image")

        self.horizontalLayout_12.addWidget(self.checkBox_image)

        self.label_9 = QLabel(self.layoutWidget8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.label_9)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.checkBox_6 = QCheckBox(self.layoutWidget8)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_12.addWidget(self.checkBox_6)

        self.layoutWidget9 = QWidget(self.frame_2)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(400, 10, 101, 49))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 10pt \"Myriad Pro\";\n"
"color: rgb(85, 170, 255);")

        self.verticalLayout_11.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignVCenter)

        self.comboBox_2 = QComboBox(self.layoutWidget9)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QSize(61, 25))
        self.comboBox_2.setMaximumSize(QSize(5016777, 16777215))
        self.comboBox_2.setStyleSheet(u"font: 8pt \"Microsoft YaHei UI\";")

        self.verticalLayout_11.addWidget(self.comboBox_2)

        self.layoutWidget10 = QWidget(self.frame_2)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(400, 70, 101, 47))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 9pt \"Myriad Pro\";\n"
"color: rgb(85, 170, 255);")

        self.verticalLayout_10.addWidget(self.label_15, 0, Qt.AlignmentFlag.AlignVCenter)

        self.comboBox_enter = QComboBox(self.layoutWidget10)
        self.comboBox_enter.addItem("")
        self.comboBox_enter.addItem("")
        self.comboBox_enter.addItem("")
        self.comboBox_enter.setObjectName(u"comboBox_enter")
        self.comboBox_enter.setMinimumSize(QSize(99, 25))

        self.verticalLayout_10.addWidget(self.comboBox_enter)

        self.layoutWidget4.raise_()
        self.groupBox_2.raise_()
        self.layoutWidget4.raise_()
        self.layoutWidget4.raise_()
        self.groupBox.raise_()
        icon6 = QIcon()
        icon6.addFile(u":/im/UiwDownload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_2, icon6, "")
        self.layoutWidget11 = QWidget(Newui)
        self.layoutWidget11.setObjectName(u"layoutWidget11")
        self.layoutWidget11.setGeometry(QRect(28, 367, 511, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget11)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setSizeIncrement(QSize(0, 0))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.toolButton_hide = QToolButton(self.layoutWidget11)
        self.toolButton_hide.setObjectName(u"toolButton_hide")
        self.toolButton_hide.setIcon(icon)
        self.toolButton_hide.setIconSize(QSize(16, 16))
        self.toolButton_hide.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.toolButton_hide, 0, Qt.AlignmentFlag.AlignBottom)

        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.doubleSpinBox)
        QWidget.setTabOrder(self.doubleSpinBox, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.tableWidget)

        self.retranslateUi(Newui)
        self.toolButton_2.clicked.connect(self.tableWidget.clearContents)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Newui)
    # setupUi

    def retranslateUi(self, Newui):
        Newui.setWindowTitle(QCoreApplication.translate("Newui", u"\u70ed\u952e\u590d\u5236\u7c98\u8d34", None))
        self.pushButton.setText(QCoreApplication.translate("Newui", u"\u5e94\u7528\u70ed\u952e", None))
        self.label.setText(QCoreApplication.translate("Newui", u"\u590d\u5236\u70ed\u952e", None))
        self.label_2.setText(QCoreApplication.translate("Newui", u"\u7c98\u8d34\u70ed\u952e", None))
        self.label_8.setText(QCoreApplication.translate("Newui", u"\u5206\u9694\u7b26", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("Newui", u"\u6362\u884c\u7b26", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Newui", u"\u7a7a\u683c", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Newui", u"|", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Newui", u"-", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Newui", u"\uff1b\u6216;", None))

        self.label_5.setText(QCoreApplication.translate("Newui", u"\u70ed\u952e\u72b6\u6001\uff1a\u672a\u751f\u6548", None))
        self.label_6.setText(QCoreApplication.translate("Newui", u"\u53cd\u5e94\u95f4\u9694\uff1a\u672a\u751f\u6548", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u5220\u9664\u9009\u4e2d\u6587\u672c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.toolButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.toolButton.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_2.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u6e05\u7a7a\u6587\u672c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.toolButton_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.toolButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_3.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u5faa\u73af\u4f7f\u7528\u6587\u672c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolButton_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.toolButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_switch.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u5207\u6362\u663e\u793a\u6a21\u5f0f&lt;\u6839\u636e\u5206\u9875\u6a21\u5f0f\u8bbe\u7f6e&gt;</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_switch.setText(QCoreApplication.translate("Newui", u"\u5206\u9875", None))
#if QT_CONFIG(tooltip)
        self.toolButton_4.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u6253\u5f00\u5c0f\u7a97\u53e3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolButton_4.setWhatsThis(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u6253\u5f00\u5c0f\u7a97\u53e3</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolButton_4.setText("")

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_12.setText(QCoreApplication.translate("Newui", u"\u00b7", None))
        self.page_input.setText("")
        self.label_page.setText("")
        self.toolButton_up.setText(QCoreApplication.translate("Newui", u"U", None))
        self.toolButton_down.setText(QCoreApplication.translate("Newui", u"D", None))
        self.groupBox_3.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Newui", u"\u53cd\u5e94\u95f4\u9694", None))
        self.doubleSpinBox.setSuffix(QCoreApplication.translate("Newui", u"ms", None))
        self.checkBox.setText(QCoreApplication.translate("Newui", u"\u590d\u5236\u53bb\u91cd", None))
        self.checkBox_2.setText(QCoreApplication.translate("Newui", u"\u5012\u5e8f\u7c98\u8d34", None))
#if QT_CONFIG(tooltip)
        self.checkBox_enter.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u7c98\u8d34\u5b8c\u81ea\u52a8\u8f93\u5165Enter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_enter.setText(QCoreApplication.translate("Newui", u"\u81ea\u52a8\u6362\u884c", None))
#if QT_CONFIG(tooltip)
        self.checkBox_force.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u6a21\u62df\u6807\u51c6\u952e\u76d8\u8f93\u5165\uff0c\u5982\u8f93\u5165\u6cd5\u672a\u81ea\u52a8\u5207\u6362\u82f1\u6587\u8bf7\u624b\u52a8\u5207\u6362\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_force.setText(QCoreApplication.translate("Newui", u"\u5f3a\u5236\u7c98\u8d34", None))
        self.groupBox_4.setTitle("")
        self.checkBox_1.setText(QCoreApplication.translate("Newui", u"\u5f39\u51fa\u5c0f\u7a97\u53e3", None))
        self.doubleSpinBox_2.setSuffix(QCoreApplication.translate("Newui", u"s", None))
        self.checkBox_3.setText(QCoreApplication.translate("Newui", u"\u524d\u7f6e\u7a97\u53e3", None))
        self.checkBox_4.setText(QCoreApplication.translate("Newui", u"\u9690\u85cf\u7a97\u53e3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Newui", u"\u590d\u5236\u7c98\u8d34", None))
        self.groupBox.setTitle(QCoreApplication.translate("Newui", u"\u6587\u672c\u4fdd\u5b58\u8bbe\u7f6e", None))
        self.label_13.setText(QCoreApplication.translate("Newui", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.pushButton_7.setText(QCoreApplication.translate("Newui", u"\u6d4f\u89c8", None))
        self.schedule_checkBox.setText(QCoreApplication.translate("Newui", u"\u5b9a\u65f6\u4fdd\u5b58", None))
        self.label_10.setText(QCoreApplication.translate("Newui", u"\u5b9a\u65f6", None))
#if QT_CONFIG(tooltip)
        self.time_Val.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u6bcf\u8fc7\u8bbe\u5b9a\u65f6\u95f4\u4fdd\u5b58\u4e00\u6b21\u8be5\u65f6\u70b9\u5b58\u5728\u7684\u6587\u672c\uff0c\u8986\u76d6\u4fdd\u5b58\uff0c\u53ea\u4f1a\u4fdd\u7559\u6700\u540e\u4e00\u6b21\u4fdd\u5b58\u7684\u6587\u672c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.time_Val.setSuffix(QCoreApplication.translate("Newui", u"\u5206\u949f", None))
        self.checkBox_5.setText(QCoreApplication.translate("Newui", u"\u9000\u51fa\u65f6\u4fdd\u5b58(\u6258\u76d8\u9000\u51fa\u65f6\u65e0\u6548)", None))
        self.down_button.setText(QCoreApplication.translate("Newui", u"\u5bfc\u51fa\u6587\u672c", None))
        self.pushButton_4.setText(QCoreApplication.translate("Newui", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Newui", u"\u6587\u672c\u5bfc\u5165", None))
        self.pushButton_6.setText(QCoreApplication.translate("Newui", u"\u5bfc\u5165", None))
        self.label_14.setText(QCoreApplication.translate("Newui", u"\u56fe\u7247\u6216PDF", None))
        self.pushButton_8.setText(QCoreApplication.translate("Newui", u"\u9009\u53d6\u6587\u4ef6", None))
        self.label_11.setText(QCoreApplication.translate("Newui", u"TXT\u6587\u4ef6\u8def\u5f84", None))
        self.pushButton_5.setText(QCoreApplication.translate("Newui", u"\u6d4f\u89c8", None))
        self.checkBox_image.setText("")
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p align=\"center\">\uff08jpg/png/gif/bmp/<span style=\" color:#ec6324;\">pdf</span>\uff09</p><p align=\"center\">&lt;\u5efa\u8bae\u5c0f\u56fe\u7247\uff0c\u5927\u56fe\u7247\u5f88\u6162&gt;</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Newui", u"\u5c06\u56fe\u7247(PDF)\u8def\u5f84\u8f6c\u4e3a\u56fe\u7247\u7c98\u8d34", None))
#if QT_CONFIG(tooltip)
        self.checkBox_6.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>\u8d85\u8fc7100\u6761\u6570\u636e\u63a8\u8350\u52fe\u9009\uff0c\u5206\u9875\u663e\u793a\uff0c\u63d0\u9ad8\u7a97\u53e3\u54cd\u5e94\u901f\u5ea6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_6.setText(QCoreApplication.translate("Newui", u"\u5206\u9875\u6a21\u5f0f", None))
        self.label_4.setText(QCoreApplication.translate("Newui", u"suppress", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Newui", u"Flase", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Newui", u"True", None))

        self.label_15.setText(QCoreApplication.translate("Newui", u"\u6362\u884c\u65b9\u5f0f", None))
        self.comboBox_enter.setItemText(0, QCoreApplication.translate("Newui", u"Enter", None))
        self.comboBox_enter.setItemText(1, QCoreApplication.translate("Newui", u"Ctrl+Enter", None))
        self.comboBox_enter.setItemText(2, QCoreApplication.translate("Newui", u"Tab", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Newui", u"\u6587\u672c\u8bbe\u7f6e", None))
        self.label_7.setText(QCoreApplication.translate("Newui", u"\u51c6\u5907\u5c31\u7eea", None))
#if QT_CONFIG(tooltip)
        self.toolButton_hide.setToolTip(QCoreApplication.translate("Newui", u"<html><head/><body><p>&lt;\u9690\u85cf\u5230\u6258\u76d8&gt;</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_hide.setText("")
    # retranslateUi

