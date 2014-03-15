#!/usr/bin/env python
# -*- coding: cp1254 -*-
#---
import time
import sys
###- Kayitlari tutmak icin gun ve saat bilgileri degiskenlere atanir
tarih=time.strftime("%Y/%m/%d")
tarihdosya=time.strftime("%Y-%m-%d")
saat=time.strftime("%H:%M:%S")
saatdosya=time.strftime("%H.%M")
simdisaat=time.time() ##Anlik saat bilgisi
#---
######################
###- FONKSIYONLAR -###
######################
###- Saat Hesabi
def timecalc(xonce):
    xonce=time.time()-(60*60*xonce)
    xonce=(time.ctime(xonce))
    xonce=time.strptime(xonce)
    xonce=time.mktime(xonce)
    return xonce
#---
###- Ip Bilgisi
def ipadres(aa):
    dhcp5651.write("\n")
    dhcp5651.write(le_split[1].strip())
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    #---
###- Baslangic tarih ve saat  bilgisi
def tarihbas(ac):
    dhcp5651.write(le_split[ac+2])
    dhcp5651.write("-")
    dhcp5651.write(le_split[ac+3].replace(";","").strip())
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    #---
###- Bitis tarih ve saat  bilgisi
def tarihbit(ab):
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    dhcp5651.write(le_split[ab+2])
    dhcp5651.write("-")
    dhcp5651.write(le_split[ab+3].replace(";","").strip())
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    dhcp5651.write("\t")
    #---
###- Mac bilgisi
def macadres(ad):
    dhcp5651.write(le_split[ad+1].replace(";","").replace("}","").strip())
    #---
###- Epoch hasabi
def epochc(ae1,ae2):
    timec=(ae1+" "+ae2).strip()
    epoch=time.strptime(timec, "%Y/%m/%d %H:%M:%S")
    epoch=time.mktime(epoch)
    return epoch
#---
### --------------- ###
#######################
   
###- DHCP leases dosyasi okumak icin acilir.
dhcpfile=open("/var/dhcpd/var/db/dhcpd.leases").read()
#---

###- Leases icindeki bilgiler ayrilir | "lease-lease"
leases=[]
le_split=[]
leases=dhcpfile.split("lease") ##Belge istenilen parcalara ayrildi.
x=1
y=len(leases) ##Listedeki degerlerin sayisi y değiskenine atanir.
#---
###- Kayit dosyasi
dhcp5651=open("/var/log/dhcplogger/dhcp5651_{0}_{1}.txt".format(tarihdosya,saatdosya),"a") ##Kayitlarin tutulacaği dosya o gunun tarihine gore isimlendirilerek acilir.
#---
###- Baslangic degerleri
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
########################################################
### DOSYALARI GÖNDERMEK IÇIN AYARLAR ".CONF" DOSYASI ###
########################################################
check=0
say=len(sys.argv)
config_check=open("/sbin/dhcplogger.conf","a") ##Ilk acilis icin dosya olusturulur.
config_check=open("/sbin/dhcplogger.conf").read()
if config_check == "":
    print "Ilk acilis lutfen ayarlari dikkatlice giriniz."
    config_check=open("/sbin/dhcplogger.conf","a")
    config_check.write("0:192.168.1.1:log:root:toor:4")
    config_check.close()
config_zero=open("/sbin/dhcplogger.conf").read() ##Ayar dosyasi parcalara ayrilir.
deger=[]
deger=config_zero.split(":")
##1 yada 0  # deger[0] ##Daha once kayit olup olmadigini burdaki rakam belirler.
##Ip        # deger[1]
##Klasor    # deger[2]
##Kullanici # deger[3]
##Şifre     # deger[4]
##Saat      # deger[5]
print "#########################################################################- O X#"
print "#                                  Selim Akpinar                              #"
print "#                              pfSense log kaydedici                          #"
print "#                                    Surum 0.2                                #"
print "#-----------------------------------------------------------------------------#"
print "#Varsayilan degerler:                                                         #"
print "#---                                                                          #"
print "#Ip: " + deger[1] + "                                                         #"
print "#Klasor: " + deger[2] + "                                                     #"
print "#Kullanici: " + deger[3] + "                                                  #"
print "#Sifre: " + deger[4] + "                                                      #"
print "#Saat: " + deger[5] + "                                                       #"
print "#Duzenlemek icin '-d' parametlersini giriniz. (or. .../dhcplogger.py -d)      #"
print "###############################################################################"
print ""
if deger[0] == "0": ##Kullanicidan veriler istenir ve değiskenlere atanir.
    while True:
        ip=raw_input("Hedef bilgisayarin ip adresi: ")
        share_folder=raw_input("Hedef bilgisayardaki paylasilan klasorun adi: ")
        username=raw_input("Hedef bilgisayardaki yetkili kullanici: ")
        password=raw_input("Hedef bilgisayardaki yetkili kullanicinin sifresi: ")
        saatdeg=raw_input("Kac saatte bir kayit alinmasini seciniz: ")
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
                    saatdeg=raw_input("Kac saatte bir kayit alinmasini seciniz: ")
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
    config_write=open("/sbin/dhcplogger.conf","w")
    config_write.write("1:")
    config_write.write(ip)
    config_write.write(":")
    config_write.write(share_folder)
    config_write.write(":")
    config_write.write(username)
    config_write.write(":")
    config_write.write(password)
    config_write.write(":")
    config_write.write(saatdeg)
    config_write.close()
### ------------------------------------------------ ###
### ------------------------------------------------ ###
###- Gerekli bilgiler ayiklanir ve dosyaya yazilir

cngdeger=deger[5]
cngdeger=int(cngdeger)
timecal=timecalc(cngdeger)
endyaz=0
basyaz=0
ethyaz=0
deger2=0
while x<y: ##Leases kisimlari
    le_split=leases[x].split(" ")
    v=len(le_split)
    z=0
    while z<v:
        if le_split[z]=="ends":
            ae1=le_split[z+2].strip("/") ##Tarih
            ae2=le_split[z+3].replace(";","").strip(":") ##Saat
            yazili=epochc(ae1,ae2)
            if timecal < yazili:
                deger2=2
                endyaz=1
                ba=z
                z=0
                break
        z=z+1 
    while z<v:
        if le_split[z]=="starts" and deger2==2:
            deger2=deger2-1
            basyaz=1
            bb=z
            z=0
            break
        z=z+1 
    while z<v:
        if le_split[z]=="ethernet" and deger2==1:
            deger2=deger2-1
            ethyaz=1
            bc=z
            break
        z=z+1
    if endyaz == 1 and basyaz == 1 and ethyaz==1:
        ipadres(z)
        tarihbas(bb)
        tarihbit(ba)
        macadres(bc)
    x=x+1
###-Dosya kapatilir.
dhcp5651.close()
#---
###- Samba Ayarlari
import os
os.chdir(os.pardir)
os.chdir('/var/log/dhcplogger')
smb_com=('smbclient \\\\\\\\{0}\\\\{1} -U {2}%"{3}" -c "put dhcp5651_{4}_{5}.txt"').format(deger[1],deger[2],deger[3],deger[4],tarihdosya,saatdosya)
os.system(smb_com)
#---






