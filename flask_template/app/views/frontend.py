from flask import current_app, Blueprint, render_template, g, url_for
# frontend = Blueprint('frontend', __name__, url_prefix='/frontend')
bp = Blueprint('frontend', __name__, url_prefix='/<lang_code>')


@bp.url_defaults
def add_language_code(endpoint, values):
    print('调用 url_for（） 执行')
    values.setdefault('lang_code', g.lang_code)

    # if 'lang_code' in values or not g.lang_code:
    #     return
    # if bp.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
    #     values['lang_code'] = g.lang_code


@bp.url_value_preprocessor
def pull_lang_code(endpoint, values):
    print('预处理：', endpoint, values)
    g.lang_code = values.pop('lang_code')


@bp.route('/')
def index():
    print('首页： /')
    print('url:', url_for('.index'))
    return '首页  /'


@bp.route('/about')
def about():
    print('/about')
    # print(g.lang_code)
    return '/about'
