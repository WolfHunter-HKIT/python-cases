sar1 = [2, 4, -5, 7, -9, 4]
sar2 = [1, -8, 4, 9]

# Sukurti porų sąrašą, kur pirmas elementas iš sar1, antras iš sar2, kurių suma - lyginis skaičius.

sarPora = [(i, j) for i in sar1 for j in sar2 if (i + j) % 2 == 0]

# for i in sar1:
#     for j in sar2:
#         suma = i + j
#         if suma % 2 == 0:
#             sarPora.append((i, j))
print(sarPora)