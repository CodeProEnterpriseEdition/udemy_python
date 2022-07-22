def order(sentence):
    if not sentence:
        return ""
    result = []
    words_dict = {}
    for word in sentence.split():
        for char in word:
            if(char.isdigit()):
                words_dict[char] = (word)
    for n in range(len(sentence.split())):
        result.append(words_dict[str(n+1)])
    return " ".join(result)
    # None should equal 'Fo1r the2 g3ood 4of th5e pe6ople'


# print(order('Fo1r the2 g3ood 4of th5e pe6ople'))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
