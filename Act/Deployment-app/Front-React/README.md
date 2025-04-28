# React Frontend for Deep Learning Model API

This is a simple React application to interact with a Django REST API serving predictions from a deep learning model.

## Setup

```bash
npm install
npm start
```

The app will start on:

```
http://localhost:3000
```

## Usage

- Fill the input form with your data.
- Click the **Predict** button.
- The app sends a POST request to:

```
http://127.0.0.1:8000/predict/
```

- The prediction result from the API will be displayed on the page.

## Notes

- Make sure the Django API is running at `http://127.0.0.1:8000/`.
- You can modify the API URL in the React project if needed.


