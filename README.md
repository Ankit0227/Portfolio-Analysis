# 📊 Stock Portfolio Analysis & Risk Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Overview

This project provides a comprehensive analysis of a diversified stock portfolio (AAPL, MSFT, GOOGL, TSLA, JPM, PFE, WMT, VTI) to evaluate performance, risk metrics, and diversification strategy over 6+ years of historical data (2019-2025).

The project includes:

- 📓 **Jupyter Notebook Analysis**: Data exploration, cleaning, and calculation of financial metrics
- 🌐 **Interactive Streamlit Dashboard**: Dynamic visualization and portfolio analysis
- 📊 **Risk Assessment**: Comprehensive evaluation of portfolio volatility and drawdowns
- 💼 **Professional Visualizations**: Publication-ready charts and graphs

---

## 🎯 Project Goals

✅ Analyze historical stock performance (2019-2025)
✅ Calculate key financial metrics (Sharpe ratio, Beta, Max Drawdown)
✅ Evaluate portfolio diversification through correlation analysis
✅ Compare portfolio performance against market benchmarks
✅ Provide data-driven investment insights
✅ Create interactive dashboard for dynamic analysis

---

## 📊 Data & Metrics

### Dataset

- **Time Period**: January 2019 - December 2025 (6+ years)
- **Trading Days**: 1,500+ data points
- **Stocks Analyzed**: 8 stocks across multiple sectors

### Stocks Included

| Stock | Company               | Sector          | Role            |
| ----- | --------------------- | --------------- | --------------- |
| AAPL  | Apple Inc.            | Technology      | Growth          |
| MSFT  | Microsoft Corp.       | Technology      | Growth          |
| GOOGL | Alphabet Inc.         | Technology      | Growth          |
| TSLA  | Tesla Inc.            | Automotive/Tech | High Growth     |
| JPM   | JPMorgan Chase        | Finance         | Diversification |
| PFE   | Pfizer Inc.           | Healthcare      | Defensive       |
| WMT   | Walmart Inc.          | Retail          | Defensive       |
| VTI   | Vanguard Total Market | Index           | Benchmark       |

### Financial Metrics Calculated

- **Annual Return**: Total return per year
- **Annual Volatility**: Standard deviation of returns (risk measure)
- **Sharpe Ratio**: Risk-adjusted returns (higher is better)
- **Beta**: Market sensitivity (1.0 = moves with market)
- **Maximum Drawdown**: Worst loss from peak to trough
- **Correlation Matrix**: Relationships between stocks

---

## 🚀 Key Features

### Data Processing

- ✅ Automated data collection using yfinance library
- ✅ Handling of MultiIndex data structures
- ✅ Missing value imputation and data cleaning
- ✅ Efficient data storage in CSV format

### Analysis Capabilities

- ✅ Historical performance evaluation
- ✅ Risk-return analysis (6+ years of market cycles)
- ✅ Correlation analysis for diversification insights
- ✅ Market sensitivity analysis (Beta calculation)
- ✅ Drawdown analysis showing worst-case scenarios
- ✅ Comparative analysis vs market benchmarks

### Interactive Dashboard

- ✅ Multi-select stock filtering
- ✅ Real-time metric calculations
- ✅ Dynamic correlation heatmaps
- ✅ Interactive price trend visualization
- ✅ Portfolio performance metrics
- ✅ Risk vs return scatter plots

---

## 💼 Dashboard Features

The interactive Streamlit dashboard provides:

### Tab 1: 📈 Price Trends

- View historical stock price movements
- Compare multiple stocks over time
- Identify long-term trends and patterns

### Tab 2: 📊 Risk Analysis

- **Correlation Heatmap**: Understand how stocks move together
- **Risk vs Return Scatter**: Visual analysis of return potential vs volatility
- **Volatility Comparison**: Compare stock riskiness

### Tab 3: 💼 Portfolio Metrics

- **Annual Return**: Expected yearly return percentage
- **Volatility**: Portfolio risk measurement
- **Sharpe Ratio**: Risk-adjusted return metric
- **Portfolio Growth Chart**: Cumulative return visualization

### Settings

- Dynamic stock selection (multi-select)
- Real-time metric recalculation
- Responsive layout for different screen sizes

---

## 🛠 Tech Stack

| Technology   | Purpose                   | Version  |
| ------------ | ------------------------- | -------- |
| Python       | Programming Language      | 3.8+     |
| Pandas       | Data Manipulation         | >=1.5.0  |
| NumPy        | Numerical Computing       | >=1.24.0 |
| Matplotlib   | Static Visualization      | >=3.7.0  |
| Seaborn      | Statistical Visualization | >=0.12.0 |
| Streamlit    | Web Dashboard             | >=1.28.0 |
| Plotly       | Interactive Charts        | >=5.17.0 |
| yfinance     | Financial Data            | >=0.2.28 |
| SciPy        | Statistical Computing     | >=1.10.0 |
| scikit-learn | Machine Learning          | >=1.3.0  |

