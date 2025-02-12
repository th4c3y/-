from newui import Ui_Newui
from ziui import Ui_iii
import sys
import keyboard
import pyperclip
import time
import re
import os
import pathlib
from l_ima import set_clipboard, image_clipboard
from kycompulsion import text_compulsion
from pdf_to_img import pdf_to_image
from functools import partial
import configparser
import keyboard_2
from collections import deque
from PySide6 import QtWidgets
from PySide6.QtCore import QEvent, QThread, Signal, Slot, QPoint, QMutex
from PySide6.QtCore import QTimer, Qt  
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QFileDialog, QMessageBox, QStyleFactory
from PySide6.QtGui import QAction, QKeyEvent, QIcon, QColor, QIntValidator, QBrush, QMouseEvent

class HotkeyCopyThread(QThread):
    hide_signal = Signal()
    def __init__(self, parent):
        super(HotkeyCopyThread, self).__init__(parent)
        self.parent_instance = parent  # 保存父对象的引用
    def run(self):
        if self.parent_instance:  # 使用保存的引用
            self.parent_instance.hotkey_copy()
        print("执行了一次复制热键")
        self.hide_signal.emit()

class HotkeyStickThread(QThread):
    stick_signal = Signal()
    def __init__(self, parent):
        super(HotkeyStickThread, self).__init__(parent)
        self.parent_instance = parent        
    def run(self):
        if self.parent_instance:            
            self.parent_instance.hotkey_stick()
        self.stick_signal.emit()

class Worker(QThread):
    time_signal = Signal(str)
    error_signal = Signal(str)
    def __init__(self, save_function):
        super().__init__()
        self.save_function = save_function
    def run(self):
        try:
            self.save_function()  # 在子线程中执行长时间运行的保存操作
        except Exception as e:
            self.error_signal.emit("文本保存路径可能不存在或者被占用，无法定时保存")
        self.time_signal.emit(str)

class Clearkey(QThread):
    def __init__(self, parent):
        super(Clearkey, self).__init__(parent)
    def run(self):
        keyboard_2.Shortcut.health_check()
    def stop(self):
        keyboard_2.Shortcut.stop_check()  # 请求停止


