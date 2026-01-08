# 01_basics.py - 20 print statements demonstrating conversions and calculations
# All data is completely fictional and made-up (no personal info used)
# These use labeled debug prints (perfect for a "prALL" live template in IntelliJ)
# Topics: Type conversions, math operations, unit conversions, finance, physics, etc.

import math
from datetime import date

# Made-up fictional data
player_score = 87.5
level = "12"
health_points = "150"
distance_miles = 45.6
temp_celsius = 22.0
principal = 5000.0
rate_percent = 4.5
years = 10
radius = 8.0
base = 5
height = 12
weight_lbs = 180
height_inches = 70
today_fictional = date(2026, 4, 15)
game_start = date(2026, 1, 1)

# 1. String to int conversion + calculation
level_int = int(level)
next_level = level_int + 1
print(f"next_level: {next_level}")  # 13

# 2. String to int for health calculation
max_health = int(health_points) * 2
print(f"max_health: {max_health}")  # 300

# 3. Float to int (truncation)
rounded_score = int(player_score)
print(f"rounded_score: {rounded_score}")  # 87

# 4. Int to float for division
average_score = player_score / 3
print(f"average_score: {average_score}")  # 29.166...

# 5. Miles to kilometers conversion
km = distance_miles * 1.60934
print(f"km: {km}")  # ~73.43

# 6. Celsius to Fahrenheit
fahrenheit = (temp_celsius * 9 / 5) + 32
print(f"fahrenheit: {fahrenheit}")  # 71.6

# 7. Simple interest calculation
interest = principal * (rate_percent / 100) * years
print(f"interest: {interest}")  # 2250.0

# 8. Total amount after interest
total = principal + interest
print(f"total: {total}")  # 7250.0

# 9. Compound interest (annual compounding)
compound_total = principal * (1 + rate_percent / 100) ** years
print(f"compound_total: {compound_total}")  # ~7761.13 (rounded)

# 10. Circle area (math.pi usage)
area = math.pi * radius ** 2
print(f"area: {area}")  # ~201.06

# 11. Circle circumference
circumference = 2 * math.pi * radius
print(f"circumference: {circumference}")  # ~50.27

# 12. Triangle area
triangle_area = 0.5 * base * height
print(f"triangle_area: {triangle_area}")  # 30.0

# 13. Hypotenuse (Pythagorean theorem)
hypotenuse = math.sqrt(base ** 2 + height ** 2)
print(f"hypotenuse: {hypotenuse}")  # 13.0

# 14. BMI calculation (lbs and inches)
weight_kg = weight_lbs * 0.453592
height_m = height_inches * 0.0254
bmi = weight_kg / (height_m ** 2)
print(f"bmi: {bmi}")  # ~25.8 (example)

# 15. Days since game start (date calculation)
days_played = (today_fictional - game_start).days
print(f"days_played: {days_played}")  # 105

# 16. Percentage score increase
old_score = 75.0
increase_percent = ((player_score - old_score) / old_score) * 100
print(f"increase_percent: {increase_percent}")  # 16.666...

# 17. Fuel efficiency: MPG to L/100km
mpg = 28.0
liters_per_100km = 235.215 / mpg
print(f"liters_per_100km: {liters_per_100km}")  # ~8.4

# 18. Exponential growth (e.g., population or points)
growth_factor = 1.08  # 8% growth
future_value = 1000 * (growth_factor ** 5)
print(f"future_value: {future_value}")  # ~1469.33

# 19. Logarithm example (decibels or Richter scale simulation)
intensity_ratio = 10000
decibels = 10 * math.log10(intensity_ratio)
print(f"decibels: {decibels}")  # 40.0

# 20. Quadratic formula solution (made-up equation: x² - 5x + 6 = 0)
a, b, c = 1, -5, 6
discriminant = b ** 2 - 4 * a * c
root1 = (-b + math.sqrt(discriminant)) / (2 * a)
root2 = (-b - math.sqrt(discriminant)) / (2 * a)
print(f"root1: {root1}, root2: {root2}")  # 3.0, 2.0

# =============================================================================
# RECOMMENDED "prALL" LIVE TEMPLATE FOR THESE (IntelliJ 2025.2.5)
# =============================================================================
# Abbreviation: prALL
# Template text: print(f": {}")
# Variables:
#    → groovyScript("_1 ?: 'RESULT'", selection())  → uses selection as label or "RESULT"
#    → selection()
#
# Usage: Highlight any expression (e.g., "bmi") → prALL → Tab → perfect labeled print
# No selection → prALL → Tab → print(f"RESULT: ")
