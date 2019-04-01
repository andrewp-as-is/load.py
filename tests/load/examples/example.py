#!/usr/bin/env python
import load
import os

for filename in ["source1.py", "source2.py"]:
    path = os.path.join(os.path.dirname(__file__), "sources", filename)
    module = load.load(filename, path)
    print(module)
