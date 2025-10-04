class Allocation:
    def __init__(self, num_of_seats):
        self.num_of_seats = num_of_seats
        self.seat_list = []
    def add_seat(self, seat_id):
        self.seat_list.append(seat_id)

class BookingSolution:
    def __init__(self, title, rows, seats_per_row):
        self.title = title
        if rows > 26:
            raise Exception ( f" rows:{rows} higher than max supported:26")
        if seats_per_row > 50:
            raise Exception ( f" seats per row:{seats_per_row} higher than max supported:50")
        self.rows_max = rows
        self.seats_in_row = seats_per_row
        self.build_matrix(self.rows_max, self.seats_in_row)
        self.remaining = self.rows_max * self.seats_in_row
        self.booking_number = 1
        self.booking_map = {}
        self.reserve_map = {}

    def build_matrix(self, rows, seats):
        self.bookingMatrix = []
        for _ in range(rows):
            self.bookingMatrix.append([-1]*seats)

    def get_row_seat(self, input_choice):
        row = self.rows_max - (ord(input_choice[0]) - ord('A') + 1)
        seat_str = input_choice[1:]
        if len(seat_str) == 3:
            seat = int(seat_str) - 1
            return row, seat
        else:
            return row, -1

    def validate_choice(self, input_choice):
        row, seat = self.get_row_seat(input_choice)
        if row > self.rows_max or seat < 0 or seat > self.seats_in_row:
            return False
        return True

    def allocate(self, num_tickets, input_choice = None):
        allocation = Allocation(num_tickets)
        if input_choice:
            row, seat = self.get_row_seat(input_choice)
        else:   
            row = self.rows_max - 1
            seat = (self.seats_in_row - num_tickets) // 2
        while self.bookingMatrix[row][seat] != -1:
            seat += 1
            if seat > self.seats_in_row:
                row -= 1
                seat = 0
        end = seat + num_tickets 
        # print(f"\t\t selecting for row:{row} number of seats:{num_tickets}")
        for _ in range(seat, end):
            if seat >= self.seats_in_row:
                row -= 1
                seat = 0
            while self.bookingMatrix[row][seat] != -1:
                seat += 1
            allocation.add_seat((row, seat))
            self.bookingMatrix[row][seat] = 1
            seat += 1
        # print(f"\t\t allocation:{allocation.num_of_seats} - seats={allocation.seat_list}")
        return allocation
    
    def unallocate(self, seat_list:list):
        for row, seat_no in seat_list:
            self.bookingMatrix[row][seat_no] = -1

    def reserve(self, num_tickets_req):
        current_booking_number = self.booking_number
        self.booking_number += 1
        booking_id = f"KID{current_booking_number:03d}"
        allocation = self.allocate(num_tickets_req)
        self.reserve_map[booking_id] = allocation 
        return booking_id

    def change_reserve(self, booking_id, input_choice):
        current_allocation = self.reserve_map[booking_id]
        self.unallocate(current_allocation.seat_list)
        new_allocation = self.allocate(current_allocation.num_of_seats, input_choice)
        self.reserve_map[booking_id] = new_allocation

    def get_reserve_matrix(self):
        return self.bookingMatrix

    def confirm_current_proposal(self, booking_id):
        self.booking_map[booking_id] = self.reserve_map[booking_id]
        del self.reserve_map[booking_id]
        for row, col in self.booking_map[booking_id].seat_list:
            self.bookingMatrix[row][col] = 0

class InputHandlers:
    def __init__(self):
        self.booking_solution = None
    def handle_booking_workflow_tendem(self, num_tickets_req):
        input_choice = None
        booking_id = self.booking_solution.reserve(num_tickets_req)
        print(f"Successfully reserved {num_tickets_req} {self.booking_solution.title} tickets.")
        while True:
            print(f"Booking Id:{booking_id}")
            if input_choice:
                self.booking_solution.change_reserve(booking_id, input_choice)
            self.display_reserve_matrix()
            input_choice = input("Enter blank to accept seat selection, enter new seating position:\n>")
            if len(input_choice) == 0:
                self.booking_solution.confirm_current_proposal(booking_id)
                print(f"Booking id: {booking_id} confirmed.\n")
                break
            else:
                is_valid = self.booking_solution.validate_choice(input_choice)
                if not is_valid:
                    input_choice = None
                    continue

    def display_reserve_matrix(self, allocation: Allocation = None):
        rows = self.booking_solution.rows_max
        seats = self.booking_solution.seats_in_row
        print(f"{' ' * (seats // 2)} S C R E E N {' ' * (seats // 2)}")
        print(f" {'-' * (seats + 3) * 2} ")
        for row in range(rows):
            row_id = chr(ord('A') + (rows - (1 + row)) )
            print(f" {row_id} ", end = "")
            for seat in range(seats):
                if allocation :
                    if (row, seat) in allocation.seat_list:
                        seat_val = "XO-"[1]
                    else:
                        seat_val = "XO-"[-1]
                else:
                    seat_val = "XO-"[self.booking_solution.bookingMatrix[row][seat]]
                print(f" {seat_val}", end = "")
            print(" ")
        print(f"   ", end = "")
        for seat in range(1, seats + 1):
            print(f" {seat}", end = "")
        print("\n")

    def handle_top_choice(self, title, remaining: int):
        print(f"Welcome to KID Cinemas")
        print(f"[1] Book tickets for {title} ({remaining} seats available)")
        print(f"[2] Check bookings")
        print(f"[3] Exit")
        data = input(f"Please enter your selection:\n>")
        return data

    def run_checking_workflow(self):
        while True:
            booking_id = input(f"Enter booking id, or enter blank to go back to main menu:\n>")
            if len(booking_id) > 0:
                if booking_id not in self.booking_solution.booking_map.keys():
                    print(f"\t\t bookings:{self.booking_solution.booking_map}")
                    print(f"booking id does not exist, please give valid booking id:\n>")
                    continue
                else:
                    self.display_reserve_matrix(self.booking_solution.booking_map[booking_id])
            else:
                return -1

    def run_ticket_booking_workflow(self, remaining: int):
        while True:
            to_book_tickets = input(f"Enter number of tickets to book, or enter blank to go back to main menu:\n>")
            if len(to_book_tickets) > 0:
                num_tickets_req = int(to_book_tickets)
                if num_tickets_req <= remaining:
                    self.handle_booking_workflow_tendem(num_tickets_req)
                else:
                    print(f"Requested Tickets:{num_tickets_req} is more than available:{remaining}")
                    continue
            else:
                return -1
    def handle_cinema_layout(self):
        while True:
            input_data = input(f'Please define movie title and seating map in [Title] [Row] [Seats Per Row] format:\n>')
            try:
                input_splits = input_data.split(" ")
                seats_per_row = int(input_splits[-1])
                rows = int(input_splits[-2])
                separator = " "
                title = separator.join(input_splits[:-2])
            except:
                print("input:{input_data} does not confirm to the expected format:'title rows seats_per_row'")
                continue
            return title, rows, seats_per_row

def run():
    ih = InputHandlers()
    title, row, seats_per_row = ih.handle_cinema_layout()
    bs = BookingSolution(title, row, seats_per_row)
    ih.booking_solution = bs
    while True:
        data = ih.handle_top_choice(bs.title, bs.remaining)
        if data == '3':
            break
        if data == '1':
            user_input = ih.run_ticket_booking_workflow(bs.remaining)
            print(f"user_input:{user_input}")
        if data == '2':
            ih.run_checking_workflow()
    
if __name__ == "__main__":
    run()

