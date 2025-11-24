import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib
import numpy as np
import gradio as gr

# load DeBERTa model
print("Loading DeBERTa model...")
tokenizer = AutoTokenizer.from_pretrained("./content/deberta-ai-detector")
bert_model = AutoModelForSequenceClassification.from_pretrained("./content/deberta-ai-detector")

# Load SVM model
print("Loading SVM model...")
svm_model = joblib.load('./content/svm_model.pkl')
vectorizer = joblib.load('./content/vectorizer.pkl')

print("Models loaded successfully!")

LABELS = ["Human-written", "AI-written"]

def ensemble_predict(texts, svm_model, vectorizer, tokenizer, bert_model, alpha=0.5):
    # SVM prediction
    X_tfidf = vectorizer.transform(texts)
    svm_proba = svm_model.predict_proba(X_tfidf)

    # DeBERTa prediction
    tokens = tokenizer(
        texts,
        truncation=True,
        padding=True,
        max_length=512,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = bert_model(**tokens)
        bert_proba = torch.softmax(outputs.logits, dim=1).cpu().numpy()

    # weighted average
    final_proba = alpha * svm_proba + (1 - alpha) * bert_proba
    preds = np.argmax(final_proba, axis=1)

    return preds, svm_proba, bert_proba, final_proba

def gradio_predict(text):
    preds, svm_proba, bert_proba, final_proba = ensemble_predict(
        [text], svm_model, vectorizer, tokenizer, bert_model, alpha=0.5
    )

    output = {
        "Ensemble Prediction": LABELS[preds[0]],
        "Ensemble Probabilities": {
            "Human": float(final_proba[0][0]),
            "AI": float(final_proba[0][1]),
        },
        "SVM Probabilities": {
            "Human": float(svm_proba[0][0]),
            "AI": float(svm_proba[0][1]),
        },
        "DeBERTa Probabilities": {
            "Human": float(bert_proba[0][0]),
            "AI": float(bert_proba[0][1]),
        }
    }
    return output

# launch gradio interface
demo = gr.Interface(
    fn=gradio_predict,
    inputs=gr.Textbox(lines=10, placeholder="Paste text here..."),
    outputs=gr.JSON(label="Prediction Details"),
    title="AI Writing Detector (SVM + DeBERTa Ensemble)",
    description="Probability-averaged ensemble combining TF-IDF SVM and DeBERTa."
)

demo.launch()