def getIncomeTax(salary):
    personal_allowance = 11850
    tax_band_1 = 34500
    tax_band_2 = 150000

    rate_band_1 = 0.20
    rate_band_2 = 0.40
    rate_band_3 = 0.45

    tax = 0

    if salary <= personal_allowance:
        tax = 0
    elif salary <= tax_band_1:
        tax = (salary - personal_allowance) * rate_band_1
    elif salary <= tax_band_2:
        tax = (tax_band_1 - personal_allowance) * rate_band_1 \
            + (salary - tax_band_1) * rate_band_2
    else:
        tax = (tax_band_1 - personal_allowance) * rate_band_1 \
            + (tax_band_2 - tax_band_1) * rate_band_2 \
            + (salary - tax_band_2) * rate_band_3

    return tax

salary = float(input("Enter your salary: £"))
income_tax = getIncomeTax(salary)
print("Income tax:", income_tax)
