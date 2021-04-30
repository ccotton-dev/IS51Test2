# Code for sorting grades

def calculate_percentage_above_average(avg, grades):
    counter = 0
    percent = 0.0
    for i in grades:
        if float(i) > avg:
            counter = counter+1
    percent = counter/len(grades) * 100
    return round(percent,2)

def average_grade(grades):
    add = sum(grades)
    length = len(grades)
    avg = add / length
    return avg

def main():
    a_file = open("/Users/CCott_000/Desktop/Spring2021/Test2/Final.txt", "r")
    grades = []
    for i in a_file:
        grades.append(int(i))
    avg = average_grade(grades)
    print("Number of grades:", len(grades))
    print("Average grade:", avg)
    print("Percentage of grades above average: ", calculate_percentage_above_average(avg, grades), "%", sep='')
    
    ##print(a_file.read())
    a_file.close()

if __name__ == "__main__":
    main()