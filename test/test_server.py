
from hypothesis import given, strategies as st
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


@given(st.integers())
def test_prod(s):
    res = client.get(f"/api/prod/{s}")

    assert res.status_code == 200
    assert res.json() == {"message": s * s}



