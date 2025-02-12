
import keyboard
# import pywinauto as pywinauto
import time
from time import time as now

class Shortcut:
    _running = True
    @classmethod
    def health_check(cls):
        cls.on_check()
        while True and cls._running:
            with keyboard._pressed_events_lock:
                if cls._is_key_overtime(keyboard._pressed_events):  # 检查按键是否超时
                    keyboard._pressed_events.clear()
            time.sleep(5)  # 每10秒检查一次

    @staticmethod
    def _is_key_overtime(pressed_events):
        for event in pressed_events.values():
            print(event.time)            
            if now() - event.time > 10:  # 如果按键事件超过10秒
                return True

    @classmethod
    def stop_check(cls):
        cls._running = False 

    @classmethod
    def on_check(cls):
        cls._running = True 
  