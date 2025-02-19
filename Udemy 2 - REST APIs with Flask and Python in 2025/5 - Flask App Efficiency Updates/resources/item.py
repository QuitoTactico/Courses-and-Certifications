import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404, message="Item not found")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_id, item_data):
        # item_data = request.get_json()
        try:
            item = items[item_id]
            item |= item_data  # que buena forma!
            return item
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        # por culpa del uso de marshmallow, ya no es un objeto/diccionario con la lista de items, sino meramente la lista y ya
        # recuerda que era mejor el objeto/diccionario, por si el día de mañana te daba por enviar cosas extras
        # return {'items': list(items.values())}
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):
        # with the schema decorator, now i don't need this
        # item_data = request.get_json()

        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="Item already exists")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}  # pasamos todas las weas del dict
        items[item_id] = item

        return item, 201
