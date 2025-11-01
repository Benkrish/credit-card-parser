import os
import streamlit as st
import pdfplumber
import json

# --- Import ALL 5 of your parser classes ---
from parser.chase_parser import ChaseParser
from parser.amex_parser import AmexParser
from parser.bofa_parser import BofAParser
from parser.citi_parser import CitiParser
from parser.capitalone_parser import CapitalOneParser

# --- (Keep your 'get_pdf_text' function exactly as it was) ---

def get_pdf_text(filepath_or_buffer):
    
    full_text = ""
    try:
        with pdfplumber.open(filepath_or_buffer) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:  
                    full_text += text + "\n"  
        return full_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None


def get_parser(pdf_text):
   
    pdf_text_upper = pdf_text.upper()

    if "CHASE" in pdf_text_upper:
        st.info("Chase statement identified.")
        return ChaseParser(pdf_text)
        
    elif "AMERICAN EXPRESS" in pdf_text_upper:
        st.info("American Express statement identified.")
        return AmexParser(pdf_text)
    
    elif "BANK OF AMERICA" in pdf_text_upper:
        st.info("Bank of America statement identified.")
        return BofAParser(pdf_text)

    elif "CITI" in pdf_text_upper:
        st.info("Citi statement identified.")
        return CitiParser(pdf_text)
        
    elif "CAPITAL ONE" in pdf_text_upper:
        st.info("Capital One statement identified.")
        return CapitalOneParser(pdf_text)
    
    else:
        st.error("Error: Unknown statement type. No matching parser found.")
        return None


st.set_page_config(layout="centered", page_title="CC Statement Parser")
st.title("💳 Credit Card Statement Parser")
st.write("Upload a PDF statement to extract key data. This demo supports 5 major banks.")

uploaded_file = st.file_uploader("Upload your statement", type="pdf")

if uploaded_file is not None:
    st.write("---")
    
    with st.spinner("Reading PDF..."):
        raw_text = get_pdf_text(uploaded_file)
    
    if raw_text:
        parser = get_parser(raw_text)
        
        if parser:
            with st.spinner("Extracting data..."):
                data = parser.parse()
            
            if data:
                st.success("Successfully extracted data!")
                
                st.subheader("📊 Extracted Data")
                
                col1, col2 = st.columns(2)
                col1.metric("Issuer", data.get('issuer', 'N/A'))
                col2.metric("Card Variant", data.get('card_variant', 'N/A'))
                
                col3, col4 = st.columns(2)
                col3.metric("Last 4 Digits", data.get('last_4_digits', 'N/A'))
                col4.metric("Payment Due Date", data.get('due_date', 'N/A'))
                
                st.metric("Total Balance Due", f"${data.get('total_balance', '0.00')}")
                with st.expander("Show Raw JSON Output"):
                    st.json(data)
            else:
                st.error("Parsing failed. Could not extract data.")