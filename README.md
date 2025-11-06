## AI Written Essay Detector
Ensemble model containing the DeBERTa V3 Small NLP and SVM trained and tested on data from Human vs. AI Generated Essay Dataset.
In development for my Data Science Capstone class!

#### Objectives:
*  Successfully classify essays as human or AI generated
*  Understand AI writing patterns
*  Help maintain academic integrity

#### Currently Completed:
* Dataset importing
* Data pre-processing
* SVM model creation and training
* DeBERTa initial fine-tuning

### Current Performance Metrics:
##### SVM
<b>Confusion Matrix: </b>
<br>

<img width="324.5" height="273.5" alt="Support Vector Machine Confusion Matrix" src="https://github.com/user-attachments/assets/e3e5be5c-4894-4f30-835d-9f9e036fc07b" />
<br>

* This confusion matrix further represents the high performance of the SVM individually
* It shows a tendency for Type II errors

<br>
<b> Accuracy Metrics </b>
<br>

<table>
   <caption>Accuracy Metrics for SVM</caption>
   <tr>
      <th>Metric</th>
      <th>Value</th>
   </tr>
   <tr>
      <td>Accuracy</td>
      <td>0.99636</td>
   </tr>
   <tr>
      <td>Precision</td>
      <td>1.0</td>
   </tr>
   <tr>
      <td>Recall</td>
      <td>0.99248</td>
   </tr>
</table>
<br>

##### DeBERTa V3 Small
<b>F-Score: </b> 0.9962264150943396
* This value demonstrates high accuracy and recall
* It indicates robust performance
<br>

#### Next Steps:
* Chunk essay data to match token constraints
    * Currently, the longer essays are truncated
* Combine both models into more robust ensemble model
* Implement explainability using counterfactual explanations
* Use Gradio to develop a front-end that allows user input
  
