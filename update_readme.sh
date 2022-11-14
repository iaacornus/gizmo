#!/usr/bin/env bash

assets/misc/scripts/./update_proj_structure.sh
python assets/misc/scripts/replace_spec_char.py

git add README
git commit -m "update project structure documentation"
