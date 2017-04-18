![PyPacket](https://i.imgur.com/MZYHAFG.png "PyPacket")

A simple CLI logger to receive and decode APRS packets via rtl_fm ([RTL-SDR](http://osmocom.org/projects/sdr/wiki/rtl-sdr)) and [multimon-ng](https://github.com/EliasOenal/multimon-ng). This project serves as an open source expirimental tool for research into the RF spectrum and APRS.

[![Build Status](https://travis-ci.org/cceremuga/pypacket.svg?branch=master)](https://travis-ci.org/cceremuga/pypacket)

## Dependencies

Requires the following to be installed and configured on your system in order to run.

* Some form of Linux flavor. MacOS, possibly. Windows, doubtful.
* An RTL-SDR compatible device.
* Python >= v3.5
* [rtl_fm](http://osmocom.org/projects/sdr/wiki/rtl-sdr)
* [multimon-ng](https://github.com/EliasOenal/multimon-ng)
* [pip](https://pypi.python.org/pypi/pip)
* [pytest](https://docs.pytest.org/en/latest/) (if you want to run tests)

## Configuration

The `config/configuration.json` file contains all of the current configuration options including frequency, gain, etc. More options will be added as needed.

## Running

From the directory you've cloned the repository to, simply execute `python main.py`. The application will start and immediately begin listening on the configured frequency.

Logged packets will be output to your terminal and written to a file in the `logs` directory.

## Recent Patch Notes

* 4/18/17
    * Basic JSON-based configuration support.
    * Improved logging.
    * Resolved bug when logs directory did not exist.
* 4/17/17
    * Logging runtime activities to file in the logs subdirectory.
* 4/2/17
    * Start of unit tests.
    * Travis CI integration.

## Current / Future Plans

* JSON configuration options for frequency, gain [in progress].
* APRS frame deserialization for human readability [future].
* Quality code coverage [future].
* Better documentation [future].
* Performance optimization [future].
* Simple TCP server (for use in Xastir etc.) [future].
* Custom IGate uploading [future].

## Contributing

You are welcome to contribute by submitting pull requests on GitHub as you see fit!

## Credits

Thanks to the following projects / libraries for open source code / inspiration.

* [pimultimonaprs](https://github.com/asdil12/pymultimonaprs)
* [The Noun Project](https://thenounproject.com/search/?q=radio%20tower&i=749293)
