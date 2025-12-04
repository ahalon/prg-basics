class Phone:
    def __init__(self, battery_level=100, screen_on=False, connected_to_network=False):
        self.battery_level = battery_level  
        self.screen_on = screen_on         
        self.connected_to_network = connected_to_network 

    def charge(self, amount):
        """Charge the phone by a specified amount."""
        self.battery_level += amount
        if self.battery_level > 100:  
            self.battery_level = 100
        print(f"Charging... Battery is now at {self.battery_level}%")

    def turn_on_screen(self):
        """Turn on the phone's screen."""
        self.screen_on = True
        print("Screen is now ON.")

    def connect_to_network(self):
        """Connect the phone to a network."""
        self.connected_to_network = True
        print("Phone is now connected to a network.")

    def display_info(self):
        """Display the current state of the phone."""
        screen_status = "ON" if self.screen_on else "OFF"
        network_status = "Connected" if self.connected_to_network else "Disconnected"
        print(f"Phone Info:")
        print(f"Battery level: {self.battery_level}%")
        print(f"Screen: {screen_status}")
        print(f"Network: {network_status}")

def main():
    my_phone = Phone(battery_level=50)

    my_phone.display_info()

    my_phone.charge(20) 
    my_phone.turn_on_screen() 
    my_phone.connect_to_network()

    my_phone.display_info()

if __name__ == "__main__":
    main()
