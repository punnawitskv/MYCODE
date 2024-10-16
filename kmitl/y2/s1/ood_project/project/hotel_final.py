import time
import sys

class Guest:
    def __init__(self, room_num, vehicle=None):
        self.room_num = room_num
        self.vehicle = vehicle

class Hotel:
    def __init__(self):
        self.guests = []

    def add_guest(self, num_guests_per_car, num_cars_per_ship, num_ships_per_army, num_armies_per_spaceship, count, total_old_guests):
        start_time = time.time()  
        total_guests = num_guests_per_car * num_cars_per_ship * num_ships_per_army * num_armies_per_spaceship

        if total_guests <= 0:
            print("Total guests must be greater than zero.")
            return

        for i in range(total_guests):
            guess_no = i % num_guests_per_car
            car_no = (i // num_guests_per_car) % num_cars_per_ship
            ship_no = (i // (num_guests_per_car * num_cars_per_ship)) % num_ships_per_army
            army_no = (i // (num_guests_per_car * num_cars_per_ship * num_ships_per_army)) % num_armies_per_spaceship
            
            room_num = (2 ** guess_no) * (3 ** car_no) * (5 ** ship_no) * (7 ** army_no)  * (11 ** count)+ total_old_guests
            vehicle = [total_old_guests+i+1, guess_no + 1, car_no + 1, ship_no + 1, army_no + 1]
            new_guest = Guest(room_num, vehicle)
            self.guests.append(new_guest)

        print(f"Time taken for 'search_room': {(time.time() - start_time) * 1000:.15f} ms")

    def show_all_guests(self):
        start_time = time.time()  # Start time tracking
        if not self.guests:
            print("No guests in the hotel.")
            return

        print("Current guests in the hotel (sorted by room number):")
        sorted_guests = sorted(self.guests, key=lambda g: g.room_num)
        for guest in sorted_guests:
            vehicle_str = ", ".join(map(str, guest.vehicle)) if guest.vehicle else "No vehicles"
            print(f"Room {guest.room_num}: Vehicles: [{vehicle_str}]")

        print(f"Time taken for 'show_all_guests': {time.time() - start_time:.15f} seconds")

    def remove_guest(self, room_number):
        start_time = time.time()  # Start time tracking
        found_guest = next((guest for guest in self.guests if guest.room_num == room_number), None)

        if found_guest:
            self.guests.remove(found_guest)
            print(f"Guest in room {room_number} removed.")
        else:
            print(f"No guest found in room {room_number}.")

        print(f"Time taken for 'remove_guest': {time.time() - start_time:.15f} seconds")

    def show_vacant_rooms(self):
        start_time = time.time()  # Start time tracking
        if not self.guests:
            print("No occupied rooms, all rooms are vacant.")
            return

        max_room_number = max(guest.room_num for guest in self.guests)
        occupied_rooms = set(guest.room_num for guest in self.guests)
        vacant_rooms = [room for room in range(1, max_room_number + 1) if room not in occupied_rooms]

        if vacant_rooms:
            print("Vacant rooms:", vacant_rooms)
        else:
            print("No vacant rooms up to room", max_room_number)

        print(f"Time taken for 'show_vacant_rooms': {time.time() - start_time:.15f} seconds")

    def show_memory_usage(self):
        memory_used = sys.getsizeof(self.guests)
        print(f"Memory used by 'guests': {memory_used} bytes")

    def search_room(self, room_number):
        """Search for a guest by room number and display their vehicle journey."""
        start_time = time.time()  # Start time tracking
        found_guest = next((guest for guest in self.guests if guest.room_num == room_number), None)

        if found_guest:
            vehicle_str = ", ".join(map(str, found_guest.vehicle))
            print(f"Guest in room {room_number}: Vehicles: [{vehicle_str}]")
        else:
            print(f"No guest found in room {room_number}.")

        print(f"Time taken for 'search_room': {time.time() - start_time:.15f} seconds")

    def reset(self, old_number_guests):
        self.guests = []
        for i in range(1, old_number_guests+1):
            room_num = i 
            vehicle = [i,0,0,0,0]
            new_guest = Guest(room_num, vehicle)
            self.guests.append(new_guest)

    def add_manual(self, room_number):
        start_time = time.time()  
        found_guest = next((guest for guest in self.guests if guest.room_num == room_number), None)
        if found_guest:
            print("The room is already occupied")
        else:
            guest = Guest(room_number,["manual"])
            self.guests.append(guest)
        

        print(f"Time taken for 'search_room': {time.time() - start_time:.15f} seconds")
        

    def make_file(self, filename='hotel_guests.txt'):
        print("making file")
        try:
            with open(filename, 'w') as file:
                if not self.guests:
                    file.write("No guests in the hotel.\n")
                else:
                    file.write("Current guests in the hotel (sorted by room number):\n")
                    sorted_guests = sorted(self.guests, key=lambda g: g.room_num)
                    for guest in sorted_guests:
                        vehicle_str = ", ".join(map(str, guest.vehicle)) if guest.vehicle else "No vehicles"
                        file.write(f"Room {guest.room_num}: Vehicles: [{vehicle_str}]\n")
            print(f"Data successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")


hotel = Hotel()
count = 0
total_old_guests = 0
while True:
    action = input("\nType 'reset', 'add', 'add_manual', 'remove_manual', 'vacant', 'search', 'memory', or 'stop': ").lower()
    
    if action == 'm':
        hotel.make_file()

    if action == 'stop':
        break
    
    if action == 'add':
        inp = input("Input (format: num_guests_per_car,num_cars_per_ship,num_ships_per_army,num_armies_per_spaceship): ")
        try:
            num_guests_per_car, num_cars_per_ship, num_ships_per_army, num_armies_per_spaceship = map(int, inp.split(','))
            hotel.add_guest(num_guests_per_car, num_cars_per_ship, num_ships_per_army, num_armies_per_spaceship, count, total_old_guests)
            hotel.show_all_guests()
            count += 1  # Increment count after each successful input
        except ValueError:
            print("Invalid input format. Please enter numbers separated by commas.")
    
    elif action == 'remove_manual':
        try:
            room_number = int(input("Enter the room number to remove the guest: "))
            hotel.remove_guest(room_number)
            hotel.show_all_guests()
        except ValueError:
            print("Invalid room number. Please enter a valid number.")

    elif action == 'reset':  
        try:
            old_number_guests = int(input("Enter the original number of guests: "))
            hotel.reset(old_number_guests)  
            hotel.show_all_guests()
            total_old_guests = old_number_guests
        except ValueError:
            print("Please enter a valid number.")

    elif action == 'add_manual':  
        try:
            room_number = int(input("Enter the room number you wish to stay in: "))
            hotel.add_manual(room_number) 
            hotel.show_all_guests()
        except ValueError:
            print("Invalid room number. Please enter a valid number.")
        

    elif action == 'vacant':
        hotel.show_vacant_rooms()

    elif action == 'memory':
        hotel.show_memory_usage()

    elif action == 'search':
        try:
            room_number = int(input("Enter the room number to search for: "))
            hotel.search_room(room_number)
        except ValueError:
            print("Invalid room number. Please enter a valid number.")