from PyQt5 import *
from CagriListesiMenusu import *
from ItirazEtme import *
from ItirazlarListesiMenu import *
from Sistem import *
from TLItirazCevaplama import *
from TLYapilanItirazlar import *
from YeniCagriEkleme import *
import sys
from sifremiunuttum import *
from anasayfa import *
from kayitsf import *
from PyQt5.QtWidgets import *
from PrimListesiMenusu import *

uygulama= QApplication(sys.argv)
anaPencere= QMainWindow()
uiAnaPencere= Ui_MainWindow()
uiAnaPencere.setupUi(anaPencere)

kayitEkrani= QMainWindow()
uiKayitEkrani= Ui_kayitWindow()
uiKayitEkrani.setupUi(kayitEkrani)

sifremiUnuttumEkrani= QMainWindow()
uiSifremiUnuttumEkrani= Ui_SifremiUnuttum()
uiSifremiUnuttumEkrani.setupUi(sifremiUnuttumEkrani)

CagriListesiMenusuEkrani= QMainWindow()
uiCagriListesiMenusuEkrani= Ui_CagrListesiMenusu()
uiCagriListesiMenusuEkrani.setupUi(CagriListesiMenusuEkrani)

ItirazEtmeEkrani= QMainWindow()
uiItirazEtmeEkrani= Ui_ItirazEtme()
uiItirazEtmeEkrani.setupUi(ItirazEtmeEkrani)

ItirazlarListesiMenuEkrani= QMainWindow()
uiItirazlarListesiMenuEkrani= Ui_ItirazlarListesiMenu()
uiItirazlarListesiMenuEkrani.setupUi(ItirazlarListesiMenuEkrani)

PrimListesiMenusuEkrani= QMainWindow()
uiPrimListesiMenusuEkrani= Ui_PrimListesiMenusu()
uiPrimListesiMenusuEkrani.setupUi(PrimListesiMenusuEkrani)

SistemEkrani= QMainWindow()
uiSistemEkrani= Ui_Sistem()
uiSistemEkrani.setupUi(SistemEkrani)

TLItirazCevaplamaEkrani= QMainWindow()
uiTLItirazCevaplamaEkrani= Ui_TLItirazCevaplama()
uiTLItirazCevaplamaEkrani.setupUi(TLItirazCevaplamaEkrani)

TLYapilanItirazlarEkrani= QMainWindow()
uiTLYapilanItirazlarEkrani= Ui_TLYapilanItirazlar()
uiTLYapilanItirazlarEkrani.setupUi(TLYapilanItirazlarEkrani)

YeniCagriEklemeEkrani= QMainWindow()
uiYeniCagriEklemeEkrani= Ui_YeniCagriEkleme()
uiYeniCagriEklemeEkrani.setupUi(YeniCagriEklemeEkrani)

anaPencere.show()

#SQL
#------------------------------------------------

import pypyodbc as odbc

DRIVER_NAME= 'SQL SERVER'
DATABASE_NAME= 'VeritabanıProje'

connection_string= f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER=.;
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
baglanti = odbc.connect(connection_string)
islem=baglanti.cursor()
baglanti.commit()

class kullanici:
    def __init__(self, id = 0):
        self._id = id
    def get_id(self):
        return self._id
    def set_id(self, x):
        self._id=x
user = kullanici()

