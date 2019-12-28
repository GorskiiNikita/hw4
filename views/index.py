# -*- coding: utf-8 -*-
import os
from flask import render_template
from settings import PATH_TO_IMAGES


def index_page():
    images = []
    for file in os.walk(PATH_TO_IMAGES):
        images.append(file[2][0])

    return render_template('index.html', images=images)
