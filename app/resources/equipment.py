#-*- coding: utf-8 -*-
from flask_restful import Resource
from flask_restful_swagger import swagger
from app.common.fields import EquipmentResourceFields
from app.business.equipmentManager import EquipmentManager


class Equipments(Resource):
    def __init__(self):
        self._equipmentManager = EquipmentManager()

    @swagger.operation(
        notes='查询设备元数据',
        nickname='get',
        summary='查询设备元数据',
        responseClass=EquipmentResourceFields
    )
    def get(self):
        return self._equipmentManager.get_equipments()

        