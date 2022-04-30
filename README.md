# ppppocr

ppppocr 是一款自动识别图片中的文字的工具类，可以自动识别图片中的文字，非常容易调用~

# 使用非常简单
`pip install ppppocr`


```python
import ppppocr
# ocr = ppppOcr(model="server", lang="cn") # 服务端模型
# ocr = ppppOcr(model="mobile", lang="cn") # 移动端模型
# lang 语言：cn/en/japan/korean

ocr = ppppOcr()
image_path = r'test_images/det_images/ch_en_num.jpg'
dt_boxes, rec_res = ocr.ocr(image_path)
# print(rec_res)
# result = ocr.toJson(dt_boxes, rec_res) # 转换为json格式
# print(result)
result = ocr.toText(rec_res) # 转换为文本
print(result)
# ocr.toVisualize(image_path, dt_boxes, rec_res) # 结果可视化 
```