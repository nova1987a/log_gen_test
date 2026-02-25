#!/usr/bin/python3

import pytest
import sys

def run_framework():
    print("\U0001F680 Start automated framework...")

    # 定義執行參數
    args = [
        "tests/",                     # test path
        "--html=reports/report.html", # generate HTML report
        "--self-contained-html",      # the report includes CSS
        "--reruns", "2",              # retry 2 times if failed
        "--reruns-delay", "5",        # retry interval is 5 sec.
        "-v"                          # detail mode
    ]

    # execute pytest
    exit_code = pytest.main(args)

    if exit_code == 0:
        print("\U00002705 all test PASS！")
    else:
        print(f"\U0000274C Test ends，some failed (Exit Code: {exit_code})")

if __name__ == "__main__":
    run_framework()
