from collections import deque

class WaterJugProblem:
    def __init__(self, jug_a_capacity, jug_b_capacity, target):
        self.jug_a_capacity = jug_a_capacity
        self.jug_b_capacity = jug_b_capacity
        self.target = target
        self.visited = set()
        self.parent = {}
        self.action = {}
        
    def bfs(self):
        start_state = (0, 0)
        queue = deque([start_state]) #taken deque for simplicity
        self.visited.add(start_state)
        self.parent[start_state] = None
        self.action[start_state] = "Initial State"
        
        while queue:
            current_state = queue.popleft()
            
            # Check if we reached the goal state
            if current_state[0] == self.target or current_state[1] == self.target:
                return self.Step_to_find_desired_liters(current_state)
            
            # Generate all possible next states of current state
            next_states = self.generate_states(current_state)
            
            for next_state, action in next_states:
                if next_state not in self.visited:
                    self.visited.add(next_state)
                    self.parent[next_state] = current_state
                    self.action[next_state] = action
                    queue.append(next_state)
        
        return None # we will return None if we did not find any bfs path.
    
    def generate_states(self, state):
        a, b = state
        max_a, max_b = self.jug_a_capacity, self.jug_b_capacity
        states = []
        
        # 1. Fill Jug A
        states.append(((max_a, b), "Fill Jug A"))
        
        # 2. Fill Jug B
        states.append(((a, max_b), "Fill Jug B"))
        
        # 3. Empty Jug A
        states.append(((0, b), "Empty Jug A"))
        
        # 4. Empty Jug B
        states.append(((a, 0), "Empty Jug B"))
        
        # 5. Pour from A to B
        pour_amount = min(a, max_b - b)
        states.append(((a - pour_amount, b + pour_amount), "Pour water from Jug A to Jug B"))
        
        # 6. Pour from B to A
        pour_amount = min(b, max_a - a)
        states.append(((a + pour_amount, b - pour_amount), "Pour water from Jug B to Jug A"))
        
        return states
    
    def Step_to_find_desired_liters(self, goal_state):
        final_path = []
        state = goal_state
        
        while state is not None:
            final_path.append((state, self.action[state]))
            state = self.parent[state]
        
        final_path.reverse()
        return final_path
    
    def A(self):
        print(f"Initial State: (0, 0)\n")
        
        solution = self.bfs()
        
        if solution:
            for i, (state, action) in enumerate(solution):
                if i == 0:
                    continue  # We have already print this initial state
                print(f"Step {i}: {action}")
                print(f"State: {state}")
            
            # Identifying which jug contains the target
            final_state = solution[-1][0]
            if final_state[0] == self.target:
                print(f"\n Reached the Goal State")
                print(f"{self.target} liters measured in Jug A.")
            else:
                print(f"\nReached the Goal State")
                print(f"{self.target} liters measured in Jug B.")
        else:
            print("Solution of this not found!")


if __name__ == "__main__":
    jug_a = int(input("Enter capacity of Jug A in liters: "))
    jug_b = int(input("Enter capacity of Jug B in liters: "))
    target = int(input("Enter amount of liters you want: "))
    
    
    print("\nStep to get",target,"liters of water\n")
    
    
    desired_liters = WaterJugProblem(jug_a, jug_b, target)
    desired_liters.A()