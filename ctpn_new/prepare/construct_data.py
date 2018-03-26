"""
这个脚本用来处理原始的数据，将图片按照短边600为标准进行缩放，同时要缩放坐标
要将数据整理成的格式如下，存放在dataset/for_train下
以dataset/for_train为根目录
---| Imageset 保存图片文件
   | Imageinfo 保存每张图片对应的txt文本
   ----|xxxxxx.txt xxxxxx为图片名(不带扩展名)，每一行为一个文本框，格式为xmin,ymin,xmax,ymax,width,height,channel
   ----|..........
   | train_set.txt 保存所有训练样本对应的文件名，每个占一行
### 要求在ctpn_new 目录下能够直接运行，直接读取 dataset/ICPR_text_train 下的原始训练数据进行处理，结果直接输出到到dataset下，不可人工复制粘贴，ctpn_new/dataset 目录下的所有文件将被git忽略，以提高push速度和减少不必要的文件冲突###
"""