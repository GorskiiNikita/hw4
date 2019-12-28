# -*- coding: utf-8 -*-
import os
from flask import render_template
from settings import PATH_TO_IMAGES


def index_page():
    for file in os.walk(PATH_TO_IMAGES):
        images = file[2]

    return render_template('index.html', images=images)
