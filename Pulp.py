my_lp_problem  = pulp.LpProblem("Halva",pulp.LpMaximize)
FN = pulp.LpVariable('FN', lowBound=0, cat='Continuous')
DH = pulp.LpVariable('DH', lowBound=0, cat='Continuous')
KH = pulp.LpVariable('KH', lowBound=0, cat='Continuous')
KBH = pulp.LpVariable('KBH', lowBound=0, cat='Continuous')
# Objective function
my_lp_problem += 45 * FN + 50 * DH + 60 * KH + 10 * KBH, "Profit"
# Constraints
my_lp_problem += FN<=250
my_lp_problem += DH<=120
my_lp_problem += KH<=90
my_lp_problem += KBH<=550
my_lp_problem += 0.3*FN+0.2*DH+0.4*KH+0.4*KBH<=500
my_lp_problem += 0.4*FN+0.5*DH+0.8*KH+0.8*KBH<=450
my_lp_problem += 0.4*FN+0.3*DH+0.1*KH+0.1*KBH<=75
my_lp_problem += 0.2*FN+0.3*DH+0.6*KH+0.5*KBH<=300
my_lp_problem += 0.5*FN+0.5*DH+0.4*KH+0.8*KBH<=200
my_lp_problem
