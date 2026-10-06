import streamlit as st
import pandas as pd

from loan_data import BANKS, BANK_WEBSITES, LOAN_DATA
from loan_calculator import calculate_emi


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="SmartLoan India",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# SESSION STATE
# ==========================================================

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

if "selected_loan" not in st.session_state:
    st.session_state.selected_loan = None

if "selected_bank" not in st.session_state:
    st.session_state.selected_bank = None


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
<style>

/* ==========================================================
   GLOBAL
========================================================== */

.stApp {
    background-color: #f5f7fb;
    color: #111827;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1450px;
}

h1, h2, h3, h4, h5, h6 {
    color: #111827 !important;
}

p,
label,
.stMarkdown,
.stCaption {
    color: #374151;
}


/* ==========================================================
   SIDEBAR
========================================================== */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #030712 0%,
            #0f172a 100%
        );

    border-right: 1px solid #1e293b;
}

[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

[data-testid="stSidebar"] .stRadio label {
    color: #e2e8f0 !important;
}

[data-testid="stSidebar"] hr {
    border-color: #263244 !important;
}


/* ==========================================================
   HERO
========================================================== */

.hero {
    padding: 52px 48px;

    border-radius: 26px;

    background:
        radial-gradient(
            circle at 85% 15%,
            rgba(59,130,246,0.28),
            transparent 32%
        ),
        linear-gradient(
            135deg,
            #020617 0%,
            #0f172a 55%,
            #172554 100%
        );

    border: 1px solid #263244;

    box-shadow:
        0 18px 45px rgba(15,23,42,0.20);

    margin-bottom: 34px;
}

.hero-title {
    color: #ffffff !important;

    font-size: 46px;

    font-weight: 800;

    margin-bottom: 10px;
}

.hero-text {
    color: #cbd5e1 !important;

    font-size: 18px;

    line-height: 1.7;

    margin: 0;
}


/* ==========================================================
   SECTION TITLE
========================================================== */

.section-title {
    color: #0f172a !important;

    font-size: 30px;

    font-weight: 800;

    margin-top: 20px;

    margin-bottom: 8px;
}


/* ==========================================================
   LOAN CARDS
========================================================== */

.loan-card {
    position: relative;

    min-height: 190px;

    padding: 24px;

    margin-bottom: 8px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            #111827 0%,
            #0b1120 100%
        );

    border: 1px solid #263244;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.16);

    overflow: hidden;

    transition:
        transform 0.2s ease,
        border-color 0.2s ease,
        box-shadow 0.2s ease;
}

.loan-card:hover {
    transform: translateY(-5px);

    border-color: #3b82f6;

    box-shadow:
        0 16px 34px rgba(0,0,0,0.25);
}


/* ==========================================================
   LOAN ICON
========================================================== */

.loan-icon {
    width: 56px;
    height: 56px;

    border-radius: 15px;

    display: flex;

    align-items: center;
    justify-content: center;

    background:
        linear-gradient(
            135deg,
            #1e3a8a,
            #2563eb
        );

    font-size: 27px;

    margin-bottom: 16px;
}


/* ==========================================================
   LOAN CARD TEXT
========================================================== */

.loan-title {
    color: #ffffff !important;

    font-size: 20px;

    font-weight: 750;

    margin-bottom: 7px;
}

.loan-description {
    color: #aeb9ca !important;

    font-size: 14px;

    line-height: 1.55;

    max-width: 300px;
}


/* ==========================================================
   EXPLORE BUTTON
========================================================== */

div[data-testid="column"] .stButton > button {
    border-radius: 10px;

    min-height: 40px;

    font-weight: 700;

    border: 1px solid #2563eb;

    color: #2563eb;

    background: #eff6ff;

    transition: all 0.2s ease;
}

div[data-testid="column"] .stButton > button:hover {
    background: #2563eb;

    color: white;

    border-color: #2563eb;

    transform: translateY(-2px);
}


/* ==========================================================
   STEP CARDS
========================================================== */

.step-card {
    background: #ffffff;

    border: 1px solid #e2e8f0;

    border-radius: 18px;

    padding: 20px;

    min-height: 155px;

    box-shadow:
        0 5px 18px rgba(15,23,42,0.06);
}

.step-number {
    display: inline-flex;

    align-items: center;
    justify-content: center;

    width: 36px;
    height: 36px;

    border-radius: 50%;

    background: #eff6ff;

    color: #2563eb;

    font-weight: 800;

    margin-bottom: 10px;
}

