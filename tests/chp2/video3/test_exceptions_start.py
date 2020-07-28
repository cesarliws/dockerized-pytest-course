from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point('Dakar', 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as e:
        Point('Buenos Aires', 12.11386, -555.08269)
    assert str(e.value) == 'Invalid latitude, longitude combination'


def test_invalid_name_datatype():
    with pytest.raises(ValueError) as e:
        Point(5, 12.11386, -55.08269)
    assert str(e.value) == 'City name provided must be a string'
