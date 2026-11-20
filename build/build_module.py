# -*- coding: utf-8 -*-
"""Generuje źródła kompendiów modułu (src/packs/*/*.json) ze stałymi ID."""
import json, os, re, shutil, hashlib, string, sys
sys.path.insert(0, os.path.dirname(__file__))
from embargo_content import ADVENTURE, GM_SCHOOL, HANDOUTS
from embargo_npcs import NPCS, GANGS
from embargo_maps import MAPS

ROOT = os.path.join(os.path.dirname(__file__), "..")
SRC = os.path.join(ROOT, "src", "packs")
MOD = "modules/degenesis2-embargo"
STATS = {"compendiumSource": None, "duplicateSource": None, "coreVersion": "14.370", "systemId": "degenesis2", "systemVersion": "0.6.3"}
STATS13 = dict(STATS, coreVersion="13.351")
ALPH = string.ascii_letters + string.digits

def sid(*parts):
    h = hashlib.sha256("|".join(["embargo", *parts]).encode()).digest()
    return "".join(ALPH[b % len(ALPH)] for b in h[:16])

ATTRS = {"cia": ["atletyka", "bijatyka", "sila", "bronBiala", "kondycja", "twardosc"],
         "zre": ["rzemioslo", "zwinnePalce", "prowadzenie", "mobilnosc", "strzelectwo", "skradanie"],
         "cha": ["sztuka", "obycie", "ekspresja", "przywodztwo", "negocjacje", "uwodzenie"],
         "int": ["artefakty", "inzynieria", "skupienie", "legendy", "medycyna", "nauka"],
         "psy": ["spryt", "oszustwo", "dominacja", "wiara", "refleks", "wola"],
         "ins": ["empatia", "orientacja", "percepcja", "pierwotnosc", "przetrwanie", "oswajanie"]}
SKILL_ATTR = {s: a for a, l in ATTRS.items() for s in l}
packs = {k: [] for k in ["dzienniki", "aktorzy", "sceny"]}

