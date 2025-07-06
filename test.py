from app import app

def test_info():
    tester = app.test_client()
    response = tester.get('/info')
    assert response.status_code == 200
    assert b"i am lw from india" in response.data

def test_phone():
    tester = app.test_client()
    response = tester.get('/phone')
    assert response.status_code == 200
    assert b"3465797865" in response.data
