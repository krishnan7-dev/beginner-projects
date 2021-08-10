def calculate_bmi(weight, height):
    '''
    Function that calculated the bmi given weight and 
    height of the person.
    '''

    # BMI is the ratio of weight in kg
    # divided by the square of the height
    # in meters
    bmi = weight / (height ** 2)

    return bmi

if __name__ == '__main__':
    # Taking input for weight and height
    weight = eval(input("Enter your weight in kg : "))
    height = eval(input("Enter your height in meters : "))

    # Calculating BMI
    bmi = calculate_bmi(weight, height)

    # Displaying result
    print("Your BMI : ", bmi)