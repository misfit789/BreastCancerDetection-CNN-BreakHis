import base64
import io
import os
import random

import cv2
import numpy as np
import pandas as pd
import tensorflow as tf
import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# 定义模型路径
MODEL_PATH = "../ModelTraining/DPTL-VGG16.keras"

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

# 加载CSV文件数据
df = pd.read_csv("dataset.csv")


# 处理图像数据，调整大小并归一化的函数
def process_image(image):
    # 将图像大小调整为 230x350
    image = cv2.resize(image, (230, 350))
    # 将图像转换为数组并进行归一化处理
    normalized_image = np.array(image) / 255.0
    # 增加一个新的维度来创建图像张量
    normalized_image_tensor = np.expand_dims(normalized_image, axis=0)
    return normalized_image_tensor


# 加载模型
def load_model():
    global model
    model = tf.keras.models.load_model(MODEL_PATH)


@app.on_event("startup")
async def startup_event():
    load_model()


@app.post("/upload_image")
async def upload_image(file: UploadFile = File(...)):
    global image
    try:
        # 读取图片数据
        image = np.fromstring(await file.read(), np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # 返回上传结果
        upload_message = {"message": f"图片已上传，等待处理"}
        return upload_message

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get_prediction")
async def get_prediction():
    global image, model

    # 检查是否有图片上传
    if image is None:
        raise HTTPException(status_code=400, detail="没有图片可供预测，请先上传图片")

    # 调整图片大小并进行归一化
    image = process_image(image)

    # 使用模型进行预测
    prediction = model.predict(image)

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


@app.get("/get_random_image")
async def get_random_image():
    global image
    # 生成随机数，随机选取其中一条图片数据（相对路径、类别）
    random_index = random.randint(0, len(df) - 1)
    image_data = df.iloc[random_index].to_dict()

    # 读取图片文件路径
    image_file_path = image_data['image_path']

    # 读取图片数据存储进全局变量
    with open(image_file_path, 'rb') as file:
        # 将二进制数据转换为图像对象
        image = cv2.imread(file.read())

    # 将图片转换为 Base64 编码
    buffered = io.BytesIO()
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # 构建 JSON 对象，包含图片数据和其他文本信息
    image_info = {
        "image_base64": img_str,
        "image_filename": os.path.basename(image_file_path),
        "label": image_data['label']
    }

    # 返回图片JSON对象
    return image_info


if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)
