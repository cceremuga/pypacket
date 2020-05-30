#!/usr/bin/env python3

import signal
import time

from pypacket.util.logger import Logger
from pypacket.base.receiver import Receiver
from pypacket.base.configuration import Configuration
from pypacket.util.colors import Colors
from dotenv import load_dotenv


def sigint_handler(sig, frame):
    pypacket_receiver.stop()


print(Colors.GREEN + """
  ___      ___         _       _
 | _ \_  _| _ \__ _ __| |_____| |_
 |  _/ || |  _/ _` / _| / / -_)  _|
 |_|  \_, |_| \__,_\__|_\_\___|\__|
      |__/
""" + Colors.RESET)

# Load envs.
load_dotenv()

# Configure logging.
log_handler = Logger()

# Initialize configuration.
runtime_configuration = Configuration()

# The main runner.
pypacket_receiver = Receiver(log_handler, runtime_configuration)
pypacket_receiver.start()

# Handles SIGINT interrupts, exiting the main loop and threads.
signal.signal(signal.SIGINT, sigint_handler)

try:
    while True:
        time.sleep(.05)
except KeyboardInterrupt:
    pypacket_receiver.stop()
