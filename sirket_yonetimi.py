class sirket():
    def __init__(self,calisanSayisi,sirketIsmi,mudurler,mudurYrd,faliyet):
        self.calisanSayisi=calisanSayisi
        self.sirketIsmi=sirketIsmi
        self.mudurler=mudurler
        self.mudurYrd=mudurYrd
        self.faliyet=faliyet
    def calisanAl(self,sayi):
        self.calisanSayisi +=sayi #çalışan sayısını arttırır
    def calisanCikar(self,sayi):
        self.calisanSayisi-=sayi #çalışsan sayısını azaltır
    def sirketIsmiDegistir(self,isim):
        self.sirketIsmi=isim #isimi günceller
    def sirketBatir(self):
        self.faliyet=False
    def mudurEkle(self,isim):
        self.mudurler.append(isim) #isimi mudurler' e ekler
    def mudurYrdEkle(self,isim):
        self.mudurYrd.append(isim) #isimi mudurYrd' ye ekler
    def bilgileriGoster(self):
        print("""
        Calisan Sayısı: {}
        Sirketin İsmi: {}
        Mudurler: {}
        Mudur Yardımcıları: {}
        Faliyetler: {}
        """.format(self.calisanSayisi,self.sirketIsmi,self.mudurler,self.mudurYrd,self.faliyet))
calistir =sirket(30,"ıt",["ali","mehmet","hasan"],["veli","ali"],True) #calistir adında nesne tanımlanmıştır
calistir.bilgileriGoster() #fonksiyon
calistir.calisanAl(10)
calistir.calisanCikar(20)
calistir.mudurEkle("sinan")
calistir.mudurYrdEkle("yagmur")
calistir.bilgileriGoster()