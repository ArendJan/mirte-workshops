import json

# Open the articles.json file
with open('_static/js/articles.json') as file:
    # Parse the JSON data
    data = json.load(file)

# get current script path
import os
script_path = os.path.dirname(os.path.realpath(__file__))
root = os.path.join(script_path, '..')
err_count = 0
# for every article and every language, check that the file exists
for article in data['articles']:
    for lang in data['languages']:
        # Check if the file exists
        try:
            with open(f'{root}/docs/{article}/{article}.{lang["short"]}.rst') as file:
                print("File exists: " + f'docs/{article}/{article}.{lang["short"]}.rst')
                pass
        except FileNotFoundError:
            print(f'::error title=::docs/{article}/{article}.{lang["short"]}.rst missing')
            err_count += 1
    # check that the main file does not exist
    try:
        with open(f'{root}/docs/{article}/{article}.rst') as file:
            print(f'::error title=::docs/{article}/{article}.rst should not exist')
            err_count += 1
    except FileNotFoundError:
        print("File doesn't exists(good): " + f'docs/{article}/{article}.rst')

        pass


if err_count > 0:
    print(f'::error title=::{err_count} missing files')
    exit(1)