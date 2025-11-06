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
#### SVM
<b>Confusion Matrix: </b>
<img width="649" height="547" alt="svm_cm_1" src="https://github.com/user-attachments/assets/e3e5be5c-4894-4f30-835d-9f9e036fc07b" />


#### Next Steps:
* Chunk essay data to match token constraints
    * Currently, the longer essays are truncated
* Combine both models into more robust ensemble model
* Implement explainability using counterfactual explanations
* Use Gradio to develop a front-end that allows user input
  
