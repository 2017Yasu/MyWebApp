# MyWebApp

Personal ledger application

## Models

### Transaction

| Name         | Type     | Nullable |
| :----------- | :------- | :------: |
| id           | int      |  false   |
| date         | datetime |  false   |
| amount       | int      |  false   |
| category_id  | int      |  false   |
| description  | string   |   true   |
| source_id    | int      |  false   |
| target_id    | int      |   true   |
| payment_type | int      |   true   |
| is_credit    | boolean  |  false   |

### Category

| Name          | Type     | Nullable |
| :------------ | :------- | :------: |
| id            | int      |  false   |
| name          | string   |  false   |
| is_out        | boolean  |  false   |
| creation_date | datetime |  false   |
| update_date   | datetime |  false   |

### Source

| Name          | Type     | Nullable |
| :------------ | :------- | :------: |
| id            | int      |  false   |
| name          | string   |  false   |
| balance       | int      |  false   |
| creation_date | datetime |  false   |
| update_date   | datetime |  false   |

### PaymentType

| Name          | Type     | Nullable |
| :------------ | :------- | :------: |
| id            | int      |  false   |
| name          | string   |  false   |
| creation_date | datetime |  false   |
| update_date   | datetime |  false   |
