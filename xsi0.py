# x si 0
class tabela(object):
    def __init__(self,tab,index,tab3,tab4):
        self.index = index 
        self.tab = tab
        self.tab = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.index = int('0')
        self.tab3 = tab3
        self.tab3 = []
        self.tab4 = tab4
        self.tab4 =[]
    def afis_l_goala(self):
            for i in self.tab: # o printeaza exact asa cum se vede
                print(i)
    
    def introdu(self,ix):
        self.ix = ix
        ver = 0
        while ver == 0:
            while ver == 0:
                if self.index%2 == 0:
                    #
                        a = raw_input("Introdu pozitia lui x: ")
                        aa = unicode(a)
                        if aa.isnumeric() == True:
                            self.ix = a
                            ver = 1
                        else:
                            ver = 0
                else:
                        b = raw_input("Introdu pozitia lui  0: ")
                        bb = unicode(b)
                        if bb.isnumeric() == True:
                            self.ix = b
                            ver = 1
                        else:
                            ver = 0


        self.verif_poz_in_lista()
           
    
    def verif_poz_in_lista(self):
        tt = int(self.ix)        
        print "Tabela este acum:"
        if int(self.index)%2== 0 and self.tab[(tt-1)/3][((tt-1)%3)] == ' ':
            self.tab[(tt-1)/3][((tt-1)%3)] = 'x'
            self.index +=1
            for i in self.tab:
                print i
            self.verif_castig([])
        elif int(self.index)%2== 1 and self.tab[(tt-1)/3][((tt-1)%3)] == ' ':
            self.tab[(tt-1)/3][((tt-1)%3)] = '0'
            self.index +=1
            for i in self.tab:
                print i
            self.verif_castig([])
        else:
            for i in self.tab:
                print i
            self.introdu(" ")
    
    def verif_castig(self,tab1):
        self.tab1 = tab1
        self.tab1 = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.tab3 = []
        self.tab4 = []
        k =" "
        t = 1 
        t1 = 1     
        for i in range (0,3):
            for j in range (0,3):
                k = self.tab[i][j]
                if k == 'x':
                    self.tab3.append(t)
                    for p in self.tab1:
                        r = 0
                        for h in self.tab3:
                            if h in p and len(self.tab3)>2:
                                r = r+1
                                if r==3:
                                    print("Bravo X ai castigat!!")
                                    self.iesire("")
                                    
                if k == '0':
                    self.tab4.append(t1)
                    for p in self.tab1:
                        r = 0
                        for h in self.tab4:
                            if h in p and len(self.tab4)>2:
                                r = r+1
                                if r==3:
                                    print("Bravo 0 ai castigat!!")
                                    self.iesire("")
                                    
                                    
                t+=1
                t1+=1
    def iesire(self,ii):
        self.ii = ii
        global iii 
        iii = 10
        return iii    

iii = 9
again = "y"
while again =="y":
    iii = 9
    x =  []
    y = ""
    ob1 = tabela(x,1,x,x)
    ob1.afis_l_goala()

    for i in range(0,9):
        ob1.introdu(y)
        if iii == 10:
            break

    if iii == 9:
        print("Remiza")
    again = raw_input("\nIntrodu 'y' pt a continua:\n>")
    print ("\n")  

        















