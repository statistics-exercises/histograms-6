import numpy as np

def myvariable(probs) : 
  # Your code to generate a random variable from the distribution 
  # that is given in the description section of this page goes here
  
def multinomial(n, probs) :
  nvals = np.zeros(5) 
  for i in range(n) : 
    var = myvariable(probs) 
    # Your code to count the number of times the variable is equal
    # to each of the five possible values it can take goes here.  
    # You should store the number of times each of the outcomes outcomes
    # comes up in the list called nvals 
  
  
  return nvals
  
probs = np.array([0.5, 0.1, 0.2, 0.05, 0.15 ])
print( multinomial(20, probs) )
print( multinomial(20, probs) )
print( multinomial(20, probs) )
print( multinomial(20, probs) )
