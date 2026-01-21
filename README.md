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

| Section | Duration | Description |
|---------|----------|-------------|
| Introduction + Setup | 10 min | OpenCode installation and orientation |
| OpenCode Basics | 20 min | First prompts, exploring projects |
| Data Visualization | 25 min | Generate plots from natural language |
| Automation Tasks | 25 min | Data cleaning, batch processing |
| Principles & Best Practices | 15 min | CLEAR framework, when to trust AI |
| Advanced Exercises | 20 min | Lab tools, scientific workflows |
| Q&A + Wrap-up | 10 min | Questions and next steps |

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

## Notebooks

### Main Workshop Material

### 0. OpenCode Tutorial (`00_opencode_tutorial.ipynb`) ⭐ **MAIN NOTEBOOK**
- Practical guide for using OpenCode in the terminal
- Commands synchronized with each workshop notebook
- Progressive exercises from beginner to advanced
- Cheat sheet of effective prompts
- Principles for effective use of code agents
- The CLEAR framework for scientific prompts

---

### Extra Material (Self-Study)

The following notebooks provide additional learning resources for participants who want to dive deeper into using LLMs via API:

### 1. Your First AI Assistant (`01_your_first_ai_assistant.ipynb`)
- Set up OpenAI API access
- Understand prompt engineering basics
- Make your first API call
- Practical exercise: Literature summary and analysis

### 2. Data Visualization with AI (`02_data_visualization_with_ai.ipynb`)
- Load and describe data to an LLM
- Generate matplotlib/seaborn code from natural language
- Iterate on visualizations through conversation
- Build a library of reusable prompts

### 3. Automating Repetitive Tasks (`03_automating_repetitive_tasks.ipynb`)
- Generate data processing scripts from descriptions
- Batch process multiple files with different formats
- Clean messy data with AI assistance
- Create reusable analysis pipelines

### 4. Your First AI Agent (`04_your_first_ai_agent.ipynb`)
- Understand the Agent = LLM + Tools + Loop formula
- Build a research assistant agent with custom tools
- Chain multiple LLM calls for complex analysis
- Create practical agents for scientific workflows

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

## API Costs

This workshop uses `gpt-4o-mini` by default, which is very cost-effective:
- Input: ~$0.15 per 1M tokens
- Output: ~$0.60 per 1M tokens
- **Typical workshop cost: Less than $1 total**

## Live Demo Prompts (For Instructors)

### Demo 1: After Notebook 1
```
Create a Python script that reads 'experiment_results.csv',
calculates mean and standard deviation for each numeric column
grouped by 'treatment', and generates a bar chart with error bars.
```

### Demo 2: During Notebook 2
```
Read data/climate_data.csv and create a visualization showing
temperature trends over time with a 12-month rolling average.
Make it publication-ready.
```

### Demo 3: During Notebook 4
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
│   ├── 00_opencode_tutorial.ipynb
│   ├── 01_your_first_ai_assistant.ipynb
│   ├── 02_data_visualization_with_ai.ipynb
│   ├── 03_automating_repetitive_tasks.ipynb
│   └── 04_your_first_ai_agent.ipynb
├── data/
│   ├── climate_data.csv
│   ├── experiment_results.csv
│   ├── survey_responses.csv
│   ├── messy_data.csv
│   ├── paper_abstracts.txt
│   ├── patient_vitals.csv
│   ├── protein_expression.csv
│   ├── ecological_species.csv
│   ├── crop_yield.csv
│   ├── astronomy_observations.csv
│   ├── energy_consumption.csv
│   ├── software_bugs.csv
│   ├── machine_learning_benchmarks.csv
│   └── shipping_logistics.csv
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
