# Simulating insurance market from client-side. 
# Last updated: March 6th 
# Author: Nikola Pocuca 

# imports. 
import numpy as np 
import pandas as pd 

# load policy premium offers. 
# df = pd.read_csv("example_market.csv")
df = pd.read_csv("example_market.csv") 

# define dirichlet distribution. 

# costs adjusted expenses.  
fixed_expenses_per_policy = 500 
variable_expenses_per_policy = 0.4 
loss_allocated_expenses = 0.2 

# checks to makes sure students used the correct formula. 
# profit should be determined only by profit-loading and how good their 
# models were. 
def adjust_loss_for_expenses(loss_input: np.array) -> np.array: 
    """
        Takes in an array of losses, adjusts for all expenses and returns 
        an array back with equal shape. 
    """ 

    # calculate numerator.     
    pre_variable_adjusted_loss =  loss_input * (1.0 + loss_allocated_expenses) + fixed_expenses_per_policy

    # calculate denominator. 
    variable_adjusted_loss = pre_variable_adjusted_loss / (1 -  variable_expenses_per_policy)

    return variable_adjusted_loss


def award_to_company_v1(premium_df: pd.DataFrame, upper_limit = 0.75) -> list: 
    """ 
        premium_df: Dataframe [BusinessID, name_1, ... , name_d]
        
        upper_limit for simulating data, [upper_limit, (dirichlet break over 1-upper_limit)]
    """

    # get numbers only 
    premiums_charged = premium_df.drop(['BusinessID'], axis=1).to_numpy()

    # companies 
    companies = list(premium_df.columns[1:])

    # lowest premium 
    sort_index = np.argsort(premiums_charged, 1)

    # get number of offers 
    number_of_offers = premiums_charged.shape[1]

    # sort probability index, 
    probability_breaks = np.random.dirichlet([1.0]*(number_of_offers - 1), size= premiums_charged.shape[0] )*(1-upper_limit)

    # add upper limit to first column. 
    leading_prob = np.array([upper_limit]* premiums_charged.shape[0])
    probabilities = np.concatenate((np.expand_dims(leading_prob,1), probability_breaks),1)

    awarded = []

    probabilities[:,-1] = 1.0 - probabilities[:,:-1].sum(1)

    # for loop 
    for i in range(premiums_charged.shape[0]):     
        awarded += [companies[sort_index[i, np.random.multinomial(1,probabilities[i],size=1).argmax()]]]

    return awarded

def award_to_company_v2(premium_df: pd.DataFrame) -> list:
    """
        Alex Xu contribution. 
    """

    
    # list of company names awarded 
    awarded = [] 

    # get numbers only 
    premiums_charged = premium_df.drop(['BusinessID'], axis=1).to_numpy()

    # calculate weighted probabilities. 
    inverse_premium = 1.0 / np.abs(premiums_charged) 
    probabilities = inverse_premium / np.expand_dims(inverse_premium.sum(1),1)
    probabilities[:,-1] = 1.0 - probabilities[:,:-1].sum(1)

    # companies 
    companies = list(premium_df.columns[1:])

    # lowest premium 
    sort_index = np.argsort(premiums_charged, 1)

    # get number of offers 
    number_of_offers = premiums_charged.shape[1]

    awarded = []
    # for loop 
    for i in range(premiums_charged.shape[0]):     
        try:
            awarded += [companies[sort_index[i, np.random.multinomial(1,probabilities[i],size=1).argmax()]]]
        except: 
            breakpoint()
    return awarded 



if __name__ == "__main__": 
    print("Simulating Market")


    # coolio 
    awarded_to_company = award_to_company_v1(df)

    # cool. 
    awarded_to_company_2 = award_to_company_v2(df)

    print(pd.value_counts(awarded_to_company))
    # print(pd.value_counts(awarded_to_company_2))

