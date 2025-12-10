# AI Written Essay Detector
Ensemble model containing the DeBERTa V3 Small NLP and SVM trained and tested on data from Human vs. AI Generated Essay Dataset.
This model is in development for my Data Science Capstone course!

## Example Video

<p align="center">
[![Video Title](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)]([https://www.youtube.com/watch?v=VIDEO_ID](https://youtu.be/k2hspDkF_KQ))
</p>

## Key Features
* **Essay Classification:** analyzes user's essays and classifies them as AI Generated or Human Written
* **Robust Assessment:** uses an ensemble model including and SVM and fine-tuned NLP for better responses
* **Explainability:** outputs a counterfactual explanation to explain the model's decision
* **Data Augmentation:** training data is augmented to improve perfromance on user data

## Installation
* Create free Google account if needed
* Download notebook from Github
* Download Kaggle Dataset from Github
* Upload notebook to Google Colab
* Upload dataset (drag and drop in files side panel)
* Change file name/path to match its name on your device
    * the location in the notebook has a comment to show you!
* Skip the unzip step if the dataset is not a zip folder
* Add code block with to install libraries
```bash
pip install transformers datasets torch evaulate pandas train_test_split sklearn numpy random gradio
```
* An API key will be required at the model training stage
    * Free account with Wandb.AI (https://wandb.ai/authorize?ref=models)
    * Copy API key from website for DeBERTa Model
* These instructions are also in the Colab Notebook

Python Library List:
* transformers
* datasets
* torch
* evaulate
* pandas
* train_test_split
* sklearn
* numpy
* random
* gradio

## Usage
* Run the gradio module
* Paste the link into a search engine
* Copy and paste an essay into the text box
* Select analyze
* View results - the probability that an essay is human written and AI generated

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
* Data augmentation to improve performance with out of domain data
* Text chunking to include the entirety of longer essays
* Counterfactual explanations for explainability


## Model Diagram
Block diagram showing the model's decision design and making process.


<img width="458" height="594" alt="block_diagram" src="https://github.com/user-attachments/assets/8e0fa644-aa8d-4ca2-9851-58be8eb8133b" />


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
**F-Score:** 0.9962264150943396 \\
**Test Loss:** 0.0411
* These values demonstrates high accuracy and recall
* It indicates robust performance

<table>
   <caption>DeBERTa Model Training</caption>
   <tr>
      <th>Epoch</th>
      <th>Training Loss</th>
      <th>Validation Loss</th>
      <th>F1</th>
   </tr>
   <tr>
      <td>1</td>
      <td>0.035400</td>
      <td>0.074584</td>
      <td>0.976923</td>
   </tr>
   <tr>
      <td>2</td>
      <td>0.000000</td>
      <td>0.041144</td>
      <td>0.996226</td>
   </tr>
   <tr>
      <td>3</td>
      <td>0.000000</td>
      <td>0.043746</td>
      <td>0.996226</td>
   </tr>
   <tr>
      <td>4</td>
      <td>0.000000</td>
      <td>0.044825</td>
      <td>0.996226</td>
   </tr>
   <tr>
      <td>5</td>
      <td>0.000000</td>
      <td>0.045017</td>
      <td>0.996226</td>
   </tr>
</table>
<br>


## K-Fold Validation Results

K-fold validation was done on the models to test for overfitting.

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

## Final Step:
* Deploy on Hugging Face
  
