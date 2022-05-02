import sqlite3 as lite


def unpack_sqlite3_object(obj: lite.Row):
    if obj is None:
        return None
    keys = obj.keys()
    if len(keys) < 1:
        return []
    new_dict = {}
    for key in keys:
        new_dict[key] = obj[key]
    return new_dict


def unpack_sqlite3_objects(objs: [lite.Row]):
    new_array = []
    if len(objs) < 1:
        return []
    keys = objs[0].keys()
    if len(keys) < 1:
        return []
    for obj in objs:
        new_dict = {}
        for key in keys:
            new_dict[key] = obj[key]
        new_array.append(new_dict)

    return new_array
