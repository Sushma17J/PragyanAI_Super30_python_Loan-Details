import streamlit as st
import pandas as pd

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
# SESSION STATE
# ==========================================================

if "selected_loan" not in st.session_state:
    st.session_state.selected_loan = None

if "selected_bank" not in st.session_state:
    st.session_state.selected_bank = None


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* HERO */

.hero {
    padding: 40px;
    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            #0f172a,
            #1d4ed8
        );

    color: white;

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero p {
    font-size: 19px;
}


/* CARDS */

.card {
    background: white;

    padding: 25px;

    border-radius: 18px;

    border: 1px solid #e5e7eb;

    box-shadow:
        0px 5px 20px
        rgba(0,0,0,0.06);

    margin-bottom: 20px;
}


/* SECTION */

.section-title {
    font-size: 30px;
    font-weight: 750;
    margin-top: 20px;
    margin-bottom: 20px;
}


/* INFO */

.info-box {
    padding: 18px;

    border-radius: 12px;

    background: #eff6ff;

    border-left:
        5px solid #2563eb;
}


/* WARNING */

.warning-box {
    padding: 18px;

    border-radius: 12px;

    background: #fff7ed;

    border-left:
        5px solid #f97316;
}


/* SUCCESS */

.success-box {
    padding: 18px;

    border-radius: 12px;

    background: #ecfdf5;

    border-left:
        5px solid #10b981;
}


/* FOOTER */

