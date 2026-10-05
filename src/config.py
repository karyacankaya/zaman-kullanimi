"""Ayarlar: ATUS aktivite kodlarini 7 kategoriye eslestirme."""

# ATUS 'atussum' dosyasindaki t-kodlari (prefix ile toplanir).
# Kodlar BLS Activity Coding Lexicon'a gore; emin degilsen lexicon'dan kontrol et.
CATEGORY_PREFIXES = {
    "sleep":        ["t0101"],      # uyku
    "work":         ["t0501"],      # ana is
    "eating":       ["t1101"],      # yemek-icme
    "sport":        ["t1301"],      # spor / egzersiz
    "friends":      ["t120101"],    # sosyallesme, arkadaslarla vakit
    "tv":           ["t120303"],    # TV ve film
    "social_media": ["t120308"],    # bos zamanda bilgisayar (sosyal medya icin YAKLASIK vekil)
}

CATEGORIES = list(CATEGORY_PREFIXES)

# Yasam memnuniyeti (Cantril ladder, 0-10), wbresp dosyasindaki WECANTRIL sutunu.
LIFE_SAT_COL = "WECANTRIL"
