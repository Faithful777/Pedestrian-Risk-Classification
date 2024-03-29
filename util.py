# -*- coding: utf-8 -*-
"""RoadSafetyProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CCWQUw9Ugt4fQaKe8tbuAmUONRIPFjyp
"""

!pip install google_streetview

!google_streetview -s key="your_key"

# Import google_streetview for the api module
import google_streetview.api

# Define parameters for street view api
params = [{
	'size': '640x320', # max 640x640 pixels
	'location': '6.4508593,3.3878315',
	'heading': '151.78',
	'pitch': '-0.76',
	'key': 'your_key'
}]

# Create a results object
results = google_streetview.api.results(params)

# Download images to directory 'downloads'
results.download_links('downloads')

import math

def calculate_heading(x, y):
  """Calculates the heading of `x` with respect to `y`.

  Args:
    x: A tuple containing the latitude and longitude of point `x`.
    y: A tuple containing the latitude and longitude of point `y`.

  Returns:
    A float representing the heading of `x` with respect to `y`.
  """

  # Convert the longitudes and latitudes to radians.
  x_lat = math.radians(x[0])
  y_lat = math.radians(y[0])
  x_lon = math.radians(x[1])
  y_lon = math.radians(y[1])

  # Calculate the difference in longitudes and latitudes.
  d_lon = x_lon - y_lon
  d_lat = x_lat - y_lat

  # Calculate the tangent of the heading.
  tan_heading = math.atan2(d_lat, d_lon)

  # Convert the tangent to degrees.
  heading = math.degrees(tan_heading)

  # Return the heading.
  return heading

def paramsGenerator(coordinates, key):
  """Generates a dictionary of parameters for the Google Maps Static API.

  Args:
    coordinates: A tuple of latitude and longitude coordinates.
    heading: The heading of the map in degrees.

  Returns:
    A dictionary of parameters for the Google Maps Static API.
  """

  # Remove the last item from the tuple
  #coordinates = coordinates[:-1]

  # Convert the coordinates to a string.
  coordinates_str = ','.join(str(coordinate) for coordinate in coordinates)

  # Convert the heading to a string.
  #heading_str = str(heading)

  # Create the dictionary of parameters.
  params = {
      'size': '640x320',
      'location': coordinates_str,
      'pitch': '-0.76',
      'key': key
  }

  return params

import ast

# Import google_streetview for the api module
import google_streetview.api

params= []
key = 'your_key'

with open('/content/drive/MyDrive/LagosRoads.txt', 'r') as f:
#with open('/content/drive/MyDrive/Lagos Island ring road.txt', 'r') as f:
  lines = f.readlines()

points_x = lines[:-1]
points_y = lines[1:]
x_and_y = zip(points_x, points_y)

for x,y in x_and_y:
  x = ast.literal_eval(x)
  x = x[:-1]
  # flip long and lat to follow Google streetview format
  x = x[::-1]

  y = ast.literal_eval(y)
  y = y[:-1]
  # flip long and lat to follow Google streetview format
  y = y[::-1]
  #heading = calculate_heading(x, y)
  param = paramsGenerator(x, key)
  params.append(param)

print(params)
# Create a results object
results = google_streetview.api.results(params)

# Download images to directory 'downloads'
results.download_links('/content/drive/MyDrive/downloads')

from datasets import load_dataset

dataset = load_dataset("imagefolder", data_dir="/path/to/folder")
