from cryptography.fernet import Fernet


"@f=pu=iv6@)$@f$qt99eyg!fevmxaqczgnfure6oq@mg5ej$k8lagman"
__key ="@f=pu=iv6@)$@f$qt99eyg!fevmxaqczgnfure6oq@mg5ej$k8lagman".encode('base64')

__fernet = Fernet(__key)

def encrypt(text):
    encypted = str(__fernet.encrypt(text.encode()))
    encrypted_str = encypted[2:len(encypted)-1]
    return encrypted_str

def decrypt(text):
    text = text.encode()
    return __fernet.decrypt(text).decode()

encrypted = encrypt("hello")
decrypted = decrypt(encrypted)
print(encrypted)
print(decrypted)