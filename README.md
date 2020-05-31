<p align="center"><img src="https://i.imgur.com/HvhAWed.png" width="500" height="auto" /></p>


A modular, framework-first, python [APRS](http://www.aprs.org/) logger for low cost [RTL-SDR](http://osmocom.org/projects/sdr/wiki/rtl-sdr) devices. Now with APRS-IS support!

[![Build Status](https://travis-ci.org/cceremuga/pypacket.svg?branch=master)](https://travis-ci.org/cceremuga/pypacket) [![Coverage Status](https://coveralls.io/repos/github/cceremuga/pypacket/badge.svg?branch=master)](https://coveralls.io/github/cceremuga/pypacket?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/55cfa693d652488e994b6782fed2eccc)](https://www.codacy.com/manual/cceremuga_3/pypacket?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cceremuga/pypacket&amp;utm_campaign=Badge_Grade) [![Requirements Status](https://pyup.io/repos/github/cceremuga/pypacket/shield.svg)](https://pyup.io/account/repos/github/cceremuga/pypacket/) [![Requirements Status](https://pyup.io/repos/github/cceremuga/pypacket/python-3-shield.svg)](https://pyup.io/account/repos/github/cceremuga/pypacket/) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

## Requirements

The following are required to be installed and configured on your system.

* An RTL-SDR compatible device.
* Some form of Unix-like system. I build it on Mac OS. I run it on a Raspberry Pi w/ Raspbian.
* Python >= v3.6
* [rtl_fm](http://osmocom.org/projects/sdr/wiki/rtl-sdr)
* [multimon-ng](https://github.com/EliasOenal/multimon-ng)
* A callsign login and password for APRS-IS to upload spots (optional).

## Setup

* `config/configuration.json` contains all insecure runtime configuration settings.
* If you want to upload spots to APRS-IS, ensure you have the following environment variables set:
    * `PYPACKET_USERNAME` - Your call sign for APRS-IS.
    * `PYPACKET_PASSWORD` - Your password for APRS-IS.
    * `PYPACKET_LATITUDE` - The latitude of the IGate running PyPacket. Optional.
    * `PYPACKET_LONGITUDE` - The longitude of the IGate running PyPacket. Optional.
    * Rename `.env.example` to `.env` and fill in the appropriate values.
    * See the security notes section below for situational awareness.
* Run `pip install -r requirements.txt`

## Usage

* Run `./main.py`.
    * The application will start and immediately begin listening on the configured frequency.
    * Logged packets will be output to your terminal, written to a file in the `logs` directory, and (if configured) uploaded to APRS-IS.

## Release Notes

* 5/31/2020 (v5.0)
    * Thank you to everyone who contributed bug reports, enhancements, and pull requests!
    * Support for squelch level and PPM error configuration options.
    * SIGINT is now properly handled, exiting subprocesses before terminating main thread.
    * If configured with latitude and longitude, will transmit an IGate beacon to APRS-IS every X minutes (defaulted to 10, configurable).
    * CLI packet handler has been moved to its own processor class.
    * New readme logo.
* 5/6/2020 (v4.1)
    * Simple flat file environment variable support via python-dotenv.
* 11/17/2019 (v4.0)
    * All new tabular CLI UI for packet output.
    * Can now be configured to have N processors.
    * Configuration format improvements.
    * New dependencies, be sure to `pip install -r requirements.txt`.
    * Resolves bug #11 where an rtl_fm startup crash was not being detected, causing excessive CPU usage.
* 11/9/2019 (v3.2)
    * Some configuration variables changed names.
    * Code cleanup, test cleanup, etc.
    * Quality reports via Codacy.

## Contributing

You are welcome to contribute by submitting pull requests on GitHub if you would like. Feature / enhancement requests may be submitted via GitHub issues.

## Security Notes

**APRS is never private and never secure.** APRS messages are transmitted on amateur radio frequencies in plaintext for anyone to read. **Connections to APRS-IS are insecure and only intended for licensed amateur radio operators.**

## Credits

* Inspired by the excellent [pymultimonaprs](https://github.com/asdil12/pymultimonaprs) project. I more or less learned basic Python threading by studying their work. Huge thanks to them!
* Radio tower icon found in the logo courtesy of [The Noun Project](https://thenounproject.com/search/?q=radio%20tower&i=749293).
* [ ~ Dependencies scanned by PyUp.io ~ ]
