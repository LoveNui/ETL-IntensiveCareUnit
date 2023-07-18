import json
import sys
import traceback
from java.nio.charset import StandardCharsets
from org.apache.commons.io import IOUtils
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil
from datetime import datetime

class TransformCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        try:
            # Read input FlowFile content
            input_text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
            input_obj = json.loads(input_text)
            #log.info(json.dumps(input_obj))

            # Transform content
            output_obj = add_status(input_obj)

            # Write output content
            output_text = json.dumps(output_obj)
            outputStream.write(StringUtil.toBytes(output_text))
        except:
            traceback.print_exc(file=sys.stdout)
            raise

def add_status(data):
    
    if "bedStatus" in data and data["bedStatus"] == "available":
        return data

    parameters = {
        "oxygen_level": {"min": 95, "max": 100},
        "temperature": {"min": 36.0, "max": 37.5},
        "heartbeat": {"min": 60, "max": 100},
        "bp_systolic": {"min": 90, "max": 120},
        "bp_diastolic": {"min": 60, "max": 80}
    }

    updated_data = data.copy()

    for key, value in data.items():
        if isinstance(value, dict):
            for sub_param, sub_value in value.items():
                if sub_param in parameters[key]:
                    if parameters[key][sub_param]["min"] <= sub_value <= parameters[key][sub_param]["max"]:
                        updated_data[key][sub_param + "_status"] = "normal"
                    else:
                        updated_data[key][sub_param + "_status"] = "warning"
        elif key in parameters:
            if parameters[key]["min"] <= value <= parameters[key]["max"]:
                updated_data[key + "_status"] = "normal"
            else:
                updated_data[key + "_status"] = "warning"

    return updated_data

flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, TransformCallback())

session.transfer(flowFile, REL_SUCCESS)

