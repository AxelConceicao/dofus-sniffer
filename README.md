# Dofus Sniffer
Build with Python3.7 and Scapy  
**This project is still in progress**

## Packets handled

* ChatServerMessage
```
ChatServerMessage (5722)
Channel: CHANNEL_SALES
Time: 22:36:52
Message: coucou, 870M Dispo Pour tout vos Lot Ditems THL / Equipement 200 / EXO / Dofus / Colorivant / Pepites / Parchemin kolizeton, ect. Je vous Offre le meilleur Prix !!
SenderName: Haya-doos
```

* ExchangeTypesItemsExchangerDescriptionForUserMessage
> For now only works with ressources not equipments
```
ExchangeTypesItemsExchangerDescriptionForUserMessage (8949)
- objectType: 40
    objectUID: 1016635
    objectGID: 12728
    objectName: Ardonite
    objectType: 40
    effects:
    prices:
    - 79950 
    - 884500
    - 8949000
```