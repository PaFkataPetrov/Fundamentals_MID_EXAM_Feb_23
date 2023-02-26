chat_log = []

while True:
    chat_command = input().split()
    if chat_command[0] == "Chat":
        chat_log.append(chat_command[1])
    if chat_command[0] == "Delete":
        if chat_command[1] in chat_log:
            chat_log.remove(chat_command[1])
        else:
            continue
    if chat_command[0] == "Edit":
        if chat_command[1] in chat_log:
            indx = chat_log.index(chat_command[1])
            chat_log.remove(chat_command[1])
            chat_log.insert(indx, chat_command[2])
        else:
            continue
    if chat_command[0] == "Pin":
        if chat_command[1] in chat_log:
            chat_log.remove(chat_command[1])
            chat_log.append(chat_command[1])
        else:
            continue
    if chat_command[0] == "Spam":
        list_extend = chat_command[1:]
        chat_log.extend(list_extend)
    if chat_command[0] == "end":
        break

for el in chat_log:
    print(el)

