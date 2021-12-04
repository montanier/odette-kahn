from unittest.mock import Mock, patch

from odette_kahn.model import predict


@patch("odette_kahn.model.predict.joblib")
@patch("odette_kahn.model.predict.db")
def test_predict_from_name_calls_expected_methods(mock_db, mock_joblib):
    # Given
    properties = [42] * len(predict.properties_names)
    quality = 5
    prediction = 5.3
    mock_db.get_wine_properties_and_quality.return_value = (properties, quality)
    mock_model = Mock()
    mock_model.predict.return_value = [prediction]
    mock_joblib.load.return_value = mock_model

    # When
    answer = predict.predict_from_name("wine name")

    # Then
    assert answer.pop('quality') == quality
    assert answer.pop('predicted') == prediction
    properties_values = [val for val in answer.values()]
    assert all(property_val == 42 for property_val in properties_values)
    assert False


@patch("odette_kahn.model.predict.joblib")
def test_predict_from_properties_calls_expected_methods(mock_joblib):
    # Given
    properties = {key: 42 for key in predict.properties_names}
    prediction = 5.3
    mock_model = Mock()
    mock_model.predict.return_value = [prediction]
    mock_joblib.load.return_value = mock_model

    # When
    answer = predict.predict_from_properties(properties)

    # Then
    assert answer.pop('predicted') == prediction
    properties_values = [val for val in answer.values()]
    assert all(property_val == 42 for property_val in properties_values)
