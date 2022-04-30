import unittest

from .ppppocr import *


class TestPPPPOCR(unittest.TestCase):

    def test_1(self):
        pass
        # ocr = ppppOcr(model="server", lang="cn") # 服务端模型
        # ocr = ppppOcr(model="mobile", lang="cn") # 移动端模型
        ocr = ppppOcr()
        image_path = r'test_images/det_images/ch_en_num.jpg'

        folder = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(folder, image_path)

        dt_boxes, rec_res = ocr.ocr(image_path)
        # print(rec_res)
        # result = ocr.toJson(dt_boxes, rec_res) # 转换为json格式
        # print(result)
        result = ocr.toText(rec_res)  # 转换为文本
        print(result)
        ocr.toVisualize(image_path, dt_boxes, rec_res) # 结果可视化

    def test_4(self):
        pass
        import requests
        folder = os.path.dirname(os.path.abspath(__file__))
        modelFile = os.path.join(folder, 'test.7z')
        print(modelFile)
        url = 'https://ghproxy.com/https://github.com/RapidAI/Paddle2OnnxConvertor/releases/download/20210702/ur_mobile_v2.0_rec_infer.onnx.7z'
        r = requests.get(url)
        with open(modelFile, "wb") as code:
            code.write(r.content)

    def test_2(self):
        pass
        folder = os.path.dirname(os.path.abspath(__file__))
        modelFile = os.path.join(folder, 'test.7z')
        modelsPath = os.path.join(folder, 'models')
        print(modelFile)
        print(modelsPath)
        import py7zr
        with py7zr.SevenZipFile(modelFile, mode='r') as z:
            z.extractall(modelsPath)