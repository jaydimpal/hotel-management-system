## HOTEL MANAGEMENT SYSTEM PROJECT

# 1. ROOM INVENTORY: 5 rooms with bed types, daily rates, max guest capacity, and status
# Format: Room Number -> [Room Type, Per Day Price, Max Capacity, Status / Booking Info]
rooms = {
    101: ["Single Bed", 50, 1, "Available"],
    102: ["Double Bed", 80, 2, "Available"],
    201: ["Double Bed", 80, 2, "Available"],
    202: ["Family Suite", 140, 4, "Available"],
    301: ["Luxury Suite", 220, 5, "Available"]
}

# 1. SHOW ALL ROOMS
def view_all_rooms():
    print("\n--- ALL ROOMS STATUS ---")
    # Loop through every item in the dictionary using rooms.items()
    for room_no, info in rooms.items():
        # Unpack details into readable variable names
        room_type = info[0]
        price = info[1]
        capacity = info[2]
        availability = info[3]
        
        # 2. USE OF IF / ELSE STATEMENT TO CHECK availability
        if availability == "Available":
            print(f"Room {room_no} | {room_type} | ${price}/day | Max Guests: {capacity} -> AVAILABLE")
        else:
            # Display who booked it
            guest_name = availability["name"]
            print(f"Room {room_no} | {room_type} | ${price}/day -> BOOKED BY: {guest_name}")

# 2. CHECK AVAILABLE ROOMS ONLY
def check_availability():
    print("\n--- AVAILABLE ROOMS ONLY ---")
    # Set a counter variable
    count = 0
    
    # Loop through rooms.items()
    for room_no, info in rooms.items():
        # Check if info[3] (availability) is "Available"
        if info[3] == "Available":
            print(f"✅ Room {room_no} ({info[0]}) - ${info[1]}/day (Max Guests: {info[2]})")
            # Add 1 to count
            count += 1
            
    # After loop finishes, check if count == 0
    if count == 0:
        print("Sorry, no rooms are currently free!")
    else:
        print(f"\nTotal rooms free: {count}")

# 3. GUEST BOOKINGS
def book_room():
    print("\n--- NEW GUEST BOOKING ---")
    try:
        room_no = int(input("Enter room number to book: "))
    except ValueError:
        print("Please enter a valid numeric room number.")
        return

    # Check room existence
    if room_no not in rooms:
        print("Room number not found in hotel inventory!")
        return

    # Check room availability
    if rooms[room_no][3] != "Available":
        print(f"Room {room_no} is already taken!")
        return

    # Check room capacity
    max_capacity = rooms[room_no][2]
    try:
        guest_count = int(input(f"Enter guest count (Max {max_capacity}): "))
    except ValueError:
        print("Invalid guest count.")
        return

    if guest_count <= 0 or guest_count > max_capacity:
        print(f"Booking failed! Room {room_no} can only hold up to {max_capacity} guests.")
        return

    # Check valid stay dates
    try:
        stay_days = int(input("Enter number of stay days: "))
        if stay_days <= 0:
            print("Invalid stay dates! Duration must be at least 1 day.")
            return
    except ValueError:
        print("Invalid number of days.")
        return

    # Record guest details
    name = input("Enter guest full name: ").strip()
    phone = input("Enter contact phone number: ").strip()

    # Save details into the room status slot
    rooms[room_no][3] = {
        "name": name,
        "phone": phone,
        "guests": guest_count,
        "days": stay_days
    }
    
    print(f"\nSuccess! Room {room_no} booked for {name} for {stay_days} day(s).")

# 4. CHECKOUT AND BILLING (VERY SIMPLE & HAND-TYPED STYLE)
def checkout_and_billing():
    print("\n--- CHECKOUT & BILLING ---")
    try:
        room_no = int(input("Enter room number: "))
    except ValueError:
        print("Please enter a valid room number.")
        return

    # Check if the room exists and is actually booked
    if room_no not in rooms or rooms[room_no][3] == "Available":
        print("This room is not currently booked!")
        return

    # Get stored booking info
    guest = rooms[room_no][3]
    price = rooms[room_no][1]
    
    # Calculate bill: price per day * total days
    days = guest["days"]
    total = price * days

    # Print simple receipt
    print("\n--- BILL RECEIPT ---")
    print("Guest Name:", guest["name"])
    print("Phone Number:", guest["phone"])
    print("Days Stayed:", days)
    print("Price Per Day: $", price)
    print("Total Bill: $", total)
    print("-------------------")

    # Clear room booking
    rooms[room_no][3] = "Available"
    print("Checkout complete. Room is free again.")

# MAIN PROGRAM MENU LOOP
while True:
    print("\n================================")
    print("     HOTEL MANAGEMENT SYSTEM    ")
    print("================================")
    print("1. View All Rooms")
    print("2. Check Available Rooms Only")
    print("3. Book a Room")
    print("4. Checkout & Billing")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ").strip()
    
    if choice == "1":
        view_all_rooms()
    elif choice == "2":
        check_availability()
    elif choice == "3":
        book_room()
    elif choice == "4":
        checkout_and_billing()
    elif choice == "5":
        print("Exiting project. Thank you!")
        break
    else:
        print("Invalid choice! Please choose 1 to 5.")