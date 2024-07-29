
import json, os

# Open the articles.json file
with open('_static/js/articles.json') as file:
    # Parse the JSON data
    data = json.load(file)

for lang in data['languages']:
    if(lang["short"] != data["default_language"]):
        os.system(f'sphinx-build "." "_build/html/{lang["short"]}" -t lang_{lang["short"]}')
os.system(f'sphinx-build "." "_build/html/" -t lang_{data["default_language"]}')
