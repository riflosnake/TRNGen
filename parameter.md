### *Note*: `Audio` and `Disk` modules require by default 1 second to record, you can either change the duration, or turn them off if you need faster generation.

### Available RanGen() object parameters:
#### `audio` (bool, optional)
- **Description**: Includes audio entropy module into randomization or not.
- **Default**: True
#### `a_samplerate` (int, optional)
- **Description**: Sets the sample rate of the audio stream recorded.
- **Default**: 44100 (Hz)
#### `a_duration` (int or float, optional)
- **Description**: Sets the time length of the audio stream recorded.
- **Default**: 1 (seconds)
#### `a_channels` (int, optional)
- **Description**: Sets the number of channels from where to record audio.
- **Default**: 2 (channels)
#### `disk` (bool, optional)
- **Description**: Includes disk entropy module into randomization or not.
- **Default**: True
#### `d_duration` (bool, optional)
- **Description**: Sets the time length of the disk activity recorded.
- **Default**: 1 (seconds)
#### `cursor` (bool, optional)
- **Description**: Includes cursor entropy module into randomization or not.
- **Default**: True
#### `display` (bool, optional)
- **Description**: Includes display entropy module into randomization or not.
- **Default**: True
#### `network` (bool, optional)
- **Description**: Includes network entropy module into randomization or not.
- **Default**: True
#### `timer` (bool, optional)
- **Description**: Includes timer entropy module into randomization or not.
- **Default**: True
#### `letters` (True or str, optional)
- **Description**: Includes default string letter characters into alphanumerical character set.
- **Default**: True
#### `digits` (True or str, optional)
- **Description**: Includes default string digit characters into alphanumerical character set.
- **Default**: True
#### `symbols` (True or str, optional)
- **Description**: Includes default string symbol characters into alphanumerical character set.
- **Default**: True
#### `csv_file_location` (str or bool, optional)
- **Description**: Saves data to csv file in that location, doesn't if empty string or False.
- **Default**: 'dependencies/dataset.csv'
