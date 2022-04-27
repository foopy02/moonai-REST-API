from cryptography.fernet import Fernet

"@f=pu=iv6@)$@f$qt99eyg!fevmxaqczgnfure6oq@mg5ej$k8lagman"
__key = b'5i8TMXAhKVO-SZYC3WVUnShBBqe7ODDIaEBBVCTMgJg='

__fernet = Fernet(__key)

def encrypt(text):
    encypted = str(__fernet.encrypt(text.encode()))
    wow = encypted[2:len(encypted)-1]
    return wow

def decrypt(text):
    text = text.encode()
    return __fernet.decrypt(text).decode()

