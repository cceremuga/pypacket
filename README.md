<p align="center"><img src="https://i.imgur.com/MZYHAFG.png" /></p>

Receive, decode, log, share [APRS](http://www.aprs.org/) packets using low cost [RTL-SDR](http://osmocom.org/projects/sdr/wiki/rtl-sdr) devices.

[![Build Status](https://travis-ci.org/cceremuga/pypacket.svg?branch=master)](https://travis-ci.org/cceremuga/pypacket) [![Coverage Status](https://coveralls.io/repos/github/cceremuga/pypacket/badge.svg?branch=master)](https://coveralls.io/github/cceremuga/pypacket?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/55cfa693d652488e994b6782fed2eccc)](https://www.codacy.com/manual/cceremuga_3/pypacket?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cceremuga/pypacket&amp;utm_campaign=Badge_Grade) [![Requirements Status](https://pyup.io/repos/github/cceremuga/pypacket/shield.svg)](https://pyup.io/account/repos/github/cceremuga/pypacket/) [![Requirements Status](https://pyup.io/repos/github/cceremuga/pypacket/python-3-shield.svg)](https://pyup.io/account/repos/github/cceremuga/pypacket/) 

## Requirements

The following are required to be installed and configured on your system.

* An RTL-SDR compatible device.
* Some form of Unix-like system. I build it on Mac OS. I run it on a Raspberry Pi w/ Raspbian.
* Python >= v3.6
* [rtl_fm](http://osmocom.org/projects/sdr/wiki/rtl-sdr)
* [multimon-ng](https://github.com/EliasOenal/multimon-ng)
* Optonally, a call-sign login and password for APRS-IS to upload spots.

## Setup

* `config/configuration.json` contains all insecure runtime configuration settings.
* If you want to upload spots to APRS-IS, ensure you have the following environment variables set:
    * `PYPACKET_USERNAME` - Your call sign for APRS-IS
    * `PYPACKET_PASSWORD` - Your password for APRS-IS
    * Rename `.env.example` to `.env` and fill in the appropriate values.
* Run `pip install -r requirements.txt`

## Usage

* Run `./main.py`.
    * The application will start and immediately begin listening on the configured frequency.
    * Logged packets will be output to your terminal, written to a file in the `logs` directory, and (if configured) uploaded to APRS-IS.

## Release Notes

* 5/31/2020 (v5.0)
    * Minor cosmetic adjustments.
    * Support for squelch level and PPM error configuration options.
    * Simplified environment variable loading for APRS-IS username/password.
    * SIGINT is now properly handled, exiting subprocesses before terminating main thread.
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

## Credits

* [ ~ Dependencies scanned by PyUp.io ~ ]
* Radio tower icon found in the logo courtesy of [The Noun Project](https://thenounproject.com/search/?q=radio%20tower&i=749293).
* Project was inspired by [pymultimonaprs](https://github.com/asdil12/pymultimonaprs).
