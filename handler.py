import os
from watchdog.events import FileSystemEventHandler
from utils import resize_img, add_watermark


class EventHandler(FileSystemEventHandler):
    def on_moved(self, event):
        old_img_name = event.key[1].split('/')[-1]
        new_img_name = event.key[2].split('/')[-1]
        img_path = 'static/img/'

        try:
            os.rename(f'{img_path}/copyright/{old_img_name}', f'{img_path}/copyright/{new_img_name}')
        except FileNotFoundError:
            pass

        try:
            os.rename(f'{img_path}/small/{old_img_name}', f'{img_path}/small/{new_img_name}')
        except FileNotFoundError:
            pass

        print(event)

    def on_created(self, event):
        img_name = event.src_path.split('/')[-1]
        img_path = 'static/img/'

        resize_img(img_name, f'{img_path}/original/', f'{img_path}/small/')
        add_watermark('ЛЁХА', img_name, f'{img_path}/original/', f'{img_path}/copyright/')

        print(event)

    def on_deleted(self, event):
        img_name = event.src_path.split('/')[-1]
        img_path = 'static/img/'

        try:
            os.remove(f'{img_path}/copyright/{img_name}')
        except FileNotFoundError:
            pass

        try:
            os.remove(f'{img_path}/small/{img_name}')
        except FileNotFoundError:
            pass

        print(event)

    def on_modified(self, event):
        print(event)
