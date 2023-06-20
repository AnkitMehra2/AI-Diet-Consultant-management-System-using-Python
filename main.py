from tkinter import *
from random import randint
from tkinter import StringVar
import sys
import os

import wikipedia

root = Tk()
root.title("Health is Wealth")
root.geometry("800x520")
#root.maxsize()
photo = PhotoImage(file="1.png")
bg_label = Label(image=photo)

bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def BMI():
    label23 = Label(root, text='  YOUR BMI IS:')
    label23.grid(row=2, column=7)
    weight = v2.get()
    height = v3.get()
    bmi = float(int(weight) / (int(height) / 100) ** 2)

    #l31 = Label(root, text="YOUR BMI IS:")
    #l31.grid(row=1, column=8)
    l32 = Label(root, text=bmi)
    l32.grid(row=2, column=8)

    if bmi < 18.5:
        show = StringVar()
        l26 = Label(root, textvariable=show, relief=RAISED)
        show.set("YOU ARE UNDERWEIGHT")
        l26.grid(row=4, column=8)
    elif bmi > 18.5 and bmi < 24.9:
        show1 = StringVar()
        l27 = Label(root, textvariable=show1, relief=RAISED)
        show1.set("YOU ARE HEALTHY")
        l27.grid(row=4, column=8)

    elif bmi > 25 and bmi < 29.9:
        show2 = StringVar()
        l28 = Label(root, textvariable=show2, relief=RAISED)
        show2.set("YOU ARE OVERWEIGHT")
        l28.grid(row=4, column=8)

    elif bmi > 30:
        show3 = StringVar()
        l29 = Label(root, textvariable=show3, relief=RAISED)
        show3.set("YOU ARE OBESSED")
        l29.grid(row=4, column=8)

