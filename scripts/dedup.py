


# open all .html files in build/html/en and change "images/" to "../images/" and "_static/" to "../_static/"

import os, json, shutil

script_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.abspath( f'{script_path}/../_static/js/articles.json')) as file:
    # Parse the JSON data
    articles_data = json.load(file)


def dedup_one(lang):

    folder_path = os.path.abspath( f'{script_path}/../_build/html/{lang}')
    html_files = []
    for root, dirs, files in list(os.walk(folder_path)):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))


    # replace "images/" with "../images/" and "_static/" with "../_static/"
    for file in html_files:
        with open(file, 'r+') as f:
            t = f.read()
            t = t.replace("_images/", "../_images/").replace("_static/", "../_static/")
            f.seek(0)
            f.write(t)
            f.truncate()

    # delete _images and _static
    shutil.rmtree(f'{folder_path}/_images')
    shutil.rmtree(f'{folder_path}/_static')

for lang in articles_data["languages"]:
    if(lang["short"] != articles_data["default_language"]):
        dedup_one(lang["short"])