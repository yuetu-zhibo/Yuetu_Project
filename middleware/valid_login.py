from functools import wraps

from flask import request, jsonify


def is_login(fun):
    print(fun.__name__)
    @wraps(fun)    # 装饰器修复技术
    def wrapper(*args, **kwargs):
        print(request.path)
        userid = request.args.get('userid')
        print('userid', userid)
        if userid is None:
            return jsonify({
                'status': 0,
                'msg':'No Authorization'
            })

        return fun(*args, **kwargs)
    return wrapper