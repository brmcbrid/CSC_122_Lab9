# Tests for Lab7
# Print Largest & Smallest Value & Index in a List

import os.path
import sys
from Lab7 import main
from tud_tests import *

def test_Lab7():

    try:
        exists = os.path.exists("Lab7.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input([])
    main()
    output = get_display_output()

    assert output == [
        "The highest sensor value read is at index 7 and is 99.77",
        "The lowest sensor value read is at index 12 and is -88.42"
        ]
"""
    # Test 2
    sensor=[276.25, 185.45, -521.90, 99.34, 72.20, -65.90, 666.33, 99.77, 88.5,
            -44.12, 45.75, 57.77, -88.42, 99.47, 75.75, 88.45, 65.64, 77.21, -24,62]
    highSensor=findLargest(sensor) # calling findLargest and passing sensor list
    lowSensor=findSmallest(sensor) # calling findSmallest and passing sensor list
    print(f"The highest sensor value read is at index {highSensor[1]} and is {highSensor[0]}")
    print(f"The lowest sensor value read is at index {lowSensor[1]} and is {lowSensor[0]}")
    output = get_display_output()

    assert output == [
        "The highest sensor value read is at index 6 and is 666.33",
        "The lowest sensor value read is at index 2 and is -521.9"
        ]
"""