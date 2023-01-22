import pulp as p
Lp_prob = p.LpProblem('Problem', p.LpMaximize)
# Create problem Variables 
a = p.LpVariable("a", lowBound = 0)   # Create a variable x >= 0
b = p.LpVariable("b", lowBound = 0)   # Create a variable y >= 0
  
# Objective Function
Lp_prob += 450 * a + 800 * b   
  
# Constraints:
Lp_prob += 1.5 * a +  2 * b <= 250
Lp_prob += 0.5 * a + 0.75 * b <= 100
Lp_prob += 2 * a + 3 * b <= 300
Lp_prob += a >= 100
Lp_prob += b >= 53
Lp_prob += b <= 99
Lp_prob += a <= 99

# Display the problem
print(Lp_prob)
  
status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status
  
# Printing the final solution
print(p.value(a), p.value(b), p.value(Lp_prob.objective))  