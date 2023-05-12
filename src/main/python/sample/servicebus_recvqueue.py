#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show receiving batch messages from a Service Bus Queue.
"""

from azure.servicebus import ServiceBusClient

CONNECTION_STR = 'Endpoint=sb://intelligentbackpacupdates.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=6VQKKtj9dS6YeeumpEhpPZoC9GIq8pScJ+ASbMyfl2U='
QUEUE_NAME = 'updates'

servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR)

with servicebus_client:
    receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME)
    with receiver:
        received_msgs = receiver.receive_messages(max_message_count=10, max_wait_time=5)
        for msg in received_msgs:
            print(str(msg))
            receiver.complete_message(msg)

print("Receive is done.")
