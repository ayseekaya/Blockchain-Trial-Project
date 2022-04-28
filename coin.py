from hashlib import sha256
from string import hexdigits
import time


class block:
    def __init__(self,timeStamp,data,previousHash=" "):
        self.timestamp=timeStamp
        self.data=data
        self.previousHash=previousHash
        self.kuvvet=0
        self.hash=self.hesapla()

    def hesapla(self):
        while True:
            self.kuvvet=self.kuvvet+1
            ozet=sha256((str(self.timestamp)+str(self.data)+str(self.previousHash)+str(self.kuvvet)).encode()).hexdigest()
            if ozet[0:4]=="0000":
                break
        return ozet

class blockChain:
    def __init__(self):
        self.chain=[self.genesisOlustur()]

    def genesisOlustur(self):
        return block(time.ctime(),"kaya","")
    
    def blockEkle(self,data):
        node=block(time.ctime(),data,self.chain[-1].hash)
        self.chain.append(node)
    
    def kontrol(self):
        for i in range(len(self.chain)):
            if i!=0:
                ilk=self.chain[i-1].hash
                suan=self.chain[i].previousHash
                if ilk!=suan:
                    return "Zincir kopmuş"
                if sha256((str(self.chain[i].timestamp)+str(self.chain[i].data)+str(self.chain[i].previousHash)+str(self.chain[i].kuvvet)).encode()).hexdigest()!= self.chain[i].hash:
                    return "Zincir kopmuş"

        return "Sağlam"

    def listeleme(self):
        print("Blockchain = \n")    
        for i in range(len(self.chain)):
            print("-------------------------")
            print("Block =>",i,"\nHash =",str(self.chain[i].hash),"\nZaman Damgası =",str(self.chain[i].timestamp),"\nData=",str(self.chain[i].data),"\nKuvvet=",str(self.chain[i].kuvvet),"\nPreviousHash= ",str(self.chain[i].previousHash))    
            print("-------------------------")
                


asilChain=blockChain()
while True:
    print("Lütfen seçiminizi yapınız\n Block Eklemek için 1\n Blockchain'i görmek için 2\n zinciri kontrol etmek için 3\n çıkmak için 4 ü seçin")
    data=input()
    if data=="1":
        print("Gönderilen miktarı giriniz = ")
        miktar=input()
        asilChain.blockEkle(miktar)
    elif data=="2":
        asilChain.listeleme()
    elif data=="3":
        print(str(asilChain.kontrol()))
    elif data=="4":
        break
    












