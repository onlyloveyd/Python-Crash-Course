messages = ['Python', 'Kotlin', 'C++']
sent_message = []


def show_messages():
    for message in messages:
        print(message)


def send_message():
    while messages:
        sent_message.append(messages.pop())


send_message()
print(messages)
print(sent_message)
