# Dofus Sniffer
Build with Python3.7 and Scapy  
**This project is still in progress**

## Packets handled

* ChatServerMessage
```
ChatServerMessage (5722)
Channel: 6 (CHANNEL_SEEK)
Time: 1604760854 (15:54:14)
Message: Bonjour, pas de guilde ré-ouvre ses portes portes aux joueurs PVP / PVM souhaitant partager de bons moments en communauté. L'aide au recrutement et l'entraide sont récompensées en rangs. Bon jeu !
SenderName: Tetashield
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