#coding=utf-8
import urllib,re


meteorlist=['辽宁省气象台','辽宁省大连市气象台']
alertinfo=[]
level=[]
description=[]

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getRel(html,reg):
    mre = re.compile(reg)
    relList = re.findall(mre,html)
    return relList

html = getHtml("http://search.weather.com.cn/static/xxfb/rss/alert.xml")

meteorlen=len(meteorlist)
for i in range(0,meteorlen):
    reg1 = r'<title>'+meteorlist[i]+'(.+?)</title>'    # alertinfo
    reg2 = meteorlist[i]+r'发布.+?<alevel>(.+?)</alevel>' # level
    reg3 = meteorlist[i] + r'.+?<description><!\[CDATA\[(.+?)\]\]>\s*</description>' # description
    tempAlert=getRel(html,reg1)
    tempLevel=getRel(html,reg2)
    tempDesc=getRel(html,reg3)
    L=len(tempAlert)
    for j in range(0,L):
        tempAlert[j]=meteorlist[i]+tempAlert[j]
    
    alertinfo=alertinfo+tempAlert
    level=level+tempLevel
    description=description+tempDesc 


strAler='@'.join(alertinfo)
strLeve='@'.join(level)
strDesc='@'.join(description)

#print alertinfo
#print level
#print description

print len(alertinfo)
print len(level)
print len(description)


_mlist = ['alertinfo','level','description']


f=open(r'Alert.html','w')
f.write('[{')
f.write('\"'+_mlist[0]+'\":\"'+strAler+'\",')
f.write('\"'+_mlist[1]+'\":\"'+strLeve+'\",')
f.write('\"'+_mlist[2]+'\":\"'+strDesc+'\"')
f.write('}]')

f.close()



















