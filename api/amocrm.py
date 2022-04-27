import requests
leads = {
        "name": "Адиль",
        "created_by": 0,
        "custom_fields_values": [
            {
                "field_id": 1162757, #name
                "values": [
                    {
                        "value": "Адиль"
                    }
                ]
            },
             {
                "field_id": 1162759, #number
                "values": [
                    {
                        "value": "87022438358"
                    }
                ]
            },
             {
                "field_id": 1162761, #email
                "values": [
                    {
                        "value": "meirambaiuliadil20020@gmail.com"
                    }
                ]
            }
        ]
    },
    


access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImE0MTk3ZTkyMmU5MjBhNjQ4ZGFjMTRhOWI4NzcyOWI1YzI2N2Q3NTljNTFlZTk5YTJlMmZmOGNlMWZkOGMzZTg3NjhhNTBmNTFkODBkZDA1In0.eyJhdWQiOiI0ZjJkZDlkZC1iNTFkLTRlMmQtYjI5NC04N2EyOTgyZDA4YTkiLCJqdGkiOiJhNDE5N2U5MjJlOTIwYTY0OGRhYzE0YTliODc3MjliNWMyNjdkNzU5YzUxZWU5OWEyZTJmZjhjZTFmZDhjM2U4NzY4YTUwZjUxZDgwZGQwNSIsImlhdCI6MTY1MDc3MTczMSwibmJmIjoxNjUwNzcxNzMxLCJleHAiOjE2NTA4NTgxMzEsInN1YiI6IjczMDQ4NDUiLCJhY2NvdW50X2lkIjoyOTM2MzU1MSwic2NvcGVzIjpbInB1c2hfbm90aWZpY2F0aW9ucyIsImNybSIsIm5vdGlmaWNhdGlvbnMiXX0.OP0DCAsTbHJX0fI6sC2fAhEMWCrEywp9EfYpEvaG2tIx6tE9rbZcFcEpXfmZ1wYs2grqadFG83z3wqeZIF33MB8m4JibN7PrYi2DdqAkDciQIukFU20Dne4SMgXZuJXRwBBnGYMPwEOSs8timj7Lo2LPKJnmOhnV61SpDpes6pPl17oHcXYzsJnB1kXZhF6B3jF6ffErtyNjdLxZH-9GfU9WzOYDvS_MJjNGAkkiQTFusstZ2eS4W782PI9cEWXv93KEVGn4s2tZ1gaJy6XROIKo66bGt9TE9OnJ8_DTa_piNEWSXxaiwWsyB16YuUblKtZLw6Y35gJ4mqltZaSJdA"
refresh_token = "def50200288ea121311e0268ded6523f1a6a218b811c7155b7307f5be664716c1f7c43933c0ca540487849e2e41bccdaaeb5bdf8110c5ef819eaa86291486d236fc26b87a34ae41ea0f5e02b0e3547be3650c5fa16c979d88d728e100e706f81d881395b3b3a8ca2cab962eac203de79e0b6be52bc1ed759fbc398e04fd892f713bc918b78ab75afdaf5f308996118d1e47d7c7891f538395fafbe29ceac1098701dadc818675ae32bc983d959bc6235a05ef16a1e40b8f0b2a5d821cd1a26d7cb7ccf178e35bc3fe1372f2c706808225ade520a00a6444a4a2b5303d920970bf0be70b6c7a36135bfa31dfff88fcf4283569dee91d20f8809e6b272185c928e544893fdacd8bee40266f55a11c8e0ef2611b4cf9a977a1dbcc785bcff8c7b18dd41099b0f477d34f2e52d53e1f9c2d8e84452537bd67d375699c314955a377610ad78639a211bab9d946999e2738ae488cab1b040743d4e4c676018fcef80ad5105cba37f9fba5e3026c2c7c75ba604b533505a82e3e2f2a10d9fa04f85b71c47822b519ecb8ec5372d27a3809711756249798fc9b2404aaf05c62a3fadb14d6159303c540f75b9f9846838de699555d2b9e767111818d740f834efcf24663c514fee26f84f3969c6ac"
headers = {
    'Authorization':f"Bearer {access_token}"
}
link = 'https://ioka.amocrm.ru/api/v4/leads'

# data = {
#   "client_id": "4f2dd9dd-b51d-4e2d-b294-87a2982d08a9",
#   "client_secret": "8T6Pl5NeZRgfMbQVtQzrINX4PxUWQjEfZvfOzyLapuCjO4nM1KzfFg0aKniis068",
#   "grant_type": "authorization_code",
#   "code": "def50200e813d30f66576f4023d419f5a7ca500e31c2f76a0effe86e8682f850257ce48df47bc97748fec304c3733df073481fdfe4e829464a3ae5401609f10782e96868187f5f8af3202cde1ea5de58297d0db4cb7c0970f50016c511008348745a618035a5327c0e2c75fd9ba25d098b82af09f155f26402589e1e435ae54493d8c570d63703a9a33e18984975564dbbce841c1d6e64d4f181dde4f7c2567075d863ed51ac94b6e7f0094d50859bb9326fee53e73ba5308d39a3cae6e1b7bee6d5755aae0441c447699b93765eb2ea83224552540f1b0d69a21b660cb0a51ace1ace95440432b15c8df28e1bee34113627150a45a481d12c12a6655074ac7cfd7ae8579cbdb5d371621e98db1f724e1f823e2d213a75aa38a8836d3435cd9d66f4d34e3cb04fc52053dcd1d2b26bab7df52407a83f5ec02589335836ee08e1a88364b812002430a6e13078474c7f16398cdcc440c74c599e12ea677d7b990e058d61f78c5d5a5b9a2ea57d69caba00db9b4c09183204c925760136d3140df102ba052158dd9e56d70a8f504321973eaa74ff419db65150d324e844bedce7be35e7212c662c2860d6e850290c2dc8157c28774657a393dd3e27bf8a2a46d39a03d4",
#   "redirect_uri": "https://www.google.com/"
# }

response = requests.post(url=link,json=leads, headers=headers)
print(response.content)

# class AmoCRM:

#     def get_access_token():
