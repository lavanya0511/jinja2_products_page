from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy_database import Base,engine,LocalSession
from sqlalchemy_models import Products

api = FastAPI()
Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@api.get("/",response_class=HTMLResponse)
def home(req:Request):
    return templates.TemplateResponse(request=req,name="home.html")

@api.get("/login",response_class=HTMLResponse)
def login_page(req:Request):
    return templates.TemplateResponse(request=req,name="login.html")

@api.post("/login",response_class=HTMLResponse)
def login_submit(req:Request):
    return templates.TemplateResponse(request=req,name="login.html")

@api.get("/register",response_class=HTMLResponse)
def register_page(req:Request):
    return templates.TemplateResponse(request=req,name="register.html")

@api.post("/register",response_class=HTMLResponse)
def register_submit(req:Request):
    return templates.TemplateResponse(request=req,name="register.html")

@api.get("/products",response_class=HTMLResponse)
def products_page(req:Request):
    db = LocalSession()
    products = db.query(Products).all()
    db.close()
    return templates.TemplateResponse(request=req,name="products.html",context={"products":products})
