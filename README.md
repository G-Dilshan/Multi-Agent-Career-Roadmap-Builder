# Multi-Agent Career Roadmap Builder

A powerful AI-driven application that generates detailed career roadmaps and learning paths using multiple specialized agents. This tool helps users visualize their career progression and learning journey through interactive mind maps.

## 🌟 Features

- **Interactive Web Interface**: User-friendly Streamlit-based web application
- **Multi-Agent System**: Utilizes specialized AI agents for comprehensive roadmap generation
- **Visual Roadmaps**: Generates detailed mind maps using Graphviz
- **Downloadable Outputs**: Export roadmaps as SVG files
- **Customizable Inputs**: Generate roadmaps for any career path or learning topic

## 🚀 Getting Started

### Prerequisites

- Python 3.10
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/G-Dilshan/Multi-Agent-Career-Roadmap-Builder.git
cd Multi-Agent-Career-Roadmap-Builder
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## 💡 Usage

1. Enter your topic or question in the text input field (e.g., "Roadmap for Machine Learning")
2. Wait for the system to generate your roadmap
3. View the generated mind map
4. Download the roadmap as an SVG file if desired

## 🏗️ Project Structure

```
Multi-Agent-Career-Roadmap-Builder/
├── agents/           # AI agent implementations
├── workflows/        # Processing pipelines
├── tools/           # Custom utilities
├── utils/           # Helper functions
├── data/            # Data storage
├── notebook/        # Development notebooks
├── app.py           # Main Streamlit application
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

For any questions or suggestions, please open an issue in the GitHub repository. 