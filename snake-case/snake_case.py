import os
import sys
import re

def snakify(filename):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', filename)
    s1.replace('__', '_')
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

fn = sys.argv[1]
if os.path.exists(fn):
    print "path exists: " + fn
    for filename in os.listdir(fn):
        renamed = snakify(filename)
        os.rename(fn + "/" + filename, os.path.join(fn, renamed))
        print "renaming " + filename + "->" + renamed
