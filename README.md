# 🛡️ Omniscient Software Intelligence Suite

![Version](https://img.shields.io/badge/version-4.1-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)

**An advanced, open-source unified code quality, architecture metrics, and Agile process analytics platform.**

Developed and engineered by **Ahmad Hassan (B-Ted)**.

---

## 📖 Overview

The **Omniscient Software Intelligence Suite** is a unified static analysis and software metrics platform built to handle enterprise-level repositories. Abstracting away language borders, it currently provides deep architectural insights into **Java** and **Python** codebases alongside Agile process tracking in a single, frictionless interface.

It parses Abstract Syntax Trees (ASTs) on the fly to detect design flaws, calculate cyclomatic complexity, estimate effort, and measure technical debt—all without relying on heavy external JVMs or complex build pipelines.

## 🌟 Key Features

- **Omniscient Unified Engine**: A single control center handles multiple file types and languages simultaneously.
- **Deep AST Analysis (Architecture & Smells)**: 
  - Detects God Classes, Feature Envy, Long Methods, and Swiss Army Knife patterns.
  - Verifies Naming Conventions and Javadoc coverage.
- **Code Metrics (Complexity & Maintainability)**:
  - Cyclomatic and Cognitive Complexity mapping.
  - COCOMO Estimation and Defect Density prediction.
  - Halstead Volume and raw Line-of-Code distributions.
- **Agile Process Analytics**:
  - Velocity Tracking, Scope Creep measurement, and Sprint Burndown visualization from raw JSON data.
- **Zero-Coupling Architecture**: Completely modular backend design seamlessly integrated into a reactive Streamlit frontend.

## 🚀 Live Deployment

*Note: Streamlit apps run a Python backend, so while the code is hosted on GitHub, the live application should be deployed via Streamlit Community Cloud rather than static GitHub Pages.*

To deploy this project to the world for free:
1. Push this repository to your public GitHub account.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **New App**, select your GitHub repository, and set the main file path to `app.py`.
4. Click **Deploy**. Your open-source tool is now live!

## 💻 Local Installation

To run the suite locally, ensure you have Python 3.9+ installed.

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Omniscient-Quality-Suite.git
cd Omniscient-Quality-Suite

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the platform
streamlit run app.py
```

## ⚙️ Configuration

The engine allows fine-grained control over strictness through the UI:
- **Refactoring Recommendations**: Toggle dynamic improvement suggestions.
- **Complexity Threshold**: Adjust the ceiling for acceptable method complexity (Default: 10).
- **Detector Toggles**: Selectively enable/disable Design, Implementation, Naming, or Documentation checks to speed up processing or narrow focus.

## 👨‍💻 About the Author

**Ahmad Hassan (B-Ted)** is an Open-Source Software Engineer passionate about code quality, architectural integrity, and building robust tools that empower developers to write cleaner, more maintainable software.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
