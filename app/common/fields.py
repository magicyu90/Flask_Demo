# -*- coding: utf-8 -*-
from flask_restful import fields
from flask_restful_swagger import swagger

# ------------ equipment ------------

@swagger.model
class EquipmentResourceFields:
    resource_fields = {
        # 'result': fields.Integer,
        # 'data': fields.List(fields.Nested(equipment_fields)),
        # 'msg': fields.String
        'Latitude': fields.Float,
        'Longitude': fields.Float,
        'EQP_ID': fields.String,
        'Type': fields.String,
        'Location': fields.String
    }