#G�R�S KISMI
#def
#------------------------------------------------------
def tl_giris_yap():
    
    kullaniciAdi=uiAnaPencere.kullaniciAdiLne.text()
    sifre=uiAnaPencere.sifreLne.text()
    if kullaniciAdi!= "":
        if sifre!="":
            islem.execute(f"SELECT kullaniciAdi FROM TakimLiderleri WHERE kullaniciAdi='{kullaniciAdi}'")
            kullaniciAdiMevcutMu=islem.fetchone()
            baglanti.commit()
            
            if kullaniciAdiMevcutMu is not None :
                islem.execute(f"SELECT * FROM TakimLiderleri WHERE kullaniciAdi='{kullaniciAdi}' and sifre='{sifre}'")
                sifreMevcutMu=islem.fetchone()
                baglanti.commit()
                if sifreMevcutMu is not None :
                    islem.execute(f"SELECT TakimLideriID FROM TakimLiderleri WHERE kullaniciAdi='{kullaniciAdi}' and sifre='{sifre}'")
                    liderID=islem.fetchone()[0]
                    user.set_id(liderID)

                    TLYapilanItirazlarEkrani.show()
                    anaPencere.close()
                    itiraz_listeleme()
                else : 
                    uiAnaPencere.statusbar.showMessage("Sifre Yanlis !",10000)
                
            else:
                uiAnaPencere.statusbar.showMessage("Kullanici Adi Bulunmamaktadir !",10000)
            
        else:
            uiAnaPencere.statusbar.showMessage("Lutfen Sifre Giriniz !",10000)
        
    else :
        uiAnaPencere.statusbar.showMessage("Lutfen Kullanici Adi Giriniz !",10000)

def a_giris_yap():
    
    kullaniciAdi=uiAnaPencere.kullaniciAdiLne.text()
    sifre=uiAnaPencere.sifreLne.text()
    if kullaniciAdi!= "":
        if sifre!="":
            islem.execute(f"SELECT kullaniciAdi FROM Asistanlar WHERE kullaniciAdi='{kullaniciAdi}'")
            kullaniciAdiMevcutMu=islem.fetchone()
            baglanti.commit()
            
            if kullaniciAdiMevcutMu is not None :
                islem.execute(f"SELECT * FROM Asistanlar WHERE kullaniciAdi='{kullaniciAdi}' and sifre='{sifre}'")
                sifreMevcutMu=islem.fetchone()
                baglanti.commit()
                if sifreMevcutMu is not None :
                    islem.execute(f"SELECT AsistanID FROM Asistanlar WHERE kullaniciAdi='{kullaniciAdi}' and sifre='{sifre}'")
                    asistanID=islem.fetchone()[0]
                    user.set_id(asistanID)
                    SistemEkrani.show()
                    anaPencere.close()
                else : 
                    uiAnaPencere.statusbar.showMessage("Sifre Yanlis !",10000)
                
            else:
                uiAnaPencere.statusbar.showMessage("Kullanici Adi Bulunmamaktadir !",10000)
            
        else:
            uiAnaPencere.statusbar.showMessage("Lutfen Sifre Giriniz !",10000)
        
    else :
        uiAnaPencere.statusbar.showMessage("Lutfen Kullanici Adi Giriniz !",10000)

#BUTONLAR
#------------------------------------------------

uiAnaPencere.tlgirisBtn.clicked.connect(tl_giris_yap)
uiAnaPencere.agirisBtn.clicked.connect(a_giris_yap)

#Asistan Ekrani