---

## 📂 Project Structure

```
portfolio-analysis/
│
├── 📁 data/
│   ├── 📁 raw/
│   │   ├── AAPL.csv
│   │   ├── MSFT.csv
│   │   ├── GOOGL.csv
│   │   ├── TSLA.csv
│   │   ├── JPM.csv
│   │   ├── PFE.csv
│   │   ├── WMT.csv
│   │   ├── VTI.csv
│   │   └── portfolio_prices.csv
│   │
│   └── 📁 processed/
│       ├── portfolio_prices_clean.csv
│       ├── daily_returns.csv
│       ├── annual_statistics.csv
│       ├── correlation_matrix.csv
│       ├── metrics_summary.csv
│       └── metrics_summary_formatted.csv
│
├── 📁 notebooks/
│   ├── Stock_Portfolio_Analysis.ipynb
│   └── 📁 .ipynb_checkpoints/
│
├── 📁 dashboard/
│   └── app.py
│
├── 📁 images/
│   ├── price_trends.png
│   ├── risk_return.png
│   ├── correlation_heatmap.png
│   ├── portfolio_growth.png
│   ├── drawdown.png
│   ├── efficient_frontier.png
│   └── efficient_frontier_colored_by_sharpe_ratio.png
│
├── 📁 scripts/
│   ├── download_data.py
│   └── calculate_metrics.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

## 📊 Key Insights

### Performance Findings

- **Tech Dominance**: Technology stocks (AAPL, MSFT, GOOGL) drove majority of portfolio returns
- **High Growth vs Volatility**: TSLA provides high returns but increases volatility significantly
- **Defensive Stability**: WMT and PFE stabilize portfolio during downturns
- **Market Outperformance**: Portfolio performance vs VTI index comparison

### Risk Insights

- **Concentration Risk**: 60% allocated to tech sector creates correlation risk
- **Volatility Patterns**: Tech stocks show 1.5-2.0x market volatility (high beta)
- **Drawdown Recovery**: COVID-19 crash (-34%) took ~12 months to recover
- **Diversification Benefits**: Low correlation stocks (PFE, WMT) provide portfolio protection

### Diversification Analysis

- **High Correlation Pairs**: Tech stocks move together (AAPL-MSFT: 0.85+)
- **Low Correlation Pairs**: Healthcare and Retail move independently
- **Sector Imbalance**: Recommend reducing tech to 35% and adding other sectors

---

## 📸 Visualizations

### Risk vs Return Analysis

![Risk vs Return](images/risk_return.png)
_Scatter plot showing annual return vs volatility for each stock_

### Correlation Heatmap

![Correlation](images/correlation_heatmap.png)
_Heat map showing how stocks move together (red = together, blue = separate)_

### Portfolio Growth

![Growth](images/portfolio_growth.png)
_Cumulative portfolio returns over time_

### Drawdown Analysis

![Drawdown](images/drawdown.png)
_Maximum drawdown from peak showing worst-case scenarios_

### Price Trends

![Prices](images/price_trends.png)
_Historical price movements for all stocks_

---

## 📈 Quick Start

### Run Streamlit Dashboard (Easiest)
```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

### Run Jupyter Notebook
```bash
jupyter notebook notebooks/Stock_Portfolio_Analysis.ipynb

```

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Ankit0227/Portfolio-Analysis.git
cd portfolio-analysis
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Prepare Data

```bash
# Data is already included in the 'data/raw' folder
# If you want to download fresh data, run:
python scripts/download_data.py
```

---

## 🚀 How to Run

### Option 1: Jupyter Notebook (Data Analysis)

```bash
jupyter notebook notebooks/Stock_Portfolio_Analysis.ipynb
```

This opens the interactive notebook where you can see all analysis steps and modify them.

### Option 2: Streamlit Dashboard (Recommended)

```bash
streamlit run dashboard/app.py
```

This launches the interactive web dashboard at `http://localhost:8501`

### Option 3: Command Line

```bash
python scripts/calculate_metrics.py
```

Generates all metrics and saves to processed folder.

---

## 📖 Usage Guide

### Using the Jupyter Notebook

1. Open `notebooks/Stock_Portfolio_Analysis.ipynb`
2. Run cells sequentially (Shift + Enter)
3. Modify stock selection or date range in the first cell
4. All metrics and visualizations are calculated automatically

### Using the Streamlit Dashboard

1. Run `streamlit run dashboard/app.py`
2. Use the sidebar to select stocks
3. Click tabs to view different analyses
4. Charts update in real-time as you change selections

### Customization

- **Change stocks**: Modify the stock list in `app.py` line 20
- **Change date range**: Edit date parameters in notebooks
- **Adjust weights**: Modify weight calculation in `app.py` line 40

---

## 📈 Analysis Workflow

### Phase 1: Data Collection

