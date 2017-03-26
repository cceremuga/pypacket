     ___      ___         _       _
    | _ \_  _| _ \__ _ __| |_____| |_
    |  _/ || |  _/ _` / _| / / -_)  _|
    |_|  \_, |_| \__,_\__|_\_\___|\__|
         |__/

A simple CLI logger to receive and decode APRS packets via rtl_fm (RTL-SDR) and multimon-ng. This project serves as an open source expirimental tool for research into the RF spectrum and APRS.

Additionally, it serves a means for me personally to get back into python, establishing formatting and conventions.

## Requirements

Requires the following to be installed and configured on your system in order to run.

* Python >= v3.5
* [rtl_fm](http://osmocom.org/projects/sdr/wiki/rtl-sdr)
* [multimon-ng](https://github.com/EliasOenal/multimon-ng)
* An RTL-SDR compatible device

At this time, you are on your own with regards to dependency setup. There are significant pieces of this which are hard coded and have no configurability options. See the Future Plans section for more info.

## Future Plans

* Simple TCP server (for use in Xastir etc.).
* Command line configuration options for frequency, gain, etc.
* Better documentation.
* Performance optimization.

## Contributing

You are welcome to contribute by submitting pull requests on GitHub as you see fit!

## Credits

This project makes use of some code / inspiration from [pimultimonaprs](https://github.com/asdil12/pymultimonaprs) and as such, retains the GPLv3 license of its predecessor.
