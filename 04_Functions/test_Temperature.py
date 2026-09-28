import pytest
from Temperature import celsius_to_fahrenheit

# Example data points for testing
temperatures = [
    (0, 32),
    (100, 212),
    (15, 59),
    (25, 77),
]

# Test cases using pytest
@pytest.mark.parametrize("celsius, fahrenheit", temperatures)
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert abs(celsius_to_fahrenheit(celsius) - fahrenheit) < 0.001