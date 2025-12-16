import time
from collections import deque

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("-" * 10)

def get_successors(state):
    successors = []
    state_list = list(state)
    zero_index = state_list.index(0)
    row, col = zero_index // 3, zero_index % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r, c in moves:
        new_row, new_col = row + r, col + c
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state_list)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            successors.append(tuple(new_state))
            
    return successors

def solve_bfs(start_state):
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)
    nodes_visited = 0

    print("Running BFS...")
    start_time = time.time()

    while queue:
        current_state, path = queue.popleft() # FIFO
        nodes_visited += 1

        if current_state == GOAL_STATE:
            end_time = time.time()
            return path + [current_state], nodes_visited, end_time - start_time

        for next_state in get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))
# [(successors1,path1),(successors2,path2),(successors3,path3)]
#  the new queue if there is only 3 successors 
    return None, nodes_visited, 0

# --- Main Execution ---
if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 6, 8, 7, 5, 0)
    
    solution_path, visited_count, time_taken = solve_bfs(initial_state)

    if solution_path:
        print(f"Solved! Cost: {len(solution_path) - 1} moves")
        print(f"Visited Nodes: {visited_count}")
        print(f"Time: {time_taken:.4f} seconds")
        print("--- Path ---")
        for s in solution_path:
            print_board(s)
    else:
        print("No solution found.")