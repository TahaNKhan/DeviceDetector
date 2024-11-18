from Logic.Logging.LoggerInterface import LoggerInterface


class ConsoleLogger(LoggerInterface):
    def __init__(self, log_immediately: bool):
        self.__log_immediately = log_immediately
        self.__logs: list[str] = []

    def log(self, to_log: str) -> None:
        if self.__log_immediately:
            print(to_log)
            return
        self.__logs.append(to_log)

    def publish(self) -> None:
        if self.__log_immediately:
            return
        for log in self.__logs:
            print(log)
        self.__logs = []
