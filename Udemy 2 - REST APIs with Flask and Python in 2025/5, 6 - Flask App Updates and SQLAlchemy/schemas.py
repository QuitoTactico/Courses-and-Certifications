from marshmallow import Schema, fields

# ============= PLAIN ===============

# ------------- item ----------------


class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


# -------------- store ---------------


class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


# ========== WITH RELATIONS ==========

# toca así. No puedes usar ItemSchema en StoreSchema ni visceversa, porque el otro no existirá aún
# y podrías hacerle lazy al final, usando lambda: ____Schema, pero habrá una anidación infinita
# así que toca poner la versión Plain, que no tiene referencias a nadie

class ItemSchema(PlainItemSchema):
    # store_id = fields.Str(required=True)
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