def cagri_listesi_menusu():
    CagriListesiMenusuEkrani.show()
    AsistanID=user.get_id()
    uiCagriListesiMenusuEkrani.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    uiCagriListesiMenusuEkrani.tableWidget.setHorizontalHeaderLabels(("Musteri Adi","Musteri Soyadi","Cagri Konusu","Cagri Tarihi","Baslangic Saati","Bitis Saati","Cagri Durumu"))
    sorgu=f"select MusteriAdi,MusteriSoyadi,CagriKonuID,CagriTarihi,BaslangicSaat,BitisSaat,CagriDurumID from MusteriCagrilari where AsistanID='{AsistanID}'"
    islem.execute(sorgu)    
    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun,kayitSutun in enumerate(kayitNumarasi):
            uiCagriListesiMenusuEkrani.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))


    def yeni_cagri():
        YeniCagriEklemeEkrani.show()
        
        def yeni_cagri_ekle():
            MusteriAdi=uiYeniCagriEklemeEkrani.lineEdit.text()
            MusteriSoyadi=uiYeniCagriEklemeEkrani.lineEdit_2.text()
            Konu=uiYeniCagriEklemeEkrani.comboBox_2.currentText()
            CagriTarihi = uiYeniCagriEklemeEkrani.dateEdit.date().toString("yyyy-MM-dd")
            BaslangicSaat = uiYeniCagriEklemeEkrani.timeEdit.time().toString("HH:mm:ss")
            BitisSaat = uiYeniCagriEklemeEkrani.timeEdit_2.time().toString("HH:mm:ss")

            Durum=uiYeniCagriEklemeEkrani.comboBox.currentText()
            AsistanID=user.get_id()

            if MusteriAdi and MusteriSoyadi and Konu and CagriTarihi and BaslangicSaat and BitisSaat and Durum:
                if Durum=="Tamamlandı":
                    CagriDurumID=1
                elif Durum=="Takip Ediliyor":
                    CagriDurumID=2
                else:
                    CagriDurumID=3
                if Konu=="Arıza":
                    CagriKonuID=1
                elif Konu=="Talep":
                    CagriKonuID=2
                else :
                    CagriKonuID=3
                try:
                    ekle = "insert into dbo.MusteriCagrilari(AsistanID,MusteriAdi,MusteriSoyadi,CagriKonuID,CagriTarihi,BaslangicSaat,BitisSaat,CagriDurumID) values(?,?,?,?,?,?,?,?)"
                    
                    islem.execute(ekle, (AsistanID, MusteriAdi, MusteriSoyadi, CagriKonuID,CagriTarihi,BaslangicSaat,BitisSaat,CagriDurumID))
                    baglanti.commit()
                    
                    
                    uiYeniCagriEklemeEkrani.statusbar.showMessage("Eklendi !",10000)
                except Exception as e:
                    print("Hata:", e)
                    uiYeniCagriEklemeEkrani.statusbar.showMessage("Eklenemedi !",10000)

            else :
                uiYeniCagriEklemeEkrani.statusbar.showMessage("Lutfen Bilgileri Doldurunuz !",10000)    
        
        
        
        uiYeniCagriEklemeEkrani.pushButton.clicked.connect(yeni_cagri_ekle)
    
    
    
    
    uiCagriListesiMenusuEkrani.pushButton.clicked.connect(CagriListesiMenusuEkrani.close)
    uiCagriListesiMenusuEkrani.pushButton_2.clicked.connect(yeni_cagri)

def prim_listesi_menusu():#İtiraz Etme Butonu Eksik
    PrimListesiMenusuEkrani.show()
    AsistanID=user.get_id()
    uiPrimListesiMenusuEkrani.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    uiPrimListesiMenusuEkrani.tableWidget.setHorizontalHeaderLabels(("Hesap Ayi","Prim Miktari"))
    sorgu=f"select HesapAyı,PrimMiktari from AsistanPrimHesaplari where AsistanID='{AsistanID}'"
    islem.execute(sorgu)    
    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun,kayitSutun in enumerate(kayitNumarasi):
            uiPrimListesiMenusuEkrani.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
    
    def prim_itiraz_etme():
        ItirazEtmeEkrani.show()
        def itiraz_et():
            itirazAciklama=uiItirazEtmeEkrani.textEdit.toPlainText()
            try :
                from datetime import datetime
                simdiki_tarih = datetime.now()
                mevcut_ay = simdiki_tarih.month
                aylar = {
                    1: 'Ocak',
                    2: 'Şubat',
                    3: 'Mart',
                    4: 'Nisan',
                    5: 'Mayıs',
                    6: 'Haziran',
                    7: 'Temmuz',
                    8: 'Ağustos',
                    9: 'Eylül',
                    10: 'Ekim',
                    11: 'Kasım',
                    12: 'Aralık'
                }

                hangi_ay = aylar[mevcut_ay]

                sorgu= "insert into dbo.AsistanPrimItirazlari(AsistanID,ItirazAciklamasi,ItirazYapilanAy,ItirazDurumuID) values(?,?,?,?)"
                islem.execute(sorgu,(AsistanID,itirazAciklama,hangi_ay,2))
                baglanti.commit()
                uiItirazEtmeEkrani.statusbar.showMessage("İtiraz Eklendi",10000)
            except Exception as e :
                print(e)
                uiItirazEtmeEkrani.statusbar.showMessage("İtiraz Eklenemedi",10000)
        
        
        
        uiItirazEtmeEkrani.pushButton.clicked.connect(itiraz_et)
    
    
    uiPrimListesiMenusuEkrani.pushButton.clicked.connect(prim_itiraz_etme)
    uiPrimListesiMenusuEkrani.pushButton_2.clicked.connect(PrimListesiMenusuEkrani.close)


