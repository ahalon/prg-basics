class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1 
        self.channels = [] 
        self.volume = 0 
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def set_channel(self, new_channel_no):
        if new_channel_no > 0 and new_channel_no <= len(self.channels):
            self.channel_no = new_channel_no
            print(f"Channel changed to {self.channels[self.channel_no - 1]}")
        else:
            print("Invalid channel number. Please select a valid channel.")
    
    def set_channels(self, channels_list):
        self.channels = channels_list
        print("Channels have been set.")
    
    def show_channels(self):
        if self.channels:
            print("Channel list:")
            for idx, channel in enumerate(self.channels, start=1):
                print(f"{idx}. {channel}")
        else:
            print("No channels available. Please set channels first.")
    
    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
            print(f"Volume increased to {self.volume}")
        else:
            print("Volume is already at maximum (10).")
    
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume decreased to {self.volume}")
        else:
            print("Volume is already at minimum (0).")
    
    def show_status(self):
        if self.is_on:
            if 0 < self.channel_no <= len(self.channels):
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), Volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no}, Volume {self.volume}")
        else:
            print("TV is off")