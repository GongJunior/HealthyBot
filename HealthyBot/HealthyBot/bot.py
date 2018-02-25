import config
import socket
import re
import time

#region FUNCTIONS
def chat(sock,msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))

def verifyAccess(user):
    """
    Verify access level of user
    """
    raise NotImplementedError("Verify access level of user")

#endregion

#region CONNECT
s = socket.socket()
s.connect((HOST,PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
#endregion

#region CHATMGT
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :") #id a chat message

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:

        username = re.search(r"\w+", response).group(0) # return the entire match
        message = CHAT_MSG.sub("", response)

        if message.startswith(command):
            raise NotImplementedError("Update healthtip variable!")
            confimation = "Health Tip Updated by " + username
            chat(s,confimation)
            print(username + ": " message)
        
        raise NotImplementedError("send standard or custom messages in regular intervals")
    time.sleep(1/config.RATE)
#endregion