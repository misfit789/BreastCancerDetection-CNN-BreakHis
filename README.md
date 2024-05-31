# 本科大数据专业毕设项目 -《基于深度学习的乳腺癌病理组织分类方法研究》

## 目录

1. [克隆项目](#克隆项目)
2. [模型训练部分](#模型训练部分)
3. [前端应用系统](#前端应用系统)
4. [文件结构](#文件结构)
5. [注意事项](#注意事项)
6. [版权声明](#版权声明)
7. [许可证](#许可证)
8. [联系方式](#联系方式)

## 项目介绍

此项目是中国农业大学本科（二学位）的毕业设计项目，题目为《基于深度学习的乳腺癌病理组织分类方法研究》。项目使用了公开的BreakHis数据集，采用传统的卷积神经网络（CNN）模型，并基于TensorFlow框架进行训练。项目使用的Python版本为3.9。

项目文件分为两个主要部分：模型训练和前端应用系统。

<a name="克隆项目"></a>
## 1. 克隆项目

首先，将本项目从 GitHub 克隆到本地：

```bash
git clone https://github.com/misfit789/BreastCancerDetection-CNN-BreakHis.git
cd BreastCancerDetection-CNN-BreakHis
```

<a name="模型训练部分"></a>
## 2. 模型训练部分

1. 下载数据集到ModelTraining路径，并修改数据集压缩包的名称为`dataset.zip`。

   **适用于 macOS 和 Linux 系统**：

   在 `ModelTraining` 路径中使用以下命令：
   
   ```bash
   wget http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz -O ModelTraining/dataset.zip
   ```
   
   **适用于 Windows 系统**：
   
   在 `ModelTraining` 目录下使用 PowerShell 命令：
   
   ```powershell
   Invoke-WebRequest -Uri "http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz" -OutFile "ModelTraining\dataset.zip"
   ```

2. 安装`ModelTraining`路径中`requirements.txt`文件中的库。

   安装命令如下：
   ```bash
   pip install -r ModelTraining/requirements.txt
   ```

3. 运行`DPTL-VGG16.ipynb`文件，过程中产生的图片会保存在同级`OutputImages`路径中。

<a name="前端应用系统"></a>
## 3. 前端应用系统

前端应用系统的代码存放在`Deployment`目录中，包含以下文件：
- `API_DOCUMENTATION.md`：接口说明的文档。
- `DatasetToCSV.py`：将解压后的数据集下的每一张图片数据逐一扫描，记录对应的标签和放大系数，并制作表格存放在`dataset.csv`中，用于`main.py`这个后端接口进行读取。
- `app.css`：前端样式文件。
- `app.html`：前端HTML文件。
- `app.js`：前端JavaScript文件。
- `dataset.csv`：生成的数据表格文件。
- `main.py`：后端接口文件。

### 使用步骤：

1. 确保模型训练得到的模型文件（默认名称为`DPTL-VGG16.keras`）存在于项目目录中。
2. `main.py`会自动调用模型文件并加载`DatasetToCSV.py`，自动生成`dataset.csv`文件。
3. 在浏览器中打开`app.html`文件即可进行系统的使用。

<a name="文件结构"></a>
## 4. 文件结构

```
BreastCancerDetection-CNN-BreakHis
├── ModelTraining
│   ├── DPTL-VGG16.ipynb
│   ├── requirements.txt
│   └── dataset.zip
└── Deployment
    ├── API_DOCUMENTATION.md
    ├── DatasetToCSV.py
    ├── app.css
    ├── app.html
    ├── app.js
    ├── dataset.csv
    └── main.py
```

<a name="注意事项"></a>
## 5. 注意事项

- 请确保在训练模型时已经正确下载和解压数据集，并安装了所需的Python库。
- 在运行前端应用系统前，请确认训练好的模型文件存在且路径正确。

<a name="版权声明"></a>
## 6. 版权声明

© 2024 China Agricultural University. All rights reserved.

<a name="许可证"></a>
## 7. 许可证

本项目采用 [MIT License](LICENSE) 许可证进行许可。

<a name="联系方式"></a>
## 8. 联系方式

希望此项目对你有所帮助，若有任何问题，请随时联系我。

邮箱：chenwei@alu.cau.edu.cn
```
