# 8-9

def show_message(messages):
    """Виводить прості повідомлення"""
    for message in messages:
        print(message)


message = ['hello', 'how are you', 'what are you doing']
show_message(message)

# 8-10

def show_message(messages):
    """Виводить прості повідомлення"""
    print(f"Showing all messages:")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Виводить відправлені повідомлення, та переміщує їх у список"""
    print(f'\nSending all messages: ')
    while messages:
        current_mesages = messages.pop()
        print(current_mesages)
        sent_messages.append(current_mesages)


message = ['hello', 'how are you', 'what are you doing']
sent_messages = []

show_message(message)
send_messages(message, sent_messages)

# 8-11

def show_message(messages):
    """Виводить прості повідомлення"""
    print(f"Showing all messages:")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Виводить відправлені повідомлення, та переміщує їх у список"""
    print(f'\nSending all messages: ')
    while messages:
        current_mesages = messages.pop()
        print(current_mesages)
        sent_messages.append(current_mesages)


message = ['hello', 'how are you', 'what are you doing']
sent_messages = []

show_message(message)
send_messages(message[:], sent_messages)

print("\nFinal lists:")
print(message)
print(sent_messages)