def location():
    l22 = Label(root, text="Enter the location:")
    l22.grid(row=24, column=4)
    v22 = StringVar()

    e22 = Entry(root, textvariable=v22)
    e22.grid(row=24, column=5)
    loca = v22.get()
    abc = str(loca)
    result = StringVar()
    l23 = Label(root, textvariable=result)
    result.set(wikipedia.search("Dieticians near" + abc))
    l23.grid(row=2, column=6)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def BMR():
    name = v1.get()
    weight = v2.get()
    height = v3.get()
    age = v4.get()
    Desired_weight = v8.get()
    activity = str(Lb.get(ACTIVE))
    gender = Lb2.get(ACTIVE)
    Diet_Type = Lb3.get(ACTIVE)



    # food items
    proteinVeg = ["Lentis/Dals(100gm)", "Green Peas/Matar(100gm)","Cooked Paneer(100gm)","Beans(100gm)"]
    proteinNveg = [ "Chicken(75gm)", "Chickpeas/ Chana(100gm)", "Cooked Fish(75gram)", "4 Eggs"]
    fruit = ['Bananas(200gm)', 'Apple(200gm)', 'Orange(200gm)', 'Grapes(200gm)', 'Pomegranante(200gm)', 'Papaya(200gm)']
    vegetable = ['Any vegetable(80g)']
    grains = ['Cooked Grain(150g)','Whole Grain Bread(1 slice)','Boiled Potato(75g)','Oats(250g)','2 corn/makka Roti']
    DairyProduct = ['low fat milk(200ml)','flavoured yogurt(150gm)', 'Cheese(125gm)', 'Curd(150gm)', 'Buttermilk/chaas(200ml)' ]
    FatsAndOils = ['2 TSP (10 ml) olive oil','2 TBSP (30g) reduced-calorie salad dressin','1/4 medium avocado','Small handful of nuts','1/2 ounce  grated Parmesan cheese','1 TBSP (20g) jam, jelly, honey, syrup, sugar']

    # gender logic:
    if gender == "Male":
        cal = float()
        cal1 = float()
        cal1 = 88.362 + (13.397 * float(weight)) + (4.799 * float(height)) - (5.677 * float(age))

        cal = 88.362 + (13.397 * float(Desired_weight)) + (4.799 * float(height)) - (5.677 * float(age))
    elif gender == "Female":
        cal = float()
        cal1 = float()
        cal1 = 447.593 + (9.247 * float(weight)) + (3.098 * float(height)) - (4.330 * float(age))
        cal = 447.593 + (9.247 * float(Desired_weight)) + (3.098 * float(height)) - (4.330 * float(age))

    # activity logic:
    if activity == 'Little Active(No Exercise)':
        cal = cal * 1.2
        cal1 = cal1 * 1.2

    elif activity == 'Light active (1-3 days/week)':
        cal = cal * 1.375
        cal1 = cal1 * 1.375

    elif activity == 'Moderate active (3-5 days/week)':
        cal = cal * 1.55
        cal1 = cal1 * 1.55

    elif activity == 'Highly active (6-7 days/week)':
        cal = cal * 1.725
        cal1 = cal1 * 1.725

    elif activity == 'Super active (twice/day)':
        cal = cal * 1.9
        cal1 = cal1 * 1.9
    CC = StringVar()
    a = Label(root, textvariable=CC)
    CC.set(cal1)
    a.grid(row=16, column=3)

    RC = StringVar()
    b = Label(root, textvariable=RC)
    RC.set(cal)
    b.grid(row=17, column=3)

    RC = print(cal)

    # copy paste
    #for VEGETARIAN in diet_type:
    if cal < 1500 and Diet_Type == "VEGETARIAN":
        item = StringVar()
        l6 = Label(root, textvariable=item, relief=RAISED)
        item.set("Breakfast: \n" + proteinVeg[randint(0, 5)] + " + " + fruit[randint(0, 4)])
        l6.grid(row=2, column=5)

        item2 = StringVar()
        l8 = Label(root, textvariable=item2, relief=RAISED)
        item2.set("Lunch: \n" + proteinVeg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)])
        l8.grid(row=4, column=5)

        item3 = StringVar()
        l9 = Label(root, textvariable=item3, relief=RAISED)
        item3.set("Snack: \n" + DairyProduct[randint(0, 4)] + " + " + vegetable[0])
        l9.grid(row=6, column=5)

        item4 = StringVar()
        l10 = Label(root, textvariable=item4, relief=RAISED)
        item4.set("Dinner: \n" + proteinVeg[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)])
        l10.grid(row=8, column=5)

        item5 = StringVar()
        l11 = Label(root, textvariable=item5, relief=RAISED)
        item5.set("Snack:\n " + fruit[randint(0, 5)])
        l11.grid(row=10, column=5)

    elif cal < 1500 and Diet_Type == "Non-VEGETARIAN":
        item = StringVar()
        l6 = Label(root, textvariable=item, relief=RAISED)
        item.set("Breakfast: \n" + proteinNveg[randint(0, 5)] + " + " + fruit[randint(0, 4)])
        l6.grid(row=2, column=5)

        item2 = StringVar()
        l8 = Label(root, textvariable=item2, relief=RAISED)
        item2.set("Lunch: \n" + proteinNveg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)])
        l8.grid(row=4, column=5)

        item3 = StringVar()
        l9 = Label(root, textvariable=item3, relief=RAISED)
        item3.set("Snack: \n" + DairyProduct[randint(0, 4)] + " + " + vegetable[0])
        l9.grid(row=6, column=5)

        item4 = StringVar()
        l10 = Label(root, textvariable=item4, relief=RAISED)
        item4.set("Dinner: \n" + proteinNveg[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)])
        l10.grid(row=8, column=5)

        item5 = StringVar()
        l11 = Label(root, textvariable=item5, relief=RAISED)
        item5.set("Snack:\n " + fruit[randint(0, 5)])
        l11.grid(row=10, column=5)


    elif cal < 1800 and Diet_Type=="VEGETARIAN":
        item = IntVar()
        l6 = Label(root, textvariable=item, relief=RAISED)
        item.set("Breakfast:\n " + proteinVeg[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l6.grid(row=2, column=5)

        item2 = StringVar()
        l8 = Label(a, textvariable=item2, relief=RAISED)
        item2.set("Lunch:\n " + proteinVeg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l8.grid(row=4, column=5)

        item3 = StringVar()
        l9 = Label(root, textvariable=item3, relief=RAISED)
        item3.set("Snack: \n" + DairyProduct[randint(0, 4)] + " + " + vegetable[0])
        l9.grid(row=6, column=5)

        item4 = StringVar()
        l10 = Label(root, textvariable=item4, relief=RAISED)
        item4.set("Dinner: 2\n " + proteinVeg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)])
        l10.grid(row=8, column=5)

        item5 = StringVar()
        l11 = Label(root, textvariable=item5, relief=RAISED)
        item5.set("Snack: \n" + fruit[randint(0, 5)])
        l11.grid(row=10, column=5)

    elif cal < 1800 and Diet_Type=="NON-VEGETARIAN":
        item = IntVar()
        l6 = Label(root, textvariable=item, relief=RAISED)
        item.set("Breakfast:\n " + proteinNveg[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l6.grid(row=2, column=5)

        item2 = StringVar()
        l8 = Label(a, textvariable=item2, relief=RAISED)
        item2.set("Lunch:\n " + proteinNveg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l8.grid(row=4, column=5)

        item3 = StringVar()
        l9 = Label(root, textvariable=item3, relief=RAISED)
        item3.set("Snack: \n" + DairyProduct[randint(0, 4)] + " + " + vegetable[0])
        l9.grid(row=6, column=5)

        item4 = StringVar()
        l10 = Label(root, textvariable=item4, relief=RAISED)
        item4.set("Dinner: 2\n " + proteinNveg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)])
        l10.grid(row=8, column=5)

        item5 = StringVar()
        l11 = Label(root, textvariable=item5, relief=RAISED)
        item5.set("Snack: \n" + fruit[randint(0, 5)])
        l11.grid(row=10, column=5)

    elif cal < 2200 and Diet_Type=="VEGETARIAN":
        item = StringVar()
        l6 = Label(root, textvariable=item, relief=RAISED)
        item.set("Breakfast:\n " + proteinVeg[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l6.grid(row=2, column=5)

        item2 = StringVar()
        l8 = Label(root, textvariable=item2, relief=RAISED)
        item2.set("Lunch: \n" + proteinVeg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l8.grid(row=4, column=5)

        item3 = StringVar()
        l9 = Label(root, textvariable=item3, relief=RAISED)
        item3.set("Snack:\n " + DairyProduct[randint(0, 4)] + " + " + vegetable[0])
        l9.grid(row=6, column=5)

        item4 = StringVar()
        l10 = Label(root, textvariable=item4, relief=RAISED)
        item4.set("Dinner: \n " + proteinVeg[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)])
        l10.grid(row=8, column=5)

        item5 = StringVar()
        l11 = Label(root, textvariable=item5, relief=RAISED)
        item5.set("Snack: 2\n" + fruit[randint(0, 5)])
        l11.grid(row=10, column=5)

    elif cal < 2200 and Diet_Type=="NON-VEGETARIAN":
        item = StringVar()
        l6 = Label(root, textvariable=item, relief=RAISED)
        item.set("Breakfast:\n " + proteinNveg[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l6.grid(row=2, column=5)

        item2 = StringVar()
        l8 = Label(root, textvariable=item2, relief=RAISED)
        item2.set("Lunch: \n" + proteinNveg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l8.grid(row=4, column=5)

        item3 = StringVar()
        l9 = Label(root, textvariable=item3, relief=RAISED)
        item3.set("Snack:\n " + DairyProduct[randint(0, 4)] + " + " + vegetable[0])
        l9.grid(row=6, column=5)

        item4 = StringVar()
        l10 = Label(root, textvariable=item4, relief=RAISED)
        item4.set("Dinner: \n " + proteinNveg[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)])
        l10.grid(row=8, column=5)

        item5 = StringVar()
        l11 = Label(root, textvariable=item5, relief=RAISED)
        item5.set("Snack: 2\n" + fruit[randint(0, 5)])
        l11.grid(row=10, column=5)

    elif cal >= 2200 and Diet_Type=="VEGETARIAN":
        item = StringVar()
        l6 = Label(root, textvariable=item, relief=RAISED)
        item.set(
            "Breakfast: \n " + proteinVeg[randint(0, 5)] + " + " + fruit[randint(0, 5)] + " + " + grains[randint(0, 4)])
        l6.grid(row=2, column=5)

        item2 = StringVar()
        l8 = Label(root, textvariable=item2, relief=RAISED)
        item2.set("Lunch: \n" + proteinVeg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l8.grid(row=4, column=5)

        item3 = StringVar()
        l9 = Label(root, textvariable=item3, relief=RAISED)
        item3.set("Snack:\n " + DairyProduct[randint(0, 4)] + " + " + vegetable[0])
        l9.grid(row=6, column=5)

        item4 = StringVar()
        l10 = Label(root, textvariable=item4, relief=RAISED)
        item4.set("Dinner: \n " + proteinVeg[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens + 2 " + grains[
            randint(0, 4)] + " + 2 " + FatsAndOils[randint(0, 5)])
        l10.grid(row=8, column=5)

        item5 = StringVar()
        l11 = Label(root, textvariable=item5, relief=RAISED)
        item5.set("Snack: 2\n " + fruit[randint(0, 5)])
        l11.grid(row=10, column=5)

    elif cal >= 2200 and Diet_Type=="NON-VEGETARIAN":
        item = StringVar()
        l6 = Label(root, textvariable=item, relief=RAISED)
        item.set(
            "Breakfast: \n " + proteinNveg[randint(0, 5)] + " + " + fruit[randint(0, 5)] + " + " + grains[randint(0, 4)])
        l6.grid(row=2, column=5)

        item2 = StringVar()
        l8 = Label(root, textvariable=item2, relief=RAISED)
        item2.set("Lunch: \n" + proteinNveg[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
            randint(0, 4)] + " + " + FatsAndOils[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        l8.grid(row=4, column=5)

        item3 = StringVar()
        l9 = Label(root, textvariable=item3, relief=RAISED)
        item3.set("Snack:\n " + DairyProduct[randint(0, 4)] + " + " + vegetable[0])
        l9.grid(row=6, column=5)

        item4 = StringVar()
        l10 = Label(root, textvariable=item4, relief=RAISED)
        item4.set("Dinner: \n " + proteinNveg[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens + 2 " + grains[
            randint(0, 4)] + " + 2 " + FatsAndOils[randint(0, 5)])
        l10.grid(row=8, column=5)

        item5 = StringVar()
        l11 = Label(root, textvariable=item5, relief=RAISED)
        item5.set("Snack: 2\n " + fruit[randint(0, 5)])
        l11.grid(row=10, column=5)


label1 = Label(root, text='Name')
label1.grid(row=1, column=2)
v1 = StringVar()
e1 = Entry(root, textvariable=v1, width=30)
e1.grid(row=1, column=3)

label2 = Label(root, text='Weight')
label2.grid(row=2, column=2)
v2 = StringVar()
e2 = Entry(root, textvariable=v2, width=30)
e2.grid(row=2, column=3)

label3 = Label(root, text='Height(in cms)')
label3.grid(row=3, column=2)
v3 = StringVar()
e3 = Entry(root, textvariable=v3, width=30)
e3.grid(row=3, column=3)

label4 = Label(root, text='Age  ')
label4.grid(row=4, column=2)
v4 = StringVar()
e4 = Entry(root, textvariable=v4, width=30)
e4.grid(row=4, column=3)

# SELECTING THE GENDER:
label5 = Label(root, text='Gender', bg='white')
label5.grid(row=5, column=2)
Lb2 = Listbox(root, height=2, width=30)
Lb2.insert(1, 'Male')
Lb2.insert(2, 'Female')
Lb2.grid(row=5, column=3)

label6 = Label(root, text='Activity', bg='white')
label6.grid(row=6, column=2)
Lb = Listbox(root, height=6, width=30)
Lb.insert(1, 'Little Active(No Exercise)')
Lb.insert(2, 'Light active (1-3 days/week)')
Lb.insert(3, 'Moderate active (3-5 days/week)')
Lb.insert(4, 'Highly active (6-7 days/week)')
Lb.insert(5, 'Super active (twice/day)')
Lb.grid(row=6, column=3)

label51 = Label(root, text='Diet_Type', bg='white')
label51.grid(row=7, column=2)
Lb3= Listbox(root, height=2, width=30)
Lb3.insert(1,"VEGETARIAN")
Lb3.insert(2,"NON-VEGETARIAN")
Lb3.grid(row=7, column=3)


label8 = Label(root, text="Desired Weight")
label8.grid(row=8, column=2)
v8 = StringVar()
e8 = Entry(root, textvariable=v8, width=30)
e8.grid(row=8, column=3)
label = Label(root, text=" ")
label.grid(row=9)
b1 = Button(root, text='Submit', width=25, command=BMR)
b1.grid(row=10, column=3)

b3 = Button(root, text="change Plan", width=25, command=BMR)
b3.grid(row=12, column=3)

space = Label(root, text=" ")
label.grid(row=13)

label9 = Label(root, text="Want to consult a Dietician?")
label9.grid(row=14, column=2)
b2 = Button(root, text="Click Here", width=25, command=location)
b2.grid(row=14, column=3)

space2 = Label(root, text=" ")
label.grid(row=15)
b4 = Button(root, text='CALCULATE BMI', width=25, command=BMI)
b4.grid(row=24, column=2)

label10 = Label(root, text="Current Calories:")
label10.grid(row=16, column=2)

label11 = Label(root, text="Required Calories:")
label11.grid(row=17, column=2)
b5 = Button(root, text="Restart", command=restart_program)
b5.grid(row=28, column=2)


# health tips
Health_Tips = ["Do not skip breakfast Skipping breakfast will not help you lose weight.",
               "Eat regular meals.",
               "Eat plenty of fruit and vegetables",
               "Get more active.",
               "Drink plenty of water.",
               "Eat high fibre foods.",
               "Read food labels.",
               "Use a smaller plate."]

display = StringVar()
label21 = Label(root, textvariable=display, relief=RAISED)
display.set("HEALTH TIP: \n\n" + Health_Tips[randint(0, 7)])
label21.grid(row=22, column=3)

root.mainloop()
