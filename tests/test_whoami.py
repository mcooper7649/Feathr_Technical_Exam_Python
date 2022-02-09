from flask import Flask


def test_base_route():
    app = Flask(__name__)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    print(response)
    assert response.status_code == 404


# def test_new_user():
#     app = Flask(__name__)
#     client = app.test_client()
#     url = '/'
#     response = client.get(url)
#     user = User()
#     assert user
