base_url = "http://167.172.172.115:52353"

headers = {'Content-Type': 'application/json'}

payload = {
    "name": "1",
    "data": {
        'color': 'red',
        'size': 'Biggest',
        'form': 'circle'
    }
}

payload_put = {
    "name": "aA",
    "data": {
        'color': 'blue',
    }
}

payload_patch = {
    "data": {
        'color': 'blue',
    }
}

payload_create = [
    {
        "name": "01",
        "data":
            {
                "number": "1"
            }
    },
    {
        "name": "02",
        "data":
            {
                "number": "2"
            }
    },
    {
        "name": "03",
        "data":
            {
                "number": "3"
            }
    },
]