# Undergraduate Data Science Graduation Project - Research on Pathological Tissue Classification Methods of Breast Cancer Based on Deep Learning  
# 本科大数据专业毕设项目 -《基于深度学习的乳腺癌病理组织分类方法研究》  
# 大学のデータサイエンス卒業プロジェクト - 深層学習に基づく乳癌病理組織分類方法の研究  

## Table of Contents 
## 目录  
## 目次  

1. [Clone Project](#克隆项目)  
   [克隆项目](#克隆项目)  
   [プロジェクトをクローン](#克隆项目)  

2. [Model Training](#模型训练部分)  
   [模型训练部分](#模型训练部分)  
   [モデルのトレーニング](#模型训练部分)  

3. [Frontend Application System](#前端应用系统)  
   [前端应用系统](#前端应用系统)  
   [フロントエンドアプリケーションシステム](#前端应用系统)  

4. [File Structure](#文件结构)  
   [文件结构](#文件结构)  
   [ファイル構造](#文件结构)  

5. [Precautions](#注意事项)  
   [注意事项](#注意事项)  
   [注意事項](#注意事项)  

6. [Copyright](#版权声明)  
   [版权声明](#版权声明)  
   [著作権声明](#版权声明)  

7. [License](#许可证)  
   [许可证](#许可证)  
   [ライセンス](#许可证)  

8. [Contact](#联系方式)  
   [联系方式](#联系方式)  
   [連絡先](#联系方式)  

## Project Introduction  项目介绍  プロジェクトの紹介  

This project is an undergraduate (second degree) graduation design at China Agricultural University, with the title "Research on Pathological Tissue Classification Methods of Breast Cancer Based on Deep Learning." The project uses the publicly available BreakHis dataset, employing a traditional Convolutional Neural Network (CNN) model and is trained and tested based on the TensorFlow framework. The development environment for the project is Python 3.9 and FastAPI.
The project files are divided into two main parts: model training and frontend application system. 

本项目是中国农业大学本科（二学位）的毕业设计，题目为《基于深度学习的乳腺癌病理组织分类方法研究》。项目采用公开的 BreakHis 数据集，利用传统卷积神经网络（CNN）模型，并基于 TensorFlow 框架进行训练与测试。项目开发环境使用 Python 3.9，FastAPI。
项目文件分为两个主要部分：模型训练和前端应用系统。 

このプロジェクトは中国農業大学の学部（二学位）の卒業設計であり、タイトルは「深層学習に基づく乳癌病理組織分類方法の研究」です。このプロジェクトでは公開されているBreakHisデータセットを使用し、伝統的な畳み込みニューラルネットワーク（CNN）モデルを採用し、TensorFlowフレームワークに基づいて訓練とテストを行います。開発環境はPython 3.9とFastAPIです。  
プロジェクトファイルはモデルトレーニングとフロントエンドアプリケーションシステムの2つの主要部分に分かれています。  

<a name="克隆项目"></a>  
## 1. Clone Project  克隆项目  プロジェクトをクローン  

First, clone this project from GitHub to your local environment:  

首先，将本项目从 GitHub 克隆到本地：  

まず、このプロジェクトをGitHubからローカルにクローンします：  

```bash  
git clone https://github.com/misfit789/BreastCancerDetection-CNN-BreakHis.git  
cd BreastCancerDetection-CNN-BreakHis  
```  

<a name="模型训练部分"></a>  
## 2. Model Training  模型训练部分  モデルのトレーニング  

1. Before executing the download command, make sure the working directory has switched to the ModelTraining path:  

   在执行下载命令前，请确保工作目录已经切换到 ModelTraining 路径：  

   ダウンロードコマンドを実行する前に、作業ディレクトリがModelTrainingパスに切り替わっていることを確認してください：  

```bash  
cd ModelTraining  
```  

2. Next, download the dataset to the ModelTraining path and rename the compressed dataset file to `dataset.zip`.  

   接下来，下载数据集到ModelTraining路径，并修改数据集压缩包的名称为`dataset.zip`。  

   次に、データセットをModelTrainingパスにダウンロードし、圧縮されたデータセットファイルの名前を `dataset.zip` に変更します。  

   - **For macOS and Linux systems**, use the following command in the `ModelTraining` path:  

   - **适用于 macOS 和 Linux 系统**，在 `ModelTraining` 路径中使用以下命令：  

   - **macOSおよびLinuxシステム向け**、 `ModelTraining` パスで以下のコマンドを使用します：  

```bash  
wget http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz -O ModelTraining/dataset.zip  
```  

   - **For Windows systems**, use the PowerShell command in the `ModelTraining` directory:  

   - **适用于 Windows 系统**，在 `ModelTraining` 目录下使用 PowerShell 命令：  

   - **Windowsシステム向け**、 `ModelTraining` ディレクトリでPowerShellコマンドを使用します：  

```powershell  
Invoke-WebRequest -Uri "http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz" -OutFile "ModelTraining\dataset.zip"  
```  

3. Install the libraries listed in the `requirements.txt` file under the `ModelTraining` path.  

   安装`ModelTraining`路径中`requirements.txt`文件中的库。  

   `ModelTraining` パスにある `requirements.txt` ファイルのライブラリをインストールします。  

The installation command is as follows:  
安装命令如下：  
インストールコマンドは次のとおりです：  

```bash  
pip install -r ModelTraining/requirements.txt  
```  

4. Run the `DPTL-VGG16.ipynb` file, and the generated images will be saved in the `OutputImages` directory at the same level.  

   运行`DPTL-VGG16.ipynb`文件，过程中产生的图片会保存在同级`OutputImages`路径中。  

   `DPTL-VGG16.ipynb` ファイルを実行し、生成された画像は同じレベルの `OutputImages` パスに保存されます。  

<a name="前端应用系统"></a>  
## 3. Frontend Application System  前端应用系统  フロントエンドアプリケーションシステム  

The code for the frontend application system is stored in the `Deployment` directory, and it includes the following files:  

前端应用系统的代码存放在`Deployment`目录中，包含以下文件：  

フロントエンドアプリケーションシステムのコードは `Deployment` ディレクトリに保存されており、次のファイルが含まれています：  

- `API_DOCUMENTATION.md`: Documentation for the API.  
- `DatasetToCSV.py`: Scans each image data from the decompressed dataset, records the corresponding labels and magnification factors, and creates a table stored in `dataset.csv` for `main.py` to read.  
- `app.css`: Frontend style file.  
- `app.html`: Frontend HTML file.  
- `app.js`: Frontend JavaScript file.  
- `dataset.csv`: Generated data table file.  
- `main.py`: Backend interface file.  

- `API_DOCUMENTATION.md`：接口说明的文档。  
- `DatasetToCSV.py`：将解压后的数据集下的每一张图片数据逐一扫描，记录对应的标签和放大系数，并制作表格存放在`dataset.csv`中，用于`main.py`这个后端接口进行读取。  
- `app.css`：前端样式文件。  
- `app.html`：前端HTML文件。  
- `app.js`：前端JavaScript文件。  
- `dataset.csv`：生成的数据表格文件。  
- `main.py`：后端接口文件。  

- `API_DOCUMENTATION.md`: APIドキュメント。  
- `DatasetToCSV.py`: 解凍されたデータセットの各画像データをスキャンし、対応するラベルと倍率を記録し、 `dataset.csv` に保存されます。  
- `app.css`: フロントエンドのスタイルファ

イル。  
- `app.html`: フロントエンドのHTMLファイル。  
- `app.js`: フロントエンドのJavaScriptファイル。  
- `dataset.csv`: 生成されたデータテーブルファイル。  
- `main.py`: バックエンドインターフェイスファイル。  

<a name="文件结构"></a>  
## 4. File Structure  文件结构  ファイル構造  

```bash  
├── ModelTraining # Folder for model training  
│   ├── dataset.zip  
│   ├── requirements.txt  
│   ├── DPTL-VGG16.ipynb  
│   └── OutputImages/  
├── Deployment    # Folder for frontend deployment  
    ├── API_DOCUMENTATION.md  
    ├── DatasetToCSV.py  
    ├── app.css  
    ├── app.html  
    ├── app.js  
    ├── dataset.csv  
    └── main.py  
```  

The project includes two main folders: `ModelTraining` for model training-related files and `Deployment` for frontend deployment files.  

项目包括两个主要文件夹：`ModelTraining`用于模型训练相关文件，`Deployment`用于前端部署文件。  

このプロジェクトには2つの主要なフォルダが含まれています。1つは `ModelTraining` で、モデルのトレーニングに関連するファイル用、もう1つは `Deployment` で、フロントエンドのデプロイ用です。  

<a name="注意事项"></a>  
## 5. Precautions  注意事项  注意事項  

- Ensure that the dataset is downloaded and renamed correctly before running the model training code.  
- Make sure the required libraries are installed properly to avoid runtime errors.  
- Follow the instructions in `API_DOCUMENTATION.md` for setting up and testing the frontend application.  

- 确保在运行模型训练代码之前，数据集已正确下载并重命名。  
- 确保所需的库已正确安装，以避免运行时错误。  
- 按照`API_DOCUMENTATION.md`中的说明设置并测试前端应用程序。  

- モデルのトレーニングコードを実行する前に、データセットが正しくダウンロードされて名前が変更されていることを確認してください。  
- 実行時エラーを避けるために、必要なライブラリが正しくインストールされていることを確認してください。  
- フロントエンドアプリケーションの設定とテストについては、 `API_DOCUMENTATION.md` の指示に従ってください。  

<a name="版权声明"></a>  
## 6. Copyright  版权声明  著作権声明  

The copyright of this project belongs to the author. For any use of this project, please contact the author for permission.  

本项目版权归作者所有，任何使用本项目的行为，请联系作者获得许可。  

このプロジェクトの著作権は著者に帰属します。このプロジェクトを使用する場合は、必ず著者に連絡して許可を得てください。  

<a name="许可证"></a>  
## 7. License  许可证  ライセンス  

This project is licensed under the MIT License. See the `LICENSE` file for more details.  

本项目采用 MIT 许可证。详细信息请参见 `LICENSE` 文件。  

このプロジェクトはMITライセンスの下でライセンスされています。詳細については `LICENSE` ファイルを参照してください。  

<a name="联系方式"></a>  
## 8. Contact  联系方式  連絡先  

For any inquiries regarding this project, please contact the author at:  
如需任何关于本项目的咨询，请通过以下方式联系作者：  
このプロジェクトに関する問い合わせは、以下の方法で著者にご連絡ください：  

- Email: chenwei@alu.cau.edu.cn
