#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is None or my_list_2 is None:
        return None

    _list = []
    for i in range(list_length):
        try:
            _list.append(my_list_1[i] / my_list_2[i])
        except (IndexError):
            print("out of range")
            _list.append(0)
        except (ZeroDivisionError):
            print("division by 0")
            _list.append(0)
        except (TypeError):
            print("wrong type")
            _list.append(0)
        finally:
            pass
    return _list
