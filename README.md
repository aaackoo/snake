# Snake Game
## Zadanie
Hra je inšpirovaná pôvodnov hrou SNAKE, vytvorená v Pythone pomocou knižnice PyGame. Hra ma rovnaký princíp + pár doplnkov. Hráč si vyberie konkrétnu mapu, na ktorej chce aby jeho hra prebiehala a potom môže hrať. Priebeh hry spočíva v tom, že hráč musí ovládať SNAKEa a zbierať, v tomto prípade, piť poháre s pivom. Hráč ma za úlohu nazbierať/vypiť čo najviac pohárov pričom sa hra vyšším dosiahnutým skóre zťažuje. Hráč sa musí vyhýbať aby nenarazil do stien, sám do seba a poďla konkrétnej mapy aj prekážkam, ktoré sú na mape zobrazené, inak hra skončí.
## Zvolené algoritmy
Moja hra nevyužíva žiadne špeciálne algoritmy, iba som vybral jeden triediaci algoritmus na zotriedenie pola výhercov. Je to primitívny algoritmus, ktorý prechádza pole v linearnom čase, vybere maximum z pola a appendne do druhého listu. Keď nazbiera 5 najvyšších hodnot, prechádzanie zastaví. Prípadne by sa dalo porozmýšlať nad chytrejším a rýchlejším algoritmom, ale neprišlo mi to tak závažné, keď sa prechádza maximálne 5-krát.
## Program
DOPÍSAŤ!!!
## Alternatívne riešenie programu
Ako som spomínal pri popise algoritmu, ten by sa dal prípadne vylepšiť na rýchlejší.
## Reprezentácia vstupných dát
Na začiatku hry si vyberáme ľavým kliknutím myši mapu, na ktorej chceme hrať. Stlačením klávesy ENTER začne hra. SNAKEa ovládame šípkami a had môže meniť smer iba do strán. Na záverečnej obrazovke ľavým kliknutím na input box zahájime zadávanie našej prezývky, je dôležité písať prezývku bez MEDZIER! (potom sa bude zobrazovať iba prvá časť nášho mena) a po stlačení klávesy ENTER sa naše meno s naším skóre zapíše do súboru. Stlačením klávesy N nás vráti naspäť na úvodnu obrazovku s výberom mapy.
## Reprezentácia výstupných dát
Na začiatku hry sa na obrazovke zobrazuje aktuálne zvolená mapa. V dalšej fáze hry vidíme aktuálne dianie hry a priebežné počítadlo skóre. Na konci nám hra ponúkne aby sme si skóre uložili a vypíše rekord 5 najlepších hráčov.
## Priebeh práce
Pôvodne som hru chcel programovať cez Vianočné prázdniny, ale nejako som sa k tomu nedostal tak som hru po malých kúskoch programoval počas skúškového obdobia, popri učení sa na skúšky. Mal som to skôr ako relax a oddych od učenia sa :D. Dokopy som hru mohol mať napísanú asi sa týždeň.
## Čo nebolo dokončené
Podľa môjho názoru som zvládol do hry implementovať všetko čo som chcel.
## Záver
Práca na tejto hre ma bavila, naučil som sa základy pracovania s GITom, čo mi počas štúdia a určite aj v budúcnosti uľahčí život. :)