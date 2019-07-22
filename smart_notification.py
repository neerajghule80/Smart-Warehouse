import bluetooth
import httplib
import urllib

class PushoverSender:
	def __init__(self, user_key, api_key):
		self.user_key = user_key
		self.api_key = api_key

	def send_notification(self, text):
		conn = httplib.HTTPSConnection("api.pushover.net:443")
		post_data = {'user': self.user_key, 'token': self.api_key, 'message': text}
		conn.request("POST", "/1/messages.json", urllib.urlencode(post_data), {"Content-type": "application/x-www-form-urlencoded"})
                     
def main():               
	bd_addr = "98:D3:31:20:7E:C5"
	port = 1
	sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
	sock.connect((bd_addr,port))

	user_key = "u4s7k3fnam17xw8j2xkfdg4goxgipd"
	api_key = "azf6fsyw1qn7rkioj8x9tip8154rjm"

	pushover_sender = PushoverSender(user_key, api_key)

	data = ""
	flag = 0
	level = 31.6
	while 1:
		try:
			data += sock.recv(1024)
			data_end = data.find('\n')
			if data_end != -1:
				rec = data[:data_end]
				#print rec
				rec_sep = rec.find(',')
				if rec_sep != -1:
					hh = float(rec[:rec_sep])
					tt = float(rec[rec_sep+1:])
					if tt < level:
						print "Humidity = " + str(hh) + "\t" + "Temperature = " + str(tt)
						if flag != 0:
							pushover_sender.send_notification('Temperature normal')
							flag = 0
					elif tt >= level:
						if flag != 1:
							pushover_sender.send_notification('Temperature exceeded')
							flag = 1
						print "Humidity = " + str(hh) + "\t" + "Temperature = " + str(tt) + "\tTemperature exceeding!!"
				data = data[data_end+1:]
		except KeyboardInterrupt:
			break
	sock.close()
	
if __name__ == '__main__':
    main()
