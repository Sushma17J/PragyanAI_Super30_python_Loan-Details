import streamlit as st
import pandas as pd
from textwrap import dedent

from loan_data import (
    BANKS,
    BANK_WEBSITES,
    LOAN_DATA
)

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
# HELPER FOR HTML
# ==========================================================

def html(content):
    """
    Removes Python indentation from HTML so that
    Streamlit does not interpret it as a code block.
    """
    return dedent(content).strip()


# ==========================================================
# SESSION STATE
# ==========================================================

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
   GLOBAL APP
========================================================== */

.stApp {
    background-color: #f5f7fb !important;
    color: #111827 !important;
}

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
    max-width: 1450px;
}


/* ==========================================================
   NORMAL TEXT
========================================================== */

p,
span,
label,
.stMarkdown,
.stCaption {
    color: #374151;
}


/* ==========================================================
   HEADINGS
========================================================== */

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #111827 !important;
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
        ) !important;

    border-right: 1px solid #1e293b;
}

[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}


/* Sidebar radio */

[data-testid="stSidebar"] .stRadio label {
    color: #e2e8f0 !important;
}


/* Sidebar divider */

[data-testid="stSidebar"] hr {
    border-color: #263244 !important;
}


/* ==========================================================
   HERO
========================================================== */

.hero {
    position: relative;

    padding: 55px 50px;

    border-radius: 26px;

    background:
        radial-gradient(
            circle at 85% 15%,
            rgba(59,130,246,0.28),
            transparent 32%
        ),
        radial-gradient(
            circle at 15% 100%,
            rgba(30,64,175,0.20),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #020617 0%,
            #0f172a 55%,
            #172554 100%
        );

    margin-bottom: 38px;

    border: 1px solid #263244;

    box-shadow:
        0 18px 45px rgba(15,23,42,0.20);

    overflow: hidden;
}

.hero h1 {
    color: #ffffff !important;

    font-size: 48px;

    font-weight: 800;

    margin: 0 0 12px 0;
}

.hero p {
    color: #cbd5e1 !important;

    font-size: 18px;

    max-width: 680px;

    line-height: 1.7;

    margin: 0;
}


/* ==========================================================
   SECTION TITLE
========================================================== */

.section-title {
    font-size: 30px;

    font-weight: 800;

    margin-top: 25px;

    margin-bottom: 8px;

    color: #0f172a !important;
}


/* ==========================================================
   LOAN CARDS
========================================================== */

.loan-card {
    position: relative;

    background:
        linear-gradient(
            145deg,
            #111827 0%,
            #0b1120 100%
        );

    color: white;

    padding: 26px;

    border-radius: 20px;

    border: 1px solid #263244;

    min-height: 210px;

    margin-bottom: 22px;

    overflow: hidden;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.16);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease;
}

.loan-card::before {
    content: "";

    position: absolute;

    width: 140px;
    height: 140px;

    top: -70px;
    right: -45px;

    background: rgba(59,130,246,0.12);

    border-radius: 50%;

    filter: blur(3px);
}

.loan-card::after {
    content: "";

    position: absolute;

    width: 80px;
    height: 80px;

    bottom: -50px;
    left: -30px;

    background: rgba(37,99,235,0.08);

    border-radius: 50%;
}

.loan-card:hover {
    transform: translateY(-7px);

    border-color: #3b82f6;

    box-shadow:
        0 18px 38px rgba(0,0,0,0.27),
        0 0 20px rgba(59,130,246,0.10);
}


/* ==========================================================
   LOAN ICON
========================================================== */

.loan-icon {
    width: 58px;
    height: 58px;

    display: flex;

    align-items: center;
    justify-content: center;

    background:
        linear-gradient(
            135deg,
            #1e3a8a,
            #2563eb
        );

    border-radius: 16px;

    font-size: 28px;

    margin-bottom: 18px;

    box-shadow:
        0 7px 18px rgba(37,99,235,0.28);

    position: relative;

    z-index: 2;
}


/* ==========================================================
   LOAN CARD TEXT
========================================================== */

