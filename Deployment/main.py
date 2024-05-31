import base64
<<<<<<< HEAD
import logging
import os
import random
import subprocess
=======
import os
import random
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8

import cv2
import numpy as np
import pandas as pd
import tensorflow as tf
import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# 定义模型路径
MODEL_PATH = "../ModelTraining/DPTL-VGG16.keras"
<<<<<<< HEAD
DATASET_SCRIPT_PATH = "DatasetToCSV.py"
CSV_FILE_PATH = "dataset.csv"
=======
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8

app = FastAPI()

# 用于暂存图片的全局变量
image = None
# 定义一个全局模型对象
model = None

# 设置CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许所有源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头部
)

<<<<<<< HEAD
# 设置日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
=======
# 加载CSV文件数据
df = pd.read_csv("dataset.csv")
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8


# 处理图像数据，调整大小并归一化的函数
def process_image(image):
    # 将图像大小调整为 350x230
    image = cv2.resize(image, (350, 230))
    # 将图像转换为数组并进行归一化处理
    normalized_image = np.array(image) / 255.0
    # 增加一个新的维度来创建图像张量
    normalized_image_tensor = np.expand_dims(normalized_image, axis=0)
    return normalized_image_tensor


# 加载模型
def load_model():
    global model
<<<<<<< HEAD
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        logger.info("模型加载成功")
    except Exception as e:
        logger.error(f"模型加载失败: {e}")
        raise RuntimeError("加载模型失败")


def generate_csv():
    try:
        result = subprocess.run(['python', DATASET_SCRIPT_PATH], check=True, capture_output=True, text=True)
        logger.info("CSV 文件生成成功")
        logger.debug(f"CSV 生成输出: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"生成 CSV 文件失败: {e.stderr}")
        raise RuntimeError("生成 CSV 文件失败")
=======
    model = tf.keras.models.load_model(MODEL_PATH)
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8


@app.on_event("startup")
async def startup_event():
<<<<<<< HEAD
    generate_csv()
    global df
    df = pd.read_csv(CSV_FILE_PATH)
=======
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8
    load_model()


@app.post("/upload_image")
async def upload_image(file: UploadFile = File(...)):
    global image
    try:
        # 读取图片数据
        image = np.frombuffer(await file.read(), np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

<<<<<<< HEAD
        if image is None:
            raise ValueError("无法解码图像，图像文件可能已损坏")

=======
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8
        # 返回上传结果
        upload_message = {"message": "图片已上传，等待处理"}
        return upload_message

    except Exception as e:
<<<<<<< HEAD
        logger.error(f"上传图片失败: {e}")
        raise HTTPException(status_code=500, detail=f"上传图片失败: {e}")
=======
        raise HTTPException(status_code=500, detail=str(e))
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8


@app.get("/get_prediction")
async def get_prediction():
    global image, model

<<<<<<< HEAD
    try:
        # 检查是否有图片上传
        if image is None:
            raise HTTPException(status_code=400, detail="没有图片可供预测，请先上传图片")

        # 调整图片大小并进行归一化
        image_tensor = process_image(image)

        # 使用模型进行预测
        prediction = model.predict(image_tensor)
        predicted_value = float(prediction[0][0])
        predicted_class = "malignant" if predicted_value >= 0.5 else "benign"
        predicted_confidence = predicted_value if predicted_value > 0.5 else 1 - predicted_value

        # 构建返回的预测结果字典
        prediction_result = {
            "class": predicted_class,
            "confidence": predicted_confidence
        }

        # 初始化全局变量
        image = None

        # 返回预测结果
        return prediction_result

    except Exception as e:
        logger.error(f"预测失败: {e}")
        raise HTTPException(status_code=500, detail=f"预测失败: {e}")
=======
    # 检查是否有图片上传
    if image is None:
        raise HTTPException(status_code=400, detail="没有图片可供预测，请先上传图片")

    # 调整图片大小并进行归一化
    image_tensor = process_image(image)

    # 使用模型进行预测
    prediction = model.predict(image_tensor)

    predicted_value = float(prediction[0][0])
    predicted_class = "malignant" if predicted_value >= 0.5 else "benign"
    predicted_confidence = predicted_value if predicted_value > 0.5 else 1 - predicted_value

    # 构建返回的预测结果字典
    prediction_result = {
        "class": predicted_class,
        "confidence": predicted_confidence
    }

    # 初始化全局变量
    image = None

    # 返回预测结果
    return prediction_result
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8


@app.get("/get_random_image")
async def get_random_image():
    global image
<<<<<<< HEAD
    try:
        # 生成随机数，随机选取其中一条图片数据（相对路径、类别）
        random_index = random.randint(0, len(df) - 1)
        image_data = df.iloc[random_index].to_dict()

        # 读取图片文件路径
        image_file_path = image_data['image_path']

        if not os.path.exists(image_file_path):
            raise FileNotFoundError(f"文件不存在: {image_file_path}")

        # 读取图片数据存储进全局变量
        image = cv2.imread(image_file_path)

        if image is None:
            raise ValueError("无法读取图像，图像文件可能已损坏")

        # 将图片转换为 Base64 编码
        _, buffer = cv2.imencode('.jpg', image)
        img_str = base64.b64encode(buffer).decode()

        # 构建 JSON 对象，包含图片数据和其他文本信息
        image_info = {
            "image_base64": img_str,
            "image_filename": os.path.basename(image_file_path),
            "label": image_data['label']
        }

        # 返回图片JSON对象
        return image_info

    except Exception as e:
        logger.error(f"获取随机图片失败: {e}")
        raise HTTPException(status_code=500, detail=f"获取随机图片失败: {e}")
=======
    # 生成随机数，随机选取其中一条图片数据（相对路径、类别）
    random_index = random.randint(0, len(df) - 1)
    image_data = df.iloc[random_index].to_dict()

    # 读取图片文件路径
    image_file_path = image_data['image_path']

    # 读取图片数据存储进全局变量
    image = cv2.imread(image_file_path)

    # 将图片转换为 Base64 编码
    _, buffer = cv2.imencode('.jpg', image)
    img_str = base64.b64encode(buffer).decode()

    # 构建 JSON 对象，包含图片数据和其他文本信息
    image_info = {
        "image_base64": img_str,
        "image_filename": os.path.basename(image_file_path),
        "label": image_data['label']
    }

    # 返回图片JSON对象
    return image_info
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8


if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)