def itirazlar_listesi_menusu():
    ItirazlarListesiMenuEkrani.show()
    AsistanID=user.get_id()
    uiItirazlarListesiMenuEkrani.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    uiItirazlarListesiMenuEkrani.tableWidget.setHorizontalHeaderLabels(("Itiraz Aciklamasi","Itiraz Yapilan AY","İtiraz Durumu"))
    sorgu=f"select ItirazAciklamasi,ItirazYapilanAy,ItirazDurumuID from AsistanPrimItirazlari where AsistanID='{AsistanID}'"
    islem.execute(sorgu)    
    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun,kayitSutun in enumerate(kayitNumarasi):
            uiItirazlarListesiMenuEkrani.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))


uiSistemEkrani.pushButton.clicked.connect(cagri_listesi_menusu)
uiSistemEkrani.pushButton_2.clicked.connect(prim_listesi_menusu)
uiSistemEkrani.pushButton_3.clicked.connect(itirazlar_listesi_menusu)

#Takim Lideri EKrani

def itiraz_listeleme():
    LiderID=user.get_id()
    uiTLYapilanItirazlarEkrani.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    uiTLYapilanItirazlarEkrani.tableWidget.setHorizontalHeaderLabels(("ItirazID","Itiraz Durumu","Asistan Sicil No","Asistan Ad","Asistan Soyad","Itiraz Aciklamasi","İtiraz Yapilan Ay"))
    sorgu=f"select AP.ItirazID,AP.ItirazDurumuID,A.SicilNo,A.Ad,A.Soyad,AP.ItirazAciklamasi,AP.ItirazYapilanAy from AsistanPrimItirazlari AP inner join Asistanlar A on AP.AsistanID=A.AsistanID where A.AsistanID='{LiderID}'"
    islem.execute(sorgu) 
    button = QPushButton("Itiraz Cevapla")
    for indexSatir, kayitNumarasi in enumerate(islem):
        uiTLYapilanItirazlarEkrani.tableWidget.insertRow(indexSatir)
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            if indexSutun == 1 and kayitNumarasi[1] == 2:  # ItirazDurumuID kontrolü
                
                uiTLYapilanItirazlarEkrani.tableWidget.setCellWidget(indexSatir, indexSutun, button)
                def itiraz_cevapla(ItirazID):
                    TLItirazCevaplamaEkrani.show()
                    
                    def itiraz_aciklama_gonder():
                        CevapAciklamasi = uiTLItirazCevaplamaEkrani.textEdit.toPlainText()
                        TakimLideriID = user.get_id()
                        try :
                            sorgu = "insert into dbo.TakimLideriCevaplari(ItirazID,TakimLideriID,CevapAciklamasi) values(?,?,?)"
                            islem.execute(sorgu, (ItirazID, TakimLideriID, CevapAciklamasi))
                            baglanti.commit()
                            sorgu1 = f"update AsistanPrimItirazlari set ItirazDurumuID=1 where ItirazID={ItirazID} "
                            islem.execute(sorgu1)
                            baglanti.commit()
                            uiTLItirazCevaplamaEkrani.statusbar.showMessage("Cevap Gönderildi",10000)
                        except Exception as e :
                            print(e)
                            uiTLItirazCevaplamaEkrani.statusbar.showMessage("Cevap Gönderilemedi",10000)
                        
                    
                    uiTLItirazCevaplamaEkrani.pushButton.clicked.connect(itiraz_aciklama_gonder)
                
                button.clicked.connect(lambda _, ItirazID=kayitNumarasi[0]: itiraz_cevapla(ItirazID))
                
            else:
                uiTLYapilanItirazlarEkrani.tableWidget.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))








#---------------------------------------------------------------------------------------------------------------------
sys.exit(uygulama.exec_())
