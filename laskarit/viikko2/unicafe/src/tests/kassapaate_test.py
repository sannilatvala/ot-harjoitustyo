import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti2 = Maksukortti(100)

    def test_luodun_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_maukkaiden_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_edullinen_lounas_kassassa_oleva_rahamaara_kasvaa_kun_maksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_edullinen_lounas_vaihtorahan_suuruus_oikea_kun_maksu_riittava(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(maksu, 260)

    def test_kateisosto_maukas_lounas_kassassa_oleva_rahamaara_kasvaa_kun_maksu_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_maukas_lounas_vaihtorahan_suuruus_oikea_kun_maksu_riittava(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(maksu, 100)

    def test_kateisosto_myytyjen_edullisten_lounaiden_maara_kasvaa_kun_maksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_myytyjen_maukkaiden_lounaiden_maara_kasvaa_kun_maksu_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_edullinen_lounas_kassassa_oleva_rahamaara_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_edullinen_lounas_vaihtorahan_suuruus_oikea_kun_maksu_ei_riittava(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(maksu, 100)

    def test_kateisnosto_maukas_lounas_kassassa_oleva_rahamaara_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisnosto_maukas_lounas_vaihtorahan_suuruus_oikea_kun_maksu_ei_riittava(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(maksu, 100)

    def test_kateisosto_myytyjen_edullisten_lounaiden_maara_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_myytyjen_maukkaiden_lounaiden_maara_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_edullinen_lounas_kortin_saldo_vahenee_kun_kortilla_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 760)

        return True

    def test_korttiosto_maukas_lounas_kortin_saldo_vahenee_kun_kortilla_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 600)

        return True
    
    def test_korttiosto_myytyjen_edullisten_lounaiden_maara_kasvaa_kun_kortilla_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_myytyjen_maukkaiden_lounaiden_maara_kasvaa_kun_kortilla_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_edullinen_lounas_kortin_saldo_ei_muutu_kun_kortilla_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)

        self.assertEqual(self.maksukortti.saldo, 1000)

        return False

    def test_korttiosto_maukas_lounas_kortin_saldo_ei_muutu_kun_kortilla_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)

        self.assertEqual(self.maksukortti.saldo, 1000)

        return False
    
    def test_korttiosto_myytyjen_edullisten_lounaiden_maara_ei_muutu_kun_kortilla_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_myytyjen_maukkaiden_lounaiden_maara_ei_muutu_kun_kortilla_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_lounas_kassassa_oleva_rahamaara_ei_muutu_kun_kortilla_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_maukas_lounas_kassassa_oleva_rahamaara_ei_muutu_kun_kortilla_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_edullinen_lounas_kassassa_oleva_rahamaara_ei_muutu_kun_kortilla_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_maukas_lounas_kassassa_oleva_rahamaara_ei_muutu_kun_kortilla_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_kortille_rahaa_ladattaessa_kassassa_oleva_rahamaara_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortille_negatiivisen_summan_ladattaessa_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kortille_negatiivisen_summan_ladattaessa_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)