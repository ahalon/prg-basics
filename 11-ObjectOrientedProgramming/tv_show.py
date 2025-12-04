import tv

def main():
    my_tv = tv.TV()
    
    print("Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery, BBC")
    my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "BBC"])
    
    print("Display the list of available channels:")
    my_tv.show_channels()  
    
    print("Turn TV on:")
    my_tv.turn_on()
    my_tv.show_status()  
    
    print("Increase volume:")
    my_tv.increase_volume()  
    my_tv.increase_volume() 
    my_tv.show_status()  
    
    print("Decrease volume:")
    my_tv.decrease_volume()  
    my_tv.decrease_volume()  
    my_tv.show_status()  
    
    print("Try to increase volume beyond limit:")
    for _ in range(15):  
        my_tv.increase_volume()  
    my_tv.show_status()  
    
    print("Turn TV off:")
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
