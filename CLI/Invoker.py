
class Invoker:

    def __init__(self):
        self._queue = []

    def process_command(self, command):
        self._queue.append(command)
        print(self._queue)
        command.process()