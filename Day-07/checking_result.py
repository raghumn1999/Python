import sys

math=int(sys.argv[1])
science=int(sys.argv[2])
social=int(sys.argv[3])

result=((math+science+social)/300)*100

if result >= 75:
    print("Distition")
elif result >=60 and result <75:
    print("First class")
elif result >=50 and result < 60:
    print("second class")
elif result >=35:
    print("pass")
else:
    print("fail")
