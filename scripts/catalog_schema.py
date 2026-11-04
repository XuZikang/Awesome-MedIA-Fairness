"""Controlled vocabulary for medical algorithm fairness; shared by CI and review."""
MAIN_HEADING = "## 📝 Papers"
TOPIC_HEADING = "## 🧭 By Topic"
RESOURCE_HEADING = "## 🧰 Datasets, Benchmarks and Toolkits"
ALLOWED = {
    "Domain": {"Medical imaging", "EHR and clinical prediction", "Clinical NLP and foundation models", "Physiological signals", "Other biomedical", "Healthcare operations"},
    "Focus": {"Evaluation", "Bias mechanisms", "Mitigation", "Benchmark", "Dataset", "Theory and measurement"},
    "Stage": {"Evaluation", "Pre-processing", "In-processing", "Post-processing", "Multi-stage", "Not applicable", "Not verified"},
    "Attributes": {"Sex and gender", "Age", "Race and ethnicity", "Skin tone", "Socioeconomic status", "Site and geography", "Disability", "Intersectional", "Other", "Not specified"},
    "Assets": {"Code", "Weights", "Project", "Data", "Paper only"},
    "Evidence": {"Primary metadata", "Primary abstract", "Primary full text", "Reviewed source", "Legacy unverified"},
}
TOPICS = ["Fairness Evaluation and Benchmarking", "Bias Mechanisms and Measurement", "Pre-processing Mitigation", "In-processing Mitigation", "Post-processing Mitigation", "Clinical NLP and Foundation Models", "EHR, Physiological Signals and Healthcare", "Mitigation with Unverified Stage"]
