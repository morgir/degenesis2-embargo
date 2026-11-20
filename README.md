# Degenesis 2.0 — Embargo (moduł prywatny)

Scenariusz startowy **„Embargo”** z podręcznika *Katharsys* (SIXMOREVODKA), przerobiony na zasady
[Degenesis 2.0](https://github.com/morgir/Degenesis2) dla Foundry VTT v14.

> Prywatna adaptacja do gry przy własnym stole. Fabuła, postacie i miejsca należą do SIXMOREVODKA.
> Nie udostępniaj tego repozytorium ani paczki publicznie.

## Zawartość
- **Dzienniki:** przygoda dla MG (11 rozdziałów, teksty do czytania, Cechy, tropy, zegary), *Szkoła MG: Embargo*, handouty dla graczy.
- **Aktorzy:** 12 NPC z portretami i żetonami, wataha Gendo (Banda), Śledztwo, 4 Lokacje, 3 Frakcje, Rejestr Długów.
- **Sceny:** 5 map narysowanych od nowa (siatka 1 m).

## Instalacja
Repozytorium jest prywatne, więc Foundry nie pobierze modułu samo przez manifest.
1. Zaloguj się na GitHub → **Releases** → pobierz `degenesis2-embargo.zip` z najnowszego wydania.
2. Rozpakuj do `Data/modules/` (ma powstać `Data/modules/degenesis2-embargo/module.json`).
3. W świecie Degenesis 2.0: **Manage Modules** → włącz *Degenesis 2.0 — Embargo*.
4. Przy wejściu do świata pojawi się okno importu. Później: przycisk **Embargo — importuj** w zakładce Dzienniki.

Aktualizacja: usuń stary folder `degenesis2-embargo` (albo tylko jego `packs/`), rozpakuj nowy i zaimportuj ponownie — ID dokumentów są stałe, więc nic się nie zdubluje.

## Wydania
Zmień `"version"` w `module.json` i wypchnij na `main` — akcja zbuduje paczkę i utworzy wydanie.
Źródła kompendiów: `src/packs/*/*.json` (generowane skryptami w `build/`).