- Download 6+ years of historical data
- Handle missing values and outliers
- Store in clean CSV format

### Phase 2: Data Cleaning

- Convert MultiIndex to single-level structure
- Impute missing values with forward fill
- Remove duplicates and validate data integrity

### Phase 3: Calculations

- Calculate daily returns (percentage changes)
- Annualize returns and volatility
- Compute Sharpe ratio, Beta, and Max Drawdown
- Generate correlation matrix

### Phase 4: Analysis

- Compare portfolio vs market benchmark
- Identify best/worst performers
- Analyze sector concentration
- Evaluate diversification benefits

### Phase 5: Visualization

- Create 8+ professional charts
- Build interactive dashboard
- Generate comprehensive report

---

## 🔮 Future Improvements

### Short Term (v1.1)

- [ ] Add more stocks to portfolio
- [ ] Implement portfolio rebalancing strategy
- [ ] Add dividend yield analysis
- [ ] Create performance attribution analysis

### Medium Term (v2.0)

- [ ] Portfolio optimization (Markowitz efficient frontier)
- [ ] Monte Carlo simulation for forecasting
- [ ] Machine learning for price prediction
- [ ] Real-time data integration
- [ ] Email alerts for portfolio events

### Long Term (v3.0)

- [ ] Cloud deployment (Streamlit Cloud, AWS)
- [ ] User authentication and portfolio management
- [ ] Multi-currency support
- [ ] Advanced risk models (VaR, CVaR)
- [ ] Integration with trading platforms (Alpaca, Interactive Brokers)
- [ ] Mobile app version

---

## 📚 Learning Resources

### Financial Concepts

- [Investopedia - Sharpe Ratio](https://www.investopedia.com/terms/s/sharperatio.asp)
- [Investopedia - Beta](https://www.investopedia.com/terms/b/beta.asp)
- [Investopedia - Correlation](https://www.investopedia.com/terms/c/correlation.asp)

### Python & Data Science

- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Financial Data

- [yfinance Documentation](https://github.com/ranaroussi/yfinance)
- [Yahoo Finance](https://finance.yahoo.com/)

---

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⚖️ License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Ankit Parkhe**

- GitHub: [@Ankit0227](https://github.com/Ankit0227)
- LinkedIn: [linkedin.com/in/ankit-parkhe](https://www.linkedin.com/in/ankit-parkhe/)
- Email: parkheankit.r@gmail.com
- Portfolio: [github.com/Ankit0227](https://github.com/Ankit0227)

---

## 📞 Support

If you encounter any issues or have questions:

Check the [Issues](https://github.com/Ankit0227/Portfolio-Analysis/issues) page
2. Review the documentation
3. Contact the author

---

## 🙏 Acknowledgments

- Yahoo Finance for providing free historical stock data
- Streamlit for the amazing dashboard framework
- Pandas community for excellent data tools
- All contributors and supporters

---

**Last Updated**: March 2026
**Version**: 1.0.0

```

---

## 3. Enhanced .gitignore
```

# Byte-compiled / optimized / DLL files

**pycache**/
_.py[cod]
_$py.class

# C extensions

\*.so

# Distribution / packaging

.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
_.egg-info/
.installed.cfg
_.egg
MANIFEST

# PyInstaller

_.manifest
_.spec

# Installer logs

pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports

htmlcov/
.tox/
.nox/
.coverage
.coverage._
.cache
nosetests.xml
coverage.xml
_.cover
\*.py,cover
.hypothesis/
.pytest_cache/

# Translations

_.mo
_.pot

# Django stuff:

\*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:

instance/
.webassets-cache

# Scrapy stuff:

.scrapy

# Sphinx documentation

docs/\_build/

# PyBuilder

target/

# Jupyter Notebook

.ipynb_checkpoints
\*.ipynb

# IPython

profile_default/
ipython_config.py

# pyenv

.python-version

# pipenv

Pipfile.lock

# PEP 582

**pypackages**/

# Celery stuff

celerybeat-schedule
celerybeat.pid

# SageMath parsed files

\*.sage.py

# Environments

.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings

.spyderproject
.spyproject

# Rope project settings

.ropeproject

# mkdocs documentation

/site

# mypy

.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker

.pyre/

# IDE settings

.vscode/
.idea/
_.swp
_.swo
\*~
.DS_Store

# Data files (keep processed, ignore raw if too large)

data/raw/\*.csv
!data/processed/

# Temporary files

_.tmp
_.temp

# OS specific files

.DS_Store
Thumbs.db

# Streamlit settings

.streamlit/secrets.toml

# Media files (if storing images)

# \*.png

# \*.jpg

# \*.jpeg

# Environment variables

.env.local
.env.\*.local

# Cache directories

.cache/
\*.cache

# Backup files

_.bak
_.backup
\*~

# Archives

_.zip
_.rar
_.7z
_.tar.gz

# Project specific

config.local.py
secrets.py
\*.credentials
token.pkl
