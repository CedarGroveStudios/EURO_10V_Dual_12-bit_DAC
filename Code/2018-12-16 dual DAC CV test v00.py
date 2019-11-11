# 2018-12-16 dual DAC CV test v00.py
# Simple demo of setting the DAC value up and down through its entire range
# of values.
# Author: Tony DiCola
# 2018-12-16 test of Stemma dual DAC  -- Cedar Grove Studios
#

import board
import busio
import time

import adafruit_mcp4725


# Initialize I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize MCP4725.
dac2 = adafruit_mcp4725.MCP4725(i2c, address=0x62)
dac3 = adafruit_mcp4725.MCP4725(i2c, address=0x63)

# There are a three ways to set the DAC output, you can use any of these:
dac2.value = 65535  # Use the value property with a 16-bit number just like
                   # the AnalogOut class.  Note the MCP4725 is only a 12-bit
                   # DAC so quantization errors will occur.  The range of
                   # values is 0 (minimum/ground) to 65535 (maximum/Vout).

dac2.raw_value = 4095  # Use the raw_value property to directly read and write
                      # the 12-bit DAC value.  The range of values is
                      # 0 (minimum/ground) to 4095 (maximum/Vout).

dac2.normalized_value = 1.0  # Use the normalized_value property to set the
                            # output with a floating point value in the range
                            # 0 to 1.0 where 0 is minimum/ground and 1.0 is
                            # maximum/Vout.

# Main loop will go up and down through the range of DAC values forever.
step_delay = 0.001
while True:
    # Go up the 12-bit raw range.
    print('DAC2 ++> 3.3V, DAC3 --> 0V')
    for i in range(4095):
        dac2.raw_value = i
        dac3.raw_value = 4095 - i
        time.sleep(step_delay)
    # Go back down the 12-bit raw range.
    print('DAC2 --> 03V, DAC3 ++> 3.3V')
    for i in range(4095, -1, -1):
        dac2.raw_value = i
        dac3.raw_value = 4095 - i
        time.sleep(step_delay)