.loan-card h3 {
    position: relative;

    z-index: 2;

    color: #ffffff !important;

    font-size: 21px;

    font-weight: 700;

    margin: 0 0 9px 0;
}

.loan-card p {
    position: relative;

    z-index: 2;

    color: #aeb9ca !important;

    font-size: 14px;

    line-height: 1.6;

    margin: 0;

    max-width: 290px;
}


/* ==========================================================
   EXPLORE
========================================================== */

.loan-explore {
    position: absolute;

    bottom: 20px;

    right: 22px;

    color: #60a5fa !important;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: 0.3px;

    z-index: 3;
}


/* ==========================================================
   HOW IT WORKS
========================================================== */

.step-card {
    background: #ffffff;

    border: 1px solid #e2e8f0;

    border-radius: 18px;

    padding: 22px;

    min-height: 165px;

    box-shadow:
        0 5px 18px rgba(15,23,42,0.06);

    transition: 0.2s ease;
}

.step-card:hover {
    transform: translateY(-3px);

    border-color: #bfdbfe;

    box-shadow:
        0 10px 25px rgba(15,23,42,0.09);
}

.step-number {
    display: inline-flex;

    align-items: center;
    justify-content: center;

    width: 38px;
    height: 38px;

    border-radius: 50%;

    background: #eff6ff;

    color: #2563eb !important;

    font-weight: 800;

    margin-bottom: 12px;
}

.step-icon {
    font-size: 25px;

    margin-bottom: 8px;
}

.step-card h4 {
    margin: 0 0 7px 0;

    color: #0f172a !important;

    font-size: 17px;
}

.step-card p {
    margin: 0;

    color: #64748b !important;

    font-size: 13px;

    line-height: 1.5;
}


/* ==========================================================
   INPUT LABELS
========================================================== */

.stSelectbox label,
.stMultiSelect label,
.stNumberInput label,
.stSlider label {
    color: #374151 !important;

    font-weight: 600 !important;
}


/* ==========================================================
   INPUT BOXES
========================================================== */

div[data-baseweb="select"] > div {
    background-color: #ffffff !important;

    color: #111827 !important;

    border-radius: 10px;

    border: 1px solid #d1d5db;
}

div[data-baseweb="select"] span {
    color: #111827 !important;
}

.stNumberInput input {
    background-color: #ffffff !important;

    color: #111827 !important;

    border-radius: 10px;
}


/* ==========================================================
   SLIDER
========================================================== */

.stSlider label {
    color: #374151 !important;
}


/* ==========================================================
   METRICS
========================================================== */

