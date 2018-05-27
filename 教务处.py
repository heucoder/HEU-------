import requests

keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

def encodeInp(instr):
    outstr = ""
    chr1, chr2, chr3 = "","",""
    enc1, enc2, enc3, enc4  = "","","",""
    i = 0
    while(i < len(instr)):
        if i < len(instr):
            chr1 = instr[i]; i+=1
        if i < len(instr):
            chr2 = instr[i]; i+=1
        if i < len(instr):
            chr3 = instr[i]; i+=1
        enc1 = ord(chr1)>>2
        if chr2 != "":
            enc2 = ((ord(chr1) & 3) << 4) | (ord(chr2) >> 4)
        else:
            enc2 = (ord(chr1) & 3) << 4
        if chr3 != "" and chr2 != "":
            enc3 = ((ord(chr2) & 15) << 2) | (ord(chr3) >> 6)
        elif chr2 != "":
            enc3 = (ord(chr2) & 15) << 2
        if chr3 != "":
            enc4 = ord(chr3) & 63
        if chr2 == "":
            enc3 = 64
            enc4 = 64
        elif chr3 == "":
            enc4  = 64
        # print(enc1, enc2, enc3, enc4)
        outstr = outstr + keyStr[enc1] + keyStr[enc2] + keyStr[enc3] + keyStr[enc4]
        chr1, chr2, chr3 = "", "", ""
        enc1, enc2, enc3, enc4 = "", "", "", ""
    return outstr

def getPassKey(username, password):
    encodeInp_username = encodeInp("你的学号")
    encodeInp_password = encodeInp("你的密码")
    passKey = encodeInp_username+"%%%"+encodeInp_password
    print(passKey)
    return passKey

def getcontent(username = "你的学号", password = "你的密码"):   #密码是身份证后八位或者自己设置的
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36',
        'Host':'edusys.hrbeu.edu.cn',
        'Origin':'http://edusys.hrbeu.edu.cn'
    }
    url = 'http://edusys.hrbeu.edu.cn/jsxsd/xk/LoginToXk'
    passKey = getPassKey(username, password)
    data = {
        'encoded':
            passKey
    }
    session = requests.Session()
    resp = session.post(url, data)
    # print(resp.text)

    # geturl = 'http://edusys.hrbeu.edu.cn/jsxsd/kscj/cjcx_query.do'
    # resp = session.get(geturl)
    # print(resp.text)

    score_url = "http://edusys.hrbeu.edu.cn/jsxsd/kscj/cjcx_list"
    #2015-1016第一学期:2015-1016-1
    #2015-1016第二学期:2015-1016-2
    #data内其余内容无需修改
    data = {
        'kksj':'2015-2016-1',
        'kczx':'',
        'kcmc':'',
        'xsfs':'all',
    }
    resp = session.post(score_url, data)
    print(resp.text)

if __name__ == '__main__':
    getcontent()
