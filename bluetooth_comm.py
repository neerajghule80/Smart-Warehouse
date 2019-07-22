import bluetooth

bd_addr = "98:D3:31:20:7E:C5"		#use bluetoothctl
port = 1
sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)	#RFCOMM is reliable stream-based protocol. L2CAP is a packet-based protocol
sock.connect((bd_addr,port))

data = ""
while 1:
	try:
		data += sock.recv(1024)
		data_end = data.find('\n')
		if data_end != -1:
			rec = data[:data_end]	#A colon on the left side of an index means everyting before, but not including, the index.
			#print rec
			rec_sep = rec.find(',')
			if rec_sep != -1:
				hh = float(rec[:rec_sep])
				tt = float(rec[rec_sep+1:])
				if tt < 30:
					print "Humidity = " + str(hh) + "\t" + "Temperature = " + str(tt)
				elif tt > 30:
					print "Humidity = " + str(hh) + "\t" + "Temperature = " + str(tt) + "\tTemperature exceeding 30!!"
			data = data[data_end+1:]	#A colon on the right side of an index means everything after the specified index.
	except KeyboardInterrupt:
		break
sock.close()
