# ==========================================================
# SMARTLOAN INDIA - LOAN DATA
# ==========================================================
# IMPORTANT:
# Values below are intended for comparison/educational use.
# Bank policies, rates, eligibility and limits can change.
# Always verify the latest terms on the official bank website.
# ==========================================================


# ==========================================================
# BANK LIST
# ==========================================================

BANKS = [
    "SBI",
    "HDFC Bank",
    "ICICI Bank",
    "Axis Bank",
    "Kotak Mahindra Bank",
    "Bank of Baroda",
    "Punjab National Bank",
    "Canara Bank",
    "Union Bank of India",
    "Indian Bank",
    "Bank of India",
    "Bank of Maharashtra",
    "IDFC FIRST Bank",
    "Federal Bank",
    "IndusInd Bank",
    "YES Bank",
]


# ==========================================================
# OFFICIAL BANK WEBSITES
# ==========================================================

BANK_WEBSITES = {

    "SBI":
        "https://sbi.bank.in/",

    "HDFC Bank":
        "https://www.hdfc.bank.in/",

    "ICICI Bank":
        "https://www.icici.bank.in/",

    "Axis Bank":
        "https://www.axisbank.com/",

    "Kotak Mahindra Bank":
        "https://www.kotak.bank.in/",

    "Bank of Baroda":
        "https://www.bankofbaroda.in/",

    "Punjab National Bank":
        "https://www.pnbindia.in/",

    "Canara Bank":
        "https://www.canarabank.com/",

    "Union Bank of India":
        "https://www.unionbankofindia.bank.in/",

    "Indian Bank":
        "https://www.indianbank.in/",

    "Bank of India":
        "https://bankofindia.co.in/",

    "Bank of Maharashtra":
        "https://bankofmaharashtra.in/",

    "IDFC FIRST Bank":
        "https://www.idfcfirstbank.com/",

    "Federal Bank":
        "https://www.federalbank.co.in/",

    "IndusInd Bank":
        "https://www.indusind.com/",

    "YES Bank":
        "https://www.yesbank.in/",
}


# ==========================================================
# HELPER
# ==========================================================

def product(
    available=True,
    min_amount=None,
    max_amount=None,
    interest_rate=None,
    rate_text=None,
    max_tenure=None,
    amount_text=None,
    eligibility_text=None,
    source="Official bank website",
    source_url=None
):
    return {
        "available": available,
        "min_amount": min_amount,
        "max_amount": max_amount,
        "interest_rate": interest_rate,
        "rate_text": rate_text,
        "max_tenure": max_tenure,
        "amount_text": amount_text,
        "eligibility_text": eligibility_text,
        "source": source,
        "source_url": source_url,
    }


# ==========================================================
# LOAN DATA
# ==========================================================

