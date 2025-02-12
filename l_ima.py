import win32clipboard # type: ignore
import win32con # type: ignore
from PIL import Image
import io

def set_clipboard(image_path):
    image = Image.open(image_path)
    image_clipboard(image)

def image_clipboard(image):
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_DIB, data)
        win32clipboard.CloseClipboard()
        return True
    except:
        return False

