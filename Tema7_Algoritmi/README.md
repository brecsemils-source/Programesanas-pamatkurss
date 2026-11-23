Kā strādā algoritms un sarežģītība (
𝑂
(
log
⁡
𝑛
)
O(logn))
Binārā meklēšana katrā solī pārbauda diapazona vidu (apaksa + augsa) // 2 un atmet pusi no atlikušajiem variantiem.

Laika sarežģītība ir 
𝑂
(
log
⁡
𝑛
)
O(logn), bet lineārajai meklēšanai sliktākajā gadījumā — 
𝑂
(
𝑛
)
O(n).

1–100 diapazonā: binārā meklēšana prasa ne vairāk kā 7 minējumus (lineārā sliktākajā gadījumā — 100).

1–1000 diapazonā: binārā meklēšana prasa ne vairāk kā 10 minējumus (lineārā sliktākajā gadījumā — 1000).

Ja spēlētājs atbild pretrunīgi (apaksa > augsa), programma pamana, ka neviens skaitlis vairs neder, un beidz spēli.

Testu pieraksti
Trīs partiju pārbaude (diapazons 1–100)
partija (iedomātais skaitlis 25): 2 minējumi (50 -> mazaks, 25 -> pareizi).

partija (iedomātais skaitlis 88): 3 minējumi (50 -> lielaks, 75 -> lielaks, 88 -> pareizi).

partija (iedomātais skaitlis 73): 6 minējumi (50 -> lielaks, 75 -> mazaks, 62 -> lielaks, 68 -> lielaks, 71 -> lielaks, 73 -> pareizi).

Lielākais minējumu skaits: 6 minējumi (nepārsniedz 7).

Pārbaude diapazonā 1–1000
Nomainot augšējo robežu uz 1000, jebkurš skaitlis tiek uzminēts ne vairāk kā 10 minējumos (lineārā meklēšana sliktākajā gadījumā prasītu 1000).

Pretrunīgas spēles tests
Dators min 50 -> mazaks (augsa = 49), pēc tam min 25 -> lielaks (apaksa = 26).

Turpinot atbildēt pretrunīgi, robežas sakrustojas (apaksa > augsa) un programma paziņo, ka spēlētājs atbildējis negodīgi.