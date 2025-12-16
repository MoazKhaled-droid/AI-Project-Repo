import time

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

def solve_dls(start_state):
    stack = [(start_state, [])]
    visited = set()
    nodes_visited = 0
    MAX_DEPTH = 20  

    print(f"Running DFS (Max Depth: {MAX_DEPTH})...")
    start_time = time.time()

    while stack:
        current_state, path = stack.pop()
        nodes_visited += 1

        if current_state == GOAL_STATE:
            end_time = time.time()
            return path + [current_state], nodes_visited, end_time - start_time
        
        if len(path) >= MAX_DEPTH:
            continue

        visited.add(current_state)

        neighbors = get_successors(current_state)
        neighbors.reverse()

        for next_state in neighbors:
            if next_state not in visited:
                if next_state not in path: 
                    stack.append((next_state, path + [current_state]))

    return None, nodes_visited, 0

# --- Main Execution ---
if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 6, 8, 7, 5, 0)
    
    solution_path, visited_count, time_taken = solve_dfs(initial_state)

    if solution_path:
        print(f"Solved! Cost: {len(solution_path) - 1} moves")
        print(f"Visited Nodes: {visited_count}")
        print(f"Time: {time_taken:.4f} seconds")
        print("--- Path ---")
        for s in solution_path:
            print_board(s)
    else:
        print("Solution not found within depth limit.")