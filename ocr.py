from paddleocr import PaddleOCR
import os
# 初始化 PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="en")
input_dir = './input'
# 读取input_dir目录下的所有图片
img_list = os.listdir(input_dir)

# 读取图片
for img in img_list:
    img_path = os.path.join(input_dir, img)
    # 对图片进行 OCR
    results = ocr.ocr(img_path)
    # 打印识别结果
    for result in results[0]:
        loc, text_prob = result
        text = text_prob[0]
        # 可能将I识别为1或者|，这里做了处理，只要前5个字符中包含ME、1、|，就认为是IMEI1
        if text[:5] == 'IMEI1' or text[:5] == 'IME11' or text[:5] == '1ME11' or text[:5] == 'IME|1' or text[:5] == 'IMEI|' or text[:5] == '1MEI|':
            print(text)
