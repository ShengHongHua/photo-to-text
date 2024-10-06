from paddleocr import PaddleOCR
word = []

#实例化ocr模型
ocr = PaddleOCR()

#识别图片中的文字
result = ocr.ocr('image.jpg')
print('识别结果： ',result)

#将识别结果保存到tt文件中
with open('识别结果.txt','a',encoding='utf-8') as file:
    #遍历识别结果
    for line in result:


        #提取识别数据中的文字元组
        text_line = word[-1]
        #从文字元组中提取内容
        text = text_line[0]
        print('text:',text)
        #将文字内容写入到文件中
        file.write(text + '\n')

print("识别结果以保存到txt文件中")