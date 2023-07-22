def sort_movies_obj_yearly (arr):

    for i in range(1, len(arr)):
        key = arr[i]['year']
        print(key)
        j = i - 1
        while j >= 0 and arr[j]['year'] > key:
            arr[j + 1]['year'] = arr[j]['year']
            j -= 1
        arr[j + 1]['year'] = key
    return arr
    
def sort_movies_obj_alphabetical (arr):
    

    for i in range(1, len(arr)):
            
        if arr[i]["title"].startswith(( "a", "an")):
            arr[i]["title"] = arr[i]["title"][3:]
        
        if arr[i]["title"].startswith("the"):
            arr[i]["title"] = arr[i]["title"][4:]

    
        key = arr[i]['title']
        print(key)
        j = i - 1
        while j >= 0 and arr[j]['title'] > key:
            arr[j + 1]['title'] = arr[j]['title']
            j -= 1
        arr[j + 1]['title'] = key
    return arr


if __name__ == "__main__":

    movies_arr =[
        {
            "title" : "spider_man",
            "year" : "1990",
            "genres": ["action","super_hero"]
        },
        {
            "title" : "barbe",
            "year" : "2022",
            "genres": ["drama","comedy"]
        },
                {
            "title" : "the gero",
            "year" : "2015",
            "genres": ["drama","comedy"]
        }

    ]

    # array = [20,10,60,40,30]
    # print(sort_movies_obj_yearly (movies_arr))
    print(sort_movies_obj_alphabetical (movies_arr))