def get_num_words(str):
  return len(str.split())

def cnt_chr_dict(str):
    dict = {}
    for item in str:
        key_value = dict.get(item)
        if key_value is not None:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict

def sort_on(items):
    return items["num"]

def sort_chr_dict(unsorted_dict):
    sorted_list = []
    for item in unsorted_dict:
        sorted_list.append({
            "char": item,
            "num": unsorted_dict[item]
        })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


