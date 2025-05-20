# Misalignment Injection: Type 2 Processing

This directory contains the pipeline for generating **Type 2 misaligned definitions**, where one axiom from a concept's full definition is intentionally omitted in the natural language description.


## 📁 Files Overview

```
├── processed_type2.json               # Input: ontology terms with one axiom removed
├── type2_description_generation.py    # Uses GPT to generate new, incomplete descriptions
├── type2_description_postprocessing.py# Cleans and restructures GPT output
├── Batchinput.jsonl                   # Prompts sent to GPT
├── Batchoutput.jsonl                  # Raw completions from GPT
├── Generated_description.jsonl        # Cleaned description outputs
├── type2_description_update.json      # Aligned ontology entries with new definitions
├── Final_type2.json                   # Final data used in full pipeline
├── C_example.txt / P_example.txt      # Prompt examples for class and property terms
```


## 🔄 Pipeline Description

### 1. Generate Descriptions with Omitted Axiom

- **Script**: `type2_description_generation.py`  
- **Input**: `processed_type2.json`  
- **Process**:
  - For each ontology term, creates a prompt using axiom subset and example formats.
  - Sends prompts to GPT via API.
  - Saves prompts to `Batchinput.jsonl` and raw outputs to `Batchoutput.jsonl`.

### 2. Post-process GPT Output

- **Script**: `type2_description_postprocessing.py`  
- **Input**: `Batchoutput.jsonl`  
- **Process**:
  - Cleans and reformats descriptions.
  - Saves intermediate results to:
    - `Generated_description.jsonl`
    - `type2_description_update.json`
  - Final usable output is written to:
    - `Final_type2.json` ← used in training/evaluation.


## ✅ Notes

- Only `Final_type2.json` is used in the full dataset pipeline.

