from sqlalchemy import exc

from app import db
import errors


class BaseModelMixin:

    @classmethod
    def by_id(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        else:
            raise errors.NotFound

    def add(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck


class Advertisement(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True)
    description = db.Column(db.Text)

    def __str__(self):
        return '<Advertisement {}>'.format(self.title)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
