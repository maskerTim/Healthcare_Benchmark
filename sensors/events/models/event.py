import json

class Event:
    """ Interface of event """
    def __init__(self, event):
        self.event = event

    def toJson(self):
        return json.dumps(self.event)

    def convert(self, format):
        formats = {
            "json": self.toJson
        }
        return formats[format]()