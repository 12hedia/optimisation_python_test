import pulp as p
Lp_prob = p.LpProblem('Problem', p.LpMaximize)
# Create problem Variables 
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0
  
# Objective Function
Lp_prob += 40 * x + 50 * y   
  
# Constraints:
Lp_prob += 2 * x +  y <= 800
Lp_prob += x + 2 * y <= 700
Lp_prob += y <= 300
  
# Display the problem
print(Lp_prob)
  
status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status
  
# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))  