# compiling
```
$ python3 -m venv docs-env
$ source docs-env/bin/activate
(docs-env)$ pip install -r requirements.txt
(docs-env)$ make build_lang
(docs-env)$ python3 -m http.server


$ firefox _build/html/index.html
```

requires python3.10 for sphinx==7.4.7

# Languages

make build_lang will invoke scripts/build.py. This will run sphinx-build for every language in the _static/js/articles.json file. /{lang.shortcode}/ for all except default, / for default language.
Then all the static and images folders are deleted from the non-default folders. All html files are rewritten to link to the original ones.

## Add language
add it to _static/js/articles.json
add all translations

## articles
every article that is translated, is stored as {name}.{lang.shortcode}.rst. Just before compiling, they are copied to {name}.rst.