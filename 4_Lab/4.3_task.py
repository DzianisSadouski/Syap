class Transport:
    def __init__(self, name, speed, cost_per_km):
        self.name = name
        self.speed = speed
        self.cost_per_km = cost_per_km

    def move(self, distance):
        return distance / self.speed

    def transport_cost(self, distance):
        return distance * self.cost_per_km

class Airplane(Transport):
    def __init__(self):
        super().__init__("Самолет", 800, 5)

class Train(Transport):
    def __init__(self):
        super().__init__("Поезд", 120, 2)

class Car(Transport):
    def __init__(self):
        super().__init__("Автомобиль", 100, 3)

class TransportCompany:
    def __init__(self):
        self.transports = []

    def add_transport(self, transport):
        self.transports.append(transport)

    def fastest_trip(self, distance):
        if not self.transports:
            return "Нет доступных транспортных средств"

        fastest_transport = min(self.transports, key=lambda t: t.move(distance))
        time = fastest_transport.move(distance)
        cost = fastest_transport.transport_cost(distance)

        return f"Самый быстрый транспорт: {fastest_transport.name}, Время: {time:.2f} часа, Стоимость: {cost} руб."

    def most_economical_trip(self, distance):
        if not self.transports:
            return "Нет доступных транспортных средств"

        economical_transport = min(self.transports, key=lambda t: t.transport_cost(distance))
        time = economical_transport.move(distance)
        cost = economical_transport.transport_cost(distance)

        return f"Самая экономичная поездка: {economical_transport.name}, Время: {time:.2f} часа, Стоимость: {cost} руб."

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for transport in self.transports:
                file.write(f"{transport.name},{transport.speed},{transport.cost_per_km}\n")

# Пример использования
company = TransportCompany()
company.add_transport(Airplane())
company.add_transport(Train())
company.add_transport(Car())

print(company.fastest_trip(500))
print(company.most_economical_trip(500))
company.save_to_file("transport_info.txt")
