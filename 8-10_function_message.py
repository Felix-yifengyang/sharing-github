def show_message(messages) :
    for message in messages :
        print(message)
def send_mesaage(messages,sent_messages) :
    while messages :
        message = messages.pop()
        print(message)
        sent_messages.append(message)
messages = ['Are you silly B?', '这都不会？', '就这？']
sent_messages = []
# show_message(messages)
# send_mesaage(messages, sent_messages)
show_message(messages)