from flask import Flask

from app.apis import register_blue
from app.ext import init_ext
from app.settings import env

app=Flask(__name__)

def create_app(env_name):
    #从配置对象来加载对象
    app.config.from_object(env.get(env_name))
    init_ext(app)
    register_blue(app)
    return app