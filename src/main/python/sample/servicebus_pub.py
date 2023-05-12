#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show sending message(s) to a Service Bus Topic.
"""

from azure.servicebus import ServiceBusClient, ServiceBusMessage

CONNECTION_STR = 'Endpoint=sb://intelligentbackpacupdates.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=6VQKKtj9dS6YeeumpEhpPZoC9GIq8pScJ+ASbMyfl2U='
TOPIC_NAME = 'updates-sub'
SUBSCRIPTION_NAME = 'subscription'


def send_single_message(sender):
    message = ServiceBusMessage("Single Message")
    sender.send_messages(message)


def send_a_list_of_messages(sender):
    messages = [ServiceBusMessage("Message in list") for _ in range(10)]
    sender.send_messages(messages)


def send_batch_message(sender):
    batch_message = sender.create_message_batch()
    for _ in range(10):
        try:
            batch_message.add_message(ServiceBusMessage("Message inside ServiceBusMessageBatch"))
        except ValueError:
            # ServiceBusMessageBatch object reaches max_size.
            # New ServiceBusMessageBatch object can be created here to send more data.
            break
    sender.send_messages(batch_message)


servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)
with servicebus_client:
    sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
    with sender:
        send_single_message(sender)
        # send_a_list_of_messages(sender)
        # send_batch_message(sender)

print("Send message is done.")