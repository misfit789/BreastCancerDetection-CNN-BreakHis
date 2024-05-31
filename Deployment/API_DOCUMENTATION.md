# API 文档

此 API 支持单张图像的预测操作。

## 上传图片

**POST** `/upload_image`

用户可以将图像上传到服务器。该图像将被存储并用于以后的预测操作。

- 请求（Request）
    - 正文
        - 图像文件（必需）：使用 `File` 参数上传图像。
- 响应（Response）
    - 一条确认信息，表明上传成功。

## 获取随机图像

**GET** `/get_random_image`

用户可以从服务器获取一张随机图像。

- 请求（Request）
    - 无需参数
- 响应（Response）
    - 包含以下内容的图像信息（JSON 格式）：
        - Base64 编码的图像
        - 图像文件名
        - 图像的标签

## 获取预测结果

**GET** `/get_prediction`

预测存储在服务器中的图像。

- 请求（Request）
    - 无需参数
- 响应（Response）
    - 图像的预测类别
    - 预测结果的置信级别

如果在服务器中找不到图像，会返回带有消息的 400 错误。
请为每次预测上传一张新图片。