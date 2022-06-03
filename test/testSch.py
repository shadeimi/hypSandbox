import schemathesis

schema = schemathesis.from_uri("http://localhost:8000/openapi.json")


@schema.parametrize()
def test_api(case):
    case.call_and_validate()
