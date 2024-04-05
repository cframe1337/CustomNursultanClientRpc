import os as o
import sys as s
import time as t

from pypresence import Presence

def premain(userid: any, nickname: any):
    if len(userid) != 0 and len(nickname) != 0:
        main(userid, nickname)
        o.system('pause')
    else:
        o.system('clear')


def main(userid: any, nickname: any):
    rpc.update(
        details=f"Username: {nickname}",
        state=f"UID: {userid}",
        start=round(t.time()),
        large_image="https://github.com/cframe1337/CustomNursultanClientRpc/blob/main/nursultan-icon.gif?raw=true",
        large_text=f"nursultan.fun",
    )
    s.stdout.write('\nНажмите Enter чтобы закрыть программу.\n')

    
def c_input(input_target: str):
    s.stdout.write(f'Input your {input_target}: ')
    return input()

if __name__ == '__main__':
    rpc = Presence(client_id=1225767284824346725)
    # Здесь вы можете использовать свой клиент айди скопированный в проекте на Discord Developers Portal
    # You can use own client id that you copied from project at Discord Developers Portal
    rpc.connect()

    premain(c_input('userid'), c_input('username'))
