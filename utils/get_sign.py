import hashlib


def sign_body(body):
    apikey = '12345678'
    a = ["".join(i) for i in body.items() if i[0] != "sign" and i[1] != '']
    strA = "".join(sorted(a))+apikey

    def jiamimd5(body):
        m = hashlib.md5()
        m.update(body.encode('UTF-8'))
        return m.hexdigest()

    sign = jiamimd5(strA)
    return sign

if __name__ == '__main__':
    body = {
        "username": "test",
        "passworld": "123456",
        "mail": "",
        "sign": ""
    }
    sign_body(body)