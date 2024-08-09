from .common import register_common_handler
from .user import register_user_handler
from .lesson import register_lesson_handler
from .study import register_study_handler
from .dicts import register_dict_handler
from .tools import register_tools_handler
from .order import register_order_handler
from .callback import register_callback_handler


def register_route(app):
    prefix = app.config.get('PATH_PREFIX','')
    app = register_common_handler(app)
    app = register_user_handler(app,prefix+'/user')
    app = register_lesson_handler(app,prefix+'/lesson')
    app = register_study_handler(app,prefix+'/study')
    app = register_dict_handler(app,prefix+'/dict')
    app = register_tools_handler(app,prefix+'/tools')
    app = register_order_handler(app,prefix+'/order')
    app = register_callback_handler(app,prefix+'/callback')
    return app