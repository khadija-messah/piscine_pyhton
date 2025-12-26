def NULL_not_found(object: any) -> int:

    if(object is None):
        print("Nothing: None ",type(object))
        return 0
    if isinstance(object,int) and object == 0:
        print("Zero: 0 ",type(object))
        return 0
    if isinstance(object,str) and object == "":
        print("Empty: ",type(object))
        return 0
    if isinstance(object,bool) and object == False:
        print("Fake: False",type(object))
        return 0
    if isinstance(object,float):
        if(object != object):
            print("Cheese: nan  ",type(object))
            return 0
        return 1
    print("Type not Found")
    return 1