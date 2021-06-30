import time


def get_response(data):
    response = {}
    
    try:
        image_bytes = data["src"]
        print(image_bytes)
        time.sleep(5)
        response = find_bears(image_bytes)
        # TODO 
        # make call to bear finder package
    except Exception as err:
        pass

    return response


def find_bears(image_src):
    return {'data': "", "count": 0}