# ==============================
# 📊 Stock Portfolio Dashboard
# ==============================
# A comprehensive interactive dashboard for portfolio analysis
# Built with Streamlit for real-time analysis

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import os
from datetime import datetime

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Stock Portfolio Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# STYLING
# ==============================
st.markdown("""
    <style>
    .main {
        padding: 0rem 0rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================
# LOAD DATA
# ==============================
@st.cache_data
def load_data():
    """Load portfolio prices from processed data"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "processed", "portfolio_prices_clean.csv")
    
    try:
        prices = pd.read_csv(data_path, index_col=0, parse_dates=True)
        return prices
    except FileNotFoundError:
        st.error(f"Data file not found at {data_path}")
        return None

# Load data
prices = load_data()

if prices is None:
    st.stop()

# ==============================
# SIDEBAR - SETTINGS
# ==============================
st.sidebar.header("⚙️ Portfolio Settings")

# Stock selection
selected_stocks = st.sidebar.multiselect(
    "📈 Select Stocks",
    options=prices.columns.tolist(),
    default=prices.columns.tolist(),
    help="Choose which stocks to analyze"
)

# Safety check
if len(selected_stocks) == 0:
    st.warning("⚠️ Please select at least one stock to analyze")
    st.stop()

# Date range selection
st.sidebar.subheader("📅 Date Range")
min_date = prices.index.min()
max_date = prices.index.max()

start_date = st.sidebar.date_input(
    "Start Date",
    value=min_date,
    min_value=min_date,
    max_value=max_date
)

end_date = st.sidebar.date_input(
    "End Date",
    value=max_date,
    min_value=min_date,
    max_value=max_date
)

# Portfolio weights
st.sidebar.subheader("⚖️ Portfolio Weights")
use_equal_weight = st.sidebar.checkbox("Equal Weight (1/N)", value=True)

if use_equal_weight:
    weights = np.array([1/len(selected_stocks)] * len(selected_stocks))
    st.sidebar.info(f"Each stock: {100/len(selected_stocks):.1f}%")
else:
    weights = st.sidebar.slider(
        "Weight Distribution",
        min_value=0.0,
        max_value=1.0,
        step=0.1,
        key="weights"
    )

# Risk-free rate
risk_free_rate = st.sidebar.slider(
    "Risk-Free Rate (%)",
    min_value=0.0,
    max_value=10.0,
    value=4.0,
    step=0.1
) / 100

# ==============================
# FILTER DATA
# ==============================
filtered_prices = prices[selected_stocks].loc[start_date:end_date]
returns = filtered_prices.pct_change().dropna()

# ==============================
# TITLE & INTRO
# ==============================
st.title("📊 Stock Portfolio Analysis Dashboard")
st.markdown("""
    ### Interactive Portfolio Performance & Risk Analysis
    Analyze your investment portfolio across multiple metrics including returns, 
    volatility, correlations, and risk-adjusted performance.
    """)

st.markdown("---")

# ==============================
# CALCULATIONS
# ==============================
TRADING_DAYS = 252

# Portfolio metrics
portfolio_returns = returns.dot(weights)
portfolio_return = portfolio_returns.mean() * TRADING_DAYS
portfolio_volatility = portfolio_returns.std() * np.sqrt(TRADING_DAYS)
portfolio_sharpe = (portfolio_return - risk_free_rate) / portfolio_volatility if portfolio_volatility > 0 else 0

# Individual stock metrics
stock_returns = returns.mean() * TRADING_DAYS
stock_volatility = returns.std() * np.sqrt(TRADING_DAYS)
stock_sharpe = (stock_returns - risk_free_rate) / stock_volatility

# Cumulative returns
cumulative_portfolio = (1 + portfolio_returns).cumprod()
cumulative_individual = (1 + returns).cumprod()

# ==============================
# KPI METRICS
# ==============================
st.subheader("📊 Portfolio Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Annual Return",
        f"{portfolio_return:.2%}",
        delta=f"{(stock_returns.mean() - portfolio_return):.2%}",
        delta_color="inverse"
    )

with col2:
    st.metric(
        "Volatility (Risk)",
        f"{portfolio_volatility:.2%}",
        help="Standard deviation of returns"
    )

with col3:
    st.metric(
        "Sharpe Ratio",
        f"{portfolio_sharpe:.2f}",
        help="Risk-adjusted returns (higher is better)"
    )

with col4:
    st.metric(
        "Number of Stocks",
        f"{len(selected_stocks)}",
        help="Stocks in portfolio"
    )

st.markdown("---")

# ==============================
# TABS
# ==============================
tab1, tab2, tab3, tab4 = st.tabs(["📈 Prices", "📊 Risk Analysis", "💼 Portfolio", "📉 Metrics Table"])

# ==============================
# TAB 1: PRICE TRENDS
# ==============================
with tab1:
    st.subheader("Stock Price Trends")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Plot with Plotly for interactivity
        fig = go.Figure()
        
        for stock in selected_stocks:
            fig.add_trace(go.Scatter(
                x=filtered_prices.index,
                y=filtered_prices[stock],
                mode='lines',
                name=stock,
                line=dict(width=2)
            ))
        
        fig.update_layout(
            title="Historical Stock Prices",
            xaxis_title="Date",
            yaxis_title="Price ($)",
            hovermode='x unified',
            height=500,
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Price Statistics")
        
        for stock in selected_stocks:
            current_price = filtered_prices[stock].iloc[-1]
            previous_price = filtered_prices[stock].iloc[0]
            change_pct = (current_price - previous_price) / previous_price
            
            st.metric(
                stock,
                f"${current_price:.2f}",
                delta=f"{change_pct:.2%}",
                delta_color="off"
            )

# ==============================
# TAB 2: RISK ANALYSIS
# ==============================
with tab2:
    st.subheader("Correlation Heatmap")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Correlation heatmap
        corr_matrix = returns.corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, square=True, linewidths=1, 
                   cbar_kws={"shrink": 0.8}, ax=ax, vmin=-1, vmax=1)
        ax.set_title('Stock Correlation Matrix', fontsize=14, fontweight='bold')
        
        st.pyplot(fig)
    
    with col2:
        st.markdown("### Correlation Insights")
        
        # Find highest correlations
        corr_pairs = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_pairs.append((
                    corr_matrix.columns[i],
                    corr_matrix.columns[j],
                    corr_matrix.iloc[i, j]
                ))
        
        corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
        
        st.markdown("**Highest Correlations:**")
        for stock1, stock2, corr in corr_pairs[:3]:
            st.write(f"• {stock1}-{stock2}: {corr:.2f}")
    
    st.markdown("---")
    st.subheader("Risk vs Return Analysis")
    
    # Risk vs Return scatter
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=stock_volatility,
        y=stock_returns,
        mode='markers+text',
        text=selected_stocks,
        textposition="top center",
        marker=dict(size=12, color=stock_sharpe, colorscale='Viridis', 
                   showscale=True, colorbar=dict(title="Sharpe Ratio")),
        name='Individual Stocks'
    ))
    
    fig.add_trace(go.Scatter(
        x=[portfolio_volatility],
        y=[portfolio_return],
        mode='markers+text',
        text=['Portfolio'],
        textposition="top center",
        marker=dict(size=20, color='red', symbol='star'),
        name='Portfolio'
    ))
    
    fig.update_layout(
        title="Risk vs Return Profile",
        xaxis_title="Annual Volatility (Risk)",
        yaxis_title="Annual Return",
        hovermode='closest',
        height=500,
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ==============================
# TAB 3: PORTFOLIO
# ==============================
with tab3:
    st.subheader("Portfolio Composition & Growth")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Portfolio Allocation")
        
        pie_data = pd.DataFrame({
            'Stock': selected_stocks,
            'Weight': weights * 100
        })
        
        fig = px.pie(pie_data, values='Weight', names='Stock',
                    title='Portfolio Weights')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Individual Weights")
        
        for stock, weight in zip(selected_stocks, weights):
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.progress(weight, text=f"{weight*100:.1f}%")
            with col_b:
                st.write(stock)
    
    st.markdown("---")
    st.subheader("Portfolio Growth (Cumulative Returns)")
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=cumulative_portfolio.index,
        y=cumulative_portfolio.values,
        fill='tozeroy',
        name='Portfolio',
        line=dict(color='darkblue', width=3)
    ))
    
    fig.update_layout(
        title="Portfolio Value Growth (Starting Value = 1.0)",
        xaxis_title="Date",
        yaxis_title="Cumulative Return",
        hovermode='x unified',
        height=500,
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Portfolio statistics
    st.markdown("### Portfolio Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    total_return = (cumulative_portfolio.iloc[-1] - 1) * 100
    max_return = cumulative_portfolio.max()
    min_return = cumulative_portfolio.min()
    
    with col1:
        st.metric("Total Return", f"{total_return:.1f}%")
    
    with col2:
        st.metric("Peak Value", f"{max_return:.2f}")
    
    with col3:
        st.metric("Lowest Value", f"{min_return:.2f}")

# ==============================
# TAB 4: METRICS TABLE
# ==============================
with tab4:
    st.subheader("Complete Metrics Summary")
    
    # Create metrics dataframe
    metrics_df = pd.DataFrame({
        'Stock': selected_stocks,
        'Annual Return': stock_returns.values,
        'Annual Volatility': stock_volatility.values,
        'Sharpe Ratio': stock_sharpe.values,
        'Max Price': filtered_prices[selected_stocks].max().values,
        'Min Price': filtered_prices[selected_stocks].min().values,
        'Current Price': filtered_prices[selected_stocks].iloc[-1].values
    })
    
    # Format for display
    metrics_display = metrics_df.copy()
    metrics_display['Annual Return'] = metrics_display['Annual Return'].apply(lambda x: f"{x:.2%}")
    metrics_display['Annual Volatility'] = metrics_display['Annual Volatility'].apply(lambda x: f"{x:.2%}")
    metrics_display['Sharpe Ratio'] = metrics_display['Sharpe Ratio'].apply(lambda x: f"{x:.3f}")
    metrics_display['Max Price'] = metrics_display['Max Price'].apply(lambda x: f"${x:.2f}")
    metrics_display['Min Price'] = metrics_display['Min Price'].apply(lambda x: f"${x:.2f}")
    metrics_display['Current Price'] = metrics_display['Current Price'].apply(lambda x: f"${x:.2f}")
    
    st.dataframe(metrics_display, use_container_width=True, hide_index=True)
    
    # Individual stock charts
    st.markdown("---")
    st.subheader("Individual Stock Analysis")
    
    for stock in selected_stocks:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(f"{stock} - Return", f"{stock_returns[stock]:.2%}")
        
        with col2:
            st.metric(f"{stock} - Volatility", f"{stock_volatility[stock]:.2%}")
        
        with col3:
            st.metric(f"{stock} - Sharpe Ratio", f"{stock_sharpe[stock]:.3f}")

# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
    <p>📊 Stock Portfolio Analysis Dashboard | Built with Streamlit</p>
    <p>Data Source: Yahoo Finance | Analysis Period: 2019-2025</p>
    <p>Last Updated: March 2026</p>
    </div>
    """, unsafe_allow_html=True)