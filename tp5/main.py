
class Airport:
    def __init__(self):
        self.military_planes = []
        self.cargo_planes = []
        self.civil_planes = []
    
    def add_military(self, plane):
        self.military_planes.append(plane)
        
    def add_cargo(self, plane):
        self.cargo_planes.append(plane)
        
    def add_civil(self, plane):
        self.civil_planes.append(plane)
        
        
    def __str__(self):
        result = "[Airport]\n"
        
        for plane in self.military_planes:
            result += str(plane) + "\n"
            
        for plane in self.cargo_planes:
            result += str(plane) + "\n"
            
        for plane in self.civil_planes:
            result += str(plane) + "\n"
    
        return result







class Airplane:
    def __init__(self, name: str):
        self._fly = False
        self.name = name
    
    def take_off(self):
        if self._fly:
            raise ValueError("The plane is already flying")
        self._fly = True
    
    def land(self):
        if self._fly:
            raise ValueError("The plane is already at land")
        self._fly = False
    
    def __str__(self):
        state = "flying" if self._fly else "ground"
        return f"{self.name} - state : {state} "
        
        

class MilitaryAircraft(Airplane):
    def __init__(self, name : str):
        super().__init__(name)
        self.mission = None
    
        
    def __str__(self):
        if self.mission:
            mission = f"{self.mission}"
        else:
            mission = "no mission"
        return f"Military aircraft {super().__str__()} - {mission}"
        
        
        
class CargoAircraft(Airplane):
    def __init__(self, name : str):
        super().__init__(name)
        self.shipment = None
    
    
    def __str__(self):
        if self.shipment:
            shipment = f"contains {self.shipment}"
        else:
            shipment = "no shipment"
        return f"Cargo aircraft {super().__str__()} - {shipment}"




class CivilAircraft(Airplane):
    def __init__(self, name : str):
        super().__init__(name)
        self.nb_passenger = 0
        
        
    def passenger_enter(self, nb: int):
        if nb <= 0:
            raise ValueError("The number of passengers must be positive")
        self.nb_passenger += nb

    def passenger_leave(self, nb: int):
        if nb <= 0:
            raise ValueError("The number of passengers must be positive")
        if nb:
            raise ValueError("There is already no passenger left")
        self.nb_passenger -= nb
    
    def __str__(self):
        if self.nb_passenger == 0:
            passengers = "no passengers"
        else:
            passengers = f"{self.nb_passenger} passengers"
        return f"Civil aircraft {super().__str__()} - {passengers}"


if __name__ == "__main__":
    
    airport = Airport()

    plane_civil = CivilAircraft("Airbus A320")
    plane_cargo = CargoAircraft("Boeing 747 Cargo")
    plane_military = MilitaryAircraft("Rafale")

    print(plane_civil)
    print(plane_cargo)
    print(plane_military)

    airport.add_civil(plane_civil)
    airport.add_cargo(plane_cargo)
    airport.add_military(plane_military)

    plane_civil.passenger_enter(150)
    plane_civil.take_off()

    plane_military2 = MilitaryAircraft("Rescue Plane") 
    plane_military2.mission = "rescue hostages"
    plane_military2.take_off()
    airport.add_military(plane_military2)

    print(airport)
    







