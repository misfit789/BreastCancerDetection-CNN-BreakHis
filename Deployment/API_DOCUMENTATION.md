# API Documentation

This API supports single image prediction operation.

## Upload Image

**POST** `/upload_image`

User can upload an image to the server. The image will be stored and used for later prediction operation.

- Request
    - Body
        - Image file (required): Uses `File` parameter to upload the image.
- Response
    - A confirmation message indicating the successful upload.

## Get Random Image

**GET** `/get_random_image`

User can get a random image from the server.

- Request
    - None
- Response
    - Image information in JSON format including:
        - Base64 encoded image
        - Image file name
        - The label of the image

## Get Prediction

**GET** `/get_prediction`

Predicts the image stored in the server.

- Request
    - None
- Response
    - The predicted class of the image
    - Confidence level of the prediction

If no image is found in the server, a 400 error with a message will be returned.
Please upload a new image for each prediction.