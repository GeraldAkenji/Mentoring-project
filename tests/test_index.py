

def test_index(app, client):
    res = client.get('/')
    print(res.data)
    assert res.status_code == 200
    assert b'Mentoring Appointment' in res.data


def test_wrong_page(app, client):
    res = client.get('/*')
    assert res.status_code == 404
    assert b'Not Found' in res.data


def test_wrong_method(app, client):
    res = client.post('/')
    assert res.status_code == 405
    assert b'Method Not Allowed' in res.data
