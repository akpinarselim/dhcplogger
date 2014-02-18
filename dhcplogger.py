#!/usr/bin/env python 
# -*- coding: cp1254 -*- 
###-DHCP leases dosyasi okumak icin acilir. 
dhcpfile=open("/var/dhcpd/var/db/dhcpd.leases").read() 
#--- 
###-Kontrol icin zaman deðiskenleri atanir. 
import time 
import sys 
zaman=time.localtime() 
yil=str(zaman[0]) 
ay=str(zaman[1]) 
gun=str(zaman[2]) 
if len(ay) == 1: 
    ay="0" + str(zaman[1]) 
if len(gun) == 1: 
    gun="0" + str(zaman[2]) 
tarih=yil+"/"+ay+"/"+gun 
tarihdosya=yil+"-"+ay+"-"+gun ##Son olarak tarih formati "gun/ay/yil" seklinde 
#--- 
###-Leases icindeki kayitlar ayrilir "lease-lease" 
leases=[] 
leases=dhcpfile.split("lease") ##Belge istenilen parcalara ayrildi. 
x=1
y=len(leases) ##Listedeki degerlerin sayisi y deðiskenine atanir. 
#--- 
###-Kayit dosyasi 
dhcp5651=open("dhcp5651_{0}.txt".format(tarihdosya),"a") ##Kayitlarin tutulacaði dosya o gunun tarihine gore isimlendirilerek acilir. 
#--- 
###-Baslangic degerleri. 
dhcp5651.write("Ip adresi") 
dhcp5651.write("\t") 
dhcp5651.write("\t") 
dhcp5651.write("\t") 
dhcp5651.write("Kullanima Baslama Tarih-Saati") 
dhcp5651.write("\t") 
dhcp5651.write("\t") 
dhcp5651.write("\t") 
dhcp5651.write("Kullanima Bitis Tarih-Saati") 
dhcp5651.write("\t") 
dhcp5651.write("\t") 
dhcp5651.write("\t") 
dhcp5651.write("\t") 
dhcp5651.write("\t") 
dhcp5651.write("Mac adresi") 
#--- 
###-Listedeki deðiskenler dosyaya yazilir. 
while x<y: 
    degerler=leases[x].split() 
    if degerler[4] == tarih and degerler[8] == tarih: 
        if (len(leases[x]))<260: 
            dhcp5651.write("\n") 
            dhcp5651.write(degerler[0]) #Ip 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write(degerler[4]) #Tarih 
            dhcp5651.write("-") 
            dhcp5651.write(degerler[5].replace(";","")) #Saat 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write(degerler[8]) #Tarih 
            dhcp5651.write("-") 
            dhcp5651.write(degerler[9].replace(";","")) #Saat 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write("\t") 
            dhcp5651.write(degerler[23].replace(";","")) #Mac 
        else: 
            if degerler[8] == "tstp": 
                x=x+1
            else: 
                dhcp5651.write("\n") 
                dhcp5651.write(degerler[0]) #Ip 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write(degerler[4]) #Tarih 
                dhcp5651.write("-") 
                dhcp5651.write(degerler[5].replace(";","")) #Saat 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write(degerler[8]) #Tarih 
                dhcp5651.write("-") 
                dhcp5651.write(degerler[9].replace(";","")) #Saat 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write("\t") 
                dhcp5651.write(degerler[27].replace(";","")) #Mac 
                ##Parcalama tamamlandi. 
    x=x+1
#--- 
###-Dosya kapatilir. 
dhcp5651.close() 
#--- 
  
########################################################################### 
###------------------DOSYALARI GÖNDERMEK IÇIN AYARLAR-------------------### 
########################################################################### 
  
