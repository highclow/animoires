import jsonpickle
import json


class JsonPrinter(object):

    def __init__(self):
        pass

    def printObject(self, object, fileName):
        pickled = jsonpickle.encode(object)

        dumped = json.dumps(object, default=lambda o: o.__dict__)
        with open(fileName, 'w') as jsonfile:
            jsonfile.write(dumped)
