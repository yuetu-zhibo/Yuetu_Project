#!/usr/bin/python3
# coding: utf-8
from mainapp.models import Base


def dumps(obj):
    if isinstance(obj, list):
        # 多个数据模型类对象的实例
        data = []
        for item in obj:
            item_dict = item.__dict__
            item_dict.pop('_sa_instance_state')

            instance = {}
            for key, value in item_dict.items():
                if isinstance(value, Base):
                    instance[key] = dumps(value)
                else:
                    instance[key] = value

                data.append(instance)

        return data
    else:
        item_dict = obj.__dict__
        item_dict.pop('_sa_instance_state')

        instance = {}
        for key, value in item_dict.items():
            if isinstance(value, Base):
                instance[key] = dumps(value)
            else:
                instance[key] = value

        return instance


def _clear_state(instance: dict):
    instance.pop('_sa_instance_state')
    return instance