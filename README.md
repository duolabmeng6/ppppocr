# ppppocr

ppppocr 是一款自动识别图片中的文字的工具类，可以自动识别图片中的文字，非常容易调用~

本项目使用 PaddleOCR 的模型效果一级棒~

# 使用非常简单
`pip install ppppocr`

```python
import ppppocr
ocr = ppppOcr() # ppppOcr(model="server", lang="cn") 服务端模型 , lang 语言：cn/en/japan/korean
image_path = r'test_images/det_images/ch_en_num.jpg'
dt_boxes, rec_res = ocr.ocr(image_path)
result = ocr.toText(rec_res) # 转换为文本
```