from flask import current_app, Blueprint, render_template, g, url_for
ho = Blueprint('index', __name__)


@ho.route('/')
def index():
    print('>>> request this index page')
    print('def index()')
    print('url:', url_for('.index'))  # 会提前调用url_defaults
    return render_template(current_app.config['INDEX_TEMPLATE'])

