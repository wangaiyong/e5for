# 导入Pillow库和os模块
from PIL import Image
import os

# 定义webp图片所在的文件夹路径
webp_dir = "webp_folder"

# 定义jpg图片要保存的文件夹路径
jpg_dir = "jpg_folder"

# 遍历webp文件夹中的所有文件
for file in os.listdir(webp_dir):
    # 如果文件是webp格式的
    if file.endswith(".webp"):
        # 拼接文件的完整路径
        webp_path = os.path.join(webp_dir, file)
        # 打开webp图片
        im = Image.open(webp_path)
        # 转换为RGB模式
        im = im.convert("RGB")
        # 调整图片的尺寸为150*200，使用ANTIALIAS滤波器
        im = im.resize((150, 200), Image.ANTIALIAS)
        # 生成jpg图片的文件名，替换后缀为jpg
        jpg_file = file.replace(".webp", ".jpg")
        # 拼接jpg图片的完整路径
        jpg_path = os.path.join(jpg_dir, jpg_file)
        # 保存为jpg图片
        im.save(jpg_path, "jpeg")
