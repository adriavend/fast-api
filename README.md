## Fast API Example

this project is a example applicacion using python fast

### create virtual evn
> python -m venv venv

### activate venv
> .\venv\Scripts\activate

### install libs
> pip install fastapi uvicorn

### run app (reload)
> uvicorn main:app --port 5000
## run app locally
> uvicorn main:app --host 0.0.0.0 --port 5000 --reload

### OpenAPI docs - Swagger
http://localhost:5000/docs
http://localhost:5000/redoc

### generate requirements.txt
pip freeze > requirements.txt

### install requirements.txt
pip install -r requirements.txt
