<p align="center"><img src="https://i.imgur.com/MZYHAFG.png" /></p>

Receive, decode, log, share [APRS](http://www.aprs.org/) packets using low cost [RTL-SDR](http://osmocom.org/projects/sdr/wiki/rtl-sdr) devices.

[![Build Status](https://travis-ci.org/cceremuga/pypacket.svg?branch=master)](https://travis-ci.org/cceremuga/pypacket) [![Coverage Status](https://coveralls.io/repos/github/cceremuga/pypacket/badge.svg?branch=master)](https://coveralls.io/github/cceremuga/pypacket?branch=master)

## Pre-requisites

The following are required to be installed and configured on your system.

* Some form of Linux flavor. I build it on Manjaro. I run it on a Raspberry Pi w/ Raspbian.
* An RTL-SDR compatible device.
* A call-sign login and password for APRS-IS.
* Python >= v3.5
* [rtl_fm](http://osmocom.org/projects/sdr/wiki/rtl-sdr)
* [multimon-ng](https://github.com/EliasOenal/multimon-ng)
* [pip](https://pypi.python.org/pypi/pip)
    * [aprslib](https://pypi.python.org/pypi/aprslib)
    * [pytest](https://docs.pytest.org/en/latest/) (optional, only required if you want to run tests)

## Configuration

The `config/configuration.json` file contains all of the insecure runtime configuration settings.

## Usage

From a terminal, in the directory where you've cloned the repository...

* Ensure you have the following environment variables set:
    * `PYPACKET_USERNAME` - Your call sign for APRS-IS
    * `PYPACKET_PASSWORD` - Your password for APRS-IS
* Run `python main.py`.
    * The application will start and immediately begin listening on the configured frequency.
    * Logged packets will be output to your terminal, written to a file in the `logs` directory, and uploaded to APRS-IS.

## Patch Notes

* 3/10/2019 (v3.1 / v3.1.1)
    * Connect once at start to APRS-IS.
    * Configurable upload time.
    * Connection resiliency, will reconnect when disconnected.
    * Configurable APRS-IS server.
* 3/9/2019 (v3.0)
    * From beyond the code-grave the zombie of PyPacket rises with version 3.0. It comes with a fully modular extension framework and once-per-minute uploads to APRS-IS.
* 5/3/2017 (v2.3)
    * Integrated code coverage reports, boosted tests.

## Contributing

You are welcome to contribute by submitting pull requests on GitHub if you would like. Feature / enhancement requests may be submitted via GitHub issues.

## Credits

The radio tower icon found in the logo courtesy of [The Noun Project](https://thenounproject.com/search/?q=radio%20tower&i=749293).
