import matplotlib.pyplot as plt
import json
# data definition
x_labels = ['AWO', 'DEM@Care', 'Stuff', 'SWO', 'OntoDT', 'Pizza']
metrics = ['Precision', 'Recall', 'F1-Score', 'Cosine Similarity']
values = {}
for metric in metrics:
    values[metric] = []
    for label in x_labels:
        with open(f"unseen_{label}_result.json", 'r') as f:
            data = json.load(f)
            if metric == 'Precision':
                values[metric].append(data["GCQ"]['precision (%)']/100)
            elif metric == 'Recall':
                values[metric].append(data["GCQ"]['recall (%)']/100)
            elif metric == 'F1-Score':
                values[metric].append(data["GCQ"]['f1_score (%)']/100)
            elif metric == 'Cosine Similarity':
                values[metric].append(data["GCQ"]['avg_max_cosine_per_gen'])

x = range(len(x_labels))
bar_width = 0.2
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # colors for each metric

# positions for each metric
positions = {
    metric: [i + idx * bar_width for i in x]
    for idx, metric in enumerate(metrics)
}

# drawing the bar chart
fig, ax = plt.subplots(figsize=(10, 5))
for idx, metric in enumerate(metrics):
    ax.bar(positions[metric], values[metric], width=bar_width, label=metric, color=colors[idx])

# axis settings
ax.set_xticks([i + 1.5 * bar_width for i in x])
ax.set_xticklabels(x_labels, fontsize=10)
ax.set_ylabel("Score", fontsize=11)
ax.set_ylim(0, 1.0)
ax.set_title("Unseen Ontology Performance by Metric", fontsize=12)
ax.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# save the figure
output_path = "unseen_ontology_metrics_bar_chart.pdf"
plt.savefig(output_path, format="pdf")
output_path