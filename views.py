from flask import request, jsonify
from flask.views import MethodView

from app import app

from models import Advertisement

from validator import validate
from schema import ADVERTISEMENT_CREATE


class AdvertisementView(MethodView):

    def get(self, ad_id):
        advertisement = Advertisement.by_id(ad_id)
        return jsonify(advertisement.to_dict())

    @validate('json', ADVERTISEMENT_CREATE)
    def post(self):
        advertisement = Advertisement(**request.json)
        advertisement.add()

        return jsonify(advertisement.to_dict())


app.add_url_rule('/advertisements/<int:ad_id>', view_func=AdvertisementView.as_view('advertisements_get'), methods=['GET', ])
app.add_url_rule('/advertisements/', view_func=AdvertisementView.as_view('advertisements_create'), methods=['POST', ])
