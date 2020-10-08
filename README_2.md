# Predicting TELCO Churn Project

## Project Planning
#### Project Description:
The purpose of this project is to create a model that predicts future Telco customer churn as accuractly as possible, based upon the provided Telco customer dataset. Another primary goal is to identify what drivers to churn are present in the current customer base.

Part of the output from this project will be several files for you to use if you desire to recreate my work, which are: acquire.py, prepare.py, model jupyter notebook and telco_predicted_churn.csv.

### Short Synopsis of Telco Data:
Project Background:
Customer retention is a key metric for a successful business. The vast majority of new customers are not new telecom customers, and have churned from another company. The costs of acquiring a new customer take time to recoup, and then reducing churn is a key goal for any telecom company.
A good synopsis on churn in the telecom industry can be found here at this [link](http://www.dbmarketing.com/telecom/churnreduction.html#:~:text=Wireless%20companies%20today%20measure%20voluntary,10%20percent%20and%2067%20percent.)

Additional information on the telco dataset and the dataset itself can be accessed [here](https://www.kaggle.com/blastchar/telco-customer-churn) if access to the Codeup database is not available to you.


## Data Dictionary

##### I only list here the columns that I ended up using in my project.

- churn: If the customer churned = Yes/1; if the customer didn't churn = No/0
- churned: If the customer churned = Yes/1; if the customer didn't churn = No/0
- tenure: Number of months person has been a customer. 
- t_yrs: Tenure adjusted for number of years (used only in explore phase).
- monthly_charges: Individual customer's monthly charge (in dollars $)
- total_charges: Individual customer's total charges over their entire tenure (in dollars $)
- gender: Female/Male
- is_female: 1 = Yes/female, 0 = No/male
- senior citizen: 0 = No, 1 = Yes
- partner: 1 = Yes, 0 = No
- dependents: 1 = Yes, 0 = No
- paperless_billing: 1 = Yes, 0 = No
- is_automatic: dirived from the payment_type column; 1 == auto bank transfer and Credit Card (auto). 0 == Mailed check and Electronic check. Used in explore and model phases.
- .csv: comma separated value, is a file in which the 
- prediction (In the final .csv): 1 = churned, 0 = didn't churn, according to model's predictions.


## Initial Hypotheses and Thoughts

### Thoughts
- The goal of this project is to discover drivers to customer churn, and create models that can accurately predict churn in the future. Thus, the dependent variable in this case will be the rate of churn, or if a customer churned or not. Finding which independent variables (the other datapoints in the dataest) are the most powerful drivers of that churn is what my models will need to focus on. 

- What about ease of payment? Does that have an impact on churn? What about monthly charges? Is that a good way to measure churn?

#### Questions to answer:
- Is customer churn rate independent of contract type when controlling for internet service type?


### Hypotheses

- Is customer churn rate related to (or independent of) contract type?
    - Null Hypothesis: Churn rate is not significantly impacted by the type of contract a customer has when controlling for payment type.
    - Alt Hypothesis: Churn rate is significatly impacted by the type of contract a customer has when controlling for payment type.

- Is customer churn rate 
    - Customer churn is not related to (is independent of) automatic payment type
    - Customer churn is related to (is not independent of) automatic payment type

## Project Plan:

#### acquire.py
Acquiring the Telco Churn dataset from the Codeup Database.

#### prepare.py
- address any missing data
- address outliers
- create `is_automatic` for holding 1/0 (True/False) values

#### Explore
- Determine tenure cohorts
- Discover average churn and retention rates by tenure cohort
- Visualize the datat
- Test both of hyptotheses

#### Model
- Try 2 different algorithms: logistic regression and random forest
- Determine which features are most influential
- fit models, evaluate on train
- select best models and evaluate with validate
- select top model, and run that model on the test dataset.
- Create model.py incorporating above steps.

#### Conclusion
- Summarize findings
- Recommendations for further study/Next Steps

## How to Reproduce
1. Clone this repository into your own Github repo, and pull to your own local working directory.
2. Have database to the Codeup DS database. 
    - You must have already created an env.py file with your host, username, and password data set as variables inside that env file.
3. Install the acquire.py and prepare.py into your working directory.
4. Run the jupyter notebook.