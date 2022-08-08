print('BMI-BMR_CALCULATOR 1.1 BY FAHAD AREFIN.')
weight_raw = input('What is your weight in kg? ')



weight = float(weight_raw)

if int(weight_raw) >= 200 or int(weight_raw) <= 0:
    print('Please check your weight.')
    import time
    time.sleep(5)
    exit()


age = input('What is your age?(years) ')
if int(age) >= 100 or int(age) <= 0:
    print('Please check your age.')
    import time
    time.sleep(20)
    exit()


gender = str(input('What is your gender? (m for male f for female) '))

gender_final = str(gender.upper())

if 'M' in gender_final or 'F' in gender_final:

    height = input('what is your height in feet? ; example:Feet.inch? ')
    if 0 <= float(height) >= 8.00:
        print('Please check your height.')
        import time

        time.sleep(20)
        exit()
    exercise_intencity = str(input('How much do you exercise? \n'
                                   ' 1. Little/no exercise \n '
                                   '2. Light exercise \n'
                                   ' 3. Moderate exercise(3-5 days/wk) \n '
                                   '4. Very active (6-7 days/wk) \n '
                                   '5. Extra active (very active & physical job) \n '
                                   'Type the number only. \n '))

    float_height = float(height)
    int_height = int(float_height)
    height_decimals = round((float_height - float(int_height)) * 10)
    final_height_cm = ((int_height * 12 + height_decimals) * 2.54)

    final_height = ((int_height * 12 + height_decimals) * 0.0254) ** 2
    bmi = weight / final_height
    BMI = str(round(bmi))
    print('Your BMI is ' + BMI)

    if bmi < 18.5:
        print("You are under weignt!")
    if 18.5 <= bmi < 24.99:
        print('You are physically fit!')
    if 25.00 <= bmi < 29.99:
        print('You are in the overweight range! Do some exercise regularly!')
    if 30.00 <= bmi < 39.99:
        print('You are in the obese range!! Ask for professional help!!')

    if 'M' in gender_final:
        bmr = 88.362 + (13.397 * weight) + (4.799 * final_height_cm) - (5.677 * float(age))

    if 'F' in gender_final:
        bmr = 447.593 + (9.247 * weight) + (3.098 * final_height_cm) - (4.330 * float(age))
    if '1' in exercise_intencity:
        BMR = bmr * 1.2

    if '2' in exercise_intencity:
        BMR = bmr * 1.375
    if '3' in exercise_intencity:
        BMR = bmr * 1.55

    if '4' in exercise_intencity:
        BMR = bmr * 1.725
    if '5' in exercise_intencity:
        BMR = bmr * 1.9
    BMR_final = str(round(BMR))
    print('You need to take ' + BMR_final + ' calories to maintain your current weight. ')
    import time

    time.sleep(20)
else:
    print('Please check your gender input.')
    import time

    time.sleep(5)
    exit()

















