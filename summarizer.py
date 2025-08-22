from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


report = """
Patient Name: John Doe
Age: 55
Diagnosis: Type 2 Diabetes
Symptoms: Fatigue, frequent urination, excessive thirst
Lab Results: HbA1c - 8.5%, Fasting glucose - 160 mg/dL
Treatment: Metformin 500mg twice daily
"""


summary = summarizer(report, max_length=100, min_length=30, do_sample=False)


print("=== Summary ===")
print(summary[0]['summary_text'])
