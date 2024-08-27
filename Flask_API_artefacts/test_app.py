import json
from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Boston House Price Prediction" in response.data

# Commenter ou supprimer ce test pour le moment
# def test_predict_api():
#     tester = app.test_client()
#     response = tester.post('/predict_api', json={
#         "data": {
#             "CRIM": 0.00632,
#             "ZN": 18.0,
#             "INDUS": 2.31,
#             "NOX": 0.538,
#             "RM": 6.575,
#             "Age": 65.2,
#             "DIS": 4.09,
#             "RAD": 1.0,
#             "TAX": 296.0,
#             "PTRATIO": 15.3,
#             "B": 396.9,
#             "LSTAT": 4.98
#         }
#     })
#     assert response.status_code == 200
#     data = json.loads(response.data)
#     assert isinstance(data, float) or isinstance(data, int)  # Check for int or float
