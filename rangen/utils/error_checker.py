def check(optional_parameters):
    if str(optional_parameters['audio']).lower() not in ('true', 'false'):
        raise ValueError(
            f"Incorrect input value for parameter => audio={optional_parameters['audio']}. Must be True or False!")

    if str(optional_parameters['disk']).lower() not in ('true', 'false'):
        raise ValueError(
            f"Incorrect input value for parameter => disk={optional_parameters['disk']}. Must be True or False!")

    if not str(optional_parameters['a_samplerate']).isdigit():
        raise ValueError(
            f"Incorrect input value for parameter => a_samplerate={optional_parameters['a_samplerate']}. Must be Integer!")

    if not str(optional_parameters['a_channels']).isdigit():
        raise ValueError(
            f"Incorrect input value for parameter => a_channels={optional_parameters['a_channels']}. Must be Integer!")

    if not str(optional_parameters['a_duration']).isdigit():
        raise ValueError(
            f"Incorrect input value for parameter => a_duration={optional_parameters['a_duration']}. Must be Integer or Float!")

    if float(optional_parameters['a_duration']) > 20:
        raise ValueError("Capturing audio duration is longer than 20. Lower it!")

    if not str(optional_parameters['d_duration']).isdigit():
        raise ValueError(
            f"Incorrect input value for parameter => d_duration={optional_parameters['d_duration']}. Must be Integer or Float!")

    if float(optional_parameters['d_duration']) > 20:
        raise ValueError("Capturing disk i/o counters duration is longer than 20. Lower it!")

