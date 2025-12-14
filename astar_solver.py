import time
import heapq

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("-" * 10)

def manhattan_distance(state):
    distance = 0
    for i, val in enumerate(state):
        if val == 0: continue
        target_index = GOAL_STATE.index(val)
        x1, y1 = i % 3, i // 3
        x2, y2 = target_index % 3, target_index // 3
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

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

def solve_astar(start_state):
    initial_h = manhattan_distance(start_state)
    pq = [(initial_h, 0, start_state, [])]
    
    visited = set()
    nodes_visited = 0

    print("Running A*...") # شيلنا الايموجي
    start_time = time.time()

    while pq:
        f, g, current_state, path = heapq.heappop(pq)
        
        if current_state in visited:
            continue
        visited.add(current_state)
        nodes_visited += 1

        if current_state == GOAL_STATE:
            end_time = time.time()
            return path + [current_state], nodes_visited, end_time - start_time

        for next_state in get_successors(current_state):
            if next_state not in visited:
                new_g = g + 1
                new_h = manhattan_distance(next_state)
                new_f = new_g + new_h
                heapq.heappush(pq, (new_f, new_g, next_state, path + [current_state]))

    return None, nodes_visited, 0

# --- Main Execution ---
if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 0, 5, 7, 8, 6)
    
    solution_path, visited_count, time_taken = solve_astar(initial_state)

    if solution_path:
        print(f"Solved! Cost: {len(solution_path) - 1} moves")
        print(f"Visited Nodes: {visited_count}")
        print(f"Time: {time_taken:.4f} seconds")
        for s in solution_path:
            print_board(s)
    else:
        print("No solution found.")