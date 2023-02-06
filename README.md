# Project 2 - Insurance Company 

You are starting your own Canadian insurance company from data you recently acquired at auction from a now-defunct commercial insurance company called AFC Industries.  


AFC industries holds market data on several commercial business clients in the GTA. There are two data sets to consider. The claims data under the name `AFC_claims.csv`, and
their policy data `AFC_policies.csv`.  

Your job is to create a premium model and attempt to acquire new clients listed under the name of `potential_clients.csv`. 

## Loss-Cost Model 

The essence of insurance pricing comes down to the loss-cost model. The premium cost is unique for every commercial building client. 

The equation for calculating a premium is as follows:

`Premium = Cost + Profit`

I.e. we are interested in modelling the cost, and then determining the margin of profit. We seek to have the client both pay their cost, and, contribute to our company profit. 

The cost can be separated into multiple sub-components denoted as the following:

- Expected Losses (Claims from the client) 
- Loss Adjustment Expenses 
- Underwriting Expenses 

This results in the following formula: 

`Premium = Expected Losses + Loss Adjustment Expenses + Underwriting Expenses`

These components can be broken down further, however, we are going to use the pure premium method to calculate premiums 
as written in Chapter 8 of Werner & Modlin.

$$ PurePremium = \frac{ExpectedLoss * (1 + LossAllocatedExpenses) + FixedExpensesPerPolicy}{1 - VariableExpensesPerPolicy - ProfitLoading} $$

- $ ExpectedLoss $ the amount of loss the targeted client is predicted to occur.  

- $ LossAllocatedExpenses $ are claim-related expenses that are directly attributable to a specific claim; for
example, fees associated with outside legal counsel hired to defend a claim can be directly
assigned to a specific claim.

- $ FixedExpensesPerPolicy $ day-to-day running expenses for facilitating insurance coverage overall. Commercial rent, server costs, etc. 

- $ VariableExpensesPerPolicy $, expenses which are unrelated to specific policies, and, could be specific to the annual year. E.g. Covid pandemic of 2020-2021 could result in lower insurance claims therefore having a smaller  $VariableExpensesPerPolicy$ for that annual year. 

- $ ProfitLoading $, similar to a profit margin; you as an executive, get to determine on how much to charge your customers.

Note that you can consolidate the last two variables of interest for the pure premium into one number, ultimately these are the annual business decisions the insurance company has to make. 


## Modelling Expected Loss 

Specifically, the most important aspect of this project is to correctly model the client loss. Otherwise known as the loss/cost model. 
There are several methods to model expected losses but the most ubiquitous approach is to model the frequency and severity of claims. 

### Frequency of Claims 
The frequency of claims refers to the number of claims can occur for a particular client. We can denote this by $Y_f$. 

To model $Y_f$ we should consider distributions that model count data. Those distributions include but are not limited to

- Poisson 
- Negative Binomial 
- Binomial 
- Zero-inflated Poisson 

The most standard approach for modelling such data is through the use of GLM's which we modelled in class. 

### Severity of Claims 

The Severity of claims refers to the monetary loss of an insurance claim. We denote this by $Y_s$. 

To model $Y_s$ we should consider distributions that model continous data. 

- Gaussian (log-link)
- Gamma (log-link)
- Log-normal 
- Variance-Gamma 
- Generalized Hyperbolic 

Again if we consider a GLM framework, we can easily use the data given in the project to model such losses. 


### Loss-Cost Model 

To calculate the expected loss, use the following formula. 

$$ ExpectedLoss = Y_s * Y_f $$

Essentially this is straight forward. You take the expectation of the number of claims for a particular client, and multiply by their 
severity (the expected monetary loss). 


# Evaluation 

You will be evaluated in two phases. 


## Phase - 1
The first phase will be purely based on quantitative performance. You will develop your model and ship your premiums using the template `potential_clients.csv`. 
I will then take each of your premiums, and pit you up-against each other, to simulate a market. The lowest premium will have a 75% chance of acquiring the client.
The rest of you will have a random chance to acquire the client via a uniform dirichlet process. 

Once the market has been simulated, and the clients have been handed out, some of your clients may have incurred claims. 
If you manage to turn a profit, you will be awarded a level 4 immediately. If you fail to turn a profit, you will have to proceed to phase 2. 

## Phase - 2 
Given that you have become bankrupt, you must re-evaluate your model performance, and submit a 6-page writeup detailing improvements and model developments. Once submitted, you will be evaluated again based on the merits of your improvements. 






















