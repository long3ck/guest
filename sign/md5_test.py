#coding=utf-8
__author__ = 'Chenkun'
__date__ = '2017/06/20 10:02'

import hashlib
md5 = hashlib.md5()
sign_str = "@admin123"
sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
md5.update(sign_bytes_utf8)
sign_md5 = md5.hexdigest()
print(sign_md5)