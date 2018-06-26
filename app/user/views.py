from flask import request, Blueprint, jsonify, render_template
from flask_mail import Message

from app.ext import db, mail
from app.user.models import User


user=Blueprint('user',__name__)

'''
username
password
email
is_active  1激活 0 未激活
'''

@user.route('/register/',methods=['POST','GET'])
def register():
    result={}
    if request.method=='GET':
        return render_template('res.html')

    if request.method=='POST':
        username=request.values.get('username')
        password=request.values.get('password')
        email=request.values.get('email')
        if username and password and email:
            user = User.query.filter(User.username == username or User.email == email).all()
            if user:
                result.update(msg='账号或者邮箱已经存在', status=-2)
            else:
                user = User(username=username, password=password, email=email)
                db.session.add(user)
                db.session.commit()
                msg = Message("Hello",
                              sender="13248400243@163.com",
                              recipients=['13248400243@163.com'])
                mail.send(msg)
        else:
            result.update(msg='必要参数不能为空', status=-1)

    else:
        result.update(msg='错误的请求方式',status=400)
    return jsonify(result)




