# DONE: import necessary libraries
import math
import matplotlib.pyplot as plt
from Generaldistribution import Distribution
# DONE: make a Binomial class that inherits from the Distribution class. Use the specifications below.
class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
    mean (float) representing the mean value of the distribution
    stdev (float) representing the standard deviation of the distribution
    data_list (list of floats) a list of floats to be extracted from the data file
    p (float) representing the probability of an event occurring
                
    """
    def __init__(self, prob=0.5, size=20):
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
        self.p=prob
        self.n=size
  
    # TODO: write a method calculate_mean() according to the specifications below
    def calculate_mean(self):   
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        mean_binomial = self.p * self.n
        self.mean=mean_binomial
        return self.mean

    #DONE: write a calculate_stdev() method accordin to the specifications below.
    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        stdev_binomial = math.sqrt(self.n * self.p * (1 - self.p))
        self.stdev=stdev_binomial
        return self.stdev

    def replace_stats_with_data(self):
            """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
            Args: 
                None
        
            Returns: 
                float: the p value
                float: the n value
    
            """
            self.n = len(self.data)
            self.p = 1.0 * sum(self.data) / len(self.data)

            self.mean=self.calculate_mean()
            self.stdev=self.calculate_stdev()

            return self.n, self.p
                 

    # TODO: write a method plot_bar() that outputs a bar chart of the data set according to the following specifications.
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        height=[(1 - self.p) * self.n, self.p * self.n]
        plt.bar(x = ['0', '1'], height = height)
        plt.title('Bar Chart')
        plt.xlabel('outcome')
        plt.ylabel('count')
    
    #TODO: Calculate the probability density function of the binomial distribution
    def pdf(self, k):  
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        return math.comb(self.n, self.k) * self.p**(self.k) * (1-self.p)**(self.n-self.k)

    # write a method to plot the probability density function of the binomial distribution
    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()

        return x, y

        # TODO: Use a bar chart to plot the probability density function from
        # k = 0 to k = n
        
        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.
        
        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists
                
    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.
    
    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """       
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        
        return result
        
        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for 
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.
        
        # the try, except statement above will raise an exception if the p values are not equal
        
        # Hint: When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.
                        
    # use the __repr__ magic method to output the characteristics of the binomial distribution object.
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        
        # TODO: Define the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        #
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format
    
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)
