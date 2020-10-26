import subprocess
from ..Exceptions.InvalidOperationError import InvalidOperationError


class CommandRunner:
    """
    A simpler abstraction over the subprocess module to start a process.
    Usage:
    1. Define a command in the constructor.
    2. Use `run` method to start the process.
    3. Use `wait` method to wait for the program to end. Alternatively use `run_and_wait`.
    4. Use `get_output` method to get the stdout output from the program.
    """
    def __init__(self, command_name: str):
        self.__command_name = command_name
        self.__is_running = False
        self.__is_finished = False
        self.__output: bytes = None
        self.__error: bytes = None
        self.__process: subprocess.Popen = None

    def run(self):
        if self.__is_finished or self.__is_running:
            return
        self.__process = subprocess.Popen(self.__command_name, stdout=subprocess.PIPE, shell=True)
        self.__is_running = True
        (self.__output, self.__error) = self.__process.communicate()

    def wait(self):
        if not self.__is_running:
            raise InvalidOperationError('Command has not been ran yet')
        if self.__is_finished:
            return
        self.__process.wait()
        self.__is_running = False
        self.__is_finished = True

    def run_and_wait(self):
        self.run()
        self.wait()

    def get_output(self) -> str:
        return self.__output.decode('utf-8')
