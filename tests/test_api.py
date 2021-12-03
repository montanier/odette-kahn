import pytest
from odette_kahn import app
from unittest.mock import patch


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@patch('odette_kahn.api.routes.predict_from_name')
def test_wine(mock_predict_from_name, client):
    # Given
    expected_return = {'property': 3, 'quality': 5, 'predicted': 4.3}
    mock_predict_from_name.return_value = expected_return

    # When
    resp = client.get('/wine', json={"name": "some wine"})

    # Then
    mock_predict_from_name.assert_called_with("some wine")
    assert resp.get_json() == expected_return


@patch('odette_kahn.api.routes.predict_from_properties')
def test_prediction(mock_predict_from_properties, client):
    # Given
    expected_return = {'property': 42, 'predicted': 4.3}
    mock_predict_from_properties.return_value = expected_return

    # When
    resp = client.get('/prediction', json={"property": 42})

    # Then
    mock_predict_from_properties.assert_called_with({"property": 42})
    assert resp.get_json() == expected_return
