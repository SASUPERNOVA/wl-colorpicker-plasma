# wl-colorpicker-plasma

A standalone color picker for Wayland and KDE Plasma.

## About

Although Wayland has [come a long way](https://arewewaylandyet.com/) since its inception, there are still not many implementations for a color picker. Current existing solutions either use [grim](https://github.com/emersion/grim) under the hood, which in turn uses [wlr-screencopy-unstable-v1](https://wayland.app/protocols/wlr-screencopy-unstable-v1), or simply do not work on KDE Plasma. `wl-colorpicker-plasma` is a stripped-down version of [kdeplasma-addons colorpicker widget](https://github.com/KDE/kdeplasma-addons/tree/master/applets/colorpicker), and thus works in KDE PLasma as intended.

## Usage

Since `wl-colorpicker-plasma` only returns the color picked as a hex value, you will need to copy the value separately as in the example below (note: this requires [wl-clipboard](https://github.com/bugaevc/wl-clipboard) to be installed on your system):

```
python3 wl-colorpicker-plasma.py | wl-copy
```

## License

[GPL v2.0](https://github.com/SASUPERNOVA/wl-colorpicker-plasma/blob/master/License.md)
