# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""This module represents the component device that connects to Azure IoT Hub using an IoTHubSession
and the thread definition that keeps listening incoming messages from cloud."""

import calendar
import time
import asyncio
from azure.iot.device import IoTHubSession
from threading import Thread
import queue


CONNECTION_STRING = "HostName=IntelligentBackpackHub.azure-devices.net;"
TOTAL_MESSAGES_RECEIVED = 0


class HubIotThread (Thread):
    """
    Thread that performs incoming messages listening.
    """

    def __init__(self, messages_queue, device_id, primary_key):
        """
        Constructor method that create the thread object of this module
            Parameters:
                messages_queue (queue): The synchronized queue to send all the received messages from the cloud

            Returns:
                void
        """
        Thread.__init__(self)
        self.connection_string = CONNECTION_STRING + "DeviceId=" + device_id + ";SharedAccessKey=" + primary_key
        self.messages_queue = messages_queue

    def run(self):
        """
        Method that executes the thread
        """
        try:
            asyncio.run(self.main())
        except KeyboardInterrupt or Exception:
            # Exit application because user indicated they wish to exit.
            # This will have cancelled `main()` implicitly.
            print("User initiated exit. Exiting")
        finally:
            print("Received {} messages in total".format(TOTAL_MESSAGES_RECEIVED))


    async def main(self):
        """
       Main function that use IoTHubSession to connect to the relative IoT Hub cloud device and listens
       all the incoming messages from the cloud, that could be different:
       - REGISTER: sent with the email of the user that wants to registrate this device
       - EXIT: message that force the exit of the application
       - UNREGISTER: sent with the email of the user that wants to unregistrate this device
       - NEW_DATA: sent with the data that will be added to the device. Used only for debug purpose
       """
        global TOTAL_MESSAGES_RECEIVED
        print("Starting C2D sample")
        print("Press Ctrl-C to exit")
        print("Connecting to IoT Hub...")
        async with IoTHubSession.from_connection_string(self.connection_string) as session:
            print("Connected to IoT Hub")
            async with session.messages() as messages:
                # print("Waiting to receive messages...")
                async for message in messages:
                    TOTAL_MESSAGES_RECEIVED += 1
                    current_GMT = time.gmtime()
                    time_stamp = calendar.timegm(current_GMT)
                    print("Message received with payload: {}".format(message.payload))
                    print("TIMESTAMP: {}".format(time_stamp))
                    # print("Email is {}".format(message.payload.split(":")[1]))
                    if message.payload == "EXIT":
                        self.messages_queue.put("EXIT")
                        raise Exception('Stop this thing')
                    if "REGISTER" in message.payload:
                        message_to_send = {
                            "type": "REGISTER",
                            "payload": {
                                "email": message.payload.split(";")[1],
                                "hash": message.payload.split(";")[2]
                            }
                        }
                        self.messages_queue.put(message_to_send)
                    if "UNREGISTER" in message.payload:
                        message_to_send = {
                            "type": "UNREGISTER",
                            "payload": ""
                        }
                        self.messages_queue.put(message_to_send)
                    # test
                    if "NEW_DATA" in message.payload:
                        message_to_send = {
                            "type": "TAG_READ",
                            "payload": "fedfwefwe"
                        }
                        self.messages_queue.put(message_to_send)



if __name__ == "__main__":
    try:
        hub = HubIotThread(queue.Queue())
        asyncio.run(hub.main())
    except KeyboardInterrupt:
        # Exit application because user indicated they wish to exit.
        # This will have cancelled `main()` implicitly.
        print("User initiated exit. Exiting")
    finally:
        print("Received {} messages in total".format(TOTAL_MESSAGES_RECEIVED))
