#!/usr/bin/env python

import threading
import subprocess
import re
import time
import sys

# PyPacket base functionality.

class PyPacket:

    def __init__(self):
        self.sub_processes = {}
        self.start()
        self.is_running = True
        self.worker_thread = threading.Thread(target=self.multimon_worker)
        self.worker_thread.setDaemon(True)
        self.worker_thread.start()

    def start(self):
        # Start rtl_fm subprocess which listens for APRS signals.
        print "Starting rtl_fm subprocess."
	
        rtl_subprocess = subprocess.Popen(
            ['rtl_fm', '-f', '144390000', '-s', '22050', '-o', '4', 
            '-g', '49.6', '-'],
            stdout=subprocess.PIPE, stderr=open('/dev/null'))

        # Start multimon-ng subprocess which decodes APRS data.
        print "Starting multimon-ng subprocess."
		
        multimon_subprocess = subprocess.Popen(
            ['multimon-ng', '-a', 'AFSK1200', '-A', '-t', 'raw', '-'],
            stdin=rtl_subprocess.stdout,
            stdout=subprocess.PIPE, stderr=open('/dev/null'))

        # Push subprocesses into collection.
        self.sub_processes['rtl'] = rtl_subprocess
        self.sub_processes['multimon'] = multimon_subprocess

    def stop(self):
        self.sub_processes['rtl'].terminate()
        self.sub_processes['multimon'].terminate()
        print '\n\nTerminate command received, exiting!'
        sys.exit(0)

    def multimon_worker(self):
        # This worker lives in its own thread and processes received packets.
        print "Worker thread starting.\n"

        while self.is_running:
            multimon_line_output = self.sub_processes['multimon'].stdout.readline().strip()
            
            # The first 6 characters are not valid APRS packet pieces, so remove them.
            aprs_match = re.compile(r'^APRS: (.*)').match(multimon_line_output)
            if aprs_match:
                print "[Packet] %s" % aprs_match.group(1)

# Main run loop.

print """
  ___      ___         _       _   
 | _ \_  _| _ \__ _ __| |_____| |_ 
 |  _/ || |  _/ _` / _| / / -_)  _|
 |_|  \_, |_| \__,_\__|_\_\___|\__|
      |__/                         
"""
print "Initializing startup sequence."
pypacket_runner = PyPacket()

try:
    while True:
        time.sleep(.05)
except KeyboardInterrupt:
    pypacket_runner.stop()
