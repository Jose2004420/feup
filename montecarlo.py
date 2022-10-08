#this program takes awhile to run so pls be a bit patient (10 seconds or so)

#ok so first of all I am going to define a function which performs the actual task of determining pi
#this function takes a int value (times)

def main_loop(times):
    import random
    import math
    import statistics

    pi=[]
    #let's determine 100 values of pi using 1000 points each time
    for i in range(100):
            n_inside_c = 0
            total = 0
            for i in range(times):


                #use random to get the postion in x and y of the needle
                x_position = random.uniform(0, 2)

                y_position = random.uniform(0, 2)

                # calculate if the needle is inside the circle
                distance = math.sqrt((1 - x_position) ** 2 + (1 - y_position) ** 2)
                if distance < 1:
                    n_inside_c += 1
                total += 1
                result = ((4 * n_inside_c) / total)

            pi.append(result)
    avg = sum(pi) / 100
    a = statistics.stdev(pi)

    answer=[a,avg]

    return answer

#while loop for checking if the deviation is less than the value asked
stdevi=[1,1]
times=1
while stdevi[0]>=0.005:
    arr=[]

    arr.append(main_loop(1000*times))
    times =times*2
    stdevi=arr[0]
#printing the result of pi using Monte Carlo
print("Pi is approximately",arr[0][1])



