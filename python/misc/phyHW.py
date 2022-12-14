# # #  Physics HW 6: Q2 Part 1

import math

c = 2.9979246e8


# # me = 9.10938215e-31
# # mn = 1.67492735e-27


# # e_e = (mn) * ((c) ** 2)

# # # 1/2mv^2
# # # k = math.sqrt(2 * (e_e - (me * (c) ** 2)) / me)

# # # with the gamma
# # v = c * math.sqrt(-((me * (c ** 2) / e_e) ** 2) + 1)


# # # Part 2
# # re_e = me * c ** 2
# # k = e_e - (re_e)

# # print(v)


# # Question 8

# w = 1.9e-13 * 0.6
# m = 9e-31
# v = 0.869 * c


# y = 1 / math.sqrt(1 - ((v / c) ** 2))


# print(w)

# # vc = math.sqrt(-((((m * c ** 2) / w) + (1 / y)) ** 2) + 1)

# vc = math.sqrt(-(((m * c ** 2) / (w + (y * m * c ** 2))) ** 2) + 1)

# print(vc)

# Question 10

m_n = 3.620124e-25
m_alp = 6.640678e-27
m_new_n = 3.553550e-25
e = 1.6e-19

rest_e = m_n * c ** 2

rest_new_e = m_new_n * c ** 2
rest_a = m_alp * c ** 2

# print(rest_new_e, rest_a, rest_new_e + rest_a, rest_e)

# Sum of all kinetic energies
sum_k = rest_e - (rest_new_e + rest_a)

print(sum_k / e)
