import subprocess
from ..Exceptions.InvalidOperationError import InvalidOperationError

class CommandRunner:
    def __init__(self, command_name: str):
        self.__command_name = command_name
        self.__is_running = False
        self.__is_finished = False
        self.__output: bytes = None
        self.__error: bytes = None

        
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
        if self.__is_running:
            raise InvalidOperationError('Command is already running')
        self.run()
        self.wait()

    def get_output(self) -> str:
        return self.__output.decode('utf-8')





