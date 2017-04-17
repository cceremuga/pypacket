     ___      ___         _       _
    | _ \_  _| _ \__ _ __| |_____| |_
    |  _/ || |  _/ _` / _| / / -_)  _|
    |_|  \_, |_| \__,_\__|_\_\___|\__|
         |__/

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

Note, there are significant pieces of this which are hard coded and have no configurability options. See the Future Plans section for more info.

## Running

From the directory you've cloned the repository to, simply execute `python main.py`. The application will start and immediately begin listening on 144.39Mhz. Logged packets will be output to your terminal.

## Patch Notes

* 4/17/17
    * Logging runtime activities to file in the logs subdirectory.
* 4/2/17
    * Start of unit tests.
    * Travis CI integration.
* 4/1/17
    * Console colors are now constants.
* 3/27/17
    * Restructured files to use proper Python module organization.
    * Basic framework for logging.
    * Resolved an exception involving unparseable decoded data.

## Future Plans

* JSON configuration options for frequency, gain, in progress.
* APRS frame deserialization for human readability, on deck.
* Quality code coverage, it's happening.
* Better documentation, definitely.
* Performance optimization, probably.
* Simple TCP server (for use in Xastir etc.), likely.
* Custom IGate uploading, maybe.

## Contributing

You are welcome to contribute by submitting pull requests on GitHub as you see fit!

## Credits

Thanks to the following projects / libraries for open source code / inspiration.

* [pimultimonaprs](https://github.com/asdil12/pymultimonaprs)
