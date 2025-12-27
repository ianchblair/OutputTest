#
# output_test.py
#
# Tester for Pico module to toggle LED
#
# (c) Ian Blair 16th. November 2025
#

from machine import Pin, Timer
import pindefs_Pico0203 as pindefs
import time

# Set up instance of timer object
#
tim=Timer()

_OUTPUT_ON_TIME = const(500)


# Set up output pin objects
#

# Test LED
testPin=Pin(pindefs.PIN_TST_LED,Pin.OUT)

# CBUS LEDs
#LedYelPin=Pin(pindefs.PIN_LED_YEL,Pin.OUT)
#LedGrnPin=Pin(pindefs.PIN_LED_GRN,Pin.OUT)
#LedRedPin=Pin(pindefs.PIN_LED_RED,Pin.OUT)

TST_OPS = [pindefs.PIN_LED_YEL, pindefs.PIN_LED_GRN, pindefs.PIN_LED_RED]

PIN_OPS = [pindefs.PIN_OP_0,
           pindefs.PIN_OP_1,
           pindefs.PIN_OP_2,
           pindefs.PIN_OP_3,
           pindefs.PIN_OP_4,
           pindefs.PIN_OP_5,
           pindefs.PIN_OP_6,
           pindefs.PIN_OP_7,
           pindefs.PIN_OP_8,
           pindefs.PIN_OP_9,
           pindefs.PIN_OP_10,
           pindefs.PIN_OP_11,
           pindefs.PIN_OP_12,
           pindefs.PIN_OP_13,
           pindefs.PIN_OP_14,
           pindefs.PIN_OP_15]

# Test LEDs        
_tst_pin = [(Pin(TST_OPS[n], Pin.OUT)) for n in range (len(TST_OPS))]

# Output LEDs        
_output_pin = [(Pin(PIN_OPS[n], Pin.OUT)) for n in range (len(PIN_OPS))]

# ***
# Set up initial output values (CBUS all on, others all off)

testPin.value(1)

# Outputs are in TST_OPS list...
for n in range (len(TST_OPS)):
    _tst_pin[n].value(1) 

# Outputs are in PIN_OPS list...
# ***
# Set up initial output values (all off)
for n in range (len(PIN_OPS)):
    _output_pin[n].value(0)
    
time.sleep_ms(_OUTPUT_ON_TIME)
      
# Clear outputs are in TST_OPS list...
for n in range (len(TST_OPS)):
    _tst_pin[n].value(0) 
      
# *** end of initialisation

#while True:
for l in range (1):
    for m in range (len(TST_OPS)):
        for n in range (len(TST_OPS)):
            if (n==m): tst_value = 1
            else: tst_value = 0
            _tst_pin[n].value(tst_value)
        time.sleep_ms(_OUTPUT_ON_TIME)
        
# Clear outputs are in TST_OPS list...
for n in range (len(TST_OPS)):
    _tst_pin[n].value(0) 
        
#for n in range (len(PIN_OPS)):
#    self._output_pin[PIN_OPS(n)].value(0) 
      
# *** end of initialisation
        
# *** Now enter main loop
# This runs indefintely
for l in range (10):        
#while True:
    for m in range (len(PIN_OPS)):
        for n in range (len(PIN_OPS)):
            if (n==m): output_value = 1
            else: output_value = 0
            _output_pin[n].value(output_value)
        time.sleep_ms(_OUTPUT_ON_TIME)
        
# Clear outputs are in TST_OPS list...
for n in range (len(PIN_OPS)):
    _output_pin[n].value(0) 

# Turn on LED to show that we have finished
_tst_pin[0].value(1) 

