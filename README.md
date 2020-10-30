# Sampling the multinomial distribution

Now that we have generating Poisson random variables and thus understand this business of extending our Bernoulli random variable code so as to generate multinomial trails we are going to return to generating random variables from a distribution with this probability mass function:

![](https://render.githubusercontent.com/render/math?math=P(X=0)=0.5\qquad\P(X=1)=0.1\qquad\P(X=2)=0.2\qquad\P(X=3)=0.05\qquad\P(X=4)=0.15)

Instead of generating a single random variable from this distribution, however, we are going to generate multiple random variables from this distribution.  In other words we are going to generate a sample from a multinomial distribution.  Remember to generate a sample from a multinomial distribution we are going to:

1. Generate multiple samples from the above distribution.
2. We are going to count how often each of the outcomes appears.

The random object that we are going to sample is thus going to be an array containing five elements.  In the code in `main.py` and the function `multinomial` I have initialised this array to five zeros. The list I have created to hold the count is called `nvals`.  To get the elements in the list to be equal to the appropriate quantities you need to do two things:

1. You need to write a function called `myvariable` that takes a vector called `probs` containing the five probabilities in the probability mass function above and that returns a random variable from this distribution.  This part should now be straightforward as we have done this multiple times.
2. You need to add one line of code inside the loop inside the function called  multinomial  to count the number of times each of the outcomes comes up.  The values of these counts for the number of times each outcome appears should be returned from this function so the counts should be stored in the variable called  `nvals`.  

Notice that you should be able to write all the code required without writing any conditional (if) statements.
