import struct


def __mac_s2a(mac):
	dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
	mac = mac.lower()
	tmp = mac.split(':')
	res = ''
	for i in range(len(tmp)):
		uc = struct.pack('B', 16*dict[tmp[i][0]] + dict[tmp[i][1]])
		res = res + uc
	return res

def __mac_a2s(mac):
	return ":".join("{:02x}".format(ord(c)) for c in mac)


def __mac_add(mac, step=1):
	mac1, mac2 = struct.unpack("!HI", mac)
	mac2 = mac2 + step
	return struct.pack("!HI", mac1, mac2)


def mac_add(mac, num=0, step=1):
	macTmp = __mac_s2a(mac)
	for i in range(num):
		macTmp = __mac_add(macTmp, step)
	return __mac_a2s(macTmp)

