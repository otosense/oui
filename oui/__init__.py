import os
import json
from pathlib import Path

from IPython.display import display, Javascript

pkg_root_dir = os.path.dirname(__file__)
pjoin = lambda *p: os.path.join(pkg_root_dir, *p)
abs_pkg_dir = os.path.realpath(__file__)
root_dir = Path(abs_pkg_dir).parent.parent
js_filename = os.path.join(root_dir, 'js', 'index.js')
with open(js_filename) as js_file:
    js_source = js_file.read()
    display(Javascript(js_source))

data_dirpath = pjoin('data')
djoin = lambda *p: os.path.join(data_dirpath, *p)


def get_pkg_data(filename):
    path = djoin(filename)
    if filename.endswith('.json'):
        return json.load(open(path, 'r'))
    else:
        raise ValueError(f"Unrecognized extension in {path}")

