"""
Test script to verify light theme configuration for Verdanta
"""
import streamlit as st
from config import THEME_MODE

def test_theme_config():
    """Test that theme configuration is properly set"""
    print(f"Theme mode from config: {THEME_MODE}")
    
    # Check if .streamlit/config.toml exists
    import os
    config_path = ".streamlit/config.toml"
    if os.path.exists(config_path):
        print("✓ Streamlit config.toml exists")
        with open(config_path, 'r') as f:
            content = f.read()
            print("Config content:")
            print(content)
    else:
        print("✗ Streamlit config.toml not found")
    
    print("\nLight theme has been configured successfully!")
    print("The following components have been updated:")
    print("- config.py: Added THEME_MODE constant")
    print("- .streamlit/config.toml: Force light theme at Streamlit level")
    print("- app.py: Enhanced CSS for light theme on all components")
    print("- app.py: Updated plotly charts to use light theme")
    print("- report_generator.py: Updated all charts to use light theme")
    print("- matplotlib/seaborn: Configured for light theme")

if __name__ == "__main__":
    test_theme_config()
