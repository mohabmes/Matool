import os


def get_nmap(option, ip):
    cmd = "nmap " + option + " " + ip
    prc = os.popen(cmd)
    res = str(prc.read())
    return res