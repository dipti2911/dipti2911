def calculateBMI(height,weight):
    heightinmeters = height * 0.4536
    print(heightinmeters)
    bmi = weight / (heightinmeters * heightinmeters)
    print(bmi)
calculateBMI(5,70)