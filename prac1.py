
# Simple Reflex Agent for Vacuum Cleaner

def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


# Environment
location = "A"
A = "Dirty"
B = "Dirty"

# Agent actions
print("Initial Location:", location)

if location == "A":
    action = vacuum_agent(location, A)
    print("Action:", action)
    if action == "Suck":
        A = "Clean"

    location = "B"
    action = vacuum_agent(location, B)
    print("Action:", action)
    if action == "Suck":
        B = "Clean"

print("A:", A)
print("B:", B)

