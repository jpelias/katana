# -*- coding: utf-8 -*-
#"ぐ" 


a = raw_input(">")

a = a.decode('utf8')

s = ord(a) + 12352

print s, unichr(s)
