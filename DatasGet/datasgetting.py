# -*- coding:utf-8 -*-
# @Time:     2021/2/13 10:46
# @Author:   Top Programmer - Hacker(Administrator)
# @Software: PyCharm
from DatasGet.urlgets import *


def get_really_number(str_num):
    return int(str_num.replace(",", ""))


def get_data():
    countries = x_paths("//tr/td/span/text()")
    diagnosis = x_paths("//tr/td[@class=\"table_card_cell_col_1 table"
                        "_card_cell_int_type\"]/text()")
    usa_places = []
    usa_diagnosis = []
    usa_deaths = x_paths("//tr/td[@class=\"table_card_cell_col_2 table"
                         "_card_cell_float_type\"]/text()")
    for i in range(0, 58):
        usa_places.append(countries[158 - i])
        usa_diagnosis.append(diagnosis[158 - i])
        del countries[158 - i]
        del diagnosis[158 - i]
    usa_diagnosis.reverse()
    usa_places.reverse()
    deaths = x_paths("//tr/td[@class=\"table_card_cell_col_4 table_"
                     "card_cell_int_type\"]/text()")
    Data = [{"World": []
             }, {
                "America": []
            }]
    """
    The confirmed cases and deaths in the world are part of it.
    The confirmed and dead cases in the United States are part of this.
    world - {
        Country - {
            Diagnosis - world of diagnosis bodies,
            Deaths - world of deaths bodies
        }
        ......
    },
    America - {
        Place - {
            Diagnosis - Number of confirmed cases in the area,
            Deaths - Death toll in the area
        }
        ......
    }
    """
    # Number of confirmed cases and deaths in the world.
    for i in range(0, 101):
        Data[0]["World"].append({
            countries[i]: {
                "Diagnosis": get_really_number(diagnosis[i]),
                "Deaths": get_really_number(deaths[i])
            }
        })
    # Number of confirmed cases and deaths in the U.S.A.
    for i in range(0, len(usa_places)):
        Data[1]["America"].append({
            usa_places[i]: {
                "Diagnosis": get_really_number(usa_diagnosis[i]),
                "Deaths": get_really_number(usa_deaths[i])
            }
        })
    return Data
