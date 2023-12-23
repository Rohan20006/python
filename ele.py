comment=""
started=False
while True:
    comment=input("> ").lower()
    if comment == 'start':
        if started:
            print("Car Alledy stared.")
        else:
            started= True
            print("Car stared.........")  
    elif comment=='stop':
        if not started:
            print("Car Allredy stoped.")
        else:
            started=False
            print("Car stoped........... ")
    elif comment == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - quit the car.
""")
    elif comment == "quit":
        break
    else:
        print("Sorry i don't understant")