###-Dosyayi istenilen konuma gondermek icin gerekli deðiskenler atanir. 
check=0
say=len(sys.argv) 
###-Ilk acilis icin dosya olusturulur. 
config_check=open("dhcplogger.conf","a") 
config_check=open("dhcplogger.conf").read() 
if config_check == "": 
    print "Ilk acilis lutfen ayarlari dikkatlice giriniz."
    config_check=open("dhcplogger.conf","a") 
    config_check.write("0:192.168.1.1:log:root:toor") 
    config_check.close() 
#--- 
###-Ayar dosyasi parcalara ayrilir. 
config_zero=open("dhcplogger.conf").read() 
deger=[] 
deger=config_zero.split(":") 
##Ip        # deger[1] 
##Klasor    # deger[2] 
##Kullanici # deger[3] 
##Þifre     # deger[4] 
#--- 
###-Ayarlar icin dosya kontrol edilir ve duruma gore kural calistirilir. 
print "#########################################################################- O X#"
print "#                                  Selim Akpinar                              #"
print "#                              pfSense log kaydedici                          #"
print "#                                    Surum 0.1                                #"
print "#-----------------------------------------------------------------------------#"
print "#Varsayilan degerler:                                                         #"
print "#---                                                                          #"
print "#Ip: " + deger[1] + "                                                             #"
print "#Klasor: " + deger[2] + "                                                                  #"
print "#Kullanici: " + deger[3] + "                                                              #"
print "#Sifre: " + deger[4] + "                                                                 #"
print "#Duzenlemek icin '-d' parametlersini giriniz. (or. .../dhcplogger.py -d)      #"
print "###############################################################################"
print "" 
if deger[0] == "0": 
    ###-Kullanicidan veriler istenir ve deðiskenlere atanir. 
    while True: 
        ip=raw_input("Hedef bilgisayarin ip adresi: ") 
        share_folder=raw_input("Hedef bilgisayardaki paylasilan klasorun adi: ") 
        username=raw_input("Hedef bilgisayardaki yetkili kullanici: ") 
        password=raw_input("Hedef bilgisayardaki yetkili kullanicinin sifresi: ") 
        son=raw_input("Ayarlar kaydedilsin mi? (e/h): ") 
        son=str(son) 
        if son == "e": 
            check=1
            break
    #--- 
if say == 2: 
    if sys.argv[1] == "-d": 
        while True: 
            try: 
                while True: 
                ###-Kullanicidan veriler istenir ve deðiskenlere atanir. 
                    ip=raw_input("Hedef bilgisayarin ip adresi: ") 
                    share_folder=raw_input("Hedef bilgisayardaki paylasilan klasorun adi: ") 
                    username=raw_input("Hedef bilgisayardaki yetkili kullanici: ") 
                    password=raw_input("Hedef bilgisayardaki yetkili kullanicinin sifresi: ") 
                    son=raw_input("Ayarlar kaydedilsin mi? (e/h): ") 
                    son=str(son) 
                    if son == "e": 
                        check=1
                        break
            except: 
                print "Hatali giris"
            else: 
                break
            #--- 
#--- 
if check == 1: 
    config_write=open("dhcplogger.conf","w") 
    config_write.write("1:") 
    config_write.write(ip) 
    config_write.write(":") 
    config_write.write(share_folder) 
    config_write.write(":") 
    config_write.write(username) 
    config_write.write(":") 
    config_write.write(password) 
    config_write.close() 
  
########################################################################### 
###---------------------------------------------------------------------### 
###---------------------------------------------------------------------### 
########################################################################### 
      
########################################################################### 
###--------------------------SMBCLIENT KOMUTLARI------------------------### 
########################################################################### 
  
import os 
smb_com='/usr/local/bin/smbclient \\\\\\\\{0}\\\\{1} -U {2}%"{3}" -c "prompt; put dhcp5651_{4}.txt"'.format(deger[1],deger[2],deger[3],deger[4],tarihdosya) 
os.system(smb_com) 
  
  
########################################################################### 
###---------------------------------------------------------------------### 
###---------------------------------------------------------------------### 
########################################################################### 
