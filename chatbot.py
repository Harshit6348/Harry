qna ={
    'HI':'HEY',
    'HOW ARE YOU?':'I AM FINE',
    'WHO ARE YOU?':'MYSELF HARRY',
    'HOW OLD ARE YOU?':'I AM 18 YEARS OLD',

}
while True:
    qs=input()

    if(qs=='quit'):
        break

    else:
        print(qna[qs])