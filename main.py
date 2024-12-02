import requests
ID=0
def get():
    response = requests.get('https://jsonplaceholder.typicode.com//posts')
    posts = response.json()
    for post in posts:
        if post['userId'] % 2 == 0:
            print(post)

def post():
    response = requests.post('https://jsonplaceholder.typicode.com//posts',data={"userId": 1,
    'title':"Тестовый пост",
    'body':"123"})
    id=response.json()
    global ID
    ID = id['id']
    print(response.text)

def put():
    global ID
    response = requests.put('https://jsonplaceholder.typicode.com//posts/101',
    data={
    "userId": 1,
    'title':"Тестовый измененный пост",
    'body':"измененно"})
    print(response.text)

if __name__ == '__main__':
    methods = {
        "get",
        "post",
        "put"}
    switch = {
        "get": get,
        "post": post,
        "put": put
    }
    method = input("Choose get, post, put: ")
    while (method in methods):
        method = input("Choose get, post, put: ")
        switch[method]()