[data-testid="stMetric"] {
    background: #ffffff !important;

    padding: 20px;

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

[data-testid="stMetricDelta"] {
    color: #374151 !important;
}


/* ==========================================================
   BUTTONS
========================================================== */

.stButton > button {
    border-radius: 11px;

    min-height: 45px;

    font-weight: 700;

    border: 1px solid #dbe3ee;

    transition: 0.2s ease;

    color: #111827;
}

.stButton > button:hover {
    transform: translateY(-2px);

    border-color: #2563eb;
}


/* Primary */

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
   LINK BUTTON
========================================================== */

.stLinkButton > a {
    border-radius: 10px !important;

    font-weight: 700 !important;
}


/* ==========================================================
   INFO / WARNING / SUCCESS
========================================================== */

.info-box {
    padding: 18px;

    border-radius: 14px;

    background: #eff6ff;

    border: 1px solid #bfdbfe;

    border-left: 5px solid #2563eb;

    color: #1e3a8a;
}

.warning-box {
    padding: 18px;

    border-radius: 14px;

    background: #fff7ed;

    border: 1px solid #fed7aa;

    border-left: 5px solid #f97316;

    color: #9a3412;
}

.success-box {
    padding: 20px;

    border-radius: 14px;

    background: #ecfdf5;

    border: 1px solid #a7f3d0;

    border-left: 5px solid #10b981;

    color: #065f46;
}


/* ==========================================================
   STREAMLIT ALERT TEXT
========================================================== */

[data-testid="stAlert"] {
    color: #111827 !important;
}


/* ==========================================================
   DATAFRAME
========================================================== */

[data-testid="stDataFrame"] {
    border-radius: 12px;
}


/* ==========================================================
   FOOTER
========================================================== */

.footer {
    text-align: center;

    padding: 35px 20px;

    margin-top: 55px;

    color: #64748b !important;

    border-top: 1px solid #e2e8f0;
}

.footer strong {
    color: #0f172a !important;
}


/* ==========================================================
   DIVIDER
========================================================== */

hr {
    border: none;

    border-top: 1px solid #e2e8f0;

    margin: 35px 0;
}

</style>
""",
    unsafe_allow_html=True
)


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.markdown(
    html(
        """
        <div style="
            text-align:center;
            padding:15px 5px 10px 5px;
        ">

            <div style="
                font-size:48px;
                margin-bottom:6px;
            ">
                🏦
            </div>

            <div style="
                font-size:23px;
                font-weight:800;
                color:#ffffff;
            ">
                SmartLoan India
            </div>

            <div style="
                font-size:12px;
                color:#94a3b8;
                margin-top:5px;
            ">
                Smart • Simple • Transparent
            </div>

        </div>
        """
    ),
    unsafe_allow_html=True
)


st.sidebar.markdown("---")


page = st.sidebar.radio(
    "NAVIGATION",
    [
        "🏠 Home",
        "🔍 Find Loan",
        "📊 Compare Loans",
        "🧮 EMI Calculator"
    ]
)


st.sidebar.markdown("---")


st.sidebar.markdown(
    html(
        """
        <div style="
            background:#111827;
            padding:16px;
            border-radius:14px;
            border:1px solid #263244;
        ">

            <div style="
                color:#60a5fa;
                font-weight:700;
                margin-bottom:8px;
            ">
                💡 Smart Tip
            </div>

            <div style="
                color:#cbd5e1;
                font-size:13px;
                line-height:1.6;
            ">
                Compare loan options and
                always verify the latest
                terms directly with the bank.
            </div>

        </div>
        """
    ),
    unsafe_allow_html=True
)


# ==========================================================
# HOME
# ==========================================================

if page == "🏠 Home":

    # ------------------------------------------------------
    # HERO
    # ------------------------------------------------------

    st.markdown(
        html(
            """
            <div class="hero">

                <h1>
                    🏦 SmartLoan India
                </h1>

                <p>
                    Find, compare and calculate loans
                    from major Indian banks — all in one place.
                </p>

            </div>
            """
        ),
        unsafe_allow_html=True
    )


    # ------------------------------------------------------
    # TITLE
    # ------------------------------------------------------

    st.markdown(
        html(
            """
            <div class="section-title">
                Choose the loan you need
            </div>

            <p style="
                color:#64748b;
                margin-top:0;
                margin-bottom:27px;
                font-size:15px;
            ">
                Explore loan options designed for different
                financial needs.
            </p>
            """
        ),
        unsafe_allow_html=True
    )


    # ======================================================
    # PERSONAL / EDUCATION / HOME
    # ======================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            html(
                """
                <div class="loan-card">

                    <div class="loan-icon">
                        👤
                    </div>

                    <h3>
                        Personal Loan
                    </h3>

                    <p>
                        Flexible financing for personal,
                        emergency and lifestyle needs.
                    </p>

                    <div class="loan-explore">
                        Explore →
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            html(
                """
                <div class="loan-card">

                    <div class="loan-icon">
                        🎓
                    </div>

                    <h3>
                        Education Loan
                    </h3>

                    <p>
                        Finance higher education in India
                        or abroad with suitable options.
                    </p>

                    <div class="loan-explore">
                        Explore →
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            html(
                """
                <div class="loan-card">

                    <div class="loan-icon">
                        🏠
                    </div>

                    <h3>
                        Home Loan
                    </h3>

                    <p>
                        Compare financing options for
                        purchasing or constructing a home.
                    </p>

                    <div class="loan-explore">
                        Explore →
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    # ======================================================
    # CAR / TWO WHEELER / GOLD
    # ======================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            html(
                """
                <div class="loan-card">

                    <div class="loan-icon">
                        🚗
                    </div>

                    <h3>
                        Car Loan
                    </h3>

                    <p>
                        Finance your new or used car with
                        flexible repayment options.
                    </p>

                    <div class="loan-explore">
                        Explore →
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            html(
                """
                <div class="loan-card">

                    <div class="loan-icon">
                        🛵
                    </div>

                    <h3>
                        Two-Wheeler Loan
                    </h3>

                    <p>
                        Get financing for bikes, scooters
                        and other two-wheelers.
                    </p>

                    <div class="loan-explore">
                        Explore →
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            html(
                """
                <div class="loan-card">

                    <div class="loan-icon">
                        🥇
                    </div>

                    <h3>
                        Gold Loan
                    </h3>

                    <p>
                        Borrow against eligible gold assets
                        for your financial requirements.
                    </p>

                    <div class="loan-explore">
                        Explore →
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    # ======================================================
    # BUSINESS / LAP / AGRICULTURE
    # ======================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            html(
                """
                <div class="loan-card">

                    <div class="loan-icon">
                        💼
                    </div>

                    <h3>
                        Business Loan
                    </h3>

                    <p>
                        Financing solutions for business
                        expansion and working capital.
                    </p>

                    <div class="loan-explore">
                        Explore →
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            html(
                """
                <div class="loan-card">

                    <div class="loan-icon">
                        🏢
                    </div>

                    <h3>
                        Loan Against Property
                    </h3>

                    <p>
                        Access funds by using eligible
                        property as security.
                    </p>

                    <div class="loan-explore">
                        Explore →
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            html(
                """
                <div class="loan-card">

                    <div class="loan-icon">
                        🚜
                    </div>

                    <h3>
                        Agriculture Loan
                    </h3>

                    <p>
                        Financial support for farming and
                        agricultural activities.
                    </p>

                    <div class="loan-explore">
                        Explore →
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    # ======================================================
    # HOW IT WORKS
    # ======================================================

    st.markdown("---")


    st.markdown(
        html(
            """
            <div class="section-title">
                How it works
            </div>

            <p style="
                color:#64748b;
                margin-top:0;
                margin-bottom:22px;
            ">
                Get from loan selection to EMI calculation
                in four simple steps.
            </p>
            """
        ),
        unsafe_allow_html=True
    )


    step1, step2, step3, step4 = st.columns(4)


    with step1:

        st.markdown(
            html(
                """
                <div class="step-card">

                    <div class="step-number">
                        01
                    </div>

                    <div class="step-icon">
                        🏦
                    </div>

                    <h4>
                        Select Loan
                    </h4>

                    <p>
                        Choose the type of loan
                        you need.
                    </p>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with step2:

        st.markdown(
            html(
                """
                <div class="step-card">

                    <div class="step-number">
                        02
                    </div>

                    <div class="step-icon">
                        🏛️
                    </div>

                    <h4>
                        Select Bank
                    </h4>

                    <p>
                        Choose a bank from
                        the available list.
                    </p>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with step3:

        st.markdown(
            html(
                """
                <div class="step-card">

                    <div class="step-number">
                        03
                    </div>

                    <div class="step-icon">
                        💰
                    </div>

                    <h4>
                        Enter Amount
                    </h4>

                    <p>
                        Enter your required
                        loan amount.
                    </p>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    with step4:

        st.markdown(
            html(
                """
                <div class="step-card">

                    <div class="step-number">
                        04
                    </div>

                    <div class="step-icon">
                        🧮
                    </div>

                    <h4>
                        Calculate EMI
                    </h4>

                    <p>
                        Get your estimated
                        monthly EMI.
                    </p>

                </div>
                """
            ),
            unsafe_allow_html=True
        )


    # ======================================================
    # IMPORTANT NOTE
    # ======================================================

    st.markdown("---")


    st.markdown(
        html(
            """
            <div class="warning-box">

                ⚠️ <b>Important:</b>

                Loan interest rates, maximum amounts,
                eligibility requirements and fees can
                change over time.

                Always verify the latest terms directly
                with the respective bank before applying.

            </div>
            """
        ),
        unsafe_allow_html=True
    )


# ==========================================================
# FIND LOAN
# ==========================================================

elif page == "🔍 Find Loan":

    st.title("🔍 Find Your Loan")

    st.write(
        "Select a loan category and bank to explore available information."
    )


    loan_type = st.selectbox(
        "🏦 Select Loan Type",
        list(LOAN_DATA.keys())
    )


    bank = st.selectbox(
        "🏛️ Select Bank",
        BANKS
    )


    product = LOAN_DATA.get(
        loan_type,
        {}
    ).get(bank)


    st.markdown("---")


    # ======================================================
    # PRODUCT NOT FOUND
    # ======================================================

    if product is None:

        st.warning(
            f"""
            ❌ {bank} does not currently have
            verified {loan_type} information in
            our database.
            """
        )


        st.info(
            """
            We don't invent loan limits or interest
            rates when they haven't been verified.
            """
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


        # ==================================================
        # METRICS
        # ==================================================

        c1, c2, c3 = st.columns(3)


        with c1:

            if product["min_amount"]:

                st.metric(
                    "Minimum Loan",
                    f"₹{product['min_amount']:,}"
                )

            else:

                st.metric(
                    "Minimum Loan",
                    "Check Bank"
                )


        with c2:

            if product["max_amount"]:

                st.metric(
                    "Maximum Loan",
                    f"₹{product['max_amount']:,}"
                )

            else:

                st.metric(
                    "Maximum Loan",
                    "Check Bank"
                )


        with c3:

            if product["interest_rate"]:

                st.metric(
                    "Interest Rate",
                    f"{product['interest_rate']}%"
                )

            else:

                st.metric(
                    "Interest Rate",
                    "Check Bank"
                )


        st.markdown("---")


        # ==================================================
        # LOAN REQUIREMENT
        # ==================================================

        st.subheader("💰 Loan Requirement")


        # --------------------------------------------------
        # CAR LOAN
        # --------------------------------------------------

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


        # --------------------------------------------------
        # TWO-WHEELER LOAN
        # --------------------------------------------------

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


        # --------------------------------------------------
        # GOLD LOAN
        # --------------------------------------------------

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


        # --------------------------------------------------
        # EDUCATION LOAN
        # --------------------------------------------------

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


        # --------------------------------------------------
        # HOME LOAN
        # --------------------------------------------------

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


        # --------------------------------------------------
        # OTHER LOANS
        # --------------------------------------------------

        else:

            min_amount = (
                product["min_amount"]
                if product["min_amount"]
                else 10000
            )


            max_amount = (
                product["max_amount"]
                if product["max_amount"]
                else 100000000
            )


            default_amount = min(
                500000,
                max_amount
            )


            loan_amount = st.number_input(
                "💰 Required Loan Amount (₹)",
                min_value=min_amount,
                max_value=max_amount,
                value=default_amount,
                step=10000
            )


        # ==================================================
        # AMOUNT VALIDATION
        # ==================================================

        if product["max_amount"]:

            if loan_amount > product["max_amount"]:

                st.error(
                    f"""
                    Requested amount exceeds the
                    displayed maximum of
                    ₹{product['max_amount']:,}.
                    """
                )

                st.stop()


        if product["min_amount"]:

            if loan_amount < product["min_amount"]:

                st.error(
                    f"""
                    Requested amount is below the
                    displayed minimum of
                    ₹{product['min_amount']:,}.
                    """
                )

                st.stop()


        # ==================================================
        # TENURE
        # ==================================================

        st.subheader("📅 Loan Tenure")


        if product["max_tenure"]:

            tenure = st.slider(
                "Select Tenure (Years)",
                min_value=1,
                max_value=product["max_tenure"],
                value=min(
                    5,
                    product["max_tenure"]
                )
            )

        else:

            tenure = st.slider(
                "Select Tenure (Years)",
                min_value=1,
                max_value=30,
                value=5
            )


        # ==================================================
        # INTEREST RATE
        # ==================================================

        if product["interest_rate"]:

            interest_rate = product["interest_rate"]

            st.info(
                f"Indicative interest rate: {interest_rate}%"
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


        # ==================================================
        # BUTTONS
        # ==================================================

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


        # ==================================================
        # OFFICIAL WEBSITE
        # ==================================================

        if official:

            st.link_button(
                "Open Official Bank Website",
                product["source_url"]
            )


        # ==================================================
        # ADD TO COMPARE
        # ==================================================

        if compare:

            st.session_state.selected_loan = loan_type

            st.session_state.selected_bank = bank

            st.success(
                f"✅ {bank} {loan_type} selected for comparison."
            )


        # ==================================================
        # CALCULATE EMI
        # ==================================================

        if calculate:

            if interest_rate <= 0:

                st.error(
                    "Please enter a valid interest rate."
                )

            else:

                emi, total_interest, total_payment = calculate_emi(
                    loan_amount,
                    interest_rate,
                    tenure
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


                st.markdown(
                    html(
                        f"""
                        <div class="success-box">

                            <b>Loan Summary</b>

                            <br><br>

                            <b>Bank:</b> {bank}

                            <br>

                            <b>Loan Type:</b> {loan_type}

                            <br>

                            <b>Loan Amount:</b>
                            ₹{loan_amount:,}

                            <br>

                            <b>Interest Rate:</b>
                            {interest_rate}%

                            <br>

                            <b>Tenure:</b>
                            {tenure} years

                        </div>
                        """
                    ),
                    unsafe_allow_html=True
                )


        # ==================================================
        # SOURCE
        # ==================================================

        st.markdown("---")

        st.caption(
            f"Information source: {product['source']}"
        )


# ==========================================================
# COMPARE LOANS
# ==========================================================

elif page == "📊 Compare Loans":

    st.title("📊 Compare Loans")


    st.write(
        "Select a loan type and multiple banks to compare available information."
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

                product = LOAN_DATA.get(
                    loan_type,
                    {}
                ).get(bank)


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

                    rows.append(
                        {
                            "Bank": bank,

                            "Available":
                                "✅ Yes",

                            "Minimum Loan":
                                (
                                    f"₹{product['min_amount']:,}"
                                    if product["min_amount"]
                                    else "Check Bank"
                                ),

                            "Maximum Loan":
                                (
                                    f"₹{product['max_amount']:,}"
                                    if product["max_amount"]
                                    else "Check Bank"
                                ),

                            "Interest Rate":
                                (
                                    f"{product['interest_rate']}%"
                                    if product["interest_rate"]
                                    else "Check Bank"
                                ),

                            "Maximum Tenure":
                                (
                                    f"{product['max_tenure']} years"
                                    if product["max_tenure"]
                                    else "Check Bank"
                                )
                        }
                    )


            df = pd.DataFrame(rows)


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

    st.title("🧮 EMI Calculator")


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


        st.markdown(
            html(
                f"""
                <div class="success-box">

                    <b>Calculation Summary</b>

                    <br><br>

                    <b>Loan Amount:</b>
                    ₹{amount:,}

                    <br>

                    <b>Interest Rate:</b>
                    {rate}%

                    <br>

                    <b>Tenure:</b>
                    {years} years

                    <br>

                    <b>Monthly EMI:</b>
                    ₹{emi:,.2f}

                </div>
                """
            ),
            unsafe_allow_html=True
        )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    html(
        """
        <div class="footer">

            <div style="
                font-size:20px;
                font-weight:800;
                color:#0f172a;
                margin-bottom:8px;
            ">
                🏦 SmartLoan India
            </div>

            <div style="
                margin-bottom:10px;
                color:#64748b;
            ">
                Compare • Calculate • Explore
            </div>

            <div style="
                font-size:13px;
                color:#94a3b8;
            ">
                Loan information is provided for
                comparison and educational purposes.
            </div>

            <div style="
                font-size:13px;
                color:#94a3b8;
                margin-top:5px;
            ">
                Always verify the latest terms with
                the respective bank.
            </div>

        </div>
        """
    ),
    unsafe_allow_html=True
)
