# create the initial variables below
age = 34
smoker = 1
sex = 0
bmi = 38.2
num_of_children = 2
# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")
# Age Factor

age += 4
print(age)
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(new_insurance_cost) + " dollars.")

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("People who are 4 years older have estimated insurance cost " + str(change_in_insurance_cost) + " dollars diferent.")
# BMI Factor

age = 28
bmi += 3.1
change_in_insurance_cost = new_insurance_cost - insurance_cost


print("The change in estimate after increasing BMI by 3.1 " + str(change_in_insurance_cost) + " dollars.")




# Male vs. Female Factor

bmi = 26.2
sex = 1

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")


# Extra Practice
