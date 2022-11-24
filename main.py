from Exscript import Account
from Exscript.protocols import SSH2

PARAM = 'phone'

def analyze_pool(info):
    pool = info.split('\r')
    with open("config.cfg", 'w') as f:
        for index, info in enumerate(pool):
            if PARAM in info:
                name = pool[index].split('-', 1)[1]
                if (host := pool[index + 1]).__contains__('host'):
                    if (mac := pool[index + 2]).__contains__('client-identifier'):
                        f.write(name + host + mac + '\n')


def start():
    account = Account('cadmin', 'crab290VD')
    connect = SSH2()
    connect.connect('10.254.254.25')
    connect.login(account)
    connect.execute('terminal length 0')
    connect.execute('sh run | s ip dhcp pool')
    connect.send('exit')
    phone_pool = analyze_pool(connect.response[25:])
    # print(phone_pools)
    # print(output[23:])

def fu():
    pass
print('dgdfg')
#fgwerg

if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print("Some unknown exception is raised:", e)
