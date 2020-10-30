import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_trial(self):
       myexp, myvar = 0, 0 
       for i in range(5) : 
          myexp = myexp + probs[i]*i
          myvar = myvar + probs[i]*i*i
       myvar = myvar - myexp

       mean = 0
       for i in range(100) : mean = mean + myvariable( probs )
       mean = mean  / 100 

       bar = np.sqrt(myvar/100)*st.norm.ppf( (0.99 + 1) / 2 )
       self.assertTrue( np.fabs( mean - myexp )<bar, "your myvariable appears to be sampling the wrong distribution" )
       
    def test_trial(self):
       for n in range(1,10):
           nn = n*10
           means = 5*[0] 
           for i in range(100) :
              mult = multinomial( nn, probs )
              for j in range(5) : means[j] = means[j] + mult[j]

           for j in range(5) : 
              myvar = nn*probs[j]*(1-probs[j]) 
              bar = np.sqrt(myvar/100)*st.norm.ppf( (0.99 + 1) / 2 )
              self.assertTrue( np.fabs( means[j]/100 - nn*probs[j])<bar, "you appear to be sampling the multinomial wrongly" )
      
