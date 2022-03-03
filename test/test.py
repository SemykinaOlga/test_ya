import allure
import pytest

from main import result


@allure.testcase(
    "https://docs.google.com/spreadsheets/d/1yv72eVpfFtXAiEtWl8R2dBW4d5WRT0bEuFSVsthMIOg/edit?usp=sharing",
    "расчет кредитной заявки")
@pytest.mark.parametrize("rating, goal, source_finance, gender, age, finance, sum_credit, period, excepted_decision, "
                         "expected_payment",
                         [
                             pytest.param(
                                 "-1", "ипотека", "пассивный", "Ж", 18, 2, 0.5, 47, "отказано", 0,
                                 id="1.1.1	отказ: превышает пенсионный возраст на момент возврата кредита, Ж"
                             ),
                             pytest.param(
                                 "0", "для бизнеса", "наемный", "М", 45, 10, 1, 22, "отказано", 0,
                                 id="1.1.2	отказ: превышает пенсионный возраст на момент возврата кредита, М"
                             ),
                             pytest.param(
                                 "1", "автокредит", "бизнес", "Ж", 20, 2.56, 5.23, 5, "отказано", 0,
                                 id="1.2.1	отказ: сумма кредита более трети годового дохода (суммы на срок)"
                             ),
                             pytest.param(
                                 "-1", "для бизнеса", "пассивный", "М", 35, 0.4, 0.5, 3.5, "отказано", 0,
                                 id="1.2.2	отказ: годовой платёж (включая проценты) больше половины дохода"
                             ),
                             pytest.param(
                                 "2", "ипотека", "безработный", "Ж", 35, 0, 2, 20, "отказано", 0,
                                 id="1.2.3	отказ: безработный"
                             ),
                             pytest.param(
                                 "-2", "потребительский", "бизнес", "М", 20, 10, 1, 5, "отказано", 0,
                                 id="1.3.1	отказ: кредитный рейтинг -2"
                             ),
                             pytest.param(
                                 "-1", "ипотека", "пассивный", "Ж", 55, 2, 1, 5, "одобрено", 0.3,
                                 id="2.1.1	пенсионный возраст равен возврату кредита Ж, сумма кредита равна лимиту для рейтинга -1"
                             ),
                             pytest.param(
                                 "-1", "для бизнеса", "бизнес", "М", 18, 0.246, 0.123, 1.5, "одобрено", 0.09695692,
                                 id="2.1.2	равен трети годового дохода (сумма на срок), сумма менее лимита для рейтинга -1"
                             ),
                             pytest.param(
                                 "-1", "потребительский", "пассивный", "М", 20, 4, 1, 10, "одобрено", 0.22,
                                 id="2.1.3	сумма кредита равна лимиту для пассивного дохода"
                             ),
                             pytest.param(
                                 "-1", "автокредит", "пассивный", "Ж", 35, 10.5, 2, 5, "одобрено", 0.32,
                                 id="2.1.4	Превышение лимита пассивный"
                             ),
                             pytest.param(
                                 "0", "ипотека", "наемный", "Ж", 23, 5, 5, 15, "одобрено", 0.68588483,
                                 id="2.2.1	сумма кредита равна лимиту, наемный"
                             ),
                             pytest.param(
                                 "0", "для бизнеса", "наемный", "Ж", 37, 10.35, 5, 3.5, "одобрено", 1.85612293,
                                 id="2.2.2	сумма кредита равна лимиту для рейтинга 0"
                             ),
                             pytest.param(
                                 "0", "потребительский", "пассивный", "М", 39, 2.5, 0.26, 5.5, "одобрено", 0.0760938,
                                 id="2.2.3	сумма кредита менее лимита для рейтинга 0"
                             ),
                             pytest.param(
                                 "0", "автокредит", "бизнес", "Ж", 44, 30, 5.235, 10, "одобрено", 0.9775515,
                                 id="2.2.4	Превышение лимита рейтинг 0"
                             ),
                             pytest.param(
                                 "1", "ипотека", "бизнес", "М", 45, 10.365, 10, 12, "одобрено", 1.53333333,
                                 id="2.3.1	сумма кредита равна лимиту, бизнес"
                             ),
                             pytest.param(
                                 "1", "для бизнеса", "пассивный", "М", 46, 10.005, 0.8, 1, "одобрено", 0.87877528,
                                 id="2.3.2	сумма кредита менее лимита, пассивный"
                             ),
                             pytest.param(
                                 "1", "автокредит", "наемный", "Ж", 47, 11, 4.999, 2.2, "одобрено", 2.71224056,
                                 id="2.3.3	сумма кредита менее лимита, наемный"
                             ),
                             pytest.param(
                                 "1", "потребительский", "бизнес", "М", 50, 20.3333, 10, 1.6, "одобрено", 7.15,
                                 id="2.3.4	сумма кредита равна лимиту для рейтинга 1"
                             ),
                             pytest.param(
                                 "1", "потребительский", "бизнес", "М", 52, 25, 9.999, 5, "одобрено", 2.89971434,
                                 id="2.3.5	сумма кредита менее лимита для рейтинга 1"
                             ),
                             pytest.param(
                                 "1", "ипотека", "бизнес", "М", 55, 40, 11, 5, "одобрено", 2.7,
                                 id="2.3.6	Превышение лимита рейтинг 1 "
                             ),
                             pytest.param(
                                 "1", "для бизнеса", "бизнес", "М", 35, 10, 4.5, 3.5, "одобрено", 1.68381972,
                                 id="2.3.7	сумма кредита менее лимита, бизнес"
                             ),
                             pytest.param(
                                 "2", "ипотека", "бизнес", "Ж", 53, 30, 10, 5, "одобрено", 2.65,
                                 id="2.4.1	сумма кредита равна лимиту для рейтинга 2"
                             ),
                             pytest.param(
                                 "2", "для бизнеса", "наемный", "М", 54, 40.50, 2, 5.5, "одобрено", 0.52761576,
                                 id="2.4.2	 годовой платеж (включая проценты) менее половины дохода"
                             ),
                             pytest.param(
                                 "2", "автокредит", "бизнес", "Ж", 54, 50, 5.2, 5, "одобрено", 1.49676783,
                                 id="2.4.3	сумма кредита менее трети годового дохода (сумма на срок)"
                             ),
                             pytest.param(
                                 "2", "потребительский", "пассивный", "М", 60, 55.55, 0.02, 5, "одобрено", 0.00628979,
                                 id="2.4.4	пенсионный возраст равен возврату кредита М"
                             ),
                             pytest.param(
                                 "2", "ипотека", "наемный", "Ж", 57, 155.55, 4.068, 2.5, "одобрено", 1.88717038,
                                 id="2.4.5	сумма кредита менее лимита для рейтинга 2"
                             ),
                             pytest.param(
                                 "2", "потребительский", "наемный", "М", 45, 11, 6, 6, "одобрено", 1.24838483,
                                 id="2.4.6	Превышение лимита наемный"
                             ),
                             pytest.param(
                                 "2", "автокредит", "наемный", "Ж", 50, 50, 20.52, 6.5, "одобрено", 1.18428227,
                                 id="2.4.7	Превышение лимита рейтинг 2"
                             ),
                             pytest.param(
                                 "2", "ипотека", "бизнес", "Ж", 50, 20, 11, 5.3, "одобрено", 2.53679245,
                                 id="2.4.8	Превышение лимита собственный бизнес"
                             ),
                         ]
                         )
def test_credit_request(rating, goal, source_finance, gender, age, finance, sum_credit, period, excepted_decision,
                        expected_payment):
    decision = result(rating, goal, source_finance, gender, age, finance, sum_credit, period)
    assert decision == (excepted_decision, expected_payment)
