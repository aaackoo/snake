# Snake Game
## Zadanie
Hra je inšpirovaná pôvodnov hrou SNAKE, vytvorená v Pythone pomocou knižnice PyGame. Hra ma rovnaký princíp + pár doplnkov. Hráč si vyberie konkrétnu mapu, na ktorej chce aby jeho hra prebiehala a potom môže hrať. Priebeh hry spočíva v tom, že hráč musí ovládať SNAKEa a zbierať, v tomto prípade, piť poháre s pivom. Hráč ma za úlohu nazbierať/vypiť čo najviac pohárov pričom sa hra vyšším dosiahnutým skóre zťažuje. Hráč sa musí vyhýbať aby nenarazil do stien, sám do seba a poďla konkrétnej mapy aj prekážkam, ktoré sú na mape zobrazené, inak hra skončí.
## Zvolené algoritmy
Moja hra nevyužíva žiadne špeciálne algoritmy, iba som vybral jeden triediaci algoritmus na zotriedenie pola výhercov. Je to primitívny algoritmus, ktorý prechádza pole v linearnom čase, vybere maximum z pola a appendne do druhého listu. Keď nazbiera 5 najvyšších hodnot, prechádzanie zastaví. Prípadne by sa dalo porozmýšlať nad chytrejším a rýchlejším algoritmom, ale neprišlo mi to tak závažné, keď sa prechádza maximálne 5-krát.
## Program
Program som podrozdelil do troch tried a štvrtej časti. Okrem knižnice Pygame som využil balík Vector2 z pygame.math. Toto som zvolil kvôli jednoduchšiemu prístupu ako k listu, kde si zjednodušiť volania TELO[0/1] na TELO.x alebo TELO.y. Príde mi to takto prehladnejšie a jednoduchšie. Ďalej som využil knižnicu random na generovanie pozícii.

Na začiatku som vytvoril triedu pre SNAKEa. Inicializujú sa tu hlavné premenné, s ktorými bude SNAKE pracovať, jeho smer, telo implementované pomocou listu s pomocou Vector2 a taktiež načítanie obrázku. Trieda SNAKE má metódy ako vytvorenie SNAKEa, vykreslenie na obrazovku, pohyb a predĺženie.

Ďalšia trieda je pre objekt, ktorý bude náš SNAKE jesť/piť. Táto trieda má taktiež incializačnú časť, kde sa mu pridelí obrázok. Metódy tejto triedy sú vygenerovanie náhodnej pozície, kde som opäť využil balík Vector2 a podobne ako pri prvej triede, vykreslenie na obrazovku. 

Posledná trieda je samotná HRA. Inicializuje sa tu celá hra, vytvorí sa objekt SNAKE a objekt FOOD, pridelujú sa rôzne premenné obrázkom, aktuálny status hry, vybratá mapa,... V tejto časti sa pracuje s objektami SNAKE a FOOD. Metódy sú napríklad inicializácia úvodnej obrazovky, záverečnej obrazovky. Aktualizácia hry, ktorá riadi hlavný chod hry a volá sa každých 180 sekúnd. Metóda, ktorá prečíta súbor odpovedajúci aktualne zvolenej mape a prečíta súradnice prekážok, ktoré dalšia metóda vykreslí na obrazovku. Samozrejme sa tu nachádza metóda, ktorá ošetruje aby sa objekt FOOD negeneroval na prekážkach, prípadne na našom SNAKOVI. Pridal som menšiu vychytávku aby hra nebola stereotypná a aby bola časom náročnejšia. Akonáhle dosiahneme skóre 10 sa začnú generovať náhodne čísla z intervalu, ktorý sa postupne zmenšuje a ak toto číslo spadne to malého intervalu, náš SNAKE náhodne odbočí, pravdepodobnosť sa vyšším skóre zvyšuje a tak je to náročnejšie. Ide v podstate o efekt veľa vypitých pív, opitie :D

Posledná časť je nekonečný cyklus, kde sa stále volá metóda HRY na kontrolovanie vstupu uživatela a podla aktualneho statusu hry sa volá príslušná metóda.
## Alternatívne riešenie programu
Ako som spomínal pri popise algoritmu, ten by sa dal prípadne vylepšiť na rýchlejší a efektívnejší. Iné alternatívne riešenie mi nenapadá.
## Reprezentácia vstupných dát
Na začiatku hry si vyberáme ľavým kliknutím myši mapu, na ktorej chceme hrať. Stlačením klávesy ENTER začne hra. SNAKEa ovládame šípkami a had môže meniť smer iba do strán. Na záverečnej obrazovke ľavým kliknutím na input box zahájime zadávanie našej prezývky, je dôležité písať prezývku bez MEDZIER! (potom sa bude zobrazovať iba prvá časť nášho mena) a po stlačení klávesy ENTER sa naše meno s naším skóre zapíše do súboru. Stlačením klávesy N nás vráti naspäť na úvodnu obrazovku s výberom mapy.
## Reprezentácia výstupných dát
Na začiatku hry sa na obrazovke zobrazuje aktuálne zvolená mapa. V dalšej fáze hry vidíme aktuálne dianie hry a priebežné počítadlo skóre. Na konci nám hra ponúkne aby sme si skóre uložili a vypíše rekord top 5 najlepších hráčov.
## Priebeh práce
Pôvodne som hru chcel programovať cez Vianočné prázdniny, ale nejako som sa k tomu nedostal tak som hru po malých kúskoch programoval počas skúškového obdobia, popri učení sa na skúšky. Mal som to skôr ako relax a oddych od učenia sa :D. Dokopy som hru mohol mať napísanú asi sa týždeň.
## Čo nebolo dokončené
Podľa môjho názoru som zvládol do hry implementovať všetko čo som chcel.
## Záver
Práca na tejto hre ma bavila, naučil som sa základy pracovania s GITom, čo mi počas štúdia a určite aj v budúcnosti uľahčí život. :)