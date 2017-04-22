#!/usr/bin/env python

import time
from pypacket.util.logger import Logger
from pypacket.base.listener import Listener
from pypacket.base.deserialization import Deserialization
from pypacket.base.configuration import Configuration
from pypacket.util.colors import Colors

print(Colors.GREEN + """
  ___      ___         _       _
 | _ \_  _| _ \__ _ __| |_____| |_
 |  _/ || |  _/ _` / _| / / -_)  _|
 |_|  \_, |_| \__,_\__|_\_\___|\__|
      |__/
""" + Colors.RESET)

# Configure logging.
log_handler = Logger()

# Initialize configuration.
runtime_configuration = Configuration()

# Initialize deserialization.
deserializer = Deserialization()

# The main runner.
pypacket_runtime = Listener(log_handler, deserializer, runtime_configuration)

# Handles Control+c interrupts, existing the main loop and threads.
try:
    while True:
        time.sleep(.05)
except KeyboardInterrupt:
    pypacket_runtime.stop()
