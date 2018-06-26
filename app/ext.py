from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

def init_ext(app):
    init_db(app)
    init_main(app)


#配置数据库的ORM框架
db=SQLAlchemy()

#数据库迁移对象
migrate=Migrate()


#封装配置数据库接口
def init_db(app):
    db.init_app(app=app)
    migrate.init_app(app,db)

#邮箱的配置

mail=Mail()

#封装配置邮箱接口
def init_main(app):
    mail.init_app(app)