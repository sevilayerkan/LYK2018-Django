import random

class uretec:
    """
        Generates random news entry
        Usage :
            uretec = Uretec()
            print(uretec.uretec())
    """
    def sehir_uretec(self):
        sehir = ["Bolu", "Samsun", "Izmır", "Adana", "Erzurum"]
        return random.choice(sehir)

    def unlu_uretec(self):
        unlu = ["Haluk Levent", "Aleyna Tilki", "Kubat", "Mustafa Topaloglu"]
        return random.choice(unlu)

    def bocek_uretec(self):
        bocek = ["arı", "sinek", "hamam bocegi"]
        return random.choice(bocek)

    def haber_uretec(self):
        haber = [
            "{}'in 3 Gün Yatmadan Yaptığı Proje'de Bug Bulan Developer Kayıp.",
            "{} Python'mu Ruby mi Kavgasında Öldü. ",
            "Şarkı dinlemesine izin verilmeyen {} Cinnet Geçirdi ",
            "{} cok icti, {} sokaklarında {} kostumuyle dolasti.",
            "{}'ye hapis soku!"
            "{}'in {}'deki evinde {} istilası."
        ]
        return random.choice(haber).format(
            self.unlu_uretec(),
            self.sehir_uretec(),
            self.bocek_uretec()
        )


    # rastgele haber sablonu sec
    # sablonu doldur
    # veri tabanına kaydet

# random.choice(list) listeden rastgele bir deger secer
# random.sample(list,1)



