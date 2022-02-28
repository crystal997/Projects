Project: Titanic 
Name: Crystal Xu 

Comparison:
The performace of the model will be measured by accuracy precision and F score

The performace of the model will be measured by accuracy precision and F score

- SVM: The Accuracy, Precision, F1_score and CV accuracy score are highest. The model has best performce. Choose SVM 

- Random Forest: Random Forest model has less overfitting, but preformance is worse than SVM

- Logistic Regression: Comparing to other models, logistic regression has lower accuracy and precision. 
  Also, because the dataset is small, the performance fluctuated a lot with different train test splits. 

- Decision Tree: Overfitting, low precision, low accuracy and low F1_score

- Nearest Neighbors: Low accuracy, low precision , low F1_score


Perforamce Stats

Model Type	Accuracy	Precision	Recall	F1_score	CV
0	Logistic Regression	0.826816	0.754098	0.741935	0.747967	0.800685
1	SVM	0.843575	0.793103	0.741935	0.766667	0.810407
2	Decision Tree	0.804469	0.721311	0.709677	0.715447	0.785113
3	Random Forest	0.843575	0.869565	0.645161	0.740741	0.820266
4	Nearest Neighbors	0.815642	0.773585	0.661290	0.713043	0.790826


