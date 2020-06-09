import datetime
import json
import os
import random
import sys
import traceback

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


def parseJSONfile(filePath):
    try:
        parsedPythonDict = json.load(open(filePath, 'r'))
        return parsedPythonDict
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)


def parseJSONString(jsonStr):
    try:
        return json.loads(jsonStr)
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)


def convertIntoJSONObject(pythonObj):
    try:
        return json.dumps(pythonObj, indent=1)
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)


def parseConfigurationFile():
    try:
        return json.load(open("../../Config/configuration.json", 'r'))
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)


randomNumber = lambda minValue, maxValue: random.randint(minValue, maxValue)
current_timestamp = lambda formatted_string: datetime.datetime.utcnow().strftime(formatted_string)
