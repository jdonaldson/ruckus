# 📻 Ruckus

Ruckus is a simple, elegant binaural beat generator that lives in your macOS menu bar. It allows you to easily play binaural beats to enhance focus, relaxation, or meditation, all with just a few clicks.

## Features

- 🎵 Generate binaural beats with customizable durations
- 🖥️ Convenient macOS menu bar application
- 🕒 Preset durations: 5, 10, and 30 minutes
- 🛑 Easy start and stop functionality
- 📢 System notifications for playback status

## Installation

### Prerequisites

- macOS 10.12 or later
- Python 3.7 or later
- pip (Python package installer)

### Steps

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ruckus.git
   cd ruckus
   ```

2. Install the package:
   ```
   pip install -e .
   ```

## Usage

After installation, you can start Ruckus in two ways:

1. From the command line:
   ```
   ruckus
   ```

2. By running the Python module:
   ```
   python -m ruckus
   ```

Once started, you'll see the 📻 icon in your menu bar. Click on it to access the following options:

- Play (5 min): Starts a 5-minute binaural beat session
- Play (10 min): Starts a 10-minute binaural beat session
- Play (30 min): Starts a 30-minute binaural beat session
- Stop: Stops the currently playing binaural beat

## Customization

The default settings use a carrier frequency of 110 Hz and a beat frequency of 4 Hz. If you'd like to customize these frequencies, you can modify the `generate_binaural_beat` method in `src/ruckus/__init__.py`.

## Contributing

Contributions to Ruckus are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [rumps](https://github.com/jaredks/rumps) for making it easy to create macOS menu bar apps
- [numpy](https://numpy.org/) for efficient numerical computations
- [sounddevice](https://python-sounddevice.readthedocs.io/) for audio playback

## Support

If you encounter any problems or have any suggestions, please open an issue on the GitHub repository.

Enjoy your binaural beats with Ruckus! 🎶
