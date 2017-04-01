#!/usr/bin/env python
#coding:utf-8
#author:ChaplinJ
#workFor:构建botNet的模板
import paramiko
class Client:
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
        print ''
    def connect(self):
        try:
            s = paramiko.SSHClient()
            s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            s.connect(hostname=self.host, port=22, username=self.user, password=self.password)
            return s
        except Exception,e:
            print e
            print '[-] Error Connecting'
    def send_command(self,cmd):
        stdin, stdout, stderr = self.session.exec_command(cmd)
        stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
        return stdout.read()
def botNetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' + client.host
        print '[+] ' + output + '\n'
def addClient(host,user,password):
    client = Client(host,user,password)
    botNet.append(client)
botNet=[]
def main():
    addClient('192.168.243.129', 'ChaplinJ', '123')
    botNetCommand('uname -a')
    botNetCommand('cat /etc/issue')
    print ''
if __name__ == '__main__':
    main()