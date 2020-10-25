import winsound

# credit: https://stackoverflow.com/questions/6537481/python-making-a-beep-noise
class Beeper:
    @staticmethod
    def beep():
        # TODO: Make this cross platform
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 500 ms == 0.5 second
        winsound.Beep(frequency, duration)