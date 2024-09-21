def max_guests(arrivals, departures):
    events = []
    
    # Create events for arrivals and departures
    for arrival in arrivals:
        events.append((arrival, 1))  # 1 for arrival
    for departure in departures:
        events.append((departure, -1))  # -1 for departure
    print(events)
    # Sort events: first by time, then by type (arrival before departure)
    events.sort(key=lambda x: (x[0], x[1]))
    print(events)
    max_guests = 0
    current_guests = 0
    
    for event in events:
        current_guests += event[1]  # Add 1 for arrival, subtract 1 for departure
        max_guests = max(max_guests, current_guests)  # Update max guests
    
    return max_guests

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arrivals = list(map(int, input().split()))
        departures = list(map(int, input().split()))
        
        result = max_guests(arrivals, departures)
        print(result)

if __name__ == "__main__":
    main()
