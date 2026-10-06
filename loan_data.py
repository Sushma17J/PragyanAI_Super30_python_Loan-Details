# loan_data.py

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
    "YES Bank"
]


BANK_WEBSITES = {
    "SBI": "https://sbi.co.in/",
    "HDFC Bank": "https://www.hdfcbank.com/",
    "ICICI Bank": "https://www.icicibank.com/",
    "Axis Bank": "https://www.axisbank.com/",
    "Kotak Mahindra Bank": "https://www.kotak.com/",
    "Bank of Baroda": "https://www.bankofbaroda.in/",
    "Punjab National Bank": "https://www.pnbindia.in/",
    "Canara Bank": "https://canarabank.com/",
    "Union Bank of India": "https://www.unionbankofindia.co.in/",
    "Indian Bank": "https://www.indianbank.in/",
    "Bank of India": "https://bankofindia.co.in/",
    "Bank of Maharashtra": "https://bankofmaharashtra.in/",
    "IDFC FIRST Bank": "https://www.idfcfirstbank.com/",
    "Federal Bank": "https://www.federalbank.co.in/",
    "IndusInd Bank": "https://www.indusind.com/",
    "YES Bank": "https://www.yesbank.in/"
}


# ==========================================================
# LOAN DATA
# ==========================================================
#
# None means:
# We have not added a verified value for that field.
#
# Do NOT treat None as zero.
# ==========================================================


