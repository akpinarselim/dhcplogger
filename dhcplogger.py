#!/usr/bin/env python
# -*- coding: cp1254 -*-
###----------###
###- DHCP leases dosyasi okumak icin acilir.
dhcpfile=open("/var/dhcpd/var/db/dhcpd.leases").read()
#---
#######################################################################
### KAYITLARI TUTMAK ICIN SAAT VE GUN BILGILERI DEGISKENLERE ATANIR ###
#######################################################################

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
### ---------------------------------------------------------------- ###

######################################################
### LEASES ICINDEKI KAYITLAR AYRILIR "lease-lease" ###
######################################################
leases=[]
le_split=[]
leases=dhcpfile.split("lease") ##Belge istenilen parcalara ayrildi.
x=1
y=len(leases) ##Listedeki degerlerin sayisi y değiskenine atanir.
### ---------------------------------------------- ###

###- Kayit dosyasi
dhcp5651=open("dhcp5651_{0}.txt".format(tarihdosya),"a") ##Kayitlarin tutulacaği dosya o gunun tarihine gore isimlendirilerek acilir.
#---

###########################
### BASLANGIC DEGERLERI ###
###########################

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
### -------------------- ###

#####################################################
### GEREKLI BILGILER AYIKLANIR VE DOSYAYA YAZILIR ###
#####################################################

while x<y: ##Leases kisimlari
    le_split=leases[x].split(" ")
    a=1
    b=len(le_split)
    ###
    while True: ##Leases icindeki kisimlar
        ###- Ip bilgisi
        dhcp5651.write("\n")
        dhcp5651.write(le_split[1].strip())
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        #---

        ###- Baslangic tarih ve saat  bilgisi
        z=0
        while True:
            if le_split[z]=="starts":
                break
            z=z+1
        dhcp5651.write(le_split[z+2])
        dhcp5651.write("-")
        dhcp5651.write(le_split[z+3].replace(";","").strip())
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        #---

        ###- Bitis tarih ve saat  bilgisi
        while True:
            if le_split[z]=="ends":
                break
            z=z+1
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        dhcp5651.write(le_split[z+2])
        dhcp5651.write("-")
        dhcp5651.write(le_split[z+3].replace(";","").strip())
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        dhcp5651.write("\t")
        #---

        ###- Mac bilgisi
        while True:
            if le_split[z]=="ethernet":
                break
            z=z+1
        dhcp5651.write(le_split[z+1].replace(";","").replace("}","").strip())
        #---
        ### -------------------------- ###
        break
    x=x+1    
###-Dosya kapatilir.
dhcp5651.close()
#---
### --------------------------------------------- ###

########################################################
### DOSYALARI GÖNDERMEK IÇIN AYARLAR ".CONF" DOSYASI ###
########################################################
check=0
say=len(sys.argv)
config_check=open("dhcplogger.conf","a") ##Ilk acilis icin dosya olusturulur.
config_check=open("dhcplogger.conf").read()
if config_check == "":
    print "Ilk acilis lutfen ayarlari dikkatlice giriniz."
    config_check=open("dhcplogger.conf","a")
    config_check.write("0:192.168.1.1:log:root:toor")
    config_check.close()
config_zero=open("dhcplogger.conf").read() ##Ayar dosyasi parcalara ayrilir.
deger=[]
deger=config_zero.split(":")
##1 yada 0  # deger[0] ##Daha once kayit olup olmadigini burdaki rakam belirler.
##Ip        # deger[1]
##Klasor    # deger[2]
##Kullanici # deger[3]
##Şifre     # deger[4]
print "#########################################################################- O X#"
print "#                                  Selim Akpinar                              #"
print "#                              pfSense log kaydedici                          #"
print "#                                    Surum 0.3                              #"
print "#-----------------------------------------------------------------------------#"
print "#Varsayilan degerler:                                                         #"
print "#---                                                                          #"
print "#Ip: " + deger[1] + "                                                         #"
print "#Klasor: " + deger[2] + "                                                     #"
print "#Kullanici: " + deger[3] + "                                                  #"
print "#Sifre: " + deger[4] + "                                                      #"
print "#Duzenlemek icin '-d' parametlersini giriniz. (or. .../dhcplogger.py -d)      #"
print "###############################################################################"
print ""
if deger[0] == "0": ##Kullanicidan veriler istenir ve değiskenlere atanir.
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
if say == 2:
    if sys.argv[1] == "-d": ##Kullanicidan veriler istenir ve değiskenlere atanir.
        while True:
            try:
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
            except:
                print "Hatali giris"
            else:
                break
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
    
###########################
### SMBCLIENT KOMUTLARI ###
###########################
import os
smb_com='/usr/local/bin/smbclient \\\\\\\\{0}\\\\{1} -U {2}%"{3}" -c "prompt; put dhcp5651_{4}.txt"'.format(deger[1],deger[2],deger[3],deger[4],tarihdosya)
os.system(smb_com)




