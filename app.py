
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
        step=10000,
    )


    rate = st.number_input(
        "📈 Interest Rate (%)",
        min_value=0.0,
        max_value=50.0,
        value=10.0,
        step=0.1,
    )


    years = st.slider(
        "📅 Tenure",
        min_value=1,
        max_value=30,
        value=5,
    )


    if st.button(
        "🧮 Calculate EMI",
        type="primary",
        use_container_width=True,
    ):

        emi, interest, total = calculate_emi(
            amount,
            rate,
            years,
        )


        st.markdown("---")


        st.subheader(
            "📊 EMI Result"
        )


        c1, c2, c3 = st.columns(3)


        with c1:

            st.metric(
                "Monthly EMI",
                f"₹{emi:,.2f}",
            )


        with c2:

            st.metric(
                "Total Interest",
                f"₹{interest:,.2f}",
            )


        with c3:

            st.metric(
                "Total Repayment",
                f"₹{total:,.2f}",
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
    '<div class="footer">'
    '<div class="footer-title">'
    '🏦 SmartLoan India'
    '</div>'
    '<div>'
    'Compare • Calculate'
    '</div>'
    '<div class="footer-text">'
    'Loan information is provided for comparison '
    'and educational purposes.'
    '</div>'
    '<div class="footer-text">'
    'Always verify the latest terms with the respective bank.'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)
