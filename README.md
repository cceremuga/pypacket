<p align="center"><img src="https://i.imgur.com/MZYHAFG.png" /></p>

A simple CLI tool to receive, decode, log [APRS](http://www.aprs.org/) packets via rtl_fm ([RTL-SDR](http://osmocom.org/projects/sdr/wiki/rtl-sdr)) and [multimon-ng](https://github.com/EliasOenal/multimon-ng). This project serves as an open source experimental tool for research into the RF spectrum and APRS.

Be warned, I probably over-engineered this quite extensively. Why? Well, it's a free-time project so I can do that with no loss but my own time. It's an outlet for perfectionism and Python learning.

[![Build Status](https://travis-ci.org/cceremuga/pypacket.svg?branch=master)](https://travis-ci.org/cceremuga/pypacket) [![Coverage Status](https://coveralls.io/repos/github/cceremuga/pypacket/badge.svg?branch=master)](https://coveralls.io/github/cceremuga/pypacket?branch=master)

## Requirements

The following are required to be installed and configured on your system.

* Some form of Linux flavor. I build it on Manjaro. I run it 24/7 on a Raspberry Pi w/ Raspbian.
* An RTL-SDR compatible device.
* Python >= v3.7
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

* 3/9/2019 (v3.0)
    * From beyond the code grave comes 3.0 with pluggable config for all modules, once-a-minute uploads to APRS-IS.
* 5/3/2017 (v2.3)
    * Integrated code coverage reports, boosted tests.
* 4/27/2017 (v2.2)
    * Listener, decoder now dynamically instantiated from JSON config.

## Feature Road Map

* None planned really. We'll see how this evolves as I run this more regularly.

## Contributing

You are welcome to contribute by submitting pull requests on GitHub if you are interested in development.

Feature / enhancement requests may be submitted via GitHub issues.

## Credits

The radio tower icon found in the logo courtesy of [The Noun Project](https://thenounproject.com/search/?q=radio%20tower&i=749293).
