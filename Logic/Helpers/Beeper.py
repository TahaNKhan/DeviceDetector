import winsound


class Beeper:
    @staticmethod
    def beep() -> None:
        """
        Uses the winsound API to create a beep-like sound.
        2500 Hz frequency for 0.5 second(s).
        credit: https://stackoverflow.com/questions/6537481/python-making-a-beep-noise
        """
        # TODO: Make this cross platform
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 500 ms == 0.5 second
        winsound.Beep(frequency, duration)
