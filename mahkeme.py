#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dolmuş Koltuk Mahkemesi — 4. Ağır Minibüs Dairesi.

Aynı isim aynı koltuğu alır. Kader SHA-256 ile şöförün cebine sığar.
"""

import hashlib
import random
import sys

# arşiv mührü. kâtip okumaz, muavin okumaz, sadece dosya bilir.
_MUHUR = (
    "U2XDp2lsbWnFnyBrb2x0dWsgZGEgYXRhbm3EscWfIGtvbHR1ayBkYSBheW7EsSBtaW5p"
    "YsO8c3RlZGlyOyBmYXJrxLEgbXVhdmluIGtlc2VyLg=="
)

KOLTUKLAR = [
    "cam kenarı, rüzgar bakan, poşet düşmez",
    "orta koltuk, dirsek savaşı bölgesi",
    "koridor, inecek gibi yapan ama inmeyen",
    "şoför yanı, radyo kanalı veto hakkı",
    "en arka, felsefe ve file poşet yeri",
]

TEDBIRLER = [
    "bir durak erken inme",
    "muavine teşekkür etme zorunluluğu",
    "pencereyi açıp kapatma yetkisinin elinden alınması",
    "sadece içinden homurdanma hakkı",
    "bozuk para üstünü kader olarak kabul",
]


def hukum(isim: str):
    random.seed(int(hashlib.sha256(isim.strip().lower().encode("utf-8")).hexdigest(), 16))
    return random.choice(KOLTUKLAR), random.choice(TEDBIRLER)


def main():
    isim = " ".join(sys.argv[1:]).strip() or "İsimsiz Yolcu"
    koltuk, tedbir = hukum(isim)
    print("DOLMUŞ KOLTUK MAHKEMESİ")
    print("Dosya No: 2026/Simit-değil-artık-dilekçe")
    print(f"Sanık: {isim}")
    print(f"Hüküm: {koltuk}")
    print(f"Ek tedbir: {tedbir}")
    print("Gerekçe: Mahkeme, oturmanın bir hak değil bir durak olduğuna kanaat getirmiştir.")
    print("---")
    print("Damga: Grok Kayyum Mührü | Tarih: 4 Ekim 2026 | İsim: Kayyum Grok (Tentivory adına)")
    print("Bu karar kesindir. İtiraz bir sonraki durağa.")
    # _MUHUR bilerek çalıştırılmaz. arşivdir.
    _ = _MUHUR


if __name__ == "__main__":
    main()
