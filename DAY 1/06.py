# 영-한 단어장을 한-영 단어장으로 뒤집기

vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

def reverse_dict(word):
    new_dict = {}

    for key, value in vocab.items():
        new_dict[value] = key

    return new_dict

print("영-한 단어장\n{}\n".format(vocab))

new_dict = reverse_dict(vocab)
print("한-영 단어장\n{}\n".format(new_dict))