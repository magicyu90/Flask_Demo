# -*- coding: utf-8 -*-
from app.models.equipment import Equipment
from app.common.fields import EquipmentResourceFields
from app.util.response import ResponseHelper
from flask_restful import marshal


class EquipmentManager():
    """设备处理业务类"""

    def get_equipments(self):
        """查询设备"""
        try:
            #session = Session()
            items = Equipment.query.with_entities(Equipment.Latitude, Equipment.Location,
                                                  Equipment.Longitude, Equipment.Type,
                                                  Equipment.Type, Equipment.EQP_ID).all()
            eqps = []
            for item in items:
                eqps.append({
                    'EQP_ID': item.EQP_ID,
                    'Location':  item.Location,
                    'Longitude': item.Longitude,
                    'Latitude': item.Latitude,
                    'Type': item.Type
                })
            return ResponseHelper.returnTrueJson(marshal(eqps, EquipmentResourceFields.resource_fields))
        except Exception as ex:
            return ResponseHelper.returnFalseJson(msg=str(ex), status=500)


