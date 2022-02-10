import json
import time
from utils import get_sign
from utils.aes_test import PrpCrypt

def sleep(n_secs):
    time.sleep(n_secs)

def sign_value(request):
    body = request.get("json")
    print(body)
    sign = get_sign.sign_body(body)
    print(sign)
    request['json']['sign'] = sign


def aes_jiami(request):
    body = request.get("json")
    params_str = json.dumps(body.get("params"))
    print(params_str)
    pc = PrpCrypt('12345678\0\0\0\0\0\0\0\0')
    body_crypt = pc.encrypt(params_str)
    request["json"]["params"] = body_crypt


def aes_jiemi(response):
    res_body = json.loads(response.content)
    # print(res_body)
    res_data = res_body.get("data")
    # print('data{}'.format(res_data))
    pc = PrpCrypt('12345678\0\0\0\0\0\0\0\0')
    de_res_data = pc.decrypt(res_data)
    dict_data = json.loads(de_res_data)
    res_body['data'] = dict_data
    bytes_body = bytes(json.dumps(res_body), encoding="utf-8")
    response.text = bytes_body
    response.body = res_body
    response.json = res_body

