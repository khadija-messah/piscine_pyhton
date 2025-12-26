def all_thing_is_obj(object: any) -> int:
    match object:
        case list():
            print("List : ", type(object))
            return 0
        case tuple():
            print("Tuple : ", type(object))
            return 0
        case set():
            print("Set : ", type(object))
            return 0
        case dict():
            print("Dict : ", type(object))
            return 0
        case str():
            print(f"{object:s} is in the kitchen : {type(object)}")
            return 0
        case int():
            return object
        case _:
            print("Type not found")
            return 0
    