<p align="center"><img src="https://i.imgur.com/HvhAWed.png" width="500" height="auto" /></p>

## Sunsetting PyPacket

**As of March, 2021, any further development with respect to new features, functionality, or bug fixes for PyPacket has ceased.** This is in support of an effort to transition development over to my next project, [Ionosphere](https://github.com/cceremuga/ionosphere). That is intended to be a long term replacement for this project.

PyPacket was a great learning opportunity for me, but has ultimately become challenging to support across multiple platforms, architectures, etc. My hope is that Ionosphere will serve as a drop-in replacement with speed, optimization improvements as well as broader support for platforms such as Windows.

That said, if anyone is interested in taking over maintenance / development efforts for PyPacket, pull requests are still welcome!

## Security and Privacy

**The Automatic Packet Reporting System (APRS) is never private and never secure.** As an amateur radio mode, it is designed solely for experimental use by licensed operators to publicly communicate positions and messages. Encryption on amateur radio frequencies is forbidden in most localities. As such, **connections to APRS-IS are also unsecured and only intended for licensed amateur radio operators.**

## Contributing

You are welcome to contribute by submitting pull requests on GitHub if you would like. Feature / enhancement requests may be submitted via GitHub issues.

## Credits

* Inspired by the excellent [pymultimonaprs](https://github.com/asdil12/pymultimonaprs) project. I more or less learned basic Python threading by studying their work. Huge thanks to them!
* Utilizes [aprs-python](https://github.com/rossengeorgiev/aprs-python) for parsing decoded packets, uploading to APRS-IS. None of this would be possible without this library.
* Radio tower icon found in the logo courtesy of [The Noun Project](https://thenounproject.com/search/?q=radio%20tower&i=749293).
* [ ~ Dependencies scanned by PyUp.io ~ ]
