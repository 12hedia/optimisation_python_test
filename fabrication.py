import pulp as p
Lp_prob = p.LpProblem('Problem', p.LpMaximize)
# Create problem Variables 
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0
  
# Objective Function
Lp_prob += 10 * x + 18 * y   
  
# Constraints:
Lp_prob += 2 * x + 3 * y <= 100
Lp_prob += 0.4 * x + 0.6 * y <= 700

  
# Display the problem
print(Lp_prob)
  
status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status
  
# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))  