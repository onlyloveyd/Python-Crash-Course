messages = ['Python', 'Kotlin', 'C++']
sent_message = []


def show_messages():
    for message in messages:
        print(message)


def send_message(messages_copy):
    while messages_copy:
        sent_message.append(messages_copy.pop())


send_message(messages[:])
print(messages)
print(sent_message)
