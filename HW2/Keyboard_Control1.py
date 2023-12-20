from  djitellopy import  tello

import KeyPressModule as kp
from time import  sleep
import socket
#   setting socket and tello ip address.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)

#   when sendmsg is called, encode the message into utf-8,
#   and use the socket to send the message to tello's ip address.
def sendmsg(msg):
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)

kp.init()
me = tello.Tello()
me.connect()
print("my battery:"+ str(me.get_battery()))

def getKeyboardInput():
    lr, fb, up, yv = 0, 0, 0, 0  # lr速度代表左右平移的速度，fb代表前進後退的速度，ud代表上下飛行的速度，yv代表左右旋轉的速度
    speed = 50

    if kp.getKey("LEFT"):
        lr = -speed
        sendmsg('EXT mled g 0000b00000000b00000000b00bbbbbbb000000b000000b000000b00000000000')
    elif kp.getKey("RIGHT"):
        sendmsg('EXT mled g 000b000000b000000b000000bbbbbbb00b00000000b00000000b000000000000')
        lr = speed

    if kp.getKey("UP"):
        fb = speed
        sendmsg('EXT mled g 000000000000b0000000b0000000b0000b00b00b00b0b0b0000bbb000000b000')
    elif kp.getKey("DOWN"):
        fb = -speed
        sendmsg('EXT mled g 0000b000000bbb0000b0b0b00b00b00b0000b0000000b0000000b00000000000')

    if kp.getKey("w"):
        up = speed
        sendmsg('EXT mled g 000b000000bbb0000b0b0b00b00b00b0000b0000000b0000bbbbbbb00000000')
    elif kp.getKey("s"):
        up = -speed
        sendmsg('EXT mled g 000000000bbbbbbb0000b0000000b0000b00b00b00b0b0b0000bbb000000b000')

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    return [lr, fb, up, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    dis = me.send_command_with_return("EXT tof?")[4:]
    if dis == 'ix ok':
        continue


    if int(dis) < 500:
        sendmsg('EXT mled g r000000r0r0000r000r00r00000rr000000rr00000r00r000r0000r0r000000r')
    else:
        sendmsg('EXT mled g 0000')
    sleep(0.05)



