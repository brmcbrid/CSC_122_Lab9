# Tests for Lab9
# Check for Integer String

import os.path
import sys
from Lab9 import main
from tud_tests import *

def test_Lab9():

    try:
        exists = os.path.exists("Lab9.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input(["1995"])
    main()
    output = get_display_output()

    assert output == ["","yes"]


    # Test 2
    set_keyboard_input(["42,000"])
    main()
    output = get_display_output()

    assert output == [
        "","no"
        ]

    # Test 3
    set_keyboard_input(["1995!"])
    main()
    output = get_display_output()

    assert output == [
        "","no"
        ]

    # Test 4
    set_keyboard_input(["93875"])
    main()
    output = get_display_output()

    assert output == [
        "","yes"
        ]
