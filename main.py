import math

base_percent = 10


def result(rating, goal, source, gender, age, finance, sum_credit, period):
    d = "одобрено"
    annual_payment = None
    pension_age_female = 60
    pension_age_male = 65
    mod = _modificator(goal, rating, sum_credit, source)
    print(mod)
    annual_payment = round(_calc(mod, sum_credit, period), 8)
    if (annual_payment > finance / 2) or rating == "-2" or source == "безработный" or (
            (sum_credit / period) > (finance / 3)):
        d = "отказано"
        annual_payment = 0
    if gender == "М":
        if age + period > pension_age_male:
            d = "отказано"
            annual_payment = 0
    if gender == "Ж":
        if age + period > pension_age_female:
            d = "отказано"
            annual_payment = 0
    if d == "одобрено":
        if (source == "пассивный" or rating == "-1") and sum_credit > 1:
            sum_credit = 0.99999999
        if (source == "наемный" or rating == "0") and sum_credit > 5:
            sum_credit = 4.99999999
        if (source == "бизнес" or rating == "1" or rating == "2") and sum_credit > 10:
            sum_credit = 9.99999999
        mod = _modificator(goal, rating, sum_credit, source)
        annual_payment = round(_calc(mod, sum_credit, period), 8)
    return d, annual_payment


def _modificator(goal, rating, sum_credit, source):
    mod = -math.log10(sum_credit)
    if goal == "ипотека":
        mod -= 2
    elif goal == "потребительский кредит":
        mod += 1.5
    elif goal == "для бизнеса":
        mod -= 0.5

    if rating == "-1":
        mod += 1.5
    elif rating == "1":
        mod -= 0.25
    elif rating == "2":
        mod -= 0.75

    if source == "пассивный":
        mod += 0.5
    elif source == "наемный":
        mod -= 0.25
    elif source == "бизнес":
        mod += 0.25
    return mod


def _calc(mod, sum_credit, period):
    annual_payment = (sum_credit * (1 + period * ((base_percent + mod) / 100))) / period
    return annual_payment

