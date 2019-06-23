from flask import current_app, Blueprint, render_template, g, url_for
admin = Blueprint('admin', __name__, url_prefix='/admin')


# @admin.url_defaults
# def add_language_code(endpoint, values):
#     print('调用 url_for（） 执行')
#     if 'lang_code' in values or not g.lang_code:
#         return
#     if admin.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
#         values['lang_code'] = g.lang_code


# @admin.url_value_preprocessor
# def pull_lang_code(endpoint, values):
#     print('预处理:', endpoint, values)
#     g.lang_code = values.pop('lang_code', None)


@admin.route('/')
def index():
    print('def index()')
    print('url:', url_for('.index'))  # 会提前调用url_defaults
    return render_template(current_app.config['INDEX_TEMPLATE'])

