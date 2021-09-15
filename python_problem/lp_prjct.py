def nm():
    nmbr = ['01703500587','01557393119','01915646010','01700000001']
    numbr2 = []#loop er vitore dile hoyna kn ? 
    while True:
        m_numbr = input("enter your number: " )
        #print("you have to entere number")
        print("do u want to quite? please press q ")
        if m_numbr == 'q':
                break
        elif m_numbr == '':
                print("please insert number. Do u want to quite? please press q ")
                continue
        elif len(m_numbr) < 11 or len(m_numbr) > 11:
                print("please insert 11 digit number")
                continue
        numbr2.append(m_numbr)
    print (numbr2) 
    temp = []
    for data in numbr2:
        if data in nmbr:
            temp.append(data)
    return temp

k = nm()
print(k)