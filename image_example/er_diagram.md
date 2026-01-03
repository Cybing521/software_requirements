``` mermaid
erDiagram
    ChemicalStockroomInventory ||--|{ ChemicalContainer : storing
    ChemicalRequest ||--|{ ChemicalContainer : fulfilling
    Requester ||--|{ ChemicalRequest : placing
    ChemicalRequest }|--|{ Chemical : listing
    Chemical ||--|{ ChemicalContainer : containing
    Chemical }|--|{ VendorCatalog : listing
    ChemicalContainer ||--|| ContainerHistory : tracking

    ChemicalStockroomInventory {
        string id PK
    }

    ChemicalRequest {
        string id PK
    }

    Requester {
        string id PK
    }

    ChemicalContainer {
        string id PK
    }

    Chemical {
        string id PK
    }

    VendorCatalog {
        string id PK
    }

    ContainerHistory {
        string id PK
    }

```
