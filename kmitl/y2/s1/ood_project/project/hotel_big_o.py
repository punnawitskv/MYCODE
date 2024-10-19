import time
import sys

class Hotel:
    def __init__(self):
        self.guests = {}

    def add_guest(self, num_old_guests, num_guests_per_car, num_cars_per_ship, num_ships_per_army, num_armies_per_spaceship):
        self.guests.clear()  
        start_time = time.time()
        total_guests = num_old_guests + num_guests_per_car * num_cars_per_ship * num_ships_per_army * num_armies_per_spaceship

        if total_guests <= 0:
            print("Total guests must be greater than zero.")
            return

        for i in range(total_guests):
            old_guess_no = i
            guess_no = i % num_guests_per_car
            car_no = (i // num_guests_per_car) % num_cars_per_ship
            ship_no = (i // (num_guests_per_car * num_cars_per_ship)) % num_ships_per_army
            army_no = (i // (num_guests_per_car * num_cars_per_ship * num_ships_per_army)) % num_armies_per_spaceship

            if i >= num_old_guests:
                room_num = (2 ** guess_no) * (3 ** car_no) * (5 ** ship_no) * (7 ** army_no) * (11 ** 1)
                vehicle = [0, guess_no + 1, car_no + 1, ship_no + 1, army_no + 1]
            else:
                room_num = (2 ** old_guess_no) * (11 ** 0)
                vehicle = [1, 0, 0, 0, i + 1]

            self.guests[room_num] = vehicle  

        print(f"Time taken for 'add_guest': {(time.time() - start_time) * 1000:.15f} ms")

    def quickSort(self, guests):
        guests_list = list(guests.items())  
        self.qSort(guests_list, 0, len(guests_list) - 1)
        return dict(guests_list) 

    def qSort(self, guests_list, left, right):
        if left < right:
            p = self.partition(guests_list, left, right)
            self.qSort(guests_list, left, p - 1)
            self.qSort(guests_list, p + 1, right)

    def partition(self, guests_list, left, right):
        pivot = guests_list[left][0]  
        i = left + 1
        j = right

        while True:
            while i <= j and guests_list[i][0] <= pivot:
                i += 1
            while i <= j and guests_list[j][0] >= pivot:
                j -= 1
            if i <= j:
                guests_list[i], guests_list[j] = guests_list[j], guests_list[i]
            else:
                break

        guests_list[left], guests_list[j] = guests_list[j], guests_list[left]
        return j

    def show_all_guests(self):
        start_time = time.time()
        if not self.guests:
            print("No guests in the hotel.")
            return
        
        print("Current guests in the hotel (sorted by room number):")
        sorted_guests = self.quickSort(self.guests)  
        for room_num, vehicle in sorted_guests.items():
            vehicle_str = ", ".join(map(str, vehicle))
            print(f"Room : {room_num} Vehicles : [{vehicle_str}]")

        print(f"Time taken for 'show_all_guests': {time.time() - start_time:.15f} seconds")

    def remove_guest(self, room_number):
        start_time = time.time()
        if room_number in self.guests:
            del self.guests[room_number]
            print(f"Guest in room {room_number} removed.")
        else:
            print(f"No guest found in room {room_number}.")

        print(f"Time taken for 'remove_guest': {time.time() - start_time:.15f} seconds")

    def show_vacant_rooms(self):
        start_time = time.time()
        if not self.guests:
            print("No occupied rooms, all rooms are vacant.")
            return

        max_room_number = max(self.guests.keys())
        occupied_rooms = set(self.guests.keys())
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
        start_time = time.time() 
        if room_number in self.guests:
            vehicle_str = ", ".join(map(str, self.guests[room_number]))
            print(f"Guest in room {room_number}: Vehicles: [{vehicle_str}]")
        else:
            print(f"No guest found in room {room_number}.")

        print(f"Time taken for 'search_room': {time.time() - start_time:.15f} seconds")

    def add_manual(self, room_number):
        start_time = time.time()
        if room_number in self.guests:
            print("The room is already occupied")
        else:
            self.guests[room_number] = ["manual"]  
        print(f"Time taken for 'add_manual': {time.time() - start_time:.15f} seconds")

    def make_file(self, filename='hotel_guests.txt'):
        print("making file")
        try:
            with open(filename, 'w') as file:
                if not self.guests:
                    file.write("No guests in the hotel.\n")
                else:
                    file.write("Current guests in the hotel (sorted by room number):\n")
                    sorted_guests = self.quickSort(self.guests)
                    for room_num, vehicle in sorted_guests.items():
                        vehicle_str = ", ".join(map(str, vehicle))
                        file.write(f"Room {room_num}: Vehicles: [{vehicle_str}]\n")
            print(f"Data successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

hotel = Hotel()
while True:
    action = input("\nType\n'add : a'\t'add_manual : am'\t'remove_manual : rm'\t'vacant : v'\n'search : s'\t'make_file : mf'\t'memory : m'\t\t'stop : st'\n: ").lower()

    if action == 'stop' or action == 'st':
        break

    elif action == 'make_file' or action == 'mf':
        hotel.make_file()

    elif action == 'add' or action == 'a':
        inp = input("Input (format : old_guests guests_per_car cars_per_ship ships_per_army armies_per_spaceship)\n: ")
        try:
            num_old_guest, num_guests_per_car, num_cars_per_ship, num_ships_per_army, num_armies_per_spaceship = map(int, inp.split(' '))
            hotel.add_guest(num_old_guest, num_guests_per_car, num_cars_per_ship, num_ships_per_army, num_armies_per_spaceship)
            hotel.show_all_guests()

        except ValueError:
            print("Invalid input format. Please enter numbers separated by spaces.")

    elif action == 'remove_manual' or action == 'rm':
        try:
            room_number = int(input("Enter the room number to remove the guest: "))
            hotel.remove_guest(room_number)
            hotel.show_all_guests()
        except ValueError:
            print("Invalid room number. Please enter a valid number.")

    elif action == 'add_manual' or action == 'am':
        try:
            room_number = int(input("Enter the room number you wish to stay in: "))
            hotel.add_manual(room_number)
            hotel.show_all_guests()
        except ValueError:
            print("Invalid room number. Please enter a valid number.")

    elif action == 'vacant' or action == 'v':
        hotel.show_vacant_rooms()

    elif action == 'memory' or action == 'm':
        hotel.show_memory_usage()

    elif action == 'search' or action == 's':
        try:
            room_number = int(input("Enter the room number to search for: "))
            hotel.search_room(room_number)
        except ValueError:
            print("Invalid room number. Please enter a valid number.")

    else:
        print("Invalid action. Please enter a valid command.")