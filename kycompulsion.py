
import keyboard
import ctypes
import win32api, win32con, win32gui, re,time

def simulate_key_press(key):
    change_english()
    caps_lock_on = ctypes.windll.user32.GetKeyState(0x14) & 0xffff != 0
    if key.isupper():  # 如果是大写字母
        if not caps_lock_on: # 检测大写锁定键是否开启
            keyboard.press_and_release('caps lock')  # 按下大写锁定键
            time.sleep(0.01)
            keyboard.press(key.lower())  # 按下对应的键位
            keyboard.release(key.lower())  # 释放对应的键位
            keyboard.press_and_release('caps lock')  # 释放大写锁定键
            time.sleep(0.01)
        else:
            keyboard.press(key.lower())  # 按下对应的键位
            keyboard.release(key.lower())  # 释放对应的键位
    elif key.isdigit():  # 如果是数字
        if keyboard.is_pressed('shift'):  # 检查 Shift 是否按下
            keyboard.release('shift')
            keyboard.press('shift')
        keyboard.press(key)
        keyboard.release(key)
    elif key == '@':
        keyboard.press('shift')
        keyboard.press('2')
        keyboard.release('2')
        keyboard.release('shift')
    elif key == '#':
        keyboard.press('shift')
        keyboard.press('3')
        keyboard.release('3')
        keyboard.release('shift')
    elif key == '!' :
        keyboard.press('shift')
        keyboard.press('1')
        keyboard.release('1')
        keyboard.release('shift')
    elif key == '$' :
        keyboard.press('shift')
        keyboard.press('4')
        keyboard.release('4')
        keyboard.release('shift')
    elif key == '%':
        keyboard.press('shift')
        keyboard.press('5')
        keyboard.release('5')
        keyboard.release('shift')
    elif key == '^':
        keyboard.press('shift')
        keyboard.press('6')
        keyboard.release('6')
        keyboard.release('shift')
    elif key == '&':
        keyboard.press('shift')
        keyboard.press('7')
        keyboard.release('7')
        keyboard.release('shift')
    elif key == '~':
        keyboard.press('shift')
        keyboard.press('`')
        keyboard.release('`')
        keyboard.release('shift')
    elif key == '(' :
        keyboard.send('SHIFT+9')
    elif key == ')' :
       keyboard.send('SHIFT+0')
    elif key == '{' :
        keyboard.press('shift')
        keyboard.press('[')
        keyboard.release('[')
        keyboard.release('shift')
    elif key == '}' :
        keyboard.press('shift')
        keyboard.press(']')
        keyboard.release(']')
        keyboard.release('shift')
    elif key == ':' :
        keyboard.press('shift')
        keyboard.press(';')
        keyboard.release(';')
        keyboard.release('shift')
    elif key == '"' :
        keyboard.send('SHIFT+\"')
    elif key == '<' :
        keyboard.press('shift')
        keyboard.press(',')
        keyboard.release(',')
        keyboard.release('shift')
    elif key == '>' :
        keyboard.press('shift')
        keyboard.press('.')
        keyboard.release('.')
        keyboard.release('shift')
    elif key == '_':
        keyboard.send('SHIFT+_')
    elif key == '|':
        keyboard.send('SHIFT+\\')
    elif key == '?':
        keyboard.send('SHIFT+?')
    else:  # 如果是小写字母
        if caps_lock_on: # 检测大写锁定键是否开启
            keyboard.press_and_release('caps lock')  # 按下大写锁定键
        keyboard.press(key)
        keyboard.release(key)
    time.sleep(0.005)

def text_compulsion(copied_text):
    if copied_text:
        try:
            for char in copied_text:
                if not re.match(r'^[A-Za-z0-9\!\@\#\$\%\^\&\*\(\)\_\+\=\-\./\\\;\"\'\,\<\>\:\[\]\{\}~\|\?\"`]+$', char):
                    keyboard.write(char)
                else:
                    simulate_key_press(char)
        except Exception as e:
            print(e)

def change_english():
    try:
        IMC_GETOPENSTATUS = 0x0005 
        IMC_SETOPENSTATUS = 0x0006 
        imm32 = ctypes.WinDLL('imm32', use_last_error=True) 
        handle = win32gui.GetForegroundWindow()	# 某进程窗口句柄 
        hIME = imm32.ImmGetDefaultIMEWnd(handle)    # 获取默认输入法窗口的句柄
        status = win32api.SendMessage(hIME, win32con.WM_IME_CONTROL, IMC_GETOPENSTATUS, 0)	 # 发送消息获取当前输入法状态：0 表示英文，1 表示中文
        if status:
            print('当前中文，切换为英文') 
            win32api.SendMessage(hIME, win32con.WM_IME_CONTROL, IMC_SETOPENSTATUS, 0) # 关闭中文
        # else: 
        #     print('当前英文') 
        #     win32api.SendMessage(hIME, win32con.WM_IME_CONTROL, IMC_SETOPENSTATUS, 1)	# 开启中文
    except Exception as e:
        print(e)

# def restore_original():
#      # 获取当前窗口的句柄
#     hwnd = win32gui.GetForegroundWindow()
#     # 恢复原来的输入法
#     win32api.SendMessage(hwnd, win32con.WM_INPUTLANGCHANGEREQUEST, 0, 0)

# if __name__ == '__main__':
#     text = r'什么天禧填那么利用？￥^abcdefghijklmnopqrstuvwxyz2314789qABCDEFGHIJKLMNOPQRSTUVWXYZqqSS@!&*()$/*?,.][;]-+.=-_\~{}:<>|"`'
#     text_compulsion(text)