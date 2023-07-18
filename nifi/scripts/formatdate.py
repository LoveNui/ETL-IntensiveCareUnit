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
            output_obj = format_json_date_time(input_obj)

            # Write output content
            output_text = json.dumps(output_obj)
            outputStream.write(StringUtil.toBytes(output_text))
        except:
            traceback.print_exc(file=sys.stdout)
            raise

def format_json_date_time(json_data):
    # Create a copy of the original JSON data
    formatted_data = json_data

    # Convert the date and time format
    date_str = formatted_data['date']
    time_str = formatted_data['time']
    timestamp_str = "{}T{}".format(date_str, time_str)
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S')

    # Format the timestamp to ISO 8601 format
    formatted_timestamp = timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Update the JSON data with the formatted timestamp
    formatted_data['timestamp'] = formatted_timestamp

    # Remove the 'date' and 'time' fields
    formatted_data.pop('date')
    formatted_data.pop('time')

    return formatted_data

flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, TransformCallback())

session.transfer(flowFile, REL_SUCCESS)