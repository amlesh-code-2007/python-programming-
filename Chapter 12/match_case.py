def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not found"
        case 500:
            return "Internal service Error"
        case _:
            return "Unkown Error"
        
print(http_status(500))