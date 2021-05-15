import json
import urllib.request
import matplotlib.pyplot as plt
# import turtle
# import time


def country_details(country_name):

    dates = []
    nr = [0]
    infected = [0]
    all_infected = [0]
    all_cases_per_million = [0]
    new_case_per_million = [0]
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    i = 1
    for p in data:
        if data[p]['location'] == country_name:

            for q in data[p]['data']:

                dates.insert(i, str(q['date']))
                infected.insert(i, q['new_cases'])
                all_infected.insert(i, q['total_cases'])
                new_case_per_million.insert(i, q['new_cases_per_million'])
                all_cases_per_million.insert(i, q['total_cases_per_million'])
                nr.insert(i, i)
                i += 1

            print("Kraj: " + data[p]['location'])
            print("Kontynent: " + data[p]['continent'])
            print("Populacja: " + str(data[p]['population']))
            print("Gęstość zaludnienia: " + str(data[p]['population_density']))
            print("Mediana wieku: " + str(data[p]['median_age']))
            print("PKB na osobe: " + str(data[p]['gdp_per_capita']))
            print("Osoby 65+: " + str(data[p]['aged_65_older']))
            print("Osoby 70+: " + str(data[p]['aged_70_older']))
            print("Śmiertelność sercowo-naczyniowa: " + str(data[p]['cardiovasc_death_rate']))
            print("Występowanie cukrzycy: " + str(data[p]['diabetes_prevalence']))
            print("Łóżka w szpiatalach na 1000 mieszkańców: " + str(data[p]['hospital_beds_per_thousand']))
            print("Średnia długość życia: " + str(data[p]['life_expectancy']))
            print("Wskaźnik Rozwoju Społecznego: " + str(data[p]['human_development_index']))

    plt.title('Ilość zakażeń')
    plt.xlabel('Dzień')
    plt.ylabel('Ilość')
    plt.plot(nr, infected, 'k')
    plt.show()

    plt.title('Całkowita ilość zakażeń')
    plt.xlabel('Dzień')
    plt.ylabel('Ilość')
    plt.plot(nr, all_infected, 'k')
    plt.show()

    plt.title('Ilość nowych zakażeń na milion mieszkańców')
    plt.xlabel('Dzień')
    plt.ylabel('Ilość')
    plt.plot(nr, new_case_per_million, 'k')
    plt.show()

    plt.title('Ilość wszystkich zakażeń na milion mieszkańców')
    plt.xlabel('Dzień')
    plt.ylabel('Ilość')
    plt.plot(nr, all_cases_per_million, 'k')
    plt.show()


if __name__ == '__main__':
    country = str(input())
    country_details(country_name=country)
