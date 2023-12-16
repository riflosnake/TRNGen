# TRNGen: Truly Random Number Generator

TRNGen is a Python package that provides a secure and unpredictable random number generator by incorporating external entropy factors such as audio, disk and network I/O readings, events, display, mouse coordinates, and timer. These factors are combined using XOR, hashing algorithms, and linearity deviation to produce truly random values that avoid algorithmic prediction.

# Content:

- [Features](#features)
- [Requirements](#requirements)
- [How to install](#installation)
- [How to use](#how-to-use)

# Features

- **External Factors:** Utilizes various external entropy factors to enable true randomness.
  - `Audio`: Captures audio data.
  - `Disk` I/O Readings: Includes disk I/O readings.
  - `Network` I/O Readings: Incorporates network I/O readings for added entropy.
  - `Display`: Utilizes random display information for increased unpredictability.
  - `Mouse Coordinates`: Captures mouse coordinates.
  - `Timer`: Includes timer values in the randomization process.
- **Secure:** Employs cryptographic techniques on top of above values to ensure unpredictability.
  - `XOR` function
  - `Hashing` algorithms
  - `Linearity Deviation` method
- **Easy Integration:** Simple Python package use for easy integration into your projects.

# Requirements

- ```Python >= 3.7```
  - [Download the installer](https://www.python.org/downloads/), run it and follow the steps.
  - Make sure to check the box that says `Add Python to PATH` during installation.
  - Reboot computer.

# Installation

*You can install TRNGen using `pip`:*

```powershell
pip install TRNGen
```

# How to use
- ### Import
```python
from trngen import TRNGen
```
- ### Create an instance of the TRNGen generator
```python
generator = TRNGen()
```
  - ### Available parameters:
    - Check here on [TRNGen() parameters](parameter.md)

- ### Available functions:

  - ####  `trngen()`
    - Main function that generates and returns the random integer hash value
  - #### `hash(algorithm='sha3_256')`
    - Returns random cryptographic hash
  - #### `percentage(simple=False)`
    - Returns random percentage in decimal form
  - #### `integer(start, end)`
    - Returns random integer in range from start to end
  - #### `float(start, end)`
    - Returns random float in range from start to end
  - #### `alphanumeric(length=any)`
    - Returns random alphanumeric value, default of letters, digits and symbols
  - #### `choice(seq)`
    - Randomly chooses a element from an iterable sequence
  - #### `shuffle(seq, in_place=True)`
    - Randomly shuffles an iterable
  - #### `sample(seq, sample_size)`
    - Randomly samples a specified number of elements from an iterable

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
If you encounter any issues or have questions, feel free to open an issue.

