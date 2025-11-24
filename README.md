# AI Written Essay Detector
Ensemble model containing the DeBERTa V3 Small NLP and SVM trained and tested on data from Human vs. AI Generated Essay Dataset.
This model is in development for my Data Science Capstone course!

## Example Video

https://github.com/user-attachments/assets/b913ee6a-0ef6-49b7-bffc-c7672bd03dcf


## How to Run the Model
* Create free Google account if needed
* Download notebook from Github
* Download Kaggle Dataset Github
* Upload notebook to Google Colab
* Upload dataset (drag and drop in files side panel)
* Change file name/path to match yours
    * the location in the notebook has a comment to show you!
* Skip the unzip step if the dataset is not a zip folder
* Add code block with pip install library_name
    * this is to install any required libraries
* API Key
    * Free account with Wandb.AI (https://wandb.ai/authorize?ref=models)
    * Copy API key from website for DeBERTa Model
* These instructions are also in the Colab Notebook

Python Library List:
* transformers
* datasets
* torch
* evaulation
* pandas
* train_test_split
* sklearn


## Objectives:
*  Successfully classify essays as human or AI generated
*  Understand AI writing patterns
*  Help maintain academic integrity

## Currently Completed:
* Dataset importing
* Data pre-processing
* SVM model creation and training
* DeBERTa initial fine-tuning
* K-fold validation for both models
* Create ensemble model
* Gradio front end


## Model Diagram
<img width="512" height="500" alt="Screenshot 2025-11-10 at 3 04 40 PM" src="https://github.com/user-attachments/assets/a52bb807-60a6-47e7-97a4-65357d63072d" />


## Current Performance Metrics:
### SVM
<b>Confusion Matrix: </b>
<br>

<img width="324.5" height="273.5" alt="Support Vector Machine Confusion Matrix" src="https://github.com/user-attachments/assets/e3e5be5c-4894-4f30-835d-9f9e036fc07b" />
<br>

* This confusion matrix further represents the high performance of the SVM individually
* It shows a tendency for Type II errors

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

### DeBERTa V3 Small
<b> F-Score: </b> 0.9962264150943396
* This value demonstrates high accuracy and recall
* It indicates robust performance

<table>
   <caption>DeBERTa Model Training</caption>
   <tr>
      <th>Epoch</th>
      <th>Training Loss</th>
      <th>Validation Loss</th>
   </tr>
   <tr>
      <td>1</td>
      <td>0.008300</td>
      <td>0.026248</td>
   </tr>
   <tr>
      <td>2</td>
      <td>0.010000</td>
      <td>0.019515</td>
   </tr>
   <tr>
      <td>3</td>
      <td>0.000400</td>
      <td>0.017369</td>
   </tr>
</table>
<br>


## K-Fold Validation Results

### SVM

<table>
   <caption>K-fold Validation Results for SVM</caption>
   <tr>
      <th>Fold</th>
      <th>Accuracy Score</th>
   </tr>
   <tr>
      <td>1</td>
      <td>0.9963636363636363</td>
   </tr>
   <tr>
      <td>2</td>
      <td>1.0</td>
   </tr>
   <tr>
      <td>3</td>
      <td>1.0</td>
   </tr>
   <tr>
      <th>4</th>
      <th>0.9981818181818182</th>
   </tr>
   <tr>
      <td>5</td>
      <td>1.0</td>
   </tr>
</table>
<br>

### DeBERTa

<table>
   <caption>K-fold Validation Results for DeBERTa</caption>
   <tr>
      <th>Fold</th>
      <th>Accuracy Score</th>
   </tr>
   <tr>
      <td>1</td>
      <td>0.99818182</td>
   </tr>
   <tr>
      <td>2</td>
      <td>1.0</td>
   </tr>
   <tr>
      <td>3</td>
      <td>0.99818182</td>
   </tr>
   <tr>
      <th>4</th>
      <th>1.0</th>
   </tr>
   <tr>
      <td>5</td>
      <td>0.99818182</td>
   </tr>
</table>
<br>

## Next Steps:
* Fix overfitting and model performance on user data
* Chunk essay data to match token constraints
    * Currently, the longer essays are truncated
* Implement explainability using counterfactual explanations
  