class UiNewui(QWidget):
    data_changed = Signal(list)
    click_signal = Signal(str)
    icon_signal = Signal(str)
    def __init__(self):
        super(UiNewui, self).__init__()
        self.ui = Ui_Newui()
        self.ui_win = self.windowFlags()
        self.ui.setupUi(self)
        self.zsub = SubWindow(self)
        self.load_config()  # 启动时加载配置
        # 识别按键设置事件过滤器
        self.ui.lineEdit.installEventFilter(self)
        self.ui.lineEdit_2.installEventFilter(self)
        
        # 创建表头标签
        headers = ['复制的文本']
        # 设置水平表头标签
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget.itemChanged.connect(self.on_item_changed)
        self.ui.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidget.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.tableWidget.setSortingEnabled(False)  # 禁止排序

        self.clipboard_queue = deque()
        self.timer = QTimer()
        self.current_icon_index = 0
        self.queue_index = 0  # 新增一个索引来跟踪当前要获取的元素位置
        self.options = '' 
        self.worker = None 
        self.row_id = 0 
        self.current_page = 1
        self.items_per_page = 10   
        self.menu_option = False
        self.mutex = QMutex()  # 初始化互斥锁

        self.state = False
        self.ui.pushButton.clicked.connect(self.toggle_hotkey)
        self.ui.pushButton_5.clicked.connect(self.openFileDialog)
        self.ui.pushButton_8.clicked.connect(self.imageFileDialog)
        self.ui.pushButton_6.clicked.connect(self.load_txt)  # 加载文件
        self.ui.pushButton_7.clicked.connect(self.openfolder)
        self.ui.pushButton_4.clicked.connect(self.txt_config)
        self.ui.down_button.clicked.connect(self.down_data)

        self.copyThread = HotkeyCopyThread(self)  # 创建线程实例
        self.copyThread.hide_signal.connect(self.main_thread)
        self.stickThread = HotkeyStickThread(self)
        self.stickThread.stick_signal.connect(self.main_thread)
        self.clear_key = Clearkey(self)

        self.ledit = self.ui.comboBox.lineEdit()
        self.ledit.setAlignment(Qt.AlignmentFlag.AlignCenter)  #文本对齐方式设置为居中对齐
        self.ui.comboBox.currentIndexChanged.connect(self.split_list)  # 提取选项框中选中的选项

        self.ui.horizontalSlider.valueChanged.connect(self.opacity)  # 窗口透明度信号

        self.ui.page_input.returnPressed.connect(self.jump_to_page)  # 回车时触发

        self.ui.toolButton_4.clicked.connect(self.show_small_window)
        self.ui.toolButton_3.clicked.connect(partial(self.change_image_3, 'button'))  # 循环按钮连接点击信号
        self.ui.toolButton_2.clicked.connect(self.clear_queue)  # 清除按钮连接点击信号
        self.ui.toolButton.clicked.connect(self.delete_selected)  # 删除按钮连接点击信号
        self.ui.toolButton_up.clicked.connect(self.previous_page)
        self.ui.toolButton_down.clicked.connect(self.next_page)
        self.ui.toolButton_switch.clicked.connect(self.table_text)
        self.ui.toolButton_hide.clicked.connect(self.win_hide)

        self.ui.checkBox_3.stateChanged.connect(self.checkbox_state_changed)
        self.ui.checkBox_4.stateChanged.connect(self.checkbox_state_changed)
        self.previous_state = self.ui.checkBox_2.checkState() 
        self.ui.checkBox_2.stateChanged.connect(self.multiselect_changed)
        self.ui.schedule_checkBox.stateChanged.connect(self.time_val_changed)

        self.ui.time_Val.valueChanged.connect(self.time_val_changed)

        self.zsub.clear_signal.connect(self.ui.tableWidget.clearContents)
        self.zsub.clear_signal.connect(self.clear_queue)
        self.zsub.row_signal.connect(self.row_index)

        self.zsub.lock_signal.connect(partial(self.change_image_3, 'zsub'))
        self.default()   #加载配置
        self.timer.timeout.connect(self.save_data_thread)  # 连接超时信号到保存数据的方法
        self.time_save()

    def time_val_changed(self):
        if self.timer.isActive():
            self.timer.stop()
        self.time_save()

    def time_save(self):
        if self.ui.schedule_checkBox.isChecked():  
            value = self.ui.time_Val.value()*60000  # 获取用户输入的时间值
            self.timer.start(value)  # 启动计时器，时间单位毫秒
    def save_data_thread(self):
        if self.worker is None or not self.worker.isRunning():
            self.worker = Worker(self.save_data)  # 创建工作线程
            self.worker.time_signal.connect(self.time_save)
            self.worker.error_signal.connect(self.show_error_message)  # 连接信号
            self.worker.start()  # 开始线程

    def default(self):   # 加载配置文件
        self.hotkey1 = self.config.get('Hotkeys', 'Hotkey1', fallback='F9')
        self.hotkey2 = self.config.get('Hotkeys', 'Hotkey2', fallback='F10')
        self.checkbox_state = Qt.CheckState.Checked if self.config.getboolean('Settings', 'CheckboxState', fallback=True) \
            else Qt.CheckState.Unchecked
        self.order = Qt.CheckState.Checked if self.config.getboolean('Settings', 'CheckboxSeq', fallback=False) \
            else Qt.CheckState.Unchecked
        self.window_hide = Qt.CheckState.Checked if self.config.getboolean('Settings', 'CheckboxSo', fallback=False) \
            else Qt.CheckState.Unchecked
        self.window_top = Qt.CheckState.Checked if self.config.getboolean('Settings', 'CheckboxTop', fallback=False) \
            else Qt.CheckState.Unchecked
        self.checkbox_enter = Qt.CheckState.Checked if self.config.getboolean('Settings', 'CheckboxEnter', fallback=False) \
            else Qt.CheckState.Unchecked
        self.ui.lineEdit.setText(self.hotkey1)
        self.ui.lineEdit_2.setText(self.hotkey2)
        self.ui.checkBox.setCheckState(self.checkbox_state)
        self.ui.checkBox_2.setCheckState(self.order)
        self.ui.checkBox_3.setCheckState(self.window_top)
        self.ui.checkBox_4.setCheckState(self.window_hide)
        self.ui.checkBox_enter.setCheckState(self.checkbox_enter)

        self.ui.doubleSpinBox.valueChanged.connect(self.update_timeValue)
        # 设置时间值和窗口值
        timeValue = float(self.config.get('Settings', 'TimeValue', fallback='100'))   
        # 将获取到的值设置给 doubleSpinBox 控件
        self.ui.doubleSpinBox.setValue(timeValue)
        win_value = float(self.config.get('Settings','WinValue', fallback='3'))
        self.ui.doubleSpinBox_2.setValue(win_value)
        self.splitting = self.config.get('ComboBox', 'Splitting', fallback="")
        self.ui.comboBox.setCurrentText(self.splitting)
        self.split_list()

        timing_value = float(self.config.get('TxtSettings','TimingValue', fallback='10'))
        self.ui.time_Val.setValue(timing_value)
        self.folder = self.config.get('TxtSettings', 'SaveFolder', fallback='')
        self.ui.lineEdit_5.setText(self.folder)
        self.schedule_checkBox = Qt.CheckState.Checked if self.config.getboolean('TxtSettings', 'Schedule_checkBox', fallback=False) \
            else Qt.CheckState.Unchecked
        self.checkBox_exit = Qt.CheckState.Checked if self.config.getboolean('TxtSettings', 'CheckboxExit', fallback=False) \
            else Qt.CheckState.Unchecked
        self.checkBox_image = Qt.CheckState.Checked if self.config.getboolean('TxtSettings', 'CheckboxImage', fallback=False) \
            else Qt.CheckState.Unchecked
        self.checkBox_pag= Qt.CheckState.Checked if self.config.getboolean('TxtSettings', 'CheckboxPag', fallback=False) \
            else Qt.CheckState.Unchecked
        self.ui.schedule_checkBox.setCheckState(self.schedule_checkBox)
        self.ui.checkBox_5.setCheckState(self.checkBox_exit)
        self.ui.checkBox_image.setCheckState(self.checkBox_image)
        self.ui.checkBox_6.setCheckState(self.checkBox_pag)
        self.selected_option = self.config.get('TxtSettings', 'SelectedOption', fallback="Enter") 
        self.ui.comboBox_enter.setCurrentText(self.selected_option)

    def show_small_window(self):  # 显示子窗口
        self.zsub.show()

    def createtrayicon(self):   #托盘图标
        if hasattr(self, 'tray_icon') and self.tray_icon.isVisible():
            return  # 托盘图标已存在，不做任何操作
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(r":/im/WhhAlertpay.png"))  # 托盘图标
        self.tray_icon.setVisible(True)
        self.tray_icon.setToolTip("热键复制粘贴")
        show_action = QAction("打开", self)
        quit_action = QAction("退出", self)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        show_action.triggered.connect(self.clear_pressed_events)
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(app.quit)
        # 使用 lambda 函数处理 activated 信号
        self.tray_icon.activated.connect(lambda reason: self.show() if reason == QSystemTrayIcon.DoubleClick else None)

    def eventFilter(self, obj, event):    # 识别键盘
        try:
            if event.type() == QEvent.KeyPress:  # 保持为 QEvent.KeyPress
                key_event = QKeyEvent(event)
                if Qt.Key.Key_A <= key_event.key() <= Qt.Key.Key_Z:
                    modifier = key_event.modifiers()
                    key_name = None
                    if modifier == Qt.KeyboardModifier.ControlModifier:
                        if key_event.key() != Qt.Key.Key_C and key_event.key() != Qt.Key.Key_V:
                            key_name = f"Ctrl+{chr(key_event.key() - Qt.Key.Key_A + ord('A'))}"
                    elif modifier == Qt.KeyboardModifier.ShiftModifier:
                        key_name = f"Shift+{chr(key_event.key() - Qt.Key.Key_A + ord('A'))}"
                    elif modifier == Qt.KeyboardModifier.AltModifier:
                        key_name = f"Alt+{chr(key_event.key() - Qt.Key.Key_A + ord('A'))}"

                    if obj == self.ui.lineEdit:
                        self.ui.lineEdit.setText(key_name)
                    elif obj == self.ui.lineEdit_2:
                        self.ui.lineEdit_2.setText(key_name)

                elif Qt.Key.Key_F1 <= key_event.key() <= Qt.Key.Key_F12:
                    if obj == self.ui.lineEdit:
                        key_name = f"F{key_event.key() - Qt.Key.Key_F1 + 1}"
                        self.ui.lineEdit.setText(key_name)
                    elif obj == self.ui.lineEdit_2:
                        key_name = f"F{key_event.key() - Qt.Key.Key_F1 + 1}"
                        self.ui.lineEdit_2.setText(key_name)
                return True
        except Exception as e:
            print(e)
        return super().eventFilter(obj, event)

    def toggle_hotkey(self):    # 热键启动取消按钮
        if not self.state:
            self.register_hotkey()
        else:
            self.unregister_hotkey()

    def register_hotkey(self):      # 设置热键
        self.hotkey1 = self.ui.lineEdit.text()
        self.hotkey2 = self.ui.lineEdit_2.text()
        self.time_value = self.ui.doubleSpinBox.value() / 1000  # 获取数字选择框的当前值
        self.ui.lineEdit.setReadOnly(True)
        self.ui.lineEdit_2.setReadOnly(True)
        if self.hotkey1 and self.hotkey2:
            self.set_hotkey()
            self.ui.pushButton.setText("取消热键")
            self.ui.pushButton.setStyleSheet("color: red")
            self.state = True
           
            self.ui.label_5.setText(f"已设置的热键：复制热键 {self.hotkey1} ；粘贴热键 {self.hotkey2}")
            self.ui.label_6.setText(f"反应间隔时间：{self.time_value} 秒")
        self.clear_pressed_events()

    def unregister_hotkey(self):        # 取消热键
        self.ui.lineEdit.setReadOnly(False)
        self.ui.lineEdit_2.setReadOnly(False)
        keyboard.unhook_all_hotkeys()
        self.ui.pushButton.setText("应用热键")
        self.ui.pushButton.setStyleSheet("color: green")
        self.state = False
        self.ui.comboBox_2.setEnabled(True)
        self.ui.label_5.setText( "热键状态：未生效")
        self.ui.label_6.setText("反应间隔时间：未生效")
        self.clear_key.stop()
       
    def set_hotkey(self):       # 热键
        suppress_t = self.ui.comboBox_2.currentText()
        self.ui.comboBox_2.setEnabled(False)
        keyboard.add_hotkey(self.hotkey1, self.on_hotkey_pressed, suppress=suppress_t)
        keyboard.add_hotkey(self.hotkey2, self.run_hotkey_stick, suppress=suppress_t)
        keyboard.add_hotkey('windows+l', self.clear_pressed_events)
        self.clear_key.start()

    def clear_pressed_events(self):
        keyboard._pressed_events.clear()

    def on_hotkey_pressed(self):   #触发热键线程     
        self.copyThread.start()  # 启动线程，将会执行 HotkeyCopyThread 类的 run 方法，从而调用 self.hotkey_copy()

    def run_hotkey_stick(self):   
        if self.mutex.tryLock():  # 尝试加锁      
            self.stickThread.start()

    def update_timeValue(self):
        self.time_value = self.ui.doubleSpinBox.value() / 1000
        if self.state == True:
            self.ui.label_6.setText(f"反应间隔时间：{self.time_value} 秒")

    def main_thread(self):  #子线程结束返回函数，GUI后续操作
        message = ''
        len_queue = len(self.clipboard_queue)
        value = self.ui.doubleSpinBox_2.value()*1000
        sender = self.sender()
        if sender == self.copyThread:
            self.table_text()
            message = f"已复制 {len_queue} 个值"
        elif sender == self.stickThread:
            message = f"剩余 {len_queue} 个值"
            order = self.ui.checkBox_2.checkState() #倒序
            if order == Qt.CheckState.Checked:
                if self.ui.checkBox_6.isChecked():
                    self.current_page = (len_queue-1+self.queue_index) // self.items_per_page+1               
                page_row = len_queue+self.queue_index-(self.current_page-1)*self.items_per_page-1
                self.row_id = len_queue+self.queue_index        
            else:
                if self.ui.checkBox_6.isChecked():
                    remainder = self.queue_index % self.items_per_page
                    self.current_page = (self.queue_index - remainder) // self.items_per_page+1
                page_row = self.queue_index-(self.current_page-1)*self.items_per_page
                self.row_id = self.queue_index
            self.table_text()  
            item = self.ui.tableWidget.item(page_row, 0)
            if item:
                self.ui.tableWidget.scrollToItem(item, QAbstractItemView.PositionAtTop)
                item.setBackground(QColor("#F2FFE8"))
        self.ui.label_7.setText( message)
        win_hide = self.ui.checkBox_4.checkState()  # 隐藏窗口
        win_top = self.ui.checkBox_3.checkState() # 前置窗口
        checkbox_small_window = self.ui.checkBox_1.checkState() # 小窗口
        if win_hide == Qt.CheckState.Checked:
            self.win_hide()
            if checkbox_small_window == Qt.CheckState.Checked:
                self.zsub.show()
                QTimer.singleShot(value, self.zsub.hide)
        elif win_top == Qt.CheckState.Checked:
            # 如果选中了置顶复选框，则设置窗口为顶层
            flags = self.windowFlags()
            self.setWindowFlags(flags | Qt.WindowStaysOnTopHint)
            self.setFocusPolicy(Qt.NoFocus)  # 禁止获取焦点
            self.show()
        else:
            # 如果都未选中，则恢复默认窗口属性
            flags = self.ui_win
            self.setWindowFlags(flags)
            self.show()


    def hotkey_copy(self):   # 热键复制
        # 清空剪贴板
        pyperclip.copy('')
        # 模拟按下和释放Ctrl键和C键
        keyboard.press_and_release('ctrl+c')
       # 记录开始时间，用于判断是否超时
        start_time = time.time()
        while True:
            current_time = time.time()
            if current_time - start_time > self.time_value + 0.01:
                break
            text = pyperclip.paste()
            if text:
                break
            time.sleep(0.01)  # 每次检查间隔0.01秒，可根据实际情况调整
        if text:
            if not self.options:
                lines = [text]
                lines = [line.strip() for line in lines]
            elif self.options == "换行符":
                # 使用 splitlines() 方法按行拆分并组成列表
                lines = [line.strip() for line in text.splitlines() if line.strip()]
            else:
                lines = re.split(self.options, text)
                # 去除每行的前后空白字符（包括换行符），并过滤掉空行
                lines = [line.strip() for line in lines if line.strip()]
            checkbox_state = self.ui.checkBox.checkState()
            if checkbox_state == Qt.CheckState.Checked:
                # 使用一个集合来记录已经见过的行，以去除重复值
                seen = set()
                new_lines = []
                for line in lines:
                    if line not in seen:
                        new_lines.append(line)
                        seen.add(line)
                self.clipboard_queue.extend(new_lines)
            else:
                self.clipboard_queue.extend(lines)
            
    def hotkey_stick(self):     # 热键粘贴
        start_time = time.time()
        if self.clipboard_queue:
            while True:
                order = self.ui.checkBox_2.checkState()
                if self.current_icon_index == 0:          #是否从中间取值
                    if order == Qt.CheckState.Checked:   #是否倒序
                        text_to_paste = self.clipboard_queue.pop()  # 从队列的右侧取出并移除一个元素
                        self.queue_index = 0
                    else:
                        if self.queue_index == 0:        #索引判断
                            text_to_paste = self.clipboard_queue.popleft() # 从队列的左侧取出并移除一个元素
                        elif 0 < self.queue_index < len(self.clipboard_queue):   #是否超出索引
                            text_to_paste = self.clipboard_queue[self.queue_index]
                            del self.clipboard_queue[self.queue_index]
                        else:
                            text_to_paste = ''
                elif self.current_icon_index == 1:                   
                    if order == Qt.CheckState.Checked: #是否倒序   
                        text_to_paste = self.clipboard_queue[self.queue_index - 1]
                        self.queue_index -= 1  # 索引递减
                    else:
                        text_to_paste = self.clipboard_queue[self.queue_index]
                        if self.menu_option == False:   #没有单值循环
                            self.queue_index += 1  # 索引递增
                    if abs(self.queue_index) >= len(self.clipboard_queue):  # 当索引超出队列长度时，重置索引
                        self.queue_index = 0
                if text_to_paste:
                    break
                current_time = time.time()
                if current_time - start_time > self.time_value + 0.02:  # 这里设置超时时间，可根据实际情况调整
                    break
                time.sleep(0.01)  # 每次检查间隔设为0.01秒，可按需调整
            if text_to_paste:
                force_check = self.ui.checkBox_force.isChecked()
                image_check = self.ui.checkBox_image.isChecked()
                if not force_check:
                    if image_check:
                        # 判断是否为图片路径
                        file_path = pathlib.Path(text_to_paste)
                        if file_path.is_file():
                            if file_path.suffix in ['.jpg', '.png', '.gif', '.bmp']:
                                set_clipboard(str(text_to_paste))
                                keyboard.press_and_release('ctrl+v')
                            elif file_path.suffix in ['.pdf']:
                                image_path = pdf_to_image(str(text_to_paste))
                                if image_path:
                                    index = 0
                                    image_path_length = len(image_path)
                                    while index < image_path_length:
                                        path = image_path[index]   
                                        success = False                                                                                                                     
                                        while not success:
                                            success = image_clipboard(path)                         
                                            time.sleep(0.1)   
                                        time.sleep(0.02)                                       
                                        keyboard.press_and_release('ctrl+v')
                                        time.sleep(self.time_value)
                                        index += 1
                        else:
                            self.clipboard_text(text_to_paste, start_time)
                            keyboard.press_and_release('ctrl+v')
                    else:
                        self.clipboard_text(text_to_paste, start_time)
                        keyboard.press_and_release('ctrl+v')
                    
                    time.sleep(self.time_value)
                    if self.ui.checkBox_enter.isChecked():
                        set_enter = self.ui.comboBox_enter.currentText()
                        keyboard.press_and_release(set_enter)
                        time.sleep(0.02)
                else:
                    text_compulsion(text_to_paste) # 强制粘贴
        self.mutex.unlock()

    def clipboard_text(self, text, start_time):
        while True:
            pyperclip.copy(text)
            current_clipboard_text = pyperclip.paste()
            if current_clipboard_text == text:
                break
            current_time = time.time()
            if current_time - start_time > 0.03 + self.time_value:
                break
            time.sleep(0.01)

                
    def split_list(self):    #分隔符处理
        spl_var = self.ui.comboBox.currentText()
        option_dict = {
            "": "",
            "换行符": "换行符",
            ";或；": "[;；]+",
            "|": "\|+",
            "空格": "\s+"
        }
        if spl_var in option_dict:
            self.options = option_dict[spl_var]
        else:
            self.options = spl_var

    def show_context_menu(self, position):   # 右键菜单
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu{
                background:rgba(255,241,219,0.9);
                border:none;
                }
            QMenu:item{
                padding:8px 15px;  /* 菜单项内边距，增大点击区域 */
                color:rgba(51,51,51,1);
                font-size:11px;
                }
            QMenu:item:hover{
                background-color:#409CE1;  /* 当鼠标悬停在菜单项上时，背景颜色变为 */
                }
            QMenu:item:selected{
                background-color:#409CE1;
                }
        """)
        option1 = menu.addAction("从此处往下顺序粘贴")
        if self.current_icon_index == 1:
            option3 = menu.addAction("循环粘贴此项")
        option2 = menu.addAction("取消")
        action = menu.exec(self.ui.tableWidget.mapToGlobal(position))
        try:
            if action == option1:
                row = self.ui.tableWidget.indexAt(position).row()  # 获取右键点击的行索引
                self.row_index(row)
            elif action == option2:
                try:
                    self.queue_index = 0
                    self.menu_option = False
                    self.ui.checkBox_2.setDisabled(False)
                    self.item.setBackground(QBrush())
                except Exception as e:
                    pass
            elif action == option3:
                row = self.ui.tableWidget.indexAt(position).row()  # 获取右键点击的行索引
                self.row_index(row)
                self.menu_option = True
        except UnboundLocalError:
            pass

    def clear_colors(self):
        """
        清空整个表格的颜色
        """
        row_count = self.ui.tableWidget.rowCount()
        col_count = self.ui.tableWidget.columnCount()
        for row in range(row_count):
            for col in range(col_count):
                item = self.ui.tableWidget.item(row, col)
                if item:
                    item.setBackground(QColor("white"))  # 将颜色设置为白色，可根据需求换为默认颜色       

    def row_index(self, row):
        self.queue_index = row+ (self.current_page-1)*self.items_per_page
        self.ui.checkBox_2.setDisabled(True)
        self.ui.checkBox_2.setChecked(False)
        self.item = self.ui.tableWidget.item(row, 0)
        if self.item:
            self.clear_colors()
            self.item.setBackground(QColor("#b9dec9"))

    def table_text(self):    # 数据加载到页面
        self.ui.tableWidget.clearContents()
        data = self.clipboard_queue
        self.len_data = len(data)       
        if not self.ui.checkBox_6.isChecked():
            self.long_table(data)   
        else:
            self.paging(data)
        self.data_changed.emit(data)

    def long_table(self,data):
        self.ui.label_page.setText('')
        self.ui.toolButton_up.setDisabled(True)
        self.ui.toolButton_down.setDisabled(True)
        self.current_page = 1
        self.ui.tableWidget.setRowCount(10)
        old_row = self.ui.tableWidget.rowCount()
        # 如果当前行数超过了表格的原有行数，增加行数
        if self.len_data > old_row:
            self.ui.tableWidget.setRowCount(self.len_data)
        for row_index in range(self.len_data):
            # 填充第队列值
            value = data[row_index]
            item_2 = QTableWidgetItem(str(value))
            self.ui.tableWidget.setItem(row_index, 0, item_2)
        # 检查是否有多余的空白行，且表格行数超过原有行数，如果有，删除
        if self.ui.tableWidget.rowCount() > 10:
            while self.ui.tableWidget.rowCount() > self.len_data:
                self.ui.tableWidget.removeRow(self.ui.tableWidget.rowCount() - 1)
        self.ui.page_input.setReadOnly(True)

    def paging(self,data):
        # 计算当前页数据的起始索引和结束索引
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = min(start_index + self.items_per_page, self.len_data)
        # if self.ui.tableWidget.rowCount()<10:
        #     # 清空表格现有内容
        #     self.ui.tableWidget.setRowCount(10-self.ui.tableWidget.rowCount())  
        self.ui.tableWidget.setRowCount(10)
        # 循环填充当前页的数据到表格中
        for row_index in range(start_index, end_index):
            # 填充第一列的值
            value_1 = data[row_index]
            item_1 = QTableWidgetItem(str(value_1))
            self.ui.tableWidget.setItem(row_index-start_index, 0, item_1)
        self.ui.toolButton_up.setEnabled(self.current_page > 1)
        self.ui.toolButton_down.setEnabled(end_index < self.len_data)
        self.update_page()

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.table_text()  # 刷新表格

    def next_page(self):
        total_pages = (self.len_data + self.items_per_page - 1) // self.items_per_page
        if self.current_page < total_pages:
            self.current_page += 1
            self.table_text()

        # 更新页码标签显示内容的方法
    def update_page(self):
        """
        计算并更新页码标签的显示，显示当前页码和总页码
        """
        total_pages = (self.len_data + self.items_per_page - 1) // self.items_per_page
        self.ui.label_page.setText(f"{self.current_page}/{total_pages}")
        self.ui.page_input.setReadOnly(False)
        validator = QIntValidator(1, total_pages)
        self.ui.page_input.setValidator(validator)


    def jump_to_page(self):  
        """
        此方法用于处理输入页面数并实现跳转
        """
        number_str = self.ui.page_input.text()  # 获取输入框中的页面数        
        page_number = int(number_str)
        total_pages = (self.len_data + self.items_per_page - 1) // self.items_per_page
        if 1 <= page_number <= total_pages:
            self.current_page = page_number
            self.table_text()
            self.update_page()
        self.ui.page_input.clear()  # 清空输入框内容

    def opacity(self, value):   # 窗口透明度调整
        opacity = 1 - float(value) / 180  # 计算透明度
        self.setWindowOpacity(opacity)  # 设置窗口透明度
        self.zsub.setWindowOpacity(opacity)

    def change_image_3(self, source, *args, **kwargs):    # 循环文本
        icon3 = QIcon()
        icon4 = QIcon()
        icon3.addFile(u":/im/UimLockOpenAlt.png")
        icon4.addFile(u":/im/BxsLock.png")
        if self.current_icon_index == 0:
            self.ui.toolButton_3.setIcon(icon4)  # 更换后的图片
            self.current_icon_index = 1
            self.ui.label_7.setText("循环已开启")
        else:
            self.ui.toolButton_3.setIcon(icon3)  # 换回原始图片
            self.current_icon_index = 0
            self.ui.label_7.setText("循环已关闭")
        if source == 'button':
            self.icon_signal.emit(str)

    def checkbox_state_changed(self, state):   #多选互斥
        sender = self.sender()
        if sender == self.ui.checkBox_3:
            if state == 2:
                self.ui.checkBox_4.setChecked(False)
        elif sender == self.ui.checkBox_4:
            if state == 2:
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_1.setEnabled(True)
                self.ui.checkBox_1.setChecked(True)
            else:
                self.ui.checkBox_1.setEnabled(False)
                self.ui.checkBox_1.setChecked(False)

    def clear_queue(self):    # 点击button_2清空
        # 清空队列
        self.clipboard_queue.clear()
        self.ui.tableWidget.setRowCount(10)
        self.ui.label_page.setText('')
        self.ui.toolButton_up.setDisabled(True)
        self.ui.toolButton_down.setDisabled(True)
        self.current_page = 1
        self.queue_index = 0
        self.click_signal.emit(str)
        self.ui.label_7.setText("清除文本")


    def delete_selected(self):   # 删除按钮
        # 获取选中的行
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        try:
            # 从后向前删除，这样就不会影响到前面的索引
            for index in sorted(selected_rows, reverse=True):
                # 从表格中删除行
                self.ui.tableWidget.removeRow(index.row())
                # 从数据列表中删除对应的数据
                del self.clipboard_queue[index.row()+(self.current_page-1)*self.items_per_page]
            # 发送数据已更改的信号
            self.data_changed.emit(self.clipboard_queue)
            # 在表格末尾添加新行
            for _ in range(len(selected_rows)):
                self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            self.table_text()
        except Exception as e:
            pass

    def load_config(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')  # 读取配置文件

    def save_config(self):
        # 保存热键设置
        self.config['Hotkeys'] = {
            'Hotkey1': self.ui.lineEdit.text(),
            'Hotkey2': self.ui.lineEdit_2.text()
        }
        # 保存选项
        self.config['ComboBox'] = {
            'Options': ', '.join([self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())]),  # 将选项以逗号分隔的字符串保存
            'Splitting': self.ui.comboBox.currentText()
        }
        # 保存时间间隔设置
        self.config['Settings'] = {
            'CheckboxState': str(int(self.ui.checkBox.checkState() == Qt.CheckState.Checked)),
            'CheckboxSo': str(int(self.ui.checkBox_4.checkState() == Qt.CheckState.Checked)),
            'CheckboxTop': str(int(self.ui.checkBox_3.checkState() == Qt.CheckState.Checked)),
            'CheckboxSeq': str(int(self.ui.checkBox_2.checkState() == Qt.CheckState.Checked)),
            'CheckboxEnter': str(int(self.ui.checkBox_enter.checkState() == Qt.CheckState.Checked)),
            'TimeValue': self.ui.doubleSpinBox.value(),
            'WinValue': self.ui.doubleSpinBox_2.value()
        }
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def txt_config(self):
        # 确保 "TxtSettings" 段存在
        if not self.config.has_section('TxtSettings'):
            self.config.add_section('TxtSettings')
        
        # 直接更新字段值，如果字段存在将会替换旧值，否则添加新字段
        self.config.set('TxtSettings', 'Schedule_checkBox',
                        str(int(self.ui.schedule_checkBox.checkState() == Qt.CheckState.Checked)))
        self.config.set('TxtSettings', 'CheckboxExit',
                        str(int(self.ui.checkBox_5.checkState() == Qt.CheckState.Checked)))
        self.config.set('TxtSettings', 'SaveFolder', self.ui.lineEdit_5.text())
        # 如果需要处理 "OpenFile"
        # self.config.set('TxtSettings', 'OpenFile', self.ui.lineEdit_4.text())
        self.config.set('TxtSettings', 'TimingValue', str(self.ui.time_Val.value()))

        self.config.set('TxtSettings', 'CheckboxImage',
                        str(int(self.ui.checkBox_image.checkState() == Qt.CheckState.Checked)))
        self.config.set('TxtSettings', 'CheckboxPag',
                        str(int(self.ui.checkBox_6.checkState() == Qt.CheckState.Checked)))
        self.config.set('TxtSettings', 'SelectedOption', self.ui.comboBox_enter.currentText() )
        # 写入文件前，覆盖以替换
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def down_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        defaultFileName = "data.txt"
        fileName, _ = QFileDialog.getSaveFileName(self, "导出文本", defaultFileName, "Text Files (*.txt)", options=options)
        # print(fileName)
        self.save_data(fileName)

    def save_data(self, file_path=None):   # 保存文本
        # 检查 clipboard_queue 是否有值
        if self.clipboard_queue:
            if not file_path:
                file_path = os.path.join(self.folder, "data.txt")
            with open(file_path, 'w') as f:
                for line in self.clipboard_queue:
                    f.write(str(line) + '\n')

    def show_error_message(self, error_message):   #提示信息
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("提示")
        msg_box.setText(error_message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.show()
        timer = QTimer(msg_box)
        timer.timeout.connect(msg_box.close)
        timer.start(5000)  # 5 秒后自动关闭

    def closeEvent(self, event):
        self.save_config()  # 保存配置
        event.accept()
        if self.ui.checkBox_5.isChecked():
            # 在关闭程序时保存 clipboard_queue 的值
            self.save_data()
            event.accept()       
        self.show_error_message("程序正在退出...")
        QApplication.processEvents()  # 处理事件，确保消息框显示
        self.clear_key.stop()
        self.clear_key.wait()

    def openFileDialog(self):
        # 弹出文件选择对话框，并获取选定文件的路径
        self.filepath, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'Text files (*.txt)')
        if self.filepath:
            self.ui.lineEdit_4.setText(self.filepath)
    def imageFileDialog(self):
        # 弹出文件选择对话框，并获取选定文件的路径
        self.imagepath, _ = QFileDialog.getOpenFileNames(self, '选择图片或PDF', '', 'Image files (*.png *.jpg *.bmp *.gif *.pdf)')
        if self.imagepath:
            self.clipboard_queue.extend(self.imagepath)
            self.table_text()
            self.ui.label_7.setText("文件路径已导入")
    def openfolder(self):
        # 弹出文件夹选择对话框
        self.folder = QFileDialog.getExistingDirectory(self, '存放路径选择', '')
        if self.folder:
            self.ui.lineEdit_5.setText(self.folder)
    def load_txt(self):
        try:
            # 如果用户选择了文件，则加载文本到deque并显示
            if self.filepath:
                self.loadTextToDeque(self.filepath)
        except Exception as e:
            pass
    def loadTextToDeque(self, filepath):
        # 打开文件并读取内容
        with open(filepath, 'r') as file:
            for line in file:
                # 移除每行末尾的换行符，并添加到 deque
                self.clipboard_queue.append(line.rstrip('\n'))
        self.table_text()
        self.ui.label_7.setText("文本已导入")

    def on_item_changed(self, item):
        row = item.row()
        new_value = item.text()
        if new_value:
            if not self.ui.checkBox_6.isChecked():
                self.clipboard_queue[row] = new_value
            else:
                self.clipboard_queue[(self.current_page-1)*self.items_per_page+row] = new_value
            self.data_changed.emit(self.clipboard_queue)

    @Slot(int)
    def multiselect_changed(self, state):
        if state!= self.previous_state:  # 比较当前状态和之前的状态
            self.queue_index = 0
            self.previous_state = state

    def win_hide(self):  # 隐藏主窗口
        self.createtrayicon()  # 创建托盘图标
        self.hide()

    def mouseDoubleClickEvent(self, event):
        """
        处理鼠标双击事件
        当鼠标左键双击时，调用自定义的处理函数
        """
        if event.button() == Qt.LeftButton:  # 仅处理左键双击事件
            self.clear_pressed_events()  # 调用自定义函数
            event.accept()  # 接受事件，表示事件已被处理

    def dragEnterEvent(self, event):
        # 如果拖放的 MIME 数据包含 URL（通常是文件路径）
        if event.mimeData().hasUrls():
            # 接受拖放事件
            event.accept()
        else:
            # 否则忽略拖放事件
            event.ignore()

    def dropEvent(self, event):
        # 遍历拖放的 URL 列表
        for url in event.mimeData().urls():
            # 获取 URL 对应的本地文件路径
            file_path = url.toLocalFile()
            self.clipboard_queue.append(file_path)
        self.table_text()

class SubWindow(QWidget):
    clear_signal = Signal(str)
    lock_signal = Signal(str)
    row_signal = Signal(int)
    def __init__(self, parents=None):
        super(SubWindow, self).__init__()
        self.parent_instance = parents  # 保存主窗口实例
        self.originalFlags = self.windowFlags()
        self.setAttribute(Qt.WA_QuitOnClose, False)
        self.setAttribute(Qt.WA_ShowWithoutActivating)  # 设置显示时不激活
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)# 设置窗口置顶且无边框
        self.sub = Ui_iii()  # 创建子窗口实例
        self.sub.setupUi(self)
        self.setStyle(QtWidgets.QStyleFactory.create("Windows11"))
        self.load_position()  # 加载窗口位置
        self.startPos = None  # 鼠标点击时的起始位置
        # self.move(1, 1)
        # 创建表头标签
        headers = ['复制的文本']
        # 设置水平表头标签
        self.sub.bbg.setHorizontalHeaderLabels(headers)
        self.click_icon = 0
        # 连接主窗口的信号
        self.parent_instance.data_changed.connect(self.sync_data)
        self.parent_instance.click_signal.connect(self.sub.bbg.clearContents)
        self.parent_instance.icon_signal.connect(partial(self.lock_data, 'zsub'))
        self.sub.toolButton_4.clicked.connect(self.set_win)
        self.sub.toolButton_3.clicked.connect(self.clear_data)
        self.sub.toolButton_3.clicked.connect(self.sub.bbg.clearContents)
        self.sub.toolButton.clicked.connect(partial(self.lock_data, 'button'))
        self.sub.go_win.clicked.connect(self.go_win)
        self.sub.bbg.doubleClicked.connect(self.on_double_click)
    def sync_data(self, data):
        self.sub.bbg.clearContents()
        column_index = 0  # 第一列的索引
        num_values = len(data)
        for row_index in range(num_values):
            # 如果当前行数超过了表格的原有行数，增加行数
            if row_index >= self.sub.bbg.rowCount():
                self.sub.bbg.insertRow(row_index)
            # 填充队列值
            value = data[row_index]
            item_2 = QTableWidgetItem(str(value))
            self.sub.bbg.setItem(row_index, column_index, item_2)
        # 检查是否有多余的空白行，且表格行数超过原有行数，如果有，删除       
        while self.sub.bbg.rowCount() > num_values and self.sub.bbg.rowCount() > 13:
            self.sub.bbg.removeRow(self.sub.bbg.rowCount() - 1)
        item = self.sub.bbg.item(self.parent_instance.row_id, column_index)
        if item is not None:
            self.sub.bbg.scrollToItem(item, QAbstractItemView.PositionAtTop)
            item.setBackground(QBrush(QColor("#F2FFE8")))
        self.sub.label.setText("剩余文本： {0}".format(num_values))

    def set_win(self):
        # 恢复原始的窗口标志，显示窗口边框
        self.setWindowFlags(self.originalFlags)
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)
        self.show()

    def clear_data(self):
        self.clear_signal.emit(str)

    def lock_data(self, source, *args, **kwargs):
        icon3 = QIcon()
        icon4 = QIcon()
        icon3.addFile(u":/im/UimLockOpenAlt.png")
        icon4.addFile(u":/im/BxsLock.png")
        if self.click_icon == 0:
            self.sub.toolButton.setIcon(icon4)  # 更换后的图片
            self.click_icon = 1
        else:
            self.sub.toolButton.setIcon(icon3)  # 换回原始图片
            self.click_icon = 0
        if source == 'button':
            self.lock_signal.emit(str)

    def go_win(self):   # 显示主窗口
        if not self.parent_instance.isVisible():
            self.parent_instance.show()
    
    def on_double_click(self, index):
        row = index.row()
        self.row_signal.emit(row)
        self.sub.label.setText("从第{0}行开始粘贴".format(row+1))

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.startPos = event.globalPosition().toPoint() - self.pos()  # 更新起始位置

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton and self.startPos is not None:
            self.move(event.globalPosition().toPoint() - self.startPos)  # 根据鼠标的移动更新窗口位置
            self.startPos = event.globalPosition().toPoint() - self.pos()  # 更新起始位置

    def closeEvent(self, event):
        self.save_position()  # 保存窗口位置
        super(SubWindow, self).closeEvent(event)

    def save_position(self):
        position = self.frameGeometry().topLeft()
        config = configparser.ConfigParser()
        config.read('config.ini')
        if 'Window' not in config.sections():
            config.add_section('Window')
        config.set('Window', 'x', str(position.x()))
        config.set('Window', 'y', str(position.y()))
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def load_position(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        if 'Window' in config.sections():
            x = config.getint('Window', 'x', fallback=1)
            y = config.getint('Window', 'y', fallback=1)
            self.move(QPoint(x, y))


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        app.setStyle(QStyleFactory.create("Fusion"))
        Guiii = UiNewui()
        Guiii.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"发生错误: {e}") 