# long-lambda-expr snippets for dask

# File: /root/ecooptimizer/dask/dask/datasets.py
# Line: 165

schema = lambda field: {
    "age": field("random.randint", a=0, b=120),
    "name": (field("person.name"), field("person.surname")),
    "occupation": field("person.occupation"),
    "telephone": field("person.telephone"),
    "address": {"address": field("address.address"), "city": field("address.city")},
    "credit-card": {
        "number": field("payment.credit_card_number"),
        "expiration-date": field("payment.credit_card_expiration_date"),
    },
}

# ==================================================
