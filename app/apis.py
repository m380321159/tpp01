from flask import Blueprint, Flask

from app.user.views import user


def register_blue(app:Flask):
    app.register_blueprint(user,url_prefix='/user')