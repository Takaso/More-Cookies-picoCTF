import base64; import httpx;
session_cookie:str = input("Insert the session cookie > ");
def xor_bit(p: int, bit: int, d: int) -> str:
    b = base64.b64decode(d); b = str(b); x = list(b); x[p] = chr(ord(x[p])^bit);
    return base64.b64encode("".join(x).encode("utf-8"));
for _ in range(0x80):
    for __ in range(0x80):
        ___ = xor_bit(_, __, session_cookie); x = httpx.get("http://mercury.picoctf.net:10868/", cookies={"auth_name": str(___)}).text
        if "picoCTF{" in x:
            print(x);
            break;
input();