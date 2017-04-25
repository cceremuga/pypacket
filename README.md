<p align="center"><img src="https://i.imgur.com/MZYHAFG.png" /></p>

A simple CLI tool to receive, decode, log [APRS](http://www.aprs.org/) packets via rtl_fm ([RTL-SDR](http://osmocom.org/projects/sdr/wiki/rtl-sdr)) and [multimon-ng](https://github.com/EliasOenal/multimon-ng). This project serves as an open source expirimental tool for research into the RF spectrum and APRS.

[![Build Status](https://travis-ci.org/cceremuga/pypacket.svg?branch=master)](https://travis-ci.org/cceremuga/pypacket)

## Requirements

The following are required to be installed and configured on your system.

* Some form of Linux flavor. MacOS, possibly. Windows, doubtful.
* An RTL-SDR compatible device.
* Python >= v3.5
* [rtl_fm](http://osmocom.org/projects/sdr/wiki/rtl-sdr)
* [multimon-ng](https://github.com/EliasOenal/multimon-ng)
* [pip](https://pypi.python.org/pypi/pip)
* [aprslib](https://pypi.python.org/pypi/aprslib)
* [pytest](https://docs.pytest.org/en/latest/) (if you want to run tests)

## Configuration

The `config/configuration.json` file contains all of the configuration options including frequency, gain, etc. More options will be added as needed.

## Running

From the directory you've cloned the repository to, simply run `python main.py` in the shell of your choice. The application will start and immediately begin listening on the configured frequency.

Logged packets will be output to your terminal and written to a file in the `logs` directory.

## Recent Patch Notes

* 4/25/2017 (v2.1)
    * Refactoring, optimization.
* 4/24/2017 (v2.0)
    * APRS frame deserialization (see requirements for new dependencies).
    * Code fully documented.
    * Main utilities unit tested. Listener class still forthcoming.
    * Code cleanup, refactoring, optimization.
* 4/18/2017 (v1.0)
    * Improved RTL settings.
    * Completed JSON configuration support.
    * Improved logging.
    * Resolved bug when logs directory did not exist.

## Feature Roadmap

* Pluggable listener, decoder framework [v3.0].
* Simple TCP server (for use in Xastir etc.) [v3.0].
* Custom IGate uploading [v4.0].
* Support for other capture methods [unknown].

## Contributing

You are welcome to contribute by submitting pull requests on GitHub if you are interested in development.

Feature / enhancement requests may be submitted via GitHub issues.

## Credits

The radio tower icon found in the logo courtesy of [The Noun Project](https://thenounproject.com/search/?q=radio%20tower&i=749293).
