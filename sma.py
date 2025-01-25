#!/usr/bin/python
import struct
import sys
import time
import json
from struct import *
from twisted.web import server, resource
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.application.internet import MulticastServer

user_pw = '0000' # default is '0000'
code_login = 0xfffd040d
code_total_today = 0x54000201
code_spot_ac_power = 0x51000201
src_serial = 2130422522 # change this to your serial number
dst_serial = 4294967295 
comm_port = 9522
comm_dst = '192.168.1.12' # change this to your IP

def get_encoded_pw(password):
    # user=0x88, install=0xBB
    encpw=[0x88,0x88,0x88,0x88,0x88,0x88,0x88,0x88,0x88,0x88,0x88,0x88]
    for index in range(min(len(encpw), len(password))):
        encpw[index] = encpw[index] + ord(password[index])

    ret = ""
    for ch in encpw:
        ret = ret + hex(ch).replace('0x','')
    return ret

cmd_login =                '534d4100000402a000000001003a001060650ea0ffffffffffff00017800%s00010000000004800c04fdff07000000840300004c20cb5100000000%s00000000' % (struct.pack('<I', src_serial).encode('hex'), get_encoded_pw(user_pw))
cmd_logout = '534d4100000402a00000000100220010606508a0ffffffffffff00037800%s000300000000d7840e01fdffffffffff00000000' % (struct.pack('<I', src_serial).encode('hex'))

cmd_query_total_today =    '534d4100000402a00000000100260010606509a0ffffffffffff0000780036abfb7e000000000000f180000200540001260022ff260000000000'
cmd_query_spot_ac_power =  '534d4100000402a00000000100260010606509e0ffffffffffff0000780036abfb7e00000000000081f0000200510001260022ff260000000000'

sma_data = {}
query_list = []
rea = 0

class MulticastClientUDP(DatagramProtocol):

  def datagramReceived(self, datagram, address):
      global sma_data, data_available
      data = datagram.encode('hex')
      code = get_code(datagram)

      if code == code_login:
         send_command(cmd_query_total_today)

      if len(datagram) <= 58:
         print "data access failed"
         reactor.stop()
         exit
      if code == code_total_today:
         total = get_long_value_at(datagram, 62)
         today = get_long_value_at(datagram, 78)
         sma_data['total'] = total
         sma_data['today'] = today
         send_command(cmd_query_spot_ac_power)
      if code == code_spot_ac_power:
         value = get_long_value_at(datagram, 62)
         if value == 0x80000000:
            value = 0
         sma_data['spotacpower'] = value
         output_data = json.dumps(sma_data)
         print output_data
         reactor.stop()

def send_command(cmd):
   data = cmd.decode('hex')
   rea.write(data, (comm_dst, comm_port))

def get_code(data):
   c = unpack('I', data[42:46])
   return c[0]

def get_long_value_at(data, index):
   v = unpack('I', data[index:index+4])
   return v[0]

def callfunc(x):
    reactor.stop()

rea = reactor.listenUDP(0, MulticastClientUDP())
_DelayedCallObj = reactor.callLater(5, callfunc, "callfunc called after 4 sec")
send_command(cmd_login)
reactor.run()