def pools_to_stats(pools):
    attrs = {a: 1 for a in ATTRS}; skills = {}
    norm = {"init": "refleks", "mental": "wola"}
    by = {}
    for k, v in pools.items():
        sk = norm.get(k, k); by.setdefault(SKILL_ATTR[sk], []).append((sk, v))
    for a, lst in by.items():
        mx = max(v for _, v in lst)
        attrs[a] = max(1, min(6, max(mx - 6, (mx + 1) // 2)))
        for sk, v in lst: skills[sk] = max(0, min(6, v - attrs[a]))
    return ({"attributes": {a: {"value": attrs[a]} for a in ATTRS},
             "skills": {s: {"value": skills.get(s, 0)} for a in ATTRS for s in ATTRS[a]}}, attrs, skills)

def folder(name, type_, sort=0):
    fid = sid("folder", type_, name)
    packs[{"JournalEntry": "dzienniki", "Actor": "aktorzy", "Scene": "sceny"}[type_]].append(
        {"_id": fid, "_key": f"!folders!{fid}", "name": name, "type": type_, "folder": None, "sorting": "m", "sort": sort,
         "color": "#7b1e12", "description": "", "flags": {}, "_stats": STATS})
    return fid

def journal(name, pages, fid, sort, observer=False):
    jid = sid("journal", name)
    out = {"_id": jid, "_key": f"!journal!{jid}", "name": name, "pages": [], "folder": fid, "sort": sort,
           "ownership": {"default": 2 if observer else 0}, "flags": {}, "_stats": STATS, "categories": []}
    for i, (title, html) in enumerate(pages):
        pid = sid("page", name, title)
        out["pages"].append({"_id": pid, "_key": f"!journal.pages!{jid}.{pid}", "name": title, "type": "text",
            "title": {"show": True, "level": 1}, "text": {"format": 1, "content": html.strip()}, "sort": (i + 1) * 100000,
            "ownership": {"default": -1}, "flags": {}, "_stats": STATS, "image": {}, "video": {"controls": True, "volume": 0.5},
            "src": None, "system": {}, "category": None})
    packs["dzienniki"].append(out)

def actor(key, name, type_, system, img, items=(), token=None, fid=None, sort=0, disposition=-1):
    aid = sid("actor", key)
    its = []
    for i, it in enumerate(items):
        iid = sid("item", key, it["name"], str(i))
        its.append({**it, "_id": iid, "_key": f"!actors.items!{aid}.{iid}", "effects": [], "folder": None, "sort": i * 100,
                    "ownership": {"default": 0}, "flags": {}, "_stats": STATS})
    packs["aktorzy"].append({"_id": aid, "_key": f"!actors!{aid}", "name": name, "type": type_, "img": img, "system": system,
        "items": its, "effects": [], "folder": fid, "sort": sort, "ownership": {"default": 0}, "flags": {}, "_stats": STATS,
        "prototypeToken": {"name": name, "actorLink": False, "disposition": disposition, "texture": {"src": token or img},
                           "displayName": 20, "displayBars": 20, "bar1": {"attribute": "ego"}}})
    return aid

def weapon(w):
    n, sk, dmg, rng, q, hand = w
    return {"name": n, "type": "bron", "img": "icons/svg/sword.svg" if sk != "strzelectwo" else "icons/svg/target.svg",
            "system": {"description": "", "skill": sk, "handling": hand, "damage": dmg, "range": rng, "magazine": {"value": 0, "max": 0},
                       "qualities": q, "encumbrance": 0, "equipped": True}}

def potential(n, d):
    return {"name": n, "type": "potencjal", "img": "icons/svg/aura.svg",
            "system": {"description": f"<p>{d}</p>", "level": 1, "kult": "", "prerequisite": "", "zjawisko": False, "poziomZjawiska": 0}}

# ---------------- Dzienniki
fj = folder("Embargo", "JournalEntry")
journal("Embargo — przygoda (MG)", ADVENTURE, fj, 100)
journal("Szkoła MG: Embargo", GM_SCHOOL, fj, 200)
journal("Embargo — handouty dla graczy", HANDOUTS, fj, 300, observer=True)

# ---------------- Aktorzy
fa = folder("Embargo", "Actor")
f_npc = sid("folder", "Actor", "Embargo — NPC"); f_tools = sid("folder", "Actor", "Embargo — śledztwo i świat")
for fid, nm, srt in [(f_npc, "Embargo — NPC", 100), (f_tools, "Embargo — śledztwo i świat", 200)]:
    packs["aktorzy"].append({"_id": fid, "_key": f"!folders!{fid}", "name": nm, "type": "Actor", "folder": fa, "sorting": "a", "sort": srt,
                             "color": "#4a1a12", "description": "", "flags": {}, "_stats": STATS})

for i, (key, name, scale, ego, armor, prog, pools, weapons, abil, motyw, lek, sekret, cena, postawa, kult, ranga, desc, por, _sub) in enumerate(NPCS):
    st, attrs, skills = pools_to_stats(pools)
    base = attrs["cia"] + skills.get("twardosc", 0)
    st.update({"scale": scale, "size": {"value": 1, "max": 1}, "ego": {"value": ego, "max": ego}, "armor": armor,
               "progBonus": max(0, prog - base), "kult": kult, "ranga": ranga, "motyw": motyw, "lek": lek, "sekret": sekret, "cena": cena,
               "postawa": postawa, "frakcja": "", "eliminated": False, "prymer": {"value": 0, "max": 0}, "zjawiskaBonus": 0,
               "defense": {"bonus": 0}, "wounds": {"lekkie": 0, "powazne": 0, "krytyczna": 0}, "notes": f"<p>{desc}</p>"})
    img = f"{MOD}/assets/portraits/{key}.webp" if por else "icons/svg/pawprint.svg"
    tok = f"{MOD}/assets/tokens/{key}.webp" if por else None
    items = [weapon(w) for w in weapons] + [potential(n, d) for n, d in abil]
    disp = {"magnus": 0, "merl": 0, "mama-dacrois": 0, "ojciec-dacrois": 0, "jatzek": 0, "token": 0, "paradygma": 0}.get(key, -1)
    actor(key, name, "npc", st, img, items, tok, f_npc, (i + 1) * 100, disp)

for key, name, scale, ego, armor, prog, size, pools, weapons, desc, por in GANGS:
    st, attrs, skills = pools_to_stats(pools)
    st.update({"scale": scale, "size": {"value": size, "max": size}, "ego": {"value": ego, "max": ego}, "armor": armor,
               "progBonus": max(0, prog - attrs["cia"] - skills.get("twardosc", 0)), "kult": "Bestie", "ranga": "", "motyw": "Głód", "lek": "Ogień",
               "sekret": "", "cena": "", "postawa": -2, "frakcja": "", "eliminated": False, "prymer": {"value": 0, "max": 0}, "zjawiskaBonus": 0,
               "defense": {"bonus": 0}, "wounds": {"lekkie": 0, "powazne": 0, "krytyczna": 0}, "notes": f"<p>{desc}</p>"})
    actor(key, name, "npc", st, "icons/svg/pawprint.svg", [weapon(w) for w in weapons], None, f_npc, 2000)

actor("sledztwo", "Śledztwo: Fałszywe Drafty", "sledztwo", {
    "pytanie": "Skąd w Tumblerze fałszywe Drafty — i kto zastawił pułapkę w Wektorze?",
    "tropy": [
        {"text": "Dwaj milczący goście karczmy to Shutterzy Kronikarzy bez masek (kod na czole, wycięte ucho).", "source": "Tumbler — izba", "kind": "kluczowy"},
        {"text": "Jatzek dostał Drafty od „Kronikarki” w ruinach za znaleziony artefakt.", "source": "Rozmowa z Jatzekiem / Mama Dacrois", "kind": "kluczowy"},
        {"text": "Drafty są niezarejestrowane — skaner Tokena alarmuje Klaster.", "source": "Spowiedź Tokena", "kind": "kluczowy"},
        {"text": "Runy w ruinach są świeże i fałszywe; prawdziwa jest tylko runa Draffa.", "source": "Labirynt runów", "kind": "szczegol"},
        {"text": "Draff zginął od mocnego Shockera — broni Kronikarzy.", "source": "Grób Złomiarza", "kind": "powiazanie"},
        {"text": "Ekrany: Kowal pod EMBARGIEM; „Obiekt próbny 1 — 3000 Draftów”.", "source": "Wnętrze Wektora", "kind": "kluczowy"},
        {"text": "Drukarka liczy kod z miejsca, czasu, numeru Kronikarza i wartości.", "source": "Drukarka Draftów", "kind": "szczegol"},
        {"text": "„Odbiornik zerowy” od Tokena to bomba.", "source": "Spowiedź Tokena (Empatia / Artefakty)", "kind": "ostrzezenie"}],
    "teorie": "",
    "clocks": [{"name": "Czystka Case'a", "size": 6, "value": 1}, {"name": "Gniew Kowala", "size": 4, "value": 0},
               {"name": "Kronikarze nadchodzą", "size": 8, "value": 2}],
    "notes": "<p><b>Prawda:</b> Scalar Nullify drukował w Wektorze fałszywe Drafty i wrobił w nie Kowala. Kowal zastawił pułapkę na twórcę fałszywek — drużyna wchodzi w nią przypadkiem. Prawidłowy Wniosek: „Kowal poluje na fałszerza, nie na nas”.</p>"
}, "icons/svg/book.svg", fid=f_tools, sort=100, disposition=0)

LOK = [
 ("lok-tumbler", "Lokacja: Tumbler", "Rubieże Protektoratu, Borca", [("Ciasna izba pełna butelek", False, 0), ("Wieża strażnicza nad drogą", False, 0), ("Piwnica Ojca Dacrois", True, 1)],
  "Przydrożna gorzelnia i karczma, która pamięta czasy gorączki złomu. Zostali tylko Dacroisowie, Sędzia Magnus i Kronikarz Token."),
 ("lok-ruiny", "Lokacja: Ruiny magazynów", "Rubieże Protektoratu", [("Fałszywe runy na każdej ścianie", False, 0), ("Dachy połączone pniami", False, 0), ("Grób Draffa", True, 1)],
  "Rzędy hal z drzewami na dachach. Ludzie Nullify'a oznaczyli je fałszywymi runami „wyczyszczone”."),
 ("lok-dzicz", "Lokacja: Wektor — Dzicz Kowala", "Podziemna hala kontenerów", [("Ciemność i pył", False, 0), ("Wataha krąży", False, 0), ("Strzałki „TĘDY” prowadzą w pułapki", True, 1), ("Głośniki i kamery Kowala", True, 1)],
  "Labirynt kontenerów, złomu i beczek, uzbrojony przez Kowala w pułapki."),
 ("lok-wnetrze", "Lokacja: Wektor — wnętrze", "Baza Nullify'a", [("Kamery i ekrany", False, 0), ("Włazy w suficie i podłodze", False, 0), ("Pulpit w spalarni steruje wszystkim", True, 1)],
  "Szkielet bazy wokół spalarni. Drukarka Draftów, ekrany, kamery w każdym kącie."),
]
for j, (key, name, region, cechy, desc) in enumerate(LOK):
    actor(key, name, "lokacja", {"region": region, "cechy": [{"name": n, "hidden": h, "free": f} for n, h, f in cechy], "description": f"<p>{desc}</p>"},
          "icons/svg/house.svg", fid=f_tools, sort=200 + j * 10, disposition=0)

FR = [
 ("fr-klaster", "Frakcja: Klaster Kronikarzy", "Oczyścić system z fałszywych Draftów", 4, 0, "Wiedza to waluta", [("Kronikarze nadchodzą", 8, 2)]),
 ("fr-nullify", "Frakcja: Ludzie Nullify'a", "Zatrzeć ślady fałszywek przed Klastrem", 3, -1, "Zabijają świadków", [("Czystka Case'a", 6, 1)]),
 ("fr-kowal", "Frakcja: Kowal i Giada", "Dopaść twórcę fałszywek", 2, -1, "Gorzej już nie będzie", [("Gniew Kowala", 4, 0)]),
]
for j, (key, name, cel, zas, imie, cecha, clocks) in enumerate(FR):
    actor(key, name, "frakcja", {"cel": cel, "zasoby": zas, "imie": {"value": imie, "echo": 0}, "osobiste": "", "cecha": cecha,
          "clocks": [{"name": n, "size": s, "value": v} for n, s, v in clocks], "notes": ""}, "icons/svg/hanging-sign.svg", fid=f_tools, sort=300 + j * 10, disposition=0)

actor("rejestr", "Rejestr Długów: Embargo", "rejestr", {"debts": [
    {"debtor": "", "debtorText": "Token", "creditor": "", "creditorText": "Drużyna", "waga": 2, "powod": "Zanieśli paczkę do fałszywej Alkowy", "status": "otwarty", "hidden": True},
    {"debtor": "", "debtorText": "Rodzina Dacrois", "creditor": "", "creditorText": "Drużyna", "waga": 2, "powod": "Uratowali Jatzeka", "status": "otwarty", "hidden": True},
    {"debtor": "", "debtorText": "Kowal", "creditor": "", "creditorText": "Drużyna", "waga": 3, "powod": "Uratowali Giadę albo jego", "status": "otwarty", "hidden": True}],
    "notes": "<p>Odkryj wpis, gdy dług powstanie w grze. Po imporcie możesz wskazać aktorów jako dłużników i wierzycieli.</p>"},
    "icons/svg/coins.svg", fid=f_tools, sort=400, disposition=0)

# ---------------- Sceny
fs = folder("Embargo", "Scene")
for i, (key, (fn, grid, nm)) in enumerate(MAPS.items()):
    w, h = (2400, 1600) if grid is None else (grid[0] * 70, grid[1] * 70)
    sc_id = sid("scene", key)
    dark = key.startswith("wektor-")
    packs["sceny"].append({"_id": sc_id, "_key": f"!scenes!{sc_id}", "name": nm, "navName": "", "navigation": True, "navOrder": i,
        "active": False, "width": w, "height": h, "padding": 0.05, "backgroundColor": "#0b0a09",
        "background": {"src": f"{MOD}/assets/maps/{key}.webp"}, "thumb": None,
        "grid": {"type": 0 if grid is None else 1, "size": 70 if grid else 100, "distance": 1, "units": "m", "alpha": 0, "color": "#000000"},
        "initial": {"x": None, "y": None, "scale": None}, "tokenVision": False, "fog": {"exploration": False},
        "environment": {"darknessLevel": 0.45 if dark else 0}, "darkness": 0.45 if dark else 0,
        "tokens": [], "lights": [], "notes": [], "sounds": [], "tiles": [], "walls": [], "drawings": [], "regions": [],
        "folder": fs, "sort": i * 100, "ownership": {"default": 0}, "flags": {}, "_stats": STATS13})

# ---------------- Zapis
if os.path.isdir(SRC): shutil.rmtree(SRC)
for name, docs in packs.items():
    d = os.path.join(SRC, name); os.makedirs(d)
    for doc in docs:
        fn = re.sub(r"[^\w]+", "_", doc["name"])[:40] + "_" + doc["_id"] + ".json"
        json.dump(doc, open(os.path.join(d, fn), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in packs.items()})
