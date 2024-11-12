import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_kassapaate_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_myytyjen_lounaiden_maara_alussa(self):
        myydyt_lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(myydyt_lounaat, 0)
    
    def test_kateisosto_edullisesti_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
    
    def test_kateisosto_edullisesti_raha_ei_riita(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(takaisin, 230)
    
    def test_kateisosto_edullisesti_raha_ei_riita_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_kateisosto_edullisesti_raha_ei_riita_myydyt_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullisesti_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_edullisesti_palauttaa_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(vaihtoraha, 10)
    
    def test_kateisosto_maukkaasti_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
    
    def test_kateisosto_maukkaasti_raha_ei_riita(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(230)

        self.assertEqual(takaisin, 230)
    
    def test_kateisosto_maukkaasti_raha_ei_riita_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_kateisosto_maukkaasti_raha_ei_riita_myydyt_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_maukkaasti_kasvattaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_edullisesti_palauttaa_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertEqual(vaihtoraha, 10)
    
    def test_kortilla_tarpeeksi_rahaa_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
    
        self.assertEqual(self.kortti.saldo_euroina(), 7.6)
    
    def test_kortilla_tarpeeksi_rahaa_edullisesti_2(self):
        success = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
    
        self.assertTrue(success)

    def test_kortilla_tarpeeksi_rahaa_edullisesti_3(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
    
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kortilla_tarpeeksi_rahaa_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo_euroina(), 6.0)
    
    def test_kortilla_tarpeeksi_rahaa_maukkaasti_2(self):
        success = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
    
        self.assertTrue(success)

    def test_kortilla_tarpeeksi_rahaa_maukkaasti_3(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
    
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_ei_tarpeeksi_rahaa_edullisesti(self):
        kortti = Maksukortti(230)
        success = self.kassapaate.syo_edullisesti_kortilla(kortti)
    
        self.assertFalse(success)
    
    def test_kortilla_ei_tarpeeksi_rahaa_edullisesti_2(self):
        kortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
    
        self.assertEqual(kortti.saldo_euroina(), 2.30)
    
    def test_kortilla_ei_tarpeeksi_rahaa_edullisesti_3(self):
        kortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
    
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortilla_ei_tarpeeksi_rahaa_maukkaasti(self):
        kortti = Maksukortti(230)
        success = self.kassapaate.syo_maukkaasti_kortilla(kortti)
    
        self.assertFalse(success)

    def test_kortilla_ei_tarpeeksi_rahaa_maukkaasti_2(self):
        kortti = Maksukortti(230)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
    
        self.assertEqual(kortti.saldo_euroina(), 2.30)
    
    def test_kortilla_ei_tarpeeksi_rahaa_maukkaasti_3(self):
        kortti = Maksukortti(230)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
    
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(self.kortti.saldo_euroina(), 20)
    
    def test_lataa_rahaa_kortille_kassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010)
    
    def test_lataa_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)