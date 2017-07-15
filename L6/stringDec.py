data = bytearray(open('secretasset_dec','rb').read())

while True:
	xorkey = int(raw_input('key: '),16)
	length = int(raw_input('length: '),16)
	offset = int(raw_input('offset: '),16)
	data_dec = [chr(xorkey ^ i) for i in data[0x5000+offset:0x5000+offset+length]]
	print '>>'+''.join(data_dec)
	print data_dec