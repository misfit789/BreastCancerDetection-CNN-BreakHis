// 绑定事件处理函数
document.getElementById('getRandomImage').addEventListener('click', getRandomImage);
document.getElementById('getPrediction').addEventListener('click', getPrediction);
document.getElementById('uploadLocalImage').addEventListener('click', uploadImage);

<<<<<<< HEAD
let selectedFile;
=======
let selectedFile; // 用于存储选中的文件
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8

// 获取随机图片
async function getRandomImage() {
    try {
        const url = 'http://localhost:8000/get_random_image';
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Image Base64 String:', data.image_base64);
        console.log('Image Filename:', data.image_filename);
        console.log('Image Label:', data.label);

        const imageElement = document.createElement('img');
        imageElement.src = 'data:image/png;base64,' + data.image_base64;
<<<<<<< HEAD
        imageElement.style.width = "100%";
        imageElement.style.height = "100%";
        imageElement.style.objectFit = "cover";
=======
        imageElement.style.width = "350px";
        imageElement.style.height = "230px";
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8

        const imagePreviewDiv = document.getElementById('imagePreview');
        imagePreviewDiv.innerHTML = '';
        imagePreviewDiv.appendChild(imageElement);

        addMessageToBox(`获取图片成功：${data.image_filename}, 标签：${data.label}`);
<<<<<<< HEAD
=======

>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8
    } catch (error) {
        console.error('Error fetching random image:', error);
        addMessageToBox(`获取图片失败：${error.message}`);
    }
}

// 获取预测结果
async function getPrediction() {
    try {
        const response = await fetch('http://localhost:8000/get_prediction');

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const predictionResult = await response.json();
        console.log('预测类别:', predictionResult.class);
        console.log('预测置信度:', predictionResult.confidence.toFixed(2));

        addMessageToBox(`预测结果：类别 - ${predictionResult.class}, 置信度 - ${predictionResult.confidence.toFixed(2)}`);
<<<<<<< HEAD
=======

>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8
    } catch (error) {
        console.error('获取预测结果时发生错误:', error);
        addMessageToBox(`获取预测结果失败：${error.message}`);
    }
}

// 预览图片
function previewImage() {
    const fileInput = document.getElementById('fileInput');
    selectedFile = fileInput.files[0];

    if (selectedFile) {
        addMessageToBox(`选中的图片文件名：${selectedFile.name}`);

        const reader = new FileReader();
        reader.onload = function (e) {
            const imagePreviewDiv = document.getElementById('imagePreview');
            imagePreviewDiv.innerHTML = '';
            const imageElement = document.createElement('img');
            imageElement.src = e.target.result;
<<<<<<< HEAD
            imageElement.style.width = "100%";
            imageElement.style.height = "100%";
            imageElement.style.objectFit = "cover";
=======
            imageElement.style.width = "350px";
            imageElement.style.height = "230px";
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8
            imagePreviewDiv.appendChild(imageElement);
        };
        reader.readAsDataURL(selectedFile);
    }
}

// 上传图片
async function uploadImage() {
    if (!selectedFile) {
        addMessageToBox('请选择要上传的图片。');
        return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
        const response = await fetch('http://localhost:8000/upload_image', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        addMessageToBox(data.message);
<<<<<<< HEAD
=======

>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8
    } catch (error) {
        console.error('上传图片时发生错误:', error);
        addMessageToBox(`上传图片失败：${error.message}`);
    }
}

// 添加消息到消息框
function addMessageToBox(message) {
<<<<<<< HEAD
    const messageBoxContent = document.getElementById('messageBoxContent');
    const messageElement = document.createElement('p');
    messageElement.textContent = message;
    messageBoxContent.appendChild(messageElement);
    messageBoxContent.scrollTop = messageBoxContent.scrollHeight; // 自动滚动到最新消息
}

// 清除消息记录
function clearMessages() {
    const messageBoxContent = document.getElementById('messageBoxContent');
    messageBoxContent.innerHTML = '';
}

// 拖放事件处理
const imagePreviewDiv = document.getElementById('imagePreview');

imagePreviewDiv.addEventListener('dragover', (e) => {
    e.preventDefault();
    e.stopPropagation();
    imagePreviewDiv.classList.add('dragover');
});

imagePreviewDiv.addEventListener('dragleave', (e) => {
    e.preventDefault();
    e.stopPropagation();
    imagePreviewDiv.classList.remove('dragover');
});

imagePreviewDiv.addEventListener('drop', (e) => {
    e.preventDefault();
    e.stopPropagation();
    imagePreviewDiv.classList.remove('dragover');

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        selectedFile = files[0];
        previewImageFromFile(selectedFile);
    }
});

// 预览从拖拽上传的文件
function previewImageFromFile(file) {
    if (file) {
        addMessageToBox(`选中的图片文件名：${file.name}`);

        const reader = new FileReader();
        reader.onload = function (e) {
            const imageElement = document.createElement('img');
            imageElement.src = e.target.result;
            imageElement.style.width = "100%";
            imageElement.style.height = "100%";
            imageElement.style.objectFit = "cover";

            const imagePreviewDiv = document.getElementById('imagePreview');
            imagePreviewDiv.innerHTML = '';
            imagePreviewDiv.appendChild(imageElement);
        };
        reader.readAsDataURL(file);
    }
}
=======
    const messageBox = document.getElementById('messageBox');
    const messageElement = document.createElement('p');
    messageElement.textContent = message;
    messageBox.appendChild(messageElement);
}
>>>>>>> f30e8c53672116fdef800be7ef7885daca1352c8
