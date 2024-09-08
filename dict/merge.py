dict1={
    "name":"alice",
    "id":1
}

dict2={
    "id":2,
    "place":"london"
}

merge_dict={**dict1,**dict2}

print(merge_dict)