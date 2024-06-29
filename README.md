## Fast API Example

this project is a example applicacion using python fast

### Installation

```
git clone https://github.com/adriavend/fast-api
cd fast-api
python -m venv venv
.\venv\Scripts\activate
pip install fastapi uvicorn
pip install -r requirements.txt
```

### Run Application (reload)
* with realod
  > uvicorn main:app --port 5000
* locally
  > uvicorn main:app --host 0.0.0.0 --port 5000 --reload

### OpenAPI docs - Swagger
* http://localhost:5000/docs
* http://localhost:5000/redoc
