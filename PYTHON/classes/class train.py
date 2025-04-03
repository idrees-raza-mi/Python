class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare
        self.booked_seats = 0

    def book_ticket(self):
        if self.booked_seats < self.seats:
            self.booked_seats += 1
            print("Ticket booked successfully!")
        else:
            print("No seats available!")

    def get_status(self):
        print(f"Train: {self.name}, Seats available: {self.seats - self.booked_seats}")

    def get_fare_info(self):
        print(f"Fare per ticket: {self.fare}")

# Example usage
train = Train("Express", 100, 150)
train.book_ticket()
train.get_status()
train.get_fare_info()