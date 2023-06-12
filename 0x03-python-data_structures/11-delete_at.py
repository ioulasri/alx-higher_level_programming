#!/usr/bin/python3
if __name__ == "__main__":
    """printing items in list"""
    def delete_at(my_list=[], idx=0):
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            del my_list[idx]
        return my_list

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
