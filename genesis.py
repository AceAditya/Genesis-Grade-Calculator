from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
from tkinter import *


def getInfo():
    info = ['parents.mcvts.net', 'natalex@optonline.net', 'Natella', 4, 10]
    info1 = ['parents.westfieldnjk12.org', 'jkneht@gmail.com', 'michael', 3, 11]
    return info
def openGenesis(information):
    #information = getInfo()
    driver = webdriver.Chrome()
    genesis = information[0]
    if 'https://' not in genesis:
        genesis = 'https://' + genesis
    driver.get(genesis)
    driver.implicitly_wait(5)
    Username = driver.find_element_by_id("j_username")
    Password = driver.find_element_by_id('j_password')
    Username.send_keys(information[1])
    Password.send_keys(information[2])
    driver.find_element_by_class_name('saveButton').click()
    driver.implicitly_wait(5)
    return driver
def goToGrading(driver, info):
    driver.find_element_by_xpath("//div[@class = 'headerCategories']/span[{}]".format(info[3])).click()
    driver.find_element_by_xpath("//div[@class = 'studentTabBar']/span[2]").click()
def gatherGrade(driver, grade):
    grades = []
    b = 3
    tally = 0
    max = grade - 9
    for i in range(1, 1000):
        try:
            fg = driver.find_element_by_xpath("//tbody/tr[{}]/td[5]".format(2*i)).text
            #print(fg)
            grades.append(fg)
        except:
            tally += 1
            if tally >= 2 * max:
                break



        #FG = fg.find_element_by_xpath("//td[@class='cellLeft[2]']").text
        try:
            fg2 = driver.find_element_by_xpath("//tbody/tr[{}]/td[5]".format(b)).text
            #print(fg2)
            grades.append(fg2)
        except:
            tally += 1
            if tally >= 2 * max:
                break

        #FG2 = fg2.find_element_by_xpath("//td[@class='cellLeft[2]']").text
        b = b + 2
    return grades
def gatherCredits(driver, grade):
    max = grade - 9
    credits = []
    b = 3
    tally = 0
    for i in range(1, 1000):
        try:
            fc = driver.find_element_by_xpath("//tbody/tr[{}]/td[7]".format(2*i)).text
           # print(fc)
            credits.append(fc)
        except:
            tally += 1
            if tally >= 2 * max:
                break

        #FG = fg.find_element_by_xpath("//td[@class='cellLeft[2]']").text
        try:
            fc2 = driver.find_element_by_xpath("//tbody/tr[{}]/td[7]".format(b)).text
          #  print(fc2)
            credits.append(fc2)
        except:
            tally += 1
            if tally >= 2 * max:
                break

        #FG2 = fg2.find_element_by_xpath("//td[@class='cellLeft[2]']").text
        b = b + 2

    return credits
def print_GPA(credits, grades):

	for i in range(len(credits)):
		credits[i] = float(credits[i])

	credits_numpy = np.array(credits)
	numbers = []
	letter_grades = ["A+","A", "A-", "B+", "B" , "B-", "C+", "C", "C-" , "D", "F"]
	scale = np.array([4.3333,4.0, 3.6666, 3.3333, 3.0, 2.6666, 2.3333 , 2.0, 1.6666, 1.0, 0.0])
	for i in range(len(grades)):
		for j in range (len(letter_grades)):
			if grades [i] == letter_grades[j]:
				numbers.append(scale[j])
	#print(numbers)
	num = np.array(numbers)
	#print (credits_numpy)
	#print (num)
	multiply_array = np.multiply(num, credits_numpy)
	#print (almost)
	multiply_array = np.sum(multiply_array)
	sum_credits = np.sum(credits)
	answer = multiply_array / sum_credits
	return(round(answer, 2))

def driver (info):
	#info = getInfo()
	driver = openGenesis(info)
	goToGrading(driver, info)
	grades = gatherGrade(driver, info[4])
	credits = gatherCredits(driver, info[4])
	lsum["text"] = "GPA: " + str(print_GPA(credits, grades)) 

data = []
master = Tk()
master.title ("Genesis GPA Calculator")
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
def do ():
	data.append( e1.get())
	data.append( e2.get())
	data.append (e3.get())
	data.append (int(e4.get()))
	data.append (int(e5.get()))
	driver(data)
Label(master, text="Exact Link to Genesis").grid(row=0)
Label(master, text="Username").grid(row=1)
Label(master, text="Password").grid(row=2)
Label(master, text="Which slot from the left if the Graded Tab").grid(row=3)
Label(master, text="Grade Currently In").grid(row=4)

e1.grid(row=0, column=2)
e2.grid(row=1, column=2)
e3.grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row =4, column=2)

Button(master, text='Show', command=do).grid(row=5, column=0, sticky=W, pady=4)	
Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
lsum = Label(master, text = 'GPA:')
lsum.grid(row=6, column=2, sticky=W, pady=4)

mainloop()