LOAN_DATA = {

    # ======================================================
    # PERSONAL LOAN
    # ======================================================

    "Personal Loan": {

        "SBI": {
            "available": True,
            "min_amount": None,
            "max_amount": 3500000,
            "interest_rate": None,
            "max_tenure": 7,
            "source": "SBI Personal Loan",
            "source_url": "https://sbi.co.in/web/personal-banking/loans/personal-loans/sbi-personal-loan"
        },

        "HDFC Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": 4000000,
            "interest_rate": None,
            "max_tenure": 7,
            "source": "HDFC Bank Personal Loan",
            "source_url": "https://www.hdfcbank.com/"
        },

        "ICICI Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": 5000000,
            "interest_rate": 10.85,
            "max_tenure": 6,
            "source": "ICICI Bank Personal Loan",
            "source_url": "https://www.icicibank.com/Personal-Banking/loans/loans.page"
        },

        "Axis Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": 4000000,
            "interest_rate": None,
            "max_tenure": 7,
            "source": "Axis Bank Personal Loan",
            "source_url": "https://www.axisbank.com/retail/loans/personal-loan"
        }
    },


    # ======================================================
    # EDUCATION LOAN
    # ======================================================

    "Education Loan": {

        "SBI": {
            "available": True,
            "min_amount": None,
            "max_amount": 5000000,
            "interest_rate": None,
            "max_tenure": 15,
            "source": "SBI Student Loan Scheme",
            "source_url": "https://sbi.bank.in/web/personal-banking/loans/education-loans/student-loan-scheme"
        },

        "HDFC Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": 15000000,
            "interest_rate": None,
            "max_tenure": None,
            "source": "HDFC Bank Education Loan",
            "source_url": "https://www.hdfc.bank.in/education-loan"
        },

        "Axis Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": 15000000,
            "interest_rate": None,
            "max_tenure": None,
            "source": "Axis Bank Education Loan",
            "source_url": "https://www.axis.bank.in/loans/education-loan"
        }
    },


    # ======================================================
    # HOME LOAN
    # ======================================================

    "Home Loan": {

        "Axis Bank": {
            "available": True,
            "min_amount": 100000,
            "max_amount": 50000000,
            "interest_rate": None,
            "max_tenure": 30,
            "source": "Axis Bank Home Loan",
            "source_url": "https://www.axisbank.com/retail/loans/home-loan"
        },

        "ICICI Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": 50000000,
            "interest_rate": None,
            "max_tenure": 30,
            "source": "ICICI Bank Home Loan",
            "source_url": "https://www.icicibank.com/Personal-Banking/loans/home-loan/index.page"
        }
    },


    # ======================================================
    # CAR LOAN
    # ======================================================

    "Car Loan": {

        "SBI": {
            "available": True,
            "min_amount": 100000,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": 7,
            "source": "SBI New Car Loan",
            "source_url": "https://sbi.co.in/web/personal-banking/loans/auto-loans/sbi-new-car-loan-scheme"
        },

        "ICICI Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": 10000000,
            "interest_rate": 9.10,
            "max_tenure": 7,
            "source": "ICICI Bank Car Loan",
            "source_url": "https://www.icicibank.com/Personal-Banking/loans/car-loan/index.page"
        },

        "Axis Bank": {
            "available": True,
            "min_amount": 100000,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": 7,
            "source": "Axis Bank Car Loan",
            "source_url": "https://www.axisbank.com/retail/loans/car-loan/new-car-loan"
        }
    },


    # ======================================================
    # TWO-WHEELER LOAN
    # ======================================================

    "Two-Wheeler Loan": {

        "SBI": {
            "available": True,
            "min_amount": 50000,
            "max_amount": 300000,
            "interest_rate": None,
            "max_tenure": None,
            "source": "SBI Two Wheeler Loan",
            "source_url": "https://sbi.co.in/web/personal-banking/loans/auto-loans/sbi-two-wheeler-loan-scheme"
        },

        "ICICI Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": 10.25,
            "max_tenure": 3,
            "source": "ICICI Bank Two-Wheeler Loan",
            "source_url": "https://www.icicibank.com/personal-banking/loans/two-wheeler-loan/review"
        },

        "HDFC Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": None,
            "source": "HDFC Bank Two Wheeler Loan",
            "source_url": "https://www.hdfcbank.com/personal/borrow/popular-loans/two-wheeler-loan"
        },

        "Axis Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": 4,
            "source": "Axis Bank Two Wheeler Loan",
            "source_url": "https://www.axisbank.com/"
        }
    },


    # ======================================================
    # GOLD LOAN
    # ======================================================

    "Gold Loan": {

        "ICICI Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": 20000000,
            "interest_rate": None,
            "max_tenure": None,
            "source": "ICICI Bank Gold Loan",
            "source_url": "https://www.icicibank.com/personal-banking/loans/gold-loan/faqs"
        },

        "Axis Bank": {
            "available": True,
            "min_amount": 50001,
            "max_amount": 4000000,
            "interest_rate": None,
            "max_tenure": 3,
            "source": "Axis Bank Gold Loan",
            "source_url": "https://www.axisbank.com/loans/gold-loan"
        }
    },


    # ======================================================
    # BUSINESS LOAN
    # ======================================================

    "Business Loan": {

        "SBI": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": None,
            "source": "SBI Business Loans",
            "source_url": "https://sbi.co.in/"
        },

        "HDFC Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": None,
            "source": "HDFC Bank Business Loans",
            "source_url": "https://www.hdfcbank.com/"
        },

        "ICICI Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": None,
            "source": "ICICI Bank Business Loans",
            "source_url": "https://www.icicibank.com/"
        },

        "Axis Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": None,
            "source": "Axis Bank Business Loans",
            "source_url": "https://www.axisbank.com/"
        }
    },


    # ======================================================
    # LOAN AGAINST PROPERTY
    # ======================================================

    "Loan Against Property": {

        "SBI": {
            "available": True,
            "min_amount": 1000000,
            "max_amount": 75000000,
            "interest_rate": None,
            "max_tenure": None,
            "source": "SBI Property Loan Scheme",
            "source_url": "https://sbi.co.in/web/personal-banking/loans/loans-against-property/loans-against-property"
        }
    },


    # ======================================================
    # AGRICULTURE LOAN
    # ======================================================

    "Agriculture Loan": {

        "SBI": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": None,
            "source": "SBI Agriculture Banking",
            "source_url": "https://sbi.co.in/"
        },

        "Bank of Baroda": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": None,
            "source": "Bank of Baroda Agriculture Banking",
            "source_url": "https://www.bankofbaroda.in/"
        },

        "Canara Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": None,
            "source": "Canara Bank Agriculture Banking",
            "source_url": "https://canarabank.com/"
        }
    },


    # ======================================================
    # CONSUMER DURABLE LOAN
    # ======================================================

    "Consumer Durable Loan": {

        "ICICI Bank": {
            "available": True,
            "min_amount": None,
            "max_amount": None,
            "interest_rate": None,
            "max_tenure": None,
            "source": "ICICI Bank Consumer Finance",
            "source_url": "https://www.icicibank.com/Personal-Banking/loans/loans.page"
        }
    }
}
