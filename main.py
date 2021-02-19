# -*- coding:utf-8 -*-
import DatasGet.datasgetting as data
import json
import pygal
from pygal.style import *

# Save data
data_original = data.get_data()
data_str = json.dumps(data.get_data(), sort_keys=True, indent=2)
try:
    with open("Data.json", "w+", encoding="utf8") as data_file:
        data_file.write(data_str)
except FileNotFoundError:
    open("Data.json", "w+")

# Visualization data
"""
Get the file content of Data.json
json.load(Data.json)
show world diagnosis figure - {
    data[0]["World"][0......]["Diagnosis"]
}
"""
# world diagnosis and deaths figures
diagnosis_deaths_world = []
world_diagnosis_number = []
world_deaths_number = []
for i in range(0, 101):
    world_name = list(data_original[0]["World"][i])[0]
    diagnosis_deaths_world.append(world_name)
    world_diagnosis_number.append(
        data_original[0]["World"][i][world_name]["Diagnosis"]
    )
    world_deaths_number.append(
        data_original[0]["World"][i][world_name]["Deaths"]
    )
# U.S diagnosis and deaths figures
us_diagnosis_deaths_places = []
us_diagnosis_number = []
us_deaths_number = []
for i in range(0, 58):
    places_name = list(data_original[1]["America"][i])[0]
    us_diagnosis_deaths_places.append(places_name)
    us_diagnosis_number.append(
        data_original[1]["America"][i][places_name]["Diagnosis"]
    )
    us_deaths_number.append(
        data_original[1]["America"][i][places_name]["Deaths"]
    )
# show
"""
World diagnosis
World deaths
America diagnosis
America deaths
"""
# World diagnosis and deaths
world_diagnosis_bar = pygal.Bar(style=DarkStyle)
world_diagnosis_bar.title = "World diagnosis in covid-19"
world_diagnosis_bar.x_labels = diagnosis_deaths_world
world_diagnosis_bar.add("Diagnosis", world_diagnosis_number)
world_diagnosis_bar.render_to_file("DataSave/World/World diagnosis.svg")
world_deaths_bar = pygal.Bar(style=DarkStyle)
world_deaths_bar.title = "World Deaths in covid-19"
world_deaths_bar.x_labels = diagnosis_deaths_world
world_deaths_bar.add("Deaths", world_deaths_number)
world_deaths_bar.render_to_file("DataSave/World/World deaths.svg")
# America diagnosis and deaths
usa_diagnosis_bar = pygal.Bar(style=DarkStyle)
usa_diagnosis_bar.title = "U.S. diagnosis in covid-19"
usa_diagnosis_bar.x_labels = us_diagnosis_deaths_places
usa_diagnosis_bar.add("Diagnosis", us_diagnosis_number)
usa_diagnosis_bar.render_to_file("DataSave/U.S/U.S diagnosis.svg")
usa_deaths_bar = pygal.Bar(style=DarkStyle)
usa_deaths_bar.title = "U.S deaths in covid-19"
usa_deaths_bar.x_labels = us_diagnosis_deaths_places
usa_deaths_bar.add("Deaths", us_deaths_number)
usa_deaths_bar.render_to_file("DataSave/U.S/U.S deaths.svg")
