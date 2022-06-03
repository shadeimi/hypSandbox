
from hypothesis import given, strategies as st
from fastapi.testclient import TestClient
from app.main import app
from math import factorial as fpy
from app.funct import factorial as flocal
import json


client = TestClient(app)


@given(st.integers())
def test_prod(s):
    res = client.get(f"/api/prod/{s}")

    assert res.status_code == 200
    assert res.json() == {"message": s * s}


@given(st.integers())
def test_fact(s):
    res = client.get(f"/api/fact/{s}")

    assert res.status_code == 200
    assert res.json() == {"message": flocal(s)}
    assert json.loads(res.json())['message'] == fpy(s)


@given(st.integers())
def test_palindrome(s):
    res = client.get(f"/api/palindrome/{s}")

    assert res.status_code == 200
    assert json.loads(res.json())['message'] == s
