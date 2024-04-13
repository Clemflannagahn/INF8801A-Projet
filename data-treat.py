import os
import re

DATA = 'data'
PHOTOS = DATA + '/photos'
SKETCHES = DATA + '/sketches'


def get_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


RENAME = True
if RENAME:
    for p in get_files(PHOTOS):
        f = os.path.join(PHOTOS, p)
        name = f
        # Women
        name = re.sub('f-', 'F-', name)
        name = re.sub('f1-', 'F1-', name)
        # Men
        name = re.sub('m-', 'M-', name)
        name = re.sub('m1-', 'M1-', name)
        os.rename(f, name)

    for s in get_files(SKETCHES):
        f = os.path.join(SKETCHES, s)
        name = f
        name = re.sub('f-', 'F-', name)
        name = re.sub('F2-', 'F-', name)
        name = re.sub('f1-', 'F1-', name)

        name = re.sub('m-', 'M-', name)
        name = re.sub('M2-', 'M-', name)
        name = re.sub('m1-', 'M1-', name)
        os.rename(f, name)
