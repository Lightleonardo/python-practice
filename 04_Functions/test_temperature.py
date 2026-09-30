import pytest
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

# Example data points for celsius to fahrenheit testing
temperatures_celsius = [
    (0, 32),
    (100, 212),
    (15, 59),
    (25, 77),
]

# Test cases using pytest
@pytest.mark.parametrize("celsius, fahrenheit", temperatures_celsius)
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert abs(celsius_to_fahrenheit(celsius) - fahrenheit) < 0.001

    # Example data points for fahrenheit to celsius testing
temperatures_fahrenheit = [
    (32, 0),
    (212, 100),
    (0, -17.77777777777778),
    (100, 37.77777777777778),
]

# Parametrized test case for fahrenheit_to_celsius
@pytest.mark.parametrize("fahrenheit, celsius", temperatures_fahrenheit)
def test_fahrenheit_to_celsius(fahrenheit, celsius):
    assert abs(fahrenheit_to_celsius(fahrenheit) - celsius) < 0.001
