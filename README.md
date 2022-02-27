# MyWebApp

Personal ledger application

## Models

### Transaction

| Name             | Type    | Nullable |
| :--------------- | :------ | :------: |
| id               | int     |  false   |
| transaction_date | date    |  false   |
| amount           | int     |  false   |
| category_id      | int     |  false   |
| description      | string  |   true   |
| source_id        | int     |  false   |
| target_id        | int     |   true   |
| payment_type_id  | int     |   true   |
| is_credit        | boolean |  false   |

### Category

| Name              | Type     | Nullable |
| :---------------- | :------- | :------: |
| id                | int      |  false   |
| name              | string   |  false   |
| is_out            | boolean  |  false   |
| creation_datetime | datetime |  false   |
| update_datetime   | datetime |  false   |

### Source

| Name              | Type     | Nullable |
| :---------------- | :------- | :------: |
| id                | int      |  false   |
| name              | string   |  false   |
| balance           | int      |  false   |
| creation_datetime | datetime |  false   |
| update_datetime   | datetime |  false   |

### PaymentType

| Name              | Type     | Nullable |
| :---------------- | :------- | :------: |
| id                | int      |  false   |
| name              | string   |  false   |
| creation_datetime | datetime |  false   |
| update_datetime   | datetime |  false   |