.footer {
    text-align: center;

    padding: 30px;

    margin-top: 50px;

    color: #64748b;
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.markdown(
    """
    <div style="text-align:center">

    <h1>🏦</h1>

    <h2>SmartLoan India</h2>

    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")


page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔍 Find Loan",
        "📊 Compare Loans",
        "🧮 EMI Calculator"
    ]
)


st.sidebar.markdown("---")


st.sidebar.info(
    """
    Compare loan products from
    major Indian banks.

    Always verify current terms
    with the respective bank.
    """
)


# ==========================================================
# HOME
# ==========================================================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="hero">

        <h1>🏦 SmartLoan India</h1>

        <p>
        Find, compare and calculate loans
        from major Indian banks.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="section-title">'
        'Choose the loan you need'
        '</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            """
            <div class="card">

            <h2>👤</h2>

            <h3>Personal Loan</h3>

            <p>
            For personal and emergency
            financial requirements.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            """
            <div class="card">

            <h2>🎓</h2>

            <h3>Education Loan</h3>

            <p>
            Finance higher education
            in India or abroad.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            """
            <div class="card">

            <h2>🏠</h2>

            <h3>Home Loan</h3>

            <p>
            Compare home financing
            options.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            """
            <div class="card">

            <h2>🚗</h2>

            <h3>Car Loan</h3>

            <p>
            Finance new or used
            vehicles.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            """
            <div class="card">

            <h2>🛵</h2>

            <h3>Two-Wheeler Loan</h3>

            <p>
            Finance bikes and
            scooters.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            """
            <div class="card">

            <h2>🥇</h2>

            <h3>Gold Loan</h3>

            <p>
            Borrow against eligible
            gold assets.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("---")


    st.subheader("🚀 How it works")


    step1, step2, step3, step4 = st.columns(4)


    with step1:
        st.markdown(
            """
            ### 01
            🏦

            **Select Loan**
            """
        )


    with step2:
        st.markdown(
            """
            ### 02
            🏛️

            **Select Bank**
            """
        )


    with step3:
        st.markdown(
            """
            ### 03
            💰

            **Enter Amount**
            """
        )


    with step4:
        st.markdown(
            """
            ### 04
            🧮

            **Calculate EMI**
            """
        )


# ==========================================================
# FIND LOAN
# ==========================================================

elif page == "🔍 Find Loan":

    st.title("🔍 Find Your Loan")


    st.write(
        "Select a loan category and bank."
    )


    # ======================================================
    # LOAN TYPE
    # ======================================================

    loan_type = st.selectbox(
        "🏦 Select Loan Type",
        list(LOAN_DATA.keys())
    )


    # ======================================================
    # BANK
    # ======================================================

    bank = st.selectbox(
        "🏛️ Select Bank",
        BANKS
    )


    # ======================================================
    # CHECK PRODUCT
    # ======================================================

    product = LOAN_DATA.get(
        loan_type,
        {}
    ).get(
        bank
    )


    st.markdown("---")


    if product is None:

        st.warning(
            f"""
            ❌ **{bank}** does not currently have
            verified {loan_type} information in
            this application's database.
            """
        )


        st.info(
            """
            The bank is still shown in the dropdown
            because this application is designed to
            contain all major banks.

            We do not invent loan limits or rates
            when they have not been verified.
            """
        )


        if bank in BANK_WEBSITES:

            st.link_button(
                "🌐 Check Bank Website",
                BANK_WEBSITES[bank]
            )


    else:

        # ==================================================
        # BANK + PRODUCT HEADER
        # ==================================================

        st.subheader(
            f"🏦 {bank} — {loan_type}"
        )


        # ==================================================
        # AVAILABILITY
        # ==================================================

        if not product.get("available", False):

            st.error(
                "This loan product is not available."
            )

        else:

            st.success(
                "✅ Loan product found"
            )


            # ==============================================
            # PRODUCT METRICS
            # ==============================================

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
                        "No fixed cap shown"
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


            # ==============================================
            # CATEGORY-SPECIFIC INPUTS
            # ==============================================

            st.subheader(
                "💰 Loan Requirement"
            )


            # ----------------------------------------------
            # CAR LOAN
            # ----------------------------------------------

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
                    f"Required Loan Amount: "
                    f"₹{loan_amount:,}"
                )


            # ----------------------------------------------
            # TWO WHEELER
            # ----------------------------------------------

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
                    f"Required Loan Amount: "
                    f"₹{loan_amount:,}"
                )


            # ----------------------------------------------
            # GOLD LOAN
            # ----------------------------------------------

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
                    f"Gold entered: "
                    f"{gold_weight} grams, "
                    f"{gold_purity}"
                )


            # ----------------------------------------------
            # EDUCATION LOAN
            # ----------------------------------------------

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
                        """
                        Required loan is greater than
                        the entered course fee.
                        """
                    )


            # ----------------------------------------------
            # HOME LOAN
            # ----------------------------------------------

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
                    f"Required Home Loan: "
                    f"₹{loan_amount:,}"
                )


            # ----------------------------------------------
            # OTHER LOANS
            # ----------------------------------------------

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
            # VALIDATE MAXIMUM
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

            st.subheader(
                "📅 Loan Tenure"
            )


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

                interest_rate = product[
                    "interest_rate"
                ]

                st.info(
                    f"Using displayed rate: "
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
            # COMPARE
            # ==================================================

            if compare:

                st.session_state.selected_loan = loan_type

                st.session_state.selected_bank = bank

                st.success(
                    f"""
                    ✅ {bank} {loan_type}
                    added for comparison.
                    """
                )


            # ==================================================
            # CALCULATE
            # ==================================================

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


                    st.markdown(
                        f"""
                        <div class="success-box">

                        <b>Loan Summary</b>

                        <br><br>

                        Bank: {bank}

                        <br>

                        Loan Type: {loan_type}

                        <br>

                        Loan Amount:
                        ₹{loan_amount:,}

                        <br>

                        Interest Rate:
                        {interest_rate}%

                        <br>

                        Tenure:
                        {tenure} years

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


            # ==================================================
            # SOURCE
            # ==================================================

            st.markdown("---")

            st.caption(
                f"Source: {product['source']}"
            )


# ==========================================================
# COMPARE LOANS
# ==========================================================

elif page == "📊 Compare Loans":

    st.title("📊 Compare Loans")


    st.write(
        """
        Select a loan type and multiple banks
        to compare the information available
        in this application.
        """
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
                ).get(
                    bank
                )


                if product is None:

                    rows.append({
                        "Bank": bank,
                        "Available": "❌ No data",
                        "Minimum Loan": "-",
                        "Maximum Loan": "-",
                        "Interest Rate": "-",
                        "Maximum Tenure": "-"
                    })

                else:

                    rows.append({
                        "Bank": bank,

                        "Available":
                            "✅ Yes"
                            if product["available"]
                            else "❌ No",

                        "Minimum Loan":
                            (
                                f"₹{product['min_amount']:,}"
                                if product["min_amount"]
                                else "-"
                            ),

                        "Maximum Loan":
                            (
                                f"₹{product['max_amount']:,}"
                                if product["max_amount"]
                                else "No fixed limit shown"
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
                    })


            df = pd.DataFrame(rows)


            st.markdown("---")


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
        "Use this calculator for an estimated EMI."
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


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <div class="footer">

    🏦 <b>SmartLoan India</b>

    <br><br>

    Compare • Calculate • Explore

    <br><br>

    Loan information is provided for
    comparison/educational purposes.
    Always verify current terms with
    the respective bank.

    </div>
    """,
    unsafe_allow_html=True
)
