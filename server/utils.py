import time


def get_response(data):
    """
    return: http code and json
    """
    response = {}
    
    try:
        image_bytes = data["src"]
        width = data["width"]
        height = data["height"]
        print(image_bytes)
        time.sleep(5)
        response = find_bears(image_bytes, width, height)
    except KeyError as err:
        return 400, {}
    except Exception as err:
        return 500, {}
    return 200, response


def find_bears(image_src, width: int, height: int):
    # TODO
    return {'src': image_src, "width": width, "height": height}