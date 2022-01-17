from datetime import datetime

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

    def delete(self, ad_id):
        advertisement = Advertisement.by_id(ad_id)
        Advertisement.delete(advertisement)
        return jsonify({'status': 204})

    def patch(self, ad_id):
        advertisement = Advertisement.query.get(ad_id)
        data = Advertisement(**request.json)

        advertisement.update(data)

        response = {
            'id': advertisement.id,
            'title': advertisement.title,
            'description': advertisement.description,
            'created_at': advertisement.created_at,
            'user_id': advertisement.user_id
        }

        return jsonify(response)

    @validate('json', ADVERTISEMENT_CREATE)
    def post(self):
        advertisement = Advertisement(created_at=datetime.now(), **request.json)
        advertisement.add()

        return jsonify(advertisement.to_dict())


ads_api = AdvertisementView.as_view('advertisements_api')

app.add_url_rule('/advertisements/<int:ad_id>', view_func=ads_api, methods=['GET', 'DELETE', 'PATCH'])
app.add_url_rule('/advertisements/', view_func=ads_api, methods=['POST', ])
