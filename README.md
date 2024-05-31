# 项目名称

## 项目介绍

此项目包括两个部分：模型训练和前端应用系统。

### 模型训练部分

1. 下载数据集到ModelTraining路径，并修改数据集压缩包的名称为`dataset.zip`。

   下载和重命名命令如下：
   ```bash
   wget http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz -O ModelTraining/dataset.zip
   ```

2. 安装`ModelTraining`路径中`requirements.txt`文件中的库。

   安装命令如下：
   ```bash
   pip install -r ModelTraining/requirements.txt
   ```

3. 运行`DPTL-VGG16.ipynb`文件，过程中产生的图片会保存在同级`OutputImages`路径中。

### 前端应用系统部分

前端应用系统的代码存放在`Deployment`目录中，包含以下文件：
- `API_DOCUMENTATION.md`：接口说明的文档。
- `DatasetToCSV.py`：将解压后的数据集下的每一张图片数据逐一扫描，记录对应的标签和放大系数，并制作表格存放在`dataset.csv`中，用于`main.py`这个后端接口进行读取。
- `app.css`：前端样式文件。
- `app.html`：前端HTML文件。
- `app.js`：前端JavaScript文件。
- `dataset.csv`：生成的数据表格文件。
- `main.py`：后端接口文件。

#### 使用步骤：

1. 确保模型训练得到的模型文件（默认名称为`DPTL-VGG16.keras`）存在于项目目录中。
2. `main.py`会自动调用模型文件并加载`DatasetToCSV.py`，自动生成`dataset.csv`文件。
3. 在浏览器中打开`app.html`文件即可进行系统的使用。

## 文件结构

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

## 注意事项

- 请确保在训练模型时已经正确下载和解压数据集，并安装了所需的Python库。
- 在运行前端应用系统前，请确认训练好的模型文件存在且路径正确。

希望此项目对你有所帮助，若有任何问题，请随时联系我。

邮箱：chenwei@alu.cau.edu.cn