LOAN_DATA = {

    # ======================================================
    # PERSONAL LOAN
    # ======================================================

    "Personal Loan": {

        "SBI": product(
            max_amount=3500000,
            amount_text="Up to ₹35 lakh",
            source_url=BANK_WEBSITES["SBI"]
        ),

        "HDFC Bank": product(
            min_amount=25000,
            max_amount=4000000,
            amount_text="₹25,000 – ₹40 lakh",
            rate_text="From 9.99%",
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            min_amount=50000,
            max_amount=5000000,
            interest_rate=10.60,
            rate_text="10.60% – 16.50%",
            max_tenure=6,
            amount_text="₹50,000 – ₹50 lakh",
            source_url=BANK_WEBSITES["ICICI Bank"]
        ),

        "Axis Bank": product(
            max_amount=4000000,
            amount_text="Up to ₹40 lakh",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            amount_text="Amount depends on eligibility",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            amount_text="Amount depends on eligibility",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            amount_text="Scheme / eligibility based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            amount_text="Scheme / eligibility based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            amount_text="Scheme / eligibility based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            amount_text="Scheme / eligibility based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            amount_text="Scheme / eligibility based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            amount_text="Scheme / eligibility based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            amount_text="Amount depends on eligibility",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            amount_text="Amount depends on eligibility",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            amount_text="Amount depends on eligibility",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            amount_text="Amount depends on eligibility",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },


    # ======================================================
    # EDUCATION LOAN
    # ======================================================

    "Education Loan": {

        "SBI": product(
            max_amount=5000000,
            rate_text="Scheme dependent",
            amount_text="Up to ₹50 lakh without security for selected premier institutes; other schemes are need-based",
            source_url="https://sbi.bank.in/web/personal-banking/loans/education-loans"
        ),

        "HDFC Bank": product(
            max_amount=15000000,
            amount_text="Up to ₹1.5 crore",
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            amount_text="Up to ₹2 crore in India / up to ₹3 crore abroad, subject to eligibility",
            source_url=BANK_WEBSITES["ICICI Bank"]
        ),

        "Axis Bank": product(
            max_amount=15000000,
            amount_text="Up to ₹1.5 crore",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            amount_text="Scheme / eligibility based",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            amount_text="Scheme / course / institution based",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            amount_text="Scheme / course / institution based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            amount_text="Scheme / course / institution based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            amount_text="Scheme / course / institution based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            amount_text="Scheme / course / institution based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            amount_text="Scheme / course / institution based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            amount_text="Scheme / course / institution based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            amount_text="Course / institution / eligibility based",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            amount_text="Course / institution / eligibility based",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            amount_text="Course / institution / eligibility based",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            amount_text="Course / institution / eligibility based",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },


    # ======================================================
    # HOME LOAN
    # ======================================================

    "Home Loan": {

        "SBI": product(
            amount_text="Amount depends on property, income and eligibility",
            max_tenure=30,
            source_url=BANK_WEBSITES["SBI"]
        ),

        "HDFC Bank": product(
            amount_text="Amount depends on property value and eligibility",
            max_tenure=30,
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            max_amount=50000000,
            max_tenure=30,
            amount_text="Up to ₹5 crore",
            source_url=BANK_WEBSITES["ICICI Bank"]
        ),

        "Axis Bank": product(
            max_amount=50000000,
            max_tenure=30,
            amount_text="Up to ₹5 crore",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            max_tenure=30,
            amount_text="Property / eligibility based",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },


    # ======================================================
    # CAR LOAN
    # ======================================================

    "Car Loan": {

        "SBI": product(
            min_amount=100000,
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["SBI"]
        ),

        "HDFC Bank": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            max_amount=10000000,
            interest_rate=9.10,
            max_tenure=7,
            amount_text="Up to ₹1 crore",
            rate_text="Starting 9.10%",
            source_url="https://www.icici.bank.in/personal-banking/loans/car-loan"
        ),

        "Axis Bank": product(
            min_amount=100000,
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            max_tenure=7,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },


    # ======================================================
    # TWO-WHEELER LOAN
    # ======================================================

    "Two-Wheeler Loan": {

        "SBI": product(
            min_amount=50000,
            max_amount=300000,
            amount_text="₹50,000 – ₹3 lakh",
            source_url=BANK_WEBSITES["SBI"]
        ),

        "HDFC Bank": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            max_amount=3000000,
            max_tenure=3,
            amount_text="Up to ₹30 lakh",
            rate_text="Product dependent",
            source_url="https://www.icici.bank.in/personal-banking/loans"
        ),

        "Axis Bank": product(
            max_tenure=4,
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            amount_text="Vehicle / eligibility based",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },


    # ======================================================
    # GOLD LOAN
    # ======================================================

    "Gold Loan": {

        "SBI": product(
            min_amount=20000,
            max_amount=10000000,
            max_tenure=3,
            amount_text="₹20,000 – ₹1 crore",
            source_url="https://sbi.bank.in/web/personal-banking/loans/gold-loan/personal-gold-loans"
        ),

        "HDFC Bank": product(
            amount_text="Gold value / eligibility based",
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            min_amount=200000,
            max_amount=20000000,
            max_tenure=1,
            amount_text="₹2 lakh/₹3 lakh minimum depending on location/customer; up to ₹2 crore",
            rate_text="8.55% – 16.50%",
            source_url="https://www.icici.bank.in/personal-banking/loans/gold-loan"
        ),

        "Axis Bank": product(
            min_amount=50001,
            max_amount=4000000,
            max_tenure=3,
            amount_text="₹50,001 – ₹40 lakh",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            amount_text="Gold value / eligibility based",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            amount_text="Gold value / scheme based",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            amount_text="Gold value / scheme based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            amount_text="Gold value / scheme based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            amount_text="Gold value / scheme based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            amount_text="Gold value / scheme based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            amount_text="Gold value / scheme based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            amount_text="Gold value / scheme based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            amount_text="Gold value / eligibility based",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            amount_text="Gold value / eligibility based",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            amount_text="Gold value / eligibility based",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            amount_text="Gold value / eligibility based",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },


    # ======================================================
    # BUSINESS LOAN
    # ======================================================

    "Business Loan": {

        "SBI": product(
            amount_text="Scheme / business eligibility based",
            source_url=BANK_WEBSITES["SBI"]
        ),

        "HDFC Bank": product(
            amount_text="Business profile / eligibility based",
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            amount_text="Business profile / eligibility based",
            source_url=BANK_WEBSITES["ICICI Bank"]
        ),

        "Axis Bank": product(
            amount_text="Business profile / eligibility based",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            amount_text="Business profile / eligibility based",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            amount_text="Scheme / business eligibility based",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            amount_text="Scheme / business eligibility based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            amount_text="Scheme / business eligibility based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            amount_text="Scheme / business eligibility based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            amount_text="Scheme / business eligibility based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            amount_text="Scheme / business eligibility based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            amount_text="Scheme / business eligibility based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            amount_text="Business profile / eligibility based",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            amount_text="Business profile / eligibility based",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            amount_text="Business profile / eligibility based",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            amount_text="Business profile / eligibility based",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },


    # ======================================================
    # LOAN AGAINST PROPERTY
    # ======================================================

    "Loan Against Property": {

        "SBI": product(
            min_amount=1000000,
            max_amount=75000000,
            amount_text="₹10 lakh – ₹7.5 crore",
            source_url=BANK_WEBSITES["SBI"]
        ),

        "HDFC Bank": product(
            amount_text="Property value / eligibility based",
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            amount_text="Property value / eligibility based",
            source_url=BANK_WEBSITES["ICICI Bank"]
        ),

        "Axis Bank": product(
            amount_text="Property value / eligibility based",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            amount_text="Property value / eligibility based",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            amount_text="Property value / scheme based",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            amount_text="Property value / scheme based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            amount_text="Property value / scheme based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            amount_text="Property value / scheme based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            amount_text="Property value / scheme based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            amount_text="Property value / scheme based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            amount_text="Property value / scheme based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            amount_text="Property value / eligibility based",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            amount_text="Property value / eligibility based",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            amount_text="Property value / eligibility based",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            amount_text="Property value / eligibility based",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },


    # ======================================================
    # AGRICULTURE LOAN
    # ======================================================

    "Agriculture Loan": {

        "SBI": product(
            amount_text="Varies by agricultural product",
            source_url=BANK_WEBSITES["SBI"]
        ),

        "HDFC Bank": product(
            amount_text="Crop / farm / eligibility based",
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            amount_text="Agricultural product / eligibility based",
            source_url=BANK_WEBSITES["ICICI Bank"]
        ),

        "Axis Bank": product(
            amount_text="Agricultural product / eligibility based",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            amount_text="Agricultural product / eligibility based",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            amount_text="Crop / agricultural scheme based",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            amount_text="Crop / agricultural scheme based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            amount_text="Crop / agricultural scheme based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            amount_text="Crop / agricultural scheme based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            amount_text="Crop / agricultural scheme based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            amount_text="Crop / agricultural scheme based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            amount_text="Crop / agricultural scheme based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            amount_text="Agricultural product / eligibility based",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            amount_text="Agricultural product / eligibility based",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            amount_text="Agricultural product / eligibility based",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            amount_text="Agricultural product / eligibility based",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },


    # ======================================================
    # CONSUMER DURABLE LOAN
    # ======================================================

    "Consumer Durable Loan": {

        "SBI": product(
            amount_text="Product / eligibility based",
            source_url=BANK_WEBSITES["SBI"]
        ),

        "HDFC Bank": product(
            amount_text="Product / eligibility based",
            source_url=BANK_WEBSITES["HDFC Bank"]
        ),

        "ICICI Bank": product(
            amount_text="Product / eligibility based",
            source_url=BANK_WEBSITES["ICICI Bank"]
        ),

        "Axis Bank": product(
            amount_text="Product / eligibility based",
            source_url=BANK_WEBSITES["Axis Bank"]
        ),

        "Kotak Mahindra Bank": product(
            amount_text="Product / eligibility based",
            source_url=BANK_WEBSITES["Kotak Mahindra Bank"]
        ),

        "Bank of Baroda": product(
            amount_text="Product / scheme based",
            source_url=BANK_WEBSITES["Bank of Baroda"]
        ),

        "Punjab National Bank": product(
            amount_text="Product / scheme based",
            source_url=BANK_WEBSITES["Punjab National Bank"]
        ),

        "Canara Bank": product(
            amount_text="Product / scheme based",
            source_url=BANK_WEBSITES["Canara Bank"]
        ),

        "Union Bank of India": product(
            amount_text="Product / scheme based",
            source_url=BANK_WEBSITES["Union Bank of India"]
        ),

        "Indian Bank": product(
            amount_text="Product / scheme based",
            source_url=BANK_WEBSITES["Indian Bank"]
        ),

        "Bank of India": product(
            amount_text="Product / scheme based",
            source_url=BANK_WEBSITES["Bank of India"]
        ),

        "Bank of Maharashtra": product(
            amount_text="Product / scheme based",
            source_url=BANK_WEBSITES["Bank of Maharashtra"]
        ),

        "IDFC FIRST Bank": product(
            amount_text="Product / eligibility based",
            source_url=BANK_WEBSITES["IDFC FIRST Bank"]
        ),

        "Federal Bank": product(
            amount_text="Product / eligibility based",
            source_url=BANK_WEBSITES["Federal Bank"]
        ),

        "IndusInd Bank": product(
            amount_text="Product / eligibility based",
            source_url=BANK_WEBSITES["IndusInd Bank"]
        ),

        "YES Bank": product(
            amount_text="Product / eligibility based",
            source_url=BANK_WEBSITES["YES Bank"]
        ),
    },
}
