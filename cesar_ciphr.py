def encoder(key, mess):
    mess = list(mess)
    while key > 1_000000:
        key -= 1_000000
    mess = "".join([chr(ord(i) + key) for i in mess])

    return mess


def decoder(key, mess):
    mess = list(mess)
    while key > 1_000000:
        key -= 1_000000
    mess = "".join([chr(ord(i) - key) for i in mess])
    return mess
