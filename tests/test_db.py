from unittest.mock import patch, Mock

from odette_kahn.api import db


@patch('odette_kahn.api.db.get_db')
@patch('odette_kahn.api.db.close_db')
def test_get_wine_properties_and_quality_for_a_known_wine(patch_close_db, patch_get_db):
    # Given
    cursor = Mock()
    cursor.fetchone.return_value = [42, 5]
    conn = Mock()
    conn.execute.return_value = cursor
    patch_get_db.return_value = conn

    # When
    properties, quality = db.get_wine_properties_and_quality('wine_name', ['property'])

    # Then
    assert properties == [42]
    assert quality == 5


@patch('odette_kahn.api.db.get_db')
@patch('odette_kahn.api.db.close_db')
def test_get_wine_properties_and_quality_for_an_unknown_wine(patch_close_db, patch_get_db):
    # Given
    cursor = Mock()
    cursor.fetchone.return_value = None
    conn = Mock()
    conn.execute.return_value = cursor
    patch_get_db.return_value = conn

    # When
    properties, quality = db.get_wine_properties_and_quality('wine_name', ['property'])

    # Then
    assert properties is None
    assert quality is None
