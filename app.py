# -*- coding: utf-8 -*-
from flask import Flask
from views import index_page


app = Flask(__name__)


app.add_url_rule('/', view_func=index_page)


if __name__ == '__main__':
    app.run()
