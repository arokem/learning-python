import circle
import numpy as np

def test_area():
    assert circle.area(1) == np.pi
    assert np.abs(circle.area(np.sqrt(np.pi))-(np.pi ** 2)) < 10e-15
