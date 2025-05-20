# VSPO: Competency Question Generation from Ontologies

This repository contains the official implementation of our research on **automatic Competency Question (CQ) generation** from OWL ontologies. It supports both template-based and LLM-based approaches, incorporating dataset construction, fine-tuning, and evaluation.

## 📁 Directory Structure

```
├── Experiments/                    # Evaluation metrics and analysis of model predictions
├── Fine-tuning/                   # LLM fine-tuning code and inference results
├── Misalignment Injection/        # Dataset generation with misalignment scenarios
├── Template-based CQ generation/  # CQ generation via axiom templates and ontology processing
├── README.md                      # Project overview (this file)
└── requirements.txt               # Python dependencies
```


## 🧱 Modules Overview

### 1. Template-based CQ generation

Implements the pipeline for rule-based CQ generation from ontologies using templates.

- **Ontology preprocessing**: Extracts axioms related to each property/class.
- **Template-based CQ generation**: Applies logic-based templates to produce natural language CQs.

### 2. Misalignment Injection

Constructs a dataset by introducing semantic mismatches between ontology axioms and natural language descriptions.

- **Injection strategies**: Removal, modification of axiom terms.
- Helps train models that can detect or correct inconsistencies.
- Output is used for both training and evaluation.

### 3. Fine-tuning

Fine-tunes LLMs (e.g., LLaMA) using LoRA adapters on the generated datasets.

- Includes training configurations, checkpoints, and inference scripts.
- Outputs model predictions for evaluation on test splits.

### 4. Experiments

Analyzes generated CQs and model performance:

- **Semantic similarity**: Measures alignment between generated and golden semantic pitfall CQs.
- Outputs are saved for comparison between baseline models and fine-tuned models.


## ✅ Requirements

Install all dependencies via:

```bash
pip install -r requirements.txt
```


