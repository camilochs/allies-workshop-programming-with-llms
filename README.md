# LLM Allies for Scientists

A practical workshop for post-doctoral researchers to enhance research productivity with AI.

> **Part of the AI4Science Series** | *Artificial Intelligence in Sustainable Development Goals* Project

**Author:** Camilo Chacón Sartori

## Overview

This workshop teaches scientists how to use Large Language Models (LLMs) as practical tools for daily research tasks. No AI/ML background required - just basic Python familiarity.

**Format**: Google Colab notebooks + Live OpenCode/ Claude Code demos

## Target Audience

- Post-doctoral researchers from non-CS scientific fields
- Basic Python familiarity (can run scripts, understand variables, loops)
- No AI/ML background required

## Workshop Structure

The workshop centers on a single comprehensive notebook that guides participants through all essential concepts:

| Section | Description |
|---------|-------------|
| Setup & Orientation | OpenCode installation and first commands |
| Core Workflow | Data visualization, automation, and complex tasks |
| CLEAR Framework | Principles for effective scientific prompts |
| Progressive Exercises | 28 hands-on exercises from beginner to advanced |
| Reference Materials | Command cheat sheet and troubleshooting guide |

## Quick Start

### Option 1: Google Colab (Recommended)

1. Open the notebooks directly in Google Colab
2. Get an OpenAI API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
3. Add your API key to Colab Secrets (click the key icon in the left sidebar)
4. Run the notebooks!

### Option 2: Local Setup

```bash
# Clone the repository
git clone https://github.com/your-username/code-llm-allies-2026.git
cd code-llm-allies-2026

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your API key
export OPENAI_API_KEY='your-key-here'  # On Windows: set OPENAI_API_KEY=your-key-here

# Launch Jupyter
jupyter notebook
```

## Workshop Notebook

### `00_opencode_tutorial.ipynb` ⭐ **THE WORKSHOP**

This is the complete workshop in a single notebook:

- **Getting Started**: Installation, first commands, exploring projects
- **Data Visualization**: Generate publication-ready plots from natural language
- **Automation**: Data cleaning, batch processing, file organization
- **Complex Tasks**: Multi-step analysis, statistical workflows
- **CLEAR Framework**: Principles for effective scientific prompts
- **28 Progressive Exercises**: From beginner to advanced, organized by skill level
- **Reference**: Command cheat sheet and troubleshooting guide

---

### Extra Material (Optional Self-Study)

For participants who want to learn how to use LLMs via API directly:

- `01_your_first_ai_assistant.ipynb` - API basics, prompt engineering
- `02_data_visualization_with_ai.ipynb` - Generate plots programmatically
- `03_automating_repetitive_tasks.ipynb` - Batch processing scripts
- `04_your_first_ai_agent.ipynb` - Build simple AI agents

### Related Workshop (Advanced)

For a more advanced workshop on LLM-based code generation and evolution techniques:

- **Code Evolution using LLMs and Python** (PyDay BCN 2025): [github.com/camilochs/pydaybcn2025-workshop-code-evolution](https://github.com/camilochs/pydaybcn2025-workshop-code-evolution)

## Sample Data Files

The `data/` folder contains sample datasets from various scientific domains:

### Core Workshop Data
| File | Description | Use Case |
|------|-------------|----------|
| `climate_data.csv` | Temperature, precipitation, CO2 over time | Time series visualization |
| `experiment_results.csv` | Lab experiment data with treatments | Statistical comparisons |
| `survey_responses.csv` | Likert scale responses with demographics | Survey analysis |
| `messy_data.csv` | Intentionally messy data | Data cleaning practice |
| `paper_abstracts.txt` | Scientific abstracts | Text processing |

### Life Sciences
| File | Description | Use Case |
|------|-------------|----------|
| `patient_vitals.csv` | Clinical data: vitals, diagnosis, outcomes | Medical statistics, survival analysis |
| `protein_expression.csv` | Western blot, gene expression, fold changes | Molecular biology analysis |
| `ecological_species.csv` | Species counts, habitats, conservation status | Biodiversity analysis |
| `crop_yield.csv` | Agricultural data: yield, soil, weather | Agricultural research |

### Physical Sciences & Engineering
| File | Description | Use Case |
|------|-------------|----------|
| `astronomy_observations.csv` | Telescope observations, magnitudes, distances | Astronomical data analysis |
| `energy_consumption.csv` | Building energy use, carbon emissions | Energy efficiency studies |

### Computer Science & Technology
| File | Description | Use Case |
|------|-------------|----------|
| `software_bugs.csv` | Bug tracking: severity, resolution time, components | Software engineering metrics |
| `machine_learning_benchmarks.csv` | Model performance: accuracy, F1, training time | ML experiment tracking |
| `shipping_logistics.csv` | Shipment data: routes, costs, delivery times | Operations research |

## Live Demo Prompts (For Instructors)

Example prompts to demonstrate OpenCode capabilities during the workshop:

```
Create a Python script that reads 'experiment_results.csv',
calculates mean and standard deviation for each numeric column
grouped by 'treatment', and generates a bar chart with error bars.
```

```
Read data/climate_data.csv and create a visualization showing
temperature trends over time with a 12-month rolling average.
Make it publication-ready.
```

```
Analyze the experiment_results.csv file:
1. Load and explore the data
2. Compare treatments statistically
3. Create a visualization of the most interesting finding
4. Explain what it means for the research
```

## File Structure

```
code-llm-allies-2026/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 00_opencode_tutorial.ipynb  ← Main workshop
│   └── (01-04: optional extras)
├── data/
│   └── (14 sample datasets)
└── slides/
    └── (optional presentation materials)
```

## Troubleshooting

### "API key not found"
- Ensure your API key is set in Colab Secrets or as an environment variable
- Check that the key starts with `sk-`

### "Rate limit exceeded"
- Wait a minute and try again
- The workshop uses efficient prompts to minimize API calls

### "Generated code has errors"
- The notebooks include `safe_execute()` functions that automatically retry with error correction
- If issues persist, check that your data matches the expected format

## Contributing

Contributions welcome! Please feel free to submit issues or pull requests.

## License

MIT License - feel free to use and adapt for your own workshops.

## Acknowledgments

This workshop is part of the **AI4Science Series**, an initiative within the *Artificial Intelligence in Sustainable Development Goals* project. The series aims to empower researchers across scientific disciplines with practical AI tools to accelerate discovery and innovation.

This workshop was designed for the scientific research community to make AI tools more accessible and practical for daily research tasks.
