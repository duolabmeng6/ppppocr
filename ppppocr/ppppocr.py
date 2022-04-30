"""
模型下载 : https://github.com/RapidAI/Paddle2OnnxConvertor/releases

"""
import os

from .rapid_ocr_api import TextSystem, visualize
from .downModel import checkTheModelAndDownload


class ppppOcr:
    def __init__(self, model='ppocrv2', lang='cn'):
        """初始化模型 model 可选模型：mobile/server lang 语言：cn/en/japan/korean"""
        cls_model_path = 'models/ch_ppocr_mobile_v2.0_cls_infer.onnx'

        if model == "server":
            checkTheModelAndDownload('ch_ppocr_server_v2.0')
            # 中英文识别
            det_model_path = 'models/ch_ppocr_server_v2.0_det_infer.onnx'
            rec_model_path = 'models/ch_ppocr_server_v2.0_rec_infer.onnx'
        if model == "mobile":
            checkTheModelAndDownload('ch_ppocr_mobile_v2.0')
            # 中英文识别
            det_model_path = 'models/ch_ppocr_mobile_v2.0_det_infer.onnx'
            rec_model_path = 'models/ch_ppocr_mobile_v2.0_rec_infer.onnx'
        if model == "ppocrv2":
            # 中英文识别
            det_model_path = 'models/ch_PP-OCRv2_det_infer.onnx'
            rec_model_path = 'models/ch_PP-OCRv2_rec_infer.onnx'

        if lang == "cn":
            keys_path = 'rec_dict/ppocr_keys_v1.txt'
        if lang == "en":
            checkTheModelAndDownload('en_number_mobile_v2.0')
            rec_model_path = 'models/en_number_mobile_v2.0_rec_infer.onnx'
            keys_path = 'rec_dict/en_dict.txt'
        if lang == "japan":
            checkTheModelAndDownload('japan_mobile_v2.0')
            rec_model_path = 'models/japan_rec_crnn.onnx'
            keys_path = 'rec_dict/japan_dict.txt'
        if lang == "korean":
            checkTheModelAndDownload('korean_mobile_v2.0')
            rec_model_path = 'models/korean_mobile_v2.0_rec_infer.onnx'
            keys_path = 'rec_dict/korean_dict.txt'

        folder = os.path.dirname(os.path.abspath(__file__))
        det_model_path = os.path.join(folder, det_model_path)
        cls_model_path = os.path.join(folder, cls_model_path)
        rec_model_path = os.path.join(folder, rec_model_path)
        keys_path = os.path.join(folder, keys_path)


        self.text_sys = TextSystem(det_model_path,
                                   rec_model_path,
                                   use_angle_cls=True,
                                   cls_model_path=cls_model_path,
                                   keys_path=keys_path)

    def ocr(self, image_path):
        """识别函数 传入图片路径"""
        dt_boxes, rec_res = self.text_sys(image_path)
        return dt_boxes, rec_res

    def toJson(self, dt_boxes, rec_res):
        """将识别结果转换为json格式"""

        results = []
        for i, (text, score) in enumerate(rec_res):
            boxs = [(int(v[0]), int(v[1])) for v in dt_boxes[i]]
            results.append({
                "text_box_position": boxs,
                "text": text,
                "confidence": str(score),
            })
        return results

    def toText(self, rec_res):
        """将识别结果转换为文本"""
        results = []
        for i, (text, score) in enumerate(rec_res):
            results.append(text)
        return " ".join(results)

    def toVisualize(self, image_path, dt_boxes, rec_res, font_path, write_directory_path=""):
        """
        将识别结果可视化
        :param image_path: 图片路径
        :param dt_boxes: 检测结果
        :param rec_res: 识别结果
        :param font_path: 字体路径 可以用微软雅黑
        :param write_directory_path: 图片输出路径
        :return: 图片路径
        """
        return visualize(image_path, dt_boxes, rec_res, font_path, write_directory_path)
