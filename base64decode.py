import base64
f1 = open('beijiema.txt', 'r')
f2 = open('jiemahou.txt', 'w')
base64.decode(f1, f2)
f1.close()
f2.close()
