import struct
import matplotlib.pyplot as plt
import webbrowser

# Key mapping constants
KEY_K1 = 1 << 0
KEY_K2 = 1 << 1
KEY_M1 = 1 << 2
KEY_M2 = 1 << 3

def parse_osr_file(file_path):
    with open(file_path, 'rb') as f:
        f.read(36)  

        key_press_events = []
        key_hold_times = {KEY_K1: [], KEY_K2: [], KEY_M1: [], KEY_M2: []}
        key_press_start = {KEY_K1: None, KEY_K2: None, KEY_M1: None, KEY_M2: None}
        prev_timestamp = 0

        while True:
            # Read the next event's time difference
            time_diff_bytes = f.read(4)
            if len(time_diff_bytes) < 4:
                break
            time_diff = struct.unpack('<i', time_diff_bytes)[0]

            # Read the rest of the event data
            x_bytes = f.read(4)
            y_bytes = f.read(4)
            keys_bytes = f.read(2)
            if len(x_bytes) < 4 or len(y_bytes) < 4 or len(keys_bytes) < 2:
                break

            x = struct.unpack('<f', x_bytes)[0]
            y = struct.unpack('<f', y_bytes)[0]
            keys = struct.unpack('<H', keys_bytes)[0]

            timestamp = prev_timestamp + time_diff

            # Track key press and release events
            for key in [KEY_K1, KEY_K2, KEY_M1, KEY_M2]:
                if keys & key:
                    if key_press_start[key] is None:
                        key_press_start[key] = timestamp  # Start time of key press
                        key_press_events.append(timestamp)
                else:
                    if key_press_start[key] is not None:
                        hold_time = timestamp - key_press_start[key]
                        key_hold_times[key].append(hold_time)
                        key_press_start[key] = None  # Reset start time

            prev_timestamp = timestamp

        return key_press_events, key_hold_times

def plot_key_presses(key_press_events, num_key_presses):
    if num_key_presses > len(key_press_events):
        num_key_presses = len(key_press_events)
        print(f"Warning: Requested number of key presses exceeds available data. Plotting all {num_key_presses} key presses.")

    # Select the first `num_key_presses` key press events
    selected_events = key_press_events[:num_key_presses]

    plt.plot(range(num_key_presses), selected_events)
    plt.xlabel('Event Index')
    plt.ylabel('Timestamp (ms)')
    plt.title('Key Presses Over Time')
    plt.savefig('key_presses.png')
    plt.close()
    webbrowser.open('key_presses.png')

    total_key_presses = len(key_press_events)
    print(f"Total number of key presses: {total_key_presses}")

def plot_hold_times(key_hold_times, num_key_presses):
    all_hold_times = [hold_time for key in key_hold_times for hold_time in key_hold_times[key]]
    
    if num_key_presses > len(all_hold_times):
        num_key_presses = len(all_hold_times)
        print(f"Warning: Requested number of hold times exceeds available data. Plotting all {num_key_presses} hold times.")

    # Select the first `num_key_presses` hold times
    selected_hold_times = all_hold_times[:num_key_presses]

    plt.plot(range(num_key_presses), selected_hold_times)
    plt.xlabel('Event Index')
    plt.ylabel('Hold Time (ms)')
    plt.title('Hold Times of Key Presses')
    plt.savefig('hold_times.png')
    plt.close()
    webbrowser.open('hold_times.png')

    total_hold_times = len(all_hold_times)
    print(f"Total number of hold times: {total_hold_times}")

if __name__ == '__main__':
    file_path = 'replay.osr'
    key_press_events, key_hold_times = parse_osr_file(file_path)
    
    total_key_presses = len(key_press_events)
    print(f"Total number of key presses available: {total_key_presses}")

    while True:
        try:
            num_key_presses = int(input("Enter the number of key presses or hold times to plot (or type '0' to plot all): "))
            if num_key_presses < 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if num_key_presses == 0:
        num_key_presses = total_key_presses

    while True:
        plot_option = input("Would you like to plot (1) Key Press Timestamps or (2) Key Hold Times? Enter 1 or 2: ")
        if plot_option == '1':
            plot_key_presses(key_press_events, num_key_presses)
            break
        elif plot_option == '2':
            plot_hold_times(key_hold_times, num_key_presses)
            break
        else:
            print("Invalid input. Please enter 1 or 2.")
