# Pokemon Card Storage Web App (working title)

```mermaid
---
title: Pokemon ER Diagram
---

%%ER Diagram for pokemon app
erDiagram
  USER ||--o{ DECK : owns
  CARD
  DECK ||--|{ CARD : contains
  ADMIN ||--|{ CARD : approves
  ADMIN ||--|{ USER : mantains

```

