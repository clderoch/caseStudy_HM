
Problem Statement
You are working for an online personal loans lending platform called “Joyful Dollars” as a lead fraud analyst. Your responsibilities include owning the analytical roadmap for fraud, monitoring the fraud model performance and adjusting the fraud pass/review/reject trigger rules appropriately.

Currently, Joyful Dollars (JD) is facing a significant challenge. Over the past quarter, Joyful Dollars has experienced thousands of fraud attacks which have produced some challenges for the company. Therefore, as the lead fraud analyst, you are responsible not only for monitoring model performance but also for proactively identifying trends, optimizing rule configurations, and recommending data-driven improvements. This involves analyzing historical data to pinpoint patterns and anomalies, visualizing key performance indicators, investigating specific rule triggers, and rethinking our decisioning framework. 

Be sure to read the tips at the bottom of the page!
You will have 48 hours to complete from the time of receiving this assessment. 

Assignment Questions:

You have been tasked with analyzing the available data to identify:
1.	What trends do you see in the data, both in terms of cases of confirmed fraud as well as false positives? What are your initial impressions? Please use statistics and visualizations to support your answer.
2.	Based on the data provided, how do Joyful Dollar’s fraud models and data explain the above trend? What are your initial thoughts about their fraud model and policy?
3.	How does JD’s fraud policy balance improving the policy's performance with mitigating the number of false positives? What would you try to change about this balance?
4.	How would you change the existing approach in order to increase JD’s fraud performance while reducing the number of false positives? (model, ruleset, etc.) Please explain your approach and impact.
5.	Open Question: Are there any features or data points that are missing from this dataset that you would have liked to have?

Tools:
You may use any tool that uses Python or R to present your answers and any additional tool to solve the questions above. Below are some free options but feel free to use whatever you are most comfortable with to manipulate the datasets below.

Examples (but not limited to): 
https://code.visualstudio.com/ 
https://www.anaconda.com/docs/getting-started/anaconda/install 

Dataset:
Please refer to this link to download the data and metadata: 

Data
Category	Link	Explanation
Fraud Data	Download
Fraud analysis data
Metadata	Download
Explanation of fields in Fraud Data
To help the analysis, there are some hints and additional information candidate should know:

TIPS:
1.	Joyful Dollars’ fraud framework comprises three main components:
a.	Device and Behavior (DNB, D&B) model: Most applications include a DnB result since this model monitors the entire process of the applicant’s behavior and device information. The outcomes are reflected in the BEHAVIOR_CHECK_SCORE and DEVICE_CHECK_SCORE.
b.	Digital Identity Trust (DIT) model: The DIT model is triggered when an application is approved by Joyful Dollars’ credit policy. If the application does not move to the offer stage or is not approved by the credit policy, the DIT model will not be activated. The outcome of this model is captured in DIT_DECISION.
c.	Kount model: Like the DIT model, the Kount model is only run when an application is approved by the credit policy. It is not triggered if the application fails to reach the offer stage or is not approved. The outcome of the Kount model is captured in KOUNT_AUTO.
2.	Based on the outcomes of these three models and additional rules set by Joyful Dollars’ fraud experts, a consolidated field, FRAUD_MODEL_RESULT, is generated with the following possible values:
a.	fraud_pass: No friction caused by JD’s fraud model
b.	fraud_reject: Application was rejected by the fraud model before executing the credit policy
c.	fraud_decline: Application was rejected by the fraud model after credit policy processing
d.	fraud_review: Application was tagged for review by the fraud modell
e.	fraud_review_no_case: The flag is identical to fraud_review in this case
3.	After the credit policy and fraud screening, applications proceed to the underwriting stage. During underwriting, the FRAUD_MODEL_RESULT is translated into a new field, FRAUD_STATUS, with the following outcomes:
a.	Pass: FRAUD_MODEL_RESULT = ‘fraud_pass’
b.	Fail: FRAUD_MODEL_RESULT = ‘fraud_decline’ or ‘fraud_fail’
c.	Manual Review: FRAUD_MODEL_RESULT = ‘fraud_review’
d.	Manual Review No Case: FRAUD_MODEL_RESULT = ‘fraud_review_no_case’
e.	False Positive: Following manual review, if the agent determines the case was a false positive, the status becomes “False Positive”.
f.	Confirmed Fraud: Following manual review, if the agent determines the case is genuine fraud, the status becomes “Confirmed Fraud”.
g.	Note: In the analysis dataset, if FRAUD_STATUS is “Manual Review” or “Manual Review No Case”, it typically indicates that the application expired or was declined due to criteria unrelated to fraud. This may include:
i.	Decline by credit policy
ii.	Offer not selected by the applicant
iii.	Failure to submit required documents on time
4.	The rules that triggered fraud reject/decline/review are detailed in the FRAUD_MODEL_REASONS column. We expect you to review and understand these rules as part of your analysis.
5.	Please note that real-world data is rarely perfect. Expect to encounter discrepancies and dirty data; your ability to process and clean such data will be an important part of this case assessment.
Notes:
●	Data Source: The dataset is a single CSV file attached with your take home challenge. If you encounter any difficulty in opening this CSV file or have any questions during the take-home challenge, please reach out to your recruiter.
●	Tools for analysis: Feel free to use whatever tools or analysis software you think makes the most sense. But we suggest using python as a widely accepted programming language in our team.
●	Outside help: You are welcome to use any free tools at your disposal to complete this task.
●	Submission: You will need to reply to the take home challenge Email to your recruiter with your completed answers including codes to question above. The submission can be in any format you prefer and be several files if you wish. Please submit your written response to your recruiter within 48 hours of receipt.



