#!/usr/bin/env python

import time
from time import localtime, strftime
import logging
from pypacket.base.listener import Listener
from pypacket.util.colors import Colors

print(Colors.GREEN + """
  ___      ___         _       _
 | _ \_  _| _ \__ _ __| |_____| |_
 |  _/ || |  _/ _` / _| / / -_)  _|
 |_|  \_, |_| \__,_\__|_\_\___|\__|
      |__/
""" + Colors.RESET)

# Configure logging.
logFormat = '[%(asctime)-15s] [%(levelname)s] %(message)s'
logging.basicConfig(filename='logs/pypacket_' + \
    strftime("%Y_%m_%d_%H_%M_%S", localtime()) + '.log', \
    format=logFormat, level=logging.INFO)

# The main runner.
pypacket_runtime = Listener()

# Handles Control+c interrupts, existing the main loop and threads.
try:
    while True:
        time.sleep(.05)
except KeyboardInterrupt:
    pypacket_runtime.stop()
