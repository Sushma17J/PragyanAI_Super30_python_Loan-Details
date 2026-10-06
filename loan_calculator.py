# loan_calculator.py


def calculate_emi(
    principal,
    annual_rate,
    years
):

    months = int(years * 12)

    if months <= 0:
        return 0, 0, 0

    monthly_rate = annual_rate / (12 * 100)

    if monthly_rate == 0:

        emi = principal / months

    else:

        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** months
        ) / (
            (1 + monthly_rate) ** months - 1
        )

    total_payment = emi * months

    total_interest = (
        total_payment - principal
    )

    return (
        emi,
        total_interest,
        total_payment
    )
