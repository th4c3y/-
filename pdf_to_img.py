import fitz  # PyMuPDF
# import keyboard, time
from PIL import Image
# from l_ima import image_clipboard

def pdf_to_image(path):
    # 打开 PDF 文件
    with fitz.open(path) as pdf_document:
        Image_path_collection = []
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            Image_path_collection.append(img)
    return Image_path_collection
        # for path in  Image_path_collection:
        #     time.sleep(0.2)
        #     image_clipboard(path)
        #     time.sleep(0.3)
        #     keyboard.press_and_release('ctrl+v')

# if __name__ == '__main__':
#     _path = 'D:\临时存放\居民企业（查账征收）企业所得税月（季）度申报.pdf'
#     pdf_to_image(_path)