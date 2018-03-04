# -*- coding: utf-8 -*-
import json


class ResponseHelper:
    @staticmethod
    def returnTrueJson(data, msg='success'):
        return {
            "result": 100,
            "data": data,
            "msg": msg
        }

    @staticmethod
    def returnFalseJson(data=None, msg="error", status=None):
        return {
            "result": status,
            "data": data,
            "msg": msg
        }
