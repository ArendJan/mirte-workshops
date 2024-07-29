import json, sys

# Open the articles.json file
with open('_static/js/articles.json') as file:
    # Parse the JSON data
    data = json.load(file)

# arg1 = list of changed files

changed_files = sys.argv[1] 
normal_text = bool(sys.argv[2]) # 0: for ci, 1 for comment
changed_files = changed_files.split(" ")
# print("Changed files: " + str(changed_files))
warn_count = 0
# for every article, check that if one of the files is changed, all are changed
for article in data['articles']:
    article_files = []
    for lang in data['languages']:
        article_files.append(f'docs/{article}/{article}.{lang["short"]}.rst')
    # print("Article files: " + str(article_files))
    are_changed = [file in changed_files for file in article_files]

    if any(are_changed) and not all(are_changed):
        warn_count += 1
        if normal_text:
            print(f'All files for article **"{article}"** should be changed. Please check!')
        else:
            print(f'::warning title=::All files for article {article} should be changed')


if warn_count == 0:
    print("No articles are partially changed (language) :thumbsup:")