import uuid

class Config():
    DEBUG = False
    SECRET_KEY = '123456'

#生成数据库连接
def get_db_uri(database: dict):
    user = database.get('USER') or 'root'
    password = database.get('PASSWORD') or '123456'
    host = database.get('HOST') or '127.0.0.1'
    port = database.get('PORT') or '3306'
    name=database.get('NAME')
    db = database.get('DB') or 'mysql'
    driver = database.get('DRIVER') or 'pymysql'
    charset = database.get('CHARSET') or 'utf8'
    return '{}+{}://{}:{}@{}:{}/{}?charset={}'.format(db, driver, user, password, host, port, name,charset)


#开发环境配置
class DevelopConfig(Config):
    DEBUG = True
    DATABASES={
        'NAME':'tpp',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASES)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #邮箱配置
    MAIL_SERVER='smtp.163.com'

    MAIL_USERNAME='13248400243@163.com'
    MAIL_PASSWORD='mo888888'



#项目上线配置
class ProductConfig(Config):
    DEBUG=False
    DATABASES = {
        'DB':'mysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'tpp',
        'DRIVER': 'pymysql',
        'CHARSET': 'utf8',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASES)


env={
    #开发环境
    'dev':DevelopConfig,
    'pro':ProductConfig
}

