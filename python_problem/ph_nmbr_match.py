def nm():
    nmbr = ['01703500587','01557393119','01915646010']
    for i in range(3):
        m_numbr = input("enter your number: " )
        numbr2 = []
        numbr2 = m_numbr
        if numbr2 in nmbr:
            print("number match",numbr2)
        else:
            print("hello loser")

nm()