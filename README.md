# MyWebApp

Personal ledger application

## Models

### Transactions

| Name        | Type     | Nullable |
| :---------- | :------- | :------: |
| Id          | Int      |  False   |
| Date        | Datetime |  False   |
| Amount      | Int      |  False   |
| CategoryId  | Int      |  False   |
| Description | String   |   True   |
| SourceId    | Int      |  False   |
| TargetId    | Int      |   True   |
| PaymentType | Int      |   True   |
| IsCredit    | Boolean  |  False   |

### Categories

| Name         | Type     | Nullable |
| :----------- | :------- | :------: |
| Id           | Int      |  False   |
| Name         | String   |  False   |
| IsOut        | Boolean  |  False   |
| CreationDate | Datetime |  False   |
| UpdateDate   | Datetime |  False   |

### Sources

| Name         | Type     | Nullable |
| :----------- | :------- | :------: |
| Id           | Int      |  False   |
| Name         | String   |  False   |
| Balance      | Int      |  False   |
| CreationDate | Datetime |  False   |
| UpdateDate   | Datetime |  False   |

### PaymentTypes

| Name         | Type     | Nullable |
| :----------- | :------- | :------: |
| Id           | Int      |  False   |
| Name         | String   |  False   |
| CreationDate | Datetime |  False   |
| UpdateDate   | Datetime |  False   |
