import re
s=input()
d=input()

part = re.split(d, s)
print(",".join(part))

#if we find d in s then we split it 
#then join them with ,