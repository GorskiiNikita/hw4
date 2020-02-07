# -*- coding: utf-8 -*-
from flask import Flask
from views import index_page, generate_copyright


app = Flask(__name__)


app.add_url_rule('/', view_func=index_page)
app.add_url_rule('/copyright/<img>', view_func=generate_copyright)


if __name__ == '__main__':
    app.run(port=5001)
