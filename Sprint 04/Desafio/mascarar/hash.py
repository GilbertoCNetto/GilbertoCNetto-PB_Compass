import hashlib

while True:
    string = input('Digite uma frase: ')

    # Gerando o hash SHA-1
    hash_sha1 = hashlib.sha1(string.encode()).hexdigest()
    print(hash_sha1)
    