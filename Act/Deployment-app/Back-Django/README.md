# Django API for Deep Learning Model

This is a simple Django REST API to serve predictions from a deep learning model.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Usage

Send a POST request to:
```
http://127.0.0.1:8000/predict/
```

With JSON data:
```json
{
  "input": [1.0, 2.0, 3.0]
}
```
