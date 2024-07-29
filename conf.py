# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import glob, subprocess, sys, time, os, json

# -- Project information -----------------------------------------------------

project = 'Mirte Workshops'
#copyright = '2023, Martin Klomp, TU Delft Robotics Institute'
articles_settings = json.loads(open('_static/js/articles.json').read())

lang = articles_settings["default_language"]  # default language
for lang_opt in articles_settings["languages"]:
    print("Checking for lang: " + str(lang_opt))
    # print(tags.tags)
    if(f'lang_{lang_opt["short"]}' in tags.tags.keys()):
        lang = lang_opt["short"]
        print(f"Found lang: {lang}")
# if 'lang_en' in tags.tags.keys():
#     lang = 'en'

# For multi-lang, copy article.{lang}.rst to article.rst


for article in articles_settings["articles"]:
    try:
        with open(f'docs/{article}/{article}.{lang}.rst') as f_lang:
            with open(f'docs/{article}/{article}.rst', 'w') as f_dest:
                f_dest.write(f_lang.read())
    except Exception as e:
        print(e)
        print("missing article file for " + article)


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.video', 'sphinx_design']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

# don't build the original language files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_modules', 'docs-env', *[f'**/*.{x["short"]}.rst' for x in articles_settings["languages"] ]]


# intl
# locale_dirs = glob.glob('./docs/*/_locale/')
# locale_dirs.append('locale/')
# print(locale_dirs)
gettext_compact = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
author = 'Martin Klomp'
html_theme = 'sphinx_book_theme'
html_title = "Mirte Workshops"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_js_files = ['js/custom.js']

html_css_files = [
      "css/custom.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/css/bootstrap.min.css",
]

## For Book Theme
html_context = {
   "mode": "darky",
   "github_repo": "mirte-workshops",
   "github_user": "mirte-robot"
}

# Try to update from git
try:
    output = subprocess.check_output(["git ls-remote --get-url origin"], shell=True).decode(sys.stdout.encoding)
    parts = str(output).split(".com/")[1].split("/")
    html_context["github_repo"] = parts[1].split(".git")[0]
    html_context["github_user"] = parts[0]
    html_context['github_version'] = str(subprocess.check_output(["git rev-parse --abbrev-ref HEAD"], shell=True).decode(sys.stdout.encoding)).strip() + "/"
except Exception as e:
    print("Could not get git information: " + str(e))

html_theme_options = {
    "use_download_button": False,
    "repository_url": f'https://github.com/{html_context["github_user"]}/{html_context["github_repo"]}',
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "use_fullscreen_button": False,
    "extra_footer": f"&copy; 2024, Martin Klomp {time.time()}, <a href='https://tudelftroboticsinstitute.nl/'>TU Delft Robotics Institute</a>",
}


linkcheck_ignore = [r'^http://$', r'^http://mirte.local.*', r'.*localhost.*', r'.*192.168.4.*']
linkcheck_anchors_ignore_for_url = [
   
]
language = lang