.step-icon {
    font-size: 24px;

    margin-bottom: 7px;
}

.step-title {
    color: #0f172a;

    font-size: 16px;

    font-weight: 750;

    margin-bottom: 5px;
}

.step-description {
    color: #64748b;

    font-size: 13px;

    line-height: 1.5;
}


/* ==========================================================
   INPUTS
========================================================== */

.stSelectbox label,
.stMultiSelect label,
.stNumberInput label,
.stSlider label {
    color: #374151 !important;

    font-weight: 600 !important;
}

div[data-baseweb="select"] > div {
    background: #ffffff !important;

    color: #111827 !important;

    border-radius: 10px;

    border: 1px solid #d1d5db;
}

div[data-baseweb="select"] span {
    color: #111827 !important;
}

.stNumberInput input {
    background: #ffffff !important;

    color: #111827 !important;

    border-radius: 10px;
}


/* ==========================================================
   METRICS
========================================================== */

[data-testid="stMetric"] {
    background: #ffffff;

    padding: 18px;

    border-radius: 15px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 5px 15px rgba(15,23,42,0.05);
}

[data-testid="stMetricLabel"] {
    color: #475569 !important;
}

[data-testid="stMetricValue"] {
    color: #111827 !important;
}


/* ==========================================================
   BUTTONS
========================================================== */

.stButton > button {
    border-radius: 11px;

    min-height: 45px;

    font-weight: 700;

    color: #111827;

    border: 1px solid #dbe3ee;

    transition: 0.2s ease;
}

.stButton > button:hover {
    border-color: #2563eb;

    transform: translateY(-1px);
}

.stButton > button[kind="primary"] {
    background:
        linear-gradient(
            135deg,
            #2563eb,
            #1d4ed8
        ) !important;

    color: #ffffff !important;

    border: none !important;
}


/* ==========================================================
   FOOTER
========================================================== */

.footer {
    text-align: center;

    padding: 32px 20px;

    margin-top: 50px;

    border-top: 1px solid #e2e8f0;

    color: #64748b;
}

.footer-title {
    color: #0f172a;

    font-size: 20px;

    font-weight: 800;

    margin-bottom: 7px;
}

.footer-text {
    color: #94a3b8;

    font-size: 13px;
}

