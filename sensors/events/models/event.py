import json

class Event:
    """ Interface of event """
    def __init__(self, event):
        self.event = event

    """ convert event to json format """
    def toJson(self):
        return json.dumps(self.event)

    """ convert the event to some format
    @param {format: the parser format}
    @return the event parsed by selected format
    """
    def convert(self, format):
        formats = {
            "json": self.toJson
        }
        return formats[format]()