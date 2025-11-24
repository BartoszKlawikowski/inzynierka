class Drink:
    """Represents a drink and its pure alcohol grams."""
    def __init__(self, name: str, volume_ml: float, alcohol_percent: float):
        self.name = name
        self.volume_ml = volume_ml
        self.alcohol_percent = alcohol_percent
        self.alcohol_grams = self.calculate_alcohol_grams(volume_ml, alcohol_percent)

    @staticmethod
    def calculate_alcohol_grams(volume_ml, alcohol_percent) -> float:
        """Calculate grams of pure alcohol."""
        pure_ml = volume_ml * (alcohol_percent / 100.0)
        return pure_ml * 0.789  # alcohol density g/ml

class BeerBig(Drink):
    def __init__(self):
        super().__init__(name="Piwo Duze", volume_ml=500, alcohol_percent=5)

class BeerSmall(Drink):
    def __init__(self):
        super().__init__(name="Piwo Male", volume_ml=250, alcohol_percent=5)

class Vine(Drink):
    def __init__(self):
        super().__init__(name="Wino", volume_ml=200, alcohol_percent=15)

class Vodka(Drink):
    def __init__(self):
        super().__init__(name="Alkohol mocny", volume_ml=50, alcohol_percent=40)

def agregate(analyzed_drinks):
    # Agregate duplications
    aggregated = {}
    for drink in analyzed_drinks:
        czas = drink['czas']
        alcohol = drink['alcohol_grams']
        if czas in aggregated:
            aggregated[czas] += alcohol
        else:
            aggregated[czas] = alcohol

    merged_drinks = [{'czas': czas, 'alcohol_grams': alcohol} for czas, alcohol in aggregated.items()]
    return merged_drinks

def calculate_can_drive(drinks):
    analyzed_drinks=[]
    for drink in drinks:
        if drink["rodzaj"] == "1":
            rodzaj = BeerBig()
        elif drink["rodzaj"] == "2":
            rodzaj = BeerSmall()
        elif drink["rodzaj"] == "3":
            rodzaj = Vine()
        elif drink["rodzaj"] == "4":
            rodzaj = Vodka()
        else:
            rodzaj = None
            continue
        analyzed_drinks.append(
            {
                "alcohol_grams": rodzaj.alcohol_grams,
                "czas": drink["czas"],
            }
        )

    analyzed_drinks_after_agregation = agregate(analyzed_drinks)
    sorted_analyzed_drinks_after_agregation = sorted(analyzed_drinks_after_agregation, key=lambda x: x['czas'], reverse=True)

    #Measurements
    time_counter = sorted_analyzed_drinks_after_agregation[0]["czas"]
    alcohol_grams = sorted_analyzed_drinks_after_agregation[0]["alcohol_grams"]
    for minute in range(time_counter):
        time_counter = time_counter - 1
        # sprawdzamy czy zostal spozyty dodatkowy alkochol
        for _ in sorted_analyzed_drinks_after_agregation:
            if _["czas"] == time_counter:
                alcohol_grams = alcohol_grams + _["alcohol_grams"]
        alcohol_grams = alcohol_grams - 0.18
        if alcohol_grams < 0:
            alcohol_grams = 0

    return alcohol_grams


# drinks = [
#     {'rodzaj': '2', 'czas': 120},
#     {'rodzaj': '2', 'czas': 90},
#     {'rodzaj': '2', 'czas': 60},
#     {'rodzaj': '2', 'czas': 60},
# ]

# print(calculate_can_drive(drinks))