import datetime
from functools import wraps
from flask import Flask, request, jsonify, make_response
from ..service.common import AppException
import json
import traceback


by_pass_login_func = []

# 装饰器函数，用于跳过Token校验
def bypass_token_validation(func):
    by_pass_login_func.append(func.__name__)
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('bypass_token_validation')
        return func(*args, **kwargs) 
    return wrapper

def register_common_handler(app:Flask)->Flask:
    @app.errorhandler(AppException)
    def handle_invalid_usage(error:AppException):
        response = jsonify({'code': error.code, 'message': error.message})
        response.status_code = 200
        return response
    
    @app.errorhandler(Exception)
    def handle_invalid_exception(error:Exception):
        app.logger.error(traceback.format_exc())
        response = jsonify({'code': -1, 'message':"系统异常"})
        response.status_code = 200
        return response
    return app


def fmt(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()
    else:
        return o.__json__()
def make_common_response(data):
    response = json.dumps({'code':0,'message': 'success','data': data},default=fmt,ensure_ascii=False)
    return response