</style>
""",
    unsafe_allow_html=True
)


# ==========================================================
# HELPER - LOAN CARD
# ==========================================================

def show_loan_card(
    icon,
    title,
    description
):

    # Card itself
    card = (
        '<div class="loan-card">'
        f'<div class="loan-icon">{icon}</div>'
        f'<div class="loan-title">{title}</div>'
        f'<div class="loan-description">{description}</div>'
        '</div>'
    )

    st.markdown(
        card,
        unsafe_allow_html=True
    )

    # Real clickable Streamlit button
    if st.button(
        "Explore →",
        key=f"explore_{title}",
        use_container_width=True
    ):

        st.session_state.selected_loan = title

        st.session_state.page = "🔍 Find Loan"

        st.rerun()


# ==========================================================
# HELPER - STEP CARD
# ==========================================================

def show_step(
    number,
    icon,
    title,
    description
):

    card = (
        '<div class="step-card">'
        f'<div class="step-number">{number}</div>'
        f'<div class="step-icon">{icon}</div>'
        f'<div class="step-title">{title}</div>'
        f'<div class="step-description">{description}</div>'
        '</div>'
    )

    st.markdown(
        card,
        unsafe_allow_html=True
    )


# ==========================================================
# HELPER - FORMAT AMOUNT
# ==========================================================

def format_amount(value):

    if value is None:
        return "Check Bank"

    return f"₹{value:,}"


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;">
            <div style="font-size:42px;">
                🏦
            </div>

            <div style="
                font-size:22px;
                font-weight:800;
                color:#ffffff;
            ">
                SmartLoan India
            </div>

            <div style="
                font-size:12px;
                color:#94a3b8;
                margin-top:4px;
            ">
                Smart • Simple • Transparent
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Home",
            "🔍 Find Loan",
            "📊 Compare Loans",
            "🧮 EMI Calculator"
        ],
        key="page"
    )

    st.markdown("---")

    st.info(
        "💡 Compare loan options and always verify "
        "the latest terms directly with the bank."
    )


# ==========================================================
# HOME
# ==========================================================

if page == "🏠 Home":

    # ------------------------------------------------------
    # HERO
    # ------------------------------------------------------

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                🏦 SmartLoan India
            </div>

            <div class="hero-text">
                Find, compare and calculate loans from
                major Indian banks — all in one place.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ------------------------------------------------------
    # LOAN SECTION
    # ------------------------------------------------------

    st.markdown(
        """
        <div class="section-title">
            Choose the loan you need
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "Explore loan options designed for different financial needs."
    )


    loan_cards = [

        (
            "👤",
            "Personal Loan",
            "Flexible financing for personal, emergency and lifestyle needs."
        ),

        (
            "🎓",
            "Education Loan",
            "Finance higher education in India or abroad with suitable options."
        ),

        (
            "🏠",
            "Home Loan",
            "Compare financing options for purchasing or constructing a home."
        ),

        (
            "🚗",
            "Car Loan",
            "Finance your new or used car with flexible repayment options."
        ),

        (
            "🛵",
            "Two-Wheeler Loan",
            "Get financing for bikes, scooters and other two-wheelers."
        ),

        (
            "🥇",
            "Gold Loan",
            "Borrow against eligible gold assets for your financial requirements."
        ),

        (
            "💼",
            "Business Loan",
            "Financing solutions for business expansion and working capital."
        ),

        (
            "🏢",
            "Loan Against Property",
            "Access funds by using eligible property as security."
        ),

        (
            "🚜",
            "Agriculture Loan",
            "Financial support for farming and agricultural activities."
        )
    ]


    # ------------------------------------------------------
    # LOAN CARD GRID
    # ------------------------------------------------------

    for start in range(
        0,
        len(loan_cards),
        3
    ):

        cols = st.columns(3)

        current_cards = loan_cards[
            start:start + 3
        ]

        for col, card_data in zip(
            cols,
            current_cards
        ):

            with col:

                show_loan_card(
                    *card_data
                )


    # ------------------------------------------------------
    # HOW IT WORKS
    # ------------------------------------------------------

    st.markdown("---")

    st.markdown(
        """
        <div class="section-title">
            How it works
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "Get from loan selection to EMI calculation in four simple steps."
    )


    steps = [

        (
            "01",
            "🏦",
            "Select Loan",
            "Choose the type of loan you need."
        ),

        (
            "02",
            "🏛️",
            "Select Bank",
            "Choose a bank from the available list."
        ),

        (
            "03",
            "💰",
            "Enter Amount",
            "Enter your required loan amount."
        ),

        (
            "04",
            "🧮",
            "Calculate EMI",
            "Get your estimated monthly EMI."
        )
    ]


    cols = st.columns(4)


    for col, step in zip(
        cols,
        steps
    ):

        with col:

            show_step(
                *step
            )


    # ------------------------------------------------------
    # IMPORTANT NOTE
    # ------------------------------------------------------

    st.markdown("---")

    st.warning(
        "⚠️ Important: Loan interest rates, maximum amounts, "
        "eligibility requirements and fees can change over time. "
        "Always verify the latest terms directly with the "
        "respective bank before applying."
    )


# ==========================================================
# FIND LOAN
# ==========================================================

elif page == "🔍 Find Loan":

    st.title(
        "🔍 Find Your Loan"
    )

    st.write(
        "Select a loan category and bank to explore available information."
    )


    # ------------------------------------------------------
    # LOAN TYPE
    # ------------------------------------------------------

    loan_types = list(
        LOAN_DATA.keys()
    )


    if (
        st.session_state.selected_loan
        in loan_types
    ):

        default_index = loan_types.index(
            st.session_state.selected_loan
        )

    else:

        default_index = 0


    loan_type = st.selectbox(
        "🏦 Select Loan Type",
        loan_types,
        index=default_index
    )


    # Keep selected loan synchronized
    st.session_state.selected_loan = loan_type


    # ------------------------------------------------------
    # BANK
    # ------------------------------------------------------

    bank = st.selectbox(
        "🏛️ Select Bank",
        BANKS
    )


    st.session_state.selected_bank = bank


    product = (
        LOAN_DATA
        .get(loan_type, {})
        .get(bank)
    )


    st.markdown("---")


    # ======================================================
    # NO VERIFIED PRODUCT
    # ======================================================

    if product is None:

        st.warning(
            f"❌ {bank} does not currently have verified "
            f"{loan_type} information in our database."
        )


        st.info(
            "We don't invent loan limits or interest rates "
            "when they haven't been verified."
        )


        if bank in BANK_WEBSITES:

            st.link_button(
                "🌐 Check Official Bank Website",
                BANK_WEBSITES[bank]
            )


    # ======================================================
    # PRODUCT FOUND
    # ======================================================

    else:

        st.subheader(
            f"🏦 {bank} — {loan_type}"
        )


        st.success(
            "✅ Loan product found"
        )


        # --------------------------------------------------
        # PRODUCT METRICS
        # --------------------------------------------------

        c1, c2, c3 = st.columns(3)


        with c1:

            st.metric(
                "Minimum Loan",
                format_amount(
                    product.get("min_amount")
                )
            )


        with c2:

            st.metric(
                "Maximum Loan",
                format_amount(
                    product.get("max_amount")
                )
            )


        with c3:

            rate = product.get(
                "interest_rate"
            )

            if rate is not None:

                rate_text = f"{rate}%"

            else:

                rate_text = "Check Bank"


            st.metric(
                "Interest Rate",
                rate_text
            )


        st.markdown("---")


        # --------------------------------------------------
        # LOAN REQUIREMENT
        # --------------------------------------------------

        st.subheader(
            "💰 Loan Requirement"
        )


        # ==================================================
        # CAR LOAN
        # ==================================================

        if loan_type == "Car Loan":

            vehicle_price = st.number_input(
                "🚗 On-Road Vehicle Price (₹)",
                min_value=10000,
                value=1000000,
                step=10000
            )


            down_payment = st.number_input(
                "💰 Down Payment (₹)",
                min_value=0,
                value=200000,
                step=10000
            )


            if down_payment > vehicle_price:

                st.error(
                    "Down payment cannot exceed vehicle price."
                )

                st.stop()


            loan_amount = (
                vehicle_price -
                down_payment
            )


            st.info(
                f"Required Loan Amount: ₹{loan_amount:,}"
            )


        # ==================================================
        # TWO-WHEELER LOAN
        # ==================================================

        elif loan_type == "Two-Wheeler Loan":

            vehicle_price = st.number_input(
                "🛵 On-Road Bike/Scooter Price (₹)",
                min_value=10000,
                value=120000,
                step=5000
            )


            down_payment = st.number_input(
                "💰 Down Payment (₹)",
                min_value=0,
                value=20000,
                step=5000
            )


            if down_payment > vehicle_price:

                st.error(
                    "Down payment cannot exceed vehicle price."
                )

                st.stop()


            loan_amount = (
                vehicle_price -
                down_payment
            )


            st.info(
                f"Required Loan Amount: ₹{loan_amount:,}"
            )


        # ==================================================
        # GOLD LOAN
        # ==================================================

        elif loan_type == "Gold Loan":

            gold_weight = st.number_input(
                "🥇 Gold Weight (grams)",
                min_value=1.0,
                value=20.0,
                step=1.0
            )


            gold_purity = st.selectbox(
                "Gold Purity",
                [
                    "18K",
                    "20K",
                    "22K",
                    "24K"
                ]
            )


            loan_amount = st.number_input(
                "💰 Required Loan Amount (₹)",
                min_value=10000,
                value=100000,
                step=5000
            )


            st.caption(
                f"Gold: {gold_weight} grams | "
                f"Purity: {gold_purity}"
            )


        # ==================================================
        # EDUCATION LOAN
        # ==================================================

        elif loan_type == "Education Loan":

            course_fee = st.number_input(
                "🎓 Total Course Fee (₹)",
                min_value=10000,
                value=800000,
                step=10000
            )


            study_location = st.selectbox(
                "Study Location",
                [
                    "India",
                    "Abroad"
                ]
            )


            loan_amount = st.number_input(
                "💰 Required Education Loan (₹)",
                min_value=10000,
                value=500000,
                step=10000
            )


            if loan_amount > course_fee:

                st.warning(
                    "Required loan is greater than "
                    "the entered course fee."
                )


        # ==================================================
        # HOME LOAN
        # ==================================================

        elif loan_type == "Home Loan":

            property_value = st.number_input(
                "🏠 Property Value (₹)",
                min_value=100000,
                value=5000000,
                step=100000
            )


            down_payment = st.number_input(
                "💰 Down Payment (₹)",
                min_value=0,
                value=1000000,
                step=100000
            )


            if down_payment > property_value:

                st.error(
                    "Down payment cannot exceed property value."
                )

                st.stop()


            loan_amount = (
                property_value -
                down_payment
            )


            st.info(
                f"Required Home Loan: ₹{loan_amount:,}"
            )


        # ==================================================
        # OTHER LOANS
        # ==================================================

        else:

            min_amount = (
                product.get("min_amount")
                if product.get("min_amount") is not None
                else 10000
            )


            max_amount = (
                product.get("max_amount")
                if product.get("max_amount") is not None
                else 100000000
            )


            default_amount = min(
                500000,
                max_amount
            )


            if default_amount < min_amount:

                default_amount = min_amount


            loan_amount = st.number_input(
                "💰 Required Loan Amount (₹)",
                min_value=min_amount,
                max_value=max_amount,
                value=default_amount,
                step=10000
            )


        # --------------------------------------------------
        # AMOUNT VALIDATION
        # --------------------------------------------------

        max_amount = product.get(
            "max_amount"
        )

        min_amount = product.get(
            "min_amount"
        )


        if (
            max_amount is not None
            and loan_amount > max_amount
        ):

            st.error(
                f"Requested amount exceeds "
                f"₹{max_amount:,}."
            )

            st.stop()


        if (
            min_amount is not None
            and loan_amount < min_amount
        ):

            st.error(
                f"Requested amount is below "
                f"₹{min_amount:,}."
            )

            st.stop()


        # --------------------------------------------------
        # TENURE
        # --------------------------------------------------

        st.subheader(
            "📅 Loan Tenure"
        )


        max_tenure = product.get(
            "max_tenure"
        )


        if max_tenure is not None:

            max_tenure = max(
                1,
                int(max_tenure)
            )


            tenure = st.slider(
                "Select Tenure (Years)",
                min_value=1,
                max_value=max_tenure,
                value=min(
                    5,
                    max_tenure
                )
            )

        else:

            tenure = st.slider(
                "Select Tenure (Years)",
                min_value=1,
                max_value=30,
                value=5
            )


        # --------------------------------------------------
        # INTEREST RATE
        # --------------------------------------------------

        product_rate = product.get(
            "interest_rate"
        )


        if product_rate is not None:

            interest_rate = float(
                product_rate
            )


            st.info(
                f"Indicative interest rate: "
                f"{interest_rate}%"
            )

        else:

            interest_rate = st.number_input(
                "📈 Enter Applicable Interest Rate (%)",
                min_value=0.0,
                max_value=50.0,
                value=10.0,
                step=0.1
            )


        st.markdown("---")


        # --------------------------------------------------
        # ACTION BUTTONS
        # --------------------------------------------------

        b1, b2, b3 = st.columns(3)


        with b1:

            calculate = st.button(
                "🧮 Calculate EMI",
                type="primary",
                use_container_width=True
            )


        with b2:

            official = st.button(
                "🌐 Official Website",
                use_container_width=True
            )


        with b3:

            compare = st.button(
                "📊 Add to Compare",
                use_container_width=True
            )


        # --------------------------------------------------
        # OFFICIAL WEBSITE
        # --------------------------------------------------

        if official:

            source_url = product.get(
                "source_url"
            )


            if source_url:

                st.link_button(
                    "Open Official Bank Website",
                    source_url
                )

            elif bank in BANK_WEBSITES:

                st.link_button(
                    "Open Official Bank Website",
                    BANK_WEBSITES[bank]
                )


        # --------------------------------------------------
        # ADD TO COMPARE
        # --------------------------------------------------

        if compare:

            st.session_state.selected_loan = loan_type

            st.session_state.selected_bank = bank

            st.success(
                f"✅ {bank} {loan_type} "
                "selected for comparison."
            )


        # --------------------------------------------------
        # CALCULATE EMI
        # --------------------------------------------------

        if calculate:

            if interest_rate <= 0:

                st.error(
                    "Please enter a valid interest rate."
                )

            else:

                emi, total_interest, total_payment = (
                    calculate_emi(
                        loan_amount,
                        interest_rate,
                        tenure
                    )
                )


                st.markdown("---")


                st.subheader(
                    "📊 Estimated Loan Result"
                )


                r1, r2, r3 = st.columns(3)


                with r1:

                    st.metric(
                        "Monthly EMI",
                        f"₹{emi:,.2f}"
                    )


                with r2:

                    st.metric(
                        "Total Interest",
                        f"₹{total_interest:,.2f}"
                    )


                with r3:

                    st.metric(
                        "Total Repayment",
                        f"₹{total_payment:,.2f}"
                    )


                st.success(
                    f"Loan Summary: {bank} | "
                    f"{loan_type} | "
                    f"₹{loan_amount:,} | "
                    f"{interest_rate}% | "
                    f"{tenure} years"
                )


        st.markdown("---")


        st.caption(
            f"Information source: "
            f"{product.get('source', 'Bank website')}"
        )


# ==========================================================
# COMPARE LOANS
# ==========================================================

elif page == "📊 Compare Loans":

    st.title(
        "📊 Compare Loans"
    )


    st.write(
        "Select a loan type and multiple banks "
        "to compare available information."
    )


    loan_type = st.selectbox(
        "🏦 Loan Type",
        list(LOAN_DATA.keys())
    )


    selected_banks = st.multiselect(
        "🏛️ Select Banks",
        BANKS,
        default=[
            "SBI",
            "HDFC Bank",
            "ICICI Bank"
        ]
    )


    if st.button(
        "📊 Compare Now",
        type="primary",
        use_container_width=True
    ):

        if len(selected_banks) < 2:

            st.warning(
                "Please select at least two banks."
            )

        else:

            rows = []


            for bank in selected_banks:

                product = (
                    LOAN_DATA
                    .get(loan_type, {})
                    .get(bank)
                )


                if product is None:

                    rows.append(
                        {
                            "Bank": bank,
                            "Available": "❌ No verified data",
                            "Minimum Loan": "-",
                            "Maximum Loan": "-",
                            "Interest Rate": "-",
                            "Maximum Tenure": "-"
                        }
                    )

                else:

                    rate = product.get(
                        "interest_rate"
                    )


                    max_tenure = product.get(
                        "max_tenure"
                    )


                    rows.append(
                        {
                            "Bank": bank,

                            "Available": "✅ Yes",

                            "Minimum Loan":
                                format_amount(
                                    product.get("min_amount")
                                ),

                            "Maximum Loan":
                                format_amount(
                                    product.get("max_amount")
                                ),

                            "Interest Rate":
                                (
                                    f"{rate}%"
                                    if rate is not None
                                    else "Check Bank"
                                ),

                            "Maximum Tenure":
                                (
                                    f"{max_tenure} years"
                                    if max_tenure is not None
                                    else "Check Bank"
                                )
                        }
                    )


            df = pd.DataFrame(
                rows
            )


            st.markdown("---")


            st.subheader(
                f"📊 {loan_type} Comparison"
            )


            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )


# ==========================================================
# EMI CALCULATOR
# ==========================================================

elif page == "🧮 EMI Calculator":

    st.title(
        "🧮 EMI Calculator"
    )


    st.write(
        "Calculate your estimated monthly loan EMI."
    )


    amount = st.number_input(
        "💰 Loan Amount (₹)",
        min_value=10000,
        max_value=100000000,
        value=500000,
        step=10000
    )


    rate = st.number_input(
        "📈 Interest Rate (%)",
        min_value=0.0,
        max_value=50.0,
        value=10.0,
        step=0.1
    )


    years = st.slider(
        "📅 Tenure",
        min_value=1,
        max_value=30,
        value=5
    )


    if st.button(
        "🧮 Calculate EMI",
        type="primary",
        use_container_width=True
    ):

        emi, interest, total = calculate_emi(
            amount,
            rate,
            years
        )


        st.markdown("---")


        st.subheader(
            "📊 EMI Result"
        )


        c1, c2, c3 = st.columns(3)


        with c1:

            st.metric(
                "Monthly EMI",
                f"₹{emi:,.2f}"
            )


        with c2:

            st.metric(
                "Total Interest",
                f"₹{interest:,.2f}"
            )


        with c3:

            st.metric(
                "Total Repayment",
                f"₹{total:,.2f}"
            )


        st.success(
            f"Calculation complete — "
            f"₹{amount:,} at {rate}% "
            f"for {years} years."
        )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <div class="footer">

        <div class="footer-title">
            🏦 SmartLoan India
        </div>

        <div>
            Compare • Calculate • Explore
        </div>

        <div class="footer-text">
            Loan information is provided for
            comparison and educational purposes.
        </div>

        <div class="footer-text">
            Always verify the latest terms with
            the respective bank.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)
