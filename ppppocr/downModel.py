"""
需要一个解压包
pip install py7zr
"""

import os




def downloadAndUnzipTheModel(model_path):
    import requests
    import py7zr
    """下载模型并解压"""
    folder = os.path.dirname(os.path.abspath(__file__))
    modelFile = os.path.join(folder, 'test.7z')
    url = 'https://ghproxy.com/' + model_path
    print("downloading model..." + url)
    r = requests.get(url)
    with open(modelFile, "wb") as code:
        code.write(r.content)
    folder = os.path.dirname(os.path.abspath(__file__))
    modelFile = os.path.join(folder, 'test.7z')
    modelsPath = os.path.join(folder, 'models')
    # print(modelFile)
    # print(modelsPath)
    # print("unzipFiles...")
    with py7zr.SevenZipFile(modelFile, mode='r') as z:
        z.extractall(modelsPath)
    print("Model download complete")
    # 删除文件
    os.remove(modelFile)


def checkTheModelAndDownload(modelName):
    modelsUrl = {
        "ch_ppocr_mobile_v2.0": [
            "https://github.com/RapidAI/Paddle2OnnxConvertor/releases/download/20210702/ch_ppocr_mobile_v2.0_det_infer.onnx.7z",
            "https://github.com/RapidAI/Paddle2OnnxConvertor/releases/download/20210702/ch_ppocr_mobile_v2.0_rec_infer.onnx.7z"
        ],
        "ch_ppocr_server_v2.0": [
            "https://github.com/RapidAI/Paddle2OnnxConvertor/releases/download/20210702/ch_ppocr_server_v2.0_det_infer.onnx.7z",
            "https://github.com/RapidAI/Paddle2OnnxConvertor/releases/download/20210702/ch_ppocr_server_v2.0_rec_infer.onnx.7z"
        ],
        "en_number_mobile_v2.0": [
            "https://github.com/RapidAI/Paddle2OnnxConvertor/releases/download/20210702/en_number_mobile_v2.0_rec_infer.onnx.7z"
        ],
        "japan_mobile_v2.0": [
            "https://github.com/RapidAI/Paddle2OnnxConvertor/releases/download/20210702/japan_mobile_v2.0_rec_infer.onnx.7z"
        ],
        "korean_mobile_v2.0": [
            "https://github.com/RapidAI/Paddle2OnnxConvertor/releases/download/20210702/korean_mobile_v2.0_rec_infer.onnx.7z"
        ],
    }
    for url in modelsUrl[modelName]:
        # 获取文件名
        model_path = url.split('/')[-1]
        # 获取文件名称
        model_name = model_path.split('.7z')[0]
        # 检查文件是否存在
        folder = os.path.dirname(os.path.abspath(__file__))
        modelFile = os.path.join(folder, "models/" + model_name)
        # print(modelFile)
        if not os.path.exists(modelFile):
            print("Model does not exist, start downloading...", model_name)
            try:
                downloadAndUnzipTheModel(url)
            except:
                print("Model download failed")
                print("Please download the model by yourself and put the model in the models folder")
                print(url)

if __name__ == '__main__':
    checkTheModelAndDownload('ch_ppocr_server_v2.0')
