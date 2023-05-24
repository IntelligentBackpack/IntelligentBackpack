# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""This sample demonstrates a simple cloud to device receive using an IoTHubSession."""

import asyncio
from azure.iot.device import IoTHubSession
from threading import Thread
import queue


CONNECTION_STRING = "HostName=IntelligentBackpackHub.azure-devices.net;DeviceId=raspTest;SharedAccessKey=NUNHoJX5KVIDuGCRg3fq6e7PAg6R9oDMu0zcdGg+IzY="
TOTAL_MESSAGES_RECEIVED = 0


class HubIotThread (Thread):

    def __init__(self, messages_queue):
        Thread.__init__(self)
        self.messages_queue = messages_queue

    def run(self):
        try:
            asyncio.run(self.main())
        except KeyboardInterrupt or Exception:
            # Exit application because user indicated they wish to exit.
            # This will have cancelled `main()` implicitly.
            print("User initiated exit. Exiting")
        finally:
            print("Received {} messages in total".format(TOTAL_MESSAGES_RECEIVED))


    async def main(self):
        global TOTAL_MESSAGES_RECEIVED
        print("Starting C2D sample")
        print("Press Ctrl-C to exit")
        print("Connecting to IoT Hub...")
        async with IoTHubSession.from_connection_string(CONNECTION_STRING) as session:
            print("Connected to IoT Hub")
            async with session.messages() as messages:
                # print("Waiting to receive messages...")
                async for message in messages:
                    TOTAL_MESSAGES_RECEIVED += 1
                    # print("Message received with payload: {}".format(message.payload))
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
                            "payload": "fedfwefwe")
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