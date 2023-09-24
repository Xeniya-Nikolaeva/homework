def clear_string(b):
    c = "" #строка с результатом
    for i in range(len(b)-1):
        if not(b[i] == ' ' and b[i+1] == ' '): #если не два "пробела" то:
            c = c + b[i]
    return c


a = clear_string(input())
word_count = a.count(" ") + 1
print("Количество слов в строке:", word_count)