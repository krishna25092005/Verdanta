# Verdanta - Carbon Accounting & Reporting Tool

![Verdanta Logo](https://img.shields.io/badge/Verdanta-Carbon%20Accounting-4CAF50?style=for-the-badge)

A lightweight, multilingual carbon accounting and reporting tool designed specifically for Small and Medium Enterprises (SMEs) in Asia. Verdanta provides AI-powered insights to help businesses track, analyze, and reduce their carbon footprint while ensuring compliance with global regulations.

## 🌍 Overview

Verdanta empowers SMEs to take control of their carbon emissions through:
- **Comprehensive Tracking**: Monitor Scope 1, 2, and 3 emissions across all business operations
- **AI-Powered Insights**: Get intelligent recommendations for data classification, offset strategies, and emission reduction
- **Regulatory Compliance**: Stay compliant with EU CBAM, Japan GX League, and Indonesia ETS regulations
- **Enterprise-Grade Features**: Multi-location tracking, data quality indicators, and verification status
- **Dark Theme UI**: Professional, modern interface optimized for long working sessions

## ✨ Features

### 📊 Dashboard & Analytics
- Real-time emissions tracking and visualization
- Interactive charts for scope breakdown, category analysis, and time-series data
- Comprehensive metrics with trend analysis
- Enterprise-grade reporting capabilities

### 🤖 AI-Powered Insights (5 Modules)
1. **Data Assistant** - Smart emission classification and scope mapping
2. **Report Summary Generator** - Automated narrative reports from raw data
3. **Offset Advisor** - Personalized carbon offset recommendations
4. **Regulation Radar** - Real-time regulatory compliance insights
5. **Emission Optimizer** - AI-driven reduction strategies and implementation tracking

### 📝 Data Management
- Manual data entry with intelligent validation
- CSV bulk upload with enterprise field mapping
- Data quality indicators (Low/Medium/High)
- Verification status tracking (Unverified/Internal/Third-party)
- Multi-facility and multi-project tracking

### 🌐 Multilingual Support
- English and Hindi language support
- Localized content and interface elements
- Cultural adaptation for Asian markets

### 🏢 Enterprise Features
- Business unit and project categorization
- Facility-level tracking with geographic data
- Responsible person assignment
- Cost tracking with multi-currency support
- Implementation plan management

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip (Python package manager)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/krishna25092005/Verdanta.git
cd Verdanta
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Access the application**
Open your browser and navigate to `http://localhost:8501`

## 📋 Usage Guide

### Getting Started
1. **Language Selection**: Choose your preferred language (English/Hindi)
2. **Add Emissions Data**: 
   - Use manual entry for detailed tracking
   - Upload CSV for bulk data import
3. **Explore AI Insights**: Access the 5 AI modules for intelligent recommendations
4. **Monitor Dashboard**: Track progress and analyze trends

### Data Entry Best Practices
- **Scope Classification**: 
  - Scope 1: Direct emissions (fuel combustion, fleet vehicles)
  - Scope 2: Indirect emissions (purchased electricity, steam)
  - Scope 3: Value chain emissions (business travel, purchased goods)
- **Data Quality**: Aim for "High" quality with measured data
- **Regular Updates**: Input data monthly for accurate trend analysis

### AI Insights Usage
- **Data Assistant**: Get help classifying complex emission sources
- **Report Summary**: Generate executive summaries for stakeholders
- **Offset Advisor**: Find verified carbon offset projects
- **Regulation Radar**: Stay updated on regulatory requirements
- **Emission Optimizer**: Get actionable reduction recommendations

## 🛠️ Technical Architecture

### Technology Stack
- **Frontend**: Streamlit with custom CSS styling
- **Backend**: Python with pandas for data processing
- **AI Engine**: CrewAI with Groq LLM integration
- **Visualization**: Plotly for interactive charts
- **Data Storage**: JSON files with backup mechanisms
- **Deployment**: Docker-ready with environment configuration

### Project Structure
```
verdanta/
├── app.py                 # Main Streamlit application
├── ai_agents.py          # AI agents and CrewAI integration
├── config.py             # Configuration settings
├── data_handler.py       # Data processing utilities
├── emission_factors.py   # Emission factor database
├── report_generator.py   # PDF/CSV report generation
├── requirements.txt      # Python dependencies
├── pyproject.toml       # Project metadata
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── data/
│   └── emissions.json   # Emissions data storage
└── README.md           # This file
```

### Key Components
- **Multi-agent AI System**: Specialized agents for different tasks
- **Dark Theme UI**: Professional styling with high contrast
- **Responsive Design**: Optimized for desktop and tablet use
- **Error Handling**: Comprehensive validation and fallback mechanisms

## 🔧 Configuration

### Environment Variables
```env
# Required
GROQ_API_KEY=your_groq_api_key_here

# Optional
THEME_MODE=dark
APP_VERSION=1.0.0
```

### Streamlit Configuration
The `.streamlit/config.toml` file contains:
- Dark theme settings
- Server configuration
- UI preferences

## 📈 Supported Emission Categories

### Scope 1 (Direct Emissions)
- Stationary Combustion (boilers, furnaces, generators)
- Mobile Combustion (company vehicles, fleet)
- Fugitive Emissions (refrigerants, SF6)
- Process Emissions (industrial processes)

### Scope 2 (Indirect Energy)
- Electricity consumption
- Steam and heating
- Cooling systems

### Scope 3 (Value Chain)
- Business travel and employee commuting
- Purchased goods and services
- Upstream/downstream transportation
- Waste generated in operations
- End-of-life treatment of products

## 🌏 Regional Compliance

### Supported Regulatory Frameworks
- **EU CBAM**: Carbon Border Adjustment Mechanism
- **Japan GX League**: Green Transformation initiatives
- **Indonesia ETS/ETP**: Emissions Trading System

### Default Emission Factors
Pre-configured for major Asian markets:
- India: Grid electricity, transportation, industrial processes
- Indonesia: Regional energy mix and industrial factors
- Japan: Advanced economy emission factors

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Code formatting
black app.py ai_agents.py

# Linting
flake8 *.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author & Support

**Krishna Chauhan**
- Email: krishna.chauhan4@s.amity.edu
- LinkedIn: [Your LinkedIn Profile]
- GitHub: [Your GitHub Profile]

### Getting Help
- 📖 Documentation: Check this README and code comments
- 🐛 Bug Reports: Open an issue on GitHub
- 💡 Feature Requests: Open an issue with the "enhancement" label
- 💬 Questions: Use GitHub Discussions

## 🔮 Roadmap

### Version 1.1 (Planned)
- [ ] REST API for third-party integrations
- [ ] Mobile app for field data collection
- [ ] Advanced analytics with machine learning
- [ ] Multi-tenant support for consultants

### Version 1.2 (Future)
- [ ] Blockchain-based verification
- [ ] IoT sensor integration
- [ ] Real-time emissions monitoring
- [ ] Supply chain emissions tracking

## 🏆 Acknowledgments

- **CrewAI Team**: For the powerful multi-agent framework
- **Streamlit**: For the excellent web app framework
- **Groq**: For fast and reliable LLM inference
- **Asian SME Community**: For feedback and requirements gathering

## 📊 Project Statistics

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)

---

**Made with ❤️ for sustainable business practices**

*Empowering SMEs to build a carbon-neutral future through intelligent technology*
