# main.py — news-image-20261124 v4 (Python 3.13, standard library only).
# The entry image is the entry.png beside this file; the program copies it
# to /output/entry.png. No network, no rendering at grade time: a byte copy
# is deterministic by construction, so two runs write identical bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # copyfile (not copy2): only the bytes travel, never file metadata,
    # so the output cannot differ between runs.
    shutil.copyfile(os.path.join(here, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
