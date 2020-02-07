from flask import send_file, make_response

from utils import add_watermark


def generate_copyright(img):
    image = add_watermark('static/img/original/', img, 'ХуЙ')

    response = make_response(image)
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set(
        'Content-Disposition', 'inline')

    return response
