from network import Client, Arguments

def move(C):
            C.get_servers_input()
            
            speed = C.S.d['speedX']
            target_speed = 160 # km/h
            steering_angle = C.S.d['angle']
            track_pos = C.S.d['trackPos']

            C.R.d['steer'] = (steering_angle - track_pos * 0.5) / 0.785398 
            
            if speed < target_speed:
                C.R.d['accel'] = 0.5
                C.R.d['brake'] = 0
            else:
                C.R.d['accel'] = 0
                C.R.d['brake'] = 0

            if speed < 50: C.R.d['gear'] = 1
            elif speed < 80: C.R.d['gear'] = 2
            else: C.R.d['gear'] = 3
            
            C.respond_to_server()
    
def main():
    
    args = Arguments() # Handles players arguments.
    
    C = Client(p=3001) # This should be a singleton class only one instance currently.

    print("Classical Control Mode Active...")

    try:
        # The MAIN loop
        
        while True:
            
            C.get_servers_input()


            C.respond_to_server()
            
    except KeyboardInterrupt:
        print("\nStopping the car.")
        C.shutdown()

if __name__ == "__main__":
    main()