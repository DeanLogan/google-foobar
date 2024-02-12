import base64

MESSAGE = 'P0ISGy8MAhIdExJ+RUYJPgoGFUkYEmMGDgIgCgYGG1EVZF9BSSkcEwQLWVcgQk1OawoBBwFGRjdC\nQVRsSA4PDUZXIAwDAilIS0FJVVEsDAQYKQICDxoTEn5FRhsiAwgCBVFWY0lBST4OBQMHQEFjRVtO\naxwGBwsTHmRCBwEjSEdbThNFLQtASTE='

KEY = 'deanlogan42'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))