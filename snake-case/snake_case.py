import os
import sys
import re

def snakify(filename):
    filename = filename.replace('__', '_')
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', filename)
    re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    s1.replace('__', '_')
    return s1
fn = sys.argv[1]
if os.path.exists(fn):
    print "path exists: " + fn
    for filename in os.listdir(fn):
        renamed = snakify(filename)
        os.rename(fn + "/" + filename, os.path.join(fn, renamed))
        print "renaming " + filename + " -> " + renamed
