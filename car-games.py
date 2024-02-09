command = ""
started = False
print("""
        start--> Start the Car!
        stop--> stop the Car!
        quite--> quite from car
        """)

while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car already Started..")
            print("Enjoy Your Drive")
        else:
            started = True
            print("Car Started..")
            print("Enjoy Your Drive")
    elif command == "stop":
        if not started:
            print("Car already Stopped ")
            print("Take a Rest!")
        else:
            started = False
            print("Car Stopped")

    elif command == "help":
        print("""
        start--> Start the Car!
        stop--> stop the Car!
        quite--> quite from car
        """)
    elif command == "quite":
        break
    else:
        print("i don't understand!")
        break
