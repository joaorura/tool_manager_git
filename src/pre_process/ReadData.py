from csv import reader
from copy import deepcopy


class ReadData:
    def __init__(self, path):
        self.path = path
        self._process_data = None

    def _execute(self):
        self._process_data = {
            'keys': None,
            'list': []
        }

        with open(self.path) as csvfile:
            readCSV = reader(csvfile, delimiter=',')

            for row in readCSV:
                self._process_data['list'].append(row[0])

            self._process_data['keys'] = self._process_data['list'][0]
            del self._process_data['list'][0]

    def getProcessData(self):
        if self._process_data is None:
            self._execute()

        return deepcopy(self._process_data)
