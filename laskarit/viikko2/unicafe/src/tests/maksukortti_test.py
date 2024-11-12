import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_kortin_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 30)
    
    def test_rahan_ottaminen_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5)

    def test_saldo_ei_muutu_jos_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
    
    def test_riittivat_true(self):
        success = self.maksukortti.ota_rahaa(500)

        self.assertTrue(success)
    
    def test_ei_tarpeeksi_rahaa_false(self):
        success = self.maksukortti.ota_rahaa(1500)

        self.assertFalse(success)
    
    def test_kortti_tulostuu_oikein(self):
        tuloste = str(self.maksukortti)

        self.assertEqual(tuloste, "Kortilla on rahaa 10.00 euroa")