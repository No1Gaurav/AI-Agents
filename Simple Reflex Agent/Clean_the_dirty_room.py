import matplotlib.pyplot as plt
import matplotlib.patches as pat
import math

while True:
    no_of_rooms = int(input("How many total rooms are there (must be a perfect square)? "))
    sqrt_val = math.isqrt(no_of_rooms)
    if sqrt_val * sqrt_val == no_of_rooms:
        break
    else:
        print("❌ Please enter a number that is a perfect square (e.g., 4, 9, 16).")

environment = {}
for i in range(no_of_rooms):
    print("Room", i + 1, ":")
    Room_condition = input("Is Room dirty or not (Enter 'C' for Clean / Enter 'D' for Dirty): ").strip().lower()
    room_no = f"Room{i+1}"
    if Room_condition == 'c':
        environment[room_no] = "Clean"
    elif Room_condition == 'd':
        environment[room_no] = "Dirty"
    else:
        print("❌ Wrong input. Exiting.")
        exit()

side = math.isqrt(no_of_rooms)
room_position = {}
for i in range(no_of_rooms):
    row = i // side
    col = i % side
    room_position[f"Room{i+1}"] = (col, side - 1 - row)


rooms = list (environment.keys())
pre_agent_index = -1
agent_index = 0

def draw_the_environment_2(environment, agent_pos):
    side = int(math.isqrt(len(environment)))
    fig, ax2 = plt.subplots()
    ax2.set_xlim(0, side)
    ax2.set_ylim(0, side)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title(f"Cleaning {rooms[agent_pos]}")

    for room, pos in room_position.items():
        x, y = pos
        color = "#FFA07A" if environment[room] == "Dirty" else "#90EE90"
        rect = pat.Rectangle((x, y), width=1, height=1, facecolor=color, edgecolor="black")
        ax2.add_patch(rect)
        ax2.text(x + 0.5, y + 0.5, room, ha="center", va="center", color="black", fontsize=10)

    agent_x, agent_y = room_position[rooms[agent_pos]]
    agent_patch = pat.Circle((agent_x + 0.5, agent_y + 0.5), radius=0.2, facecolor="blue", edgecolor="black")
    ax2.add_patch(agent_patch)

    plt.pause(1)
    plt.close()



def clean_the_dirty_room ():
    draw_the_environment_2(environment ,agent_index)

def check_if_the_room_is_dirty_or_not (state) :
    if state == "Dirty":
        clean_the_dirty_room()
        environment [current_room] = "Clean"
        return "Move"
    else :
        return "Move"
    
def draw_the_environment(environment, agent_pos, step):
    side = int(math.isqrt(len(environment)))
    fig, ax = plt.subplots()
    ax.set_xlim(0, side)
    ax.set_ylim(0, side)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Step {step} - Agent in {rooms[agent_pos]}")

    for room, pos in room_position.items():
        x, y = pos
        color = "#FFA07A" if environment[room] == "Dirty" else "#90EE90"
        rect = pat.Rectangle((x, y), width=1, height=1, facecolor=color, edgecolor="black")
        ax.add_patch(rect)
        ax.text(x + 0.5, y + 0.5, room, ha="center", va="center", color="black", fontsize=10)

    agent_x, agent_y = room_position[rooms[agent_pos]]
    agent_patch = pat.Circle((agent_x + 0.5, agent_y + 0.5), radius=0.2, facecolor="blue", edgecolor="black")
    ax.add_patch(agent_patch)

    plt.pause(1)
    plt.close()


plt.ion ()
steps = no_of_rooms*2

for step in range (steps):
    current_room = rooms[agent_index]
    state = environment[current_room]
    draw_the_environment(environment ,agent_index , step+1)
    action = check_if_the_room_is_dirty_or_not(state)

    if action == "Clean":
        environment[current_room] = "Clean"
    else:
        agent_index = (agent_index + 1 ) % len(rooms)
    
plt.ioff()
print ("SIMULATION COMPLETE")