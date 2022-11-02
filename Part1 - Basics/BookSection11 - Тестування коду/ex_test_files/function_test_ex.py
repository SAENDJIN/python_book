# 11-1 - Місто, країна

def city_country(city, country):
    """Приймає два параметри місто та країна,
     та повертає один стрінг 'Місто, Країна'. """

    return f"{city.title()}, {country.title()}"


print(city_country('santiago', 'chile'))


# 11-2 - Населення

def city_country_population(city, country, population=0):
    """Приймає два параметри місто та країна,
     та повертає один стрінг 'Місто, Країна'. """

    return f"{city.title()}, {country.title()} - {population}"
