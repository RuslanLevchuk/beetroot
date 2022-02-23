def make_country(**country_capital):
    for country, capital in country_capital.items():
        print(f"The capital of {country.title()} is {capital.title()}")



make_country(ukraine = 'kyiv', mordor = 'moscow', ethopia = 'addis ababa', japan = 'Tokyo')