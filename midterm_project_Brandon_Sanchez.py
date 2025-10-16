from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
import numpy as np

root = Tk() # this is the parent "widget", aka intializing factor
root.call('tk', 'scaling', 2.0) #makes the app larger
root.title('I-V Curve Creation')
root.geometry("1280x720")
root.columnconfigure(0, weight=1) #to set up the grid system
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)

def add_entry():
    idx = len(point_list_voltage) #allows for the points to be in the same column.
    voltage_point= Entry(point_entry_Voltage, width=10)
    voltage_point.grid(row=idx*2, column=0, pady=5, padx=5)
    point_list_voltage.append(voltage_point)
    current_point = Entry(point_entry_Current, width=10)
    current_point.grid(row=idx*2, column=0,pady=5, padx=5)
    point_list_current.append(current_point)
    # code here will let user create new data points
    #here would also go two text boxes for both points of voltahe and current

def remove_entry():
    if point_list_voltage and point_list_current:
        removeV = point_list_voltage.pop()
        removeV.destroy()
        removeA = point_list_current.pop()
        removeA.destroy()
    # code here will let user remove new data points

def user_data():
    collected_data = []

    for v_data, i_data in zip(point_list_voltage, point_list_current): #we are collecting from the entry boxes, which are appended to the point_lists.
        v_value = v_data.get().strip()
        i_value = i_data.get().strip() # gets the values and strips them to create lists

        v = float(v_value) #formats it so that float values/decimal values can be entered.
        i = float(i_value)
        collected_data.append((v, i)) #pairs the x,y together, (v,i)
    print(f"The collected data is: {collected_data}")

    #to allow the user to save their data points as a csv file
    with open("user_data.csv", "w") as file: #does this make a csv file in the same directory as the python file?
        #tested, it does!!
        file.write("Voltage (V), Current (A)\n") #titles of the the two datasets
        for v, i in collected_data:
            file.write(f"{v}, {i}\n") #writes the data in the csv file
    return collected_data
#we're so back
#def solar_graph():
    generate_solar_graph = solar_cell.get()
    if generate_solar_graph == False:
        return
    if generate_solar_graph == True:
        voltages_solar = np.linspace(0, 5.0, 100)
        currents_solar = 0.5 * (1 - np.exp(voltages_solar - 5.0)) #close to real solar cell curve
#def resistor_graph():
    ...
#def capacitor_graph():
    ...
def user_graph():
    #resistor = resistor_graph()
    #capacitor = capacitor_graph()
    data = user_data() #calls back the user_data function to get the data
    voltages = [v for v, i in data] #creates a list of just the voltages
    currents = [i for v, i in data] #creates a list of just the currents

## before adding checkboxes, this was the original graphing code
    #plt.plot(voltages, currents, color='blue') #plots the two lists as x and y
    #plt.scatter(voltages, currents, color='red') #marks the actual points plotted
    #plt.title("I-V Curve")#title of the graph
    #plt.xlabel("Voltage (V)") #x axis label 
    #plt.ylabel("Current (A)") #y axis label
    #plt.show() #shows the graph
    if solar_cell.get() == False and resistor.get() == False and capacitor.get() == False: # case in which there is none selected, user wants to make their own graph
        plt.plot(voltages, currents, color='blue', label='User Graph') #plots the two lists as x and y
        plt.scatter(voltages, currents, color='red') #marks the actual points plotted
        plt.title("I-V Curve")#title of the graph
        plt.xlabel("Voltage (V)") #x axis label 
        plt.ylabel("Current (A)") #y axis label
        plt.legend() #to show what line is what
        plt.show() #shows the graph
    if solar_cell.get() == True:
        voltages_solar = np.linspace(0, 5.0, 100)
        currents_solar = 0.075 * (1 - np.exp(voltages_solar - 5.0)) #close to real solar cell curve, based on 75mA max current on observations made in EE001 class
        plt.plot(voltages, currents, color='blue', label='User Graph') #plots the two lists as x and y
        plt.plot(voltages_solar, currents_solar, color='orange', label='Solar Cell') #plots the solar cell graph
        plt.scatter(voltages, currents, color='red') #marks the actual points plotted
        plt.title("I-V Curve with Solar Cell Comparison")#title of the graph
        plt.xlabel("Voltage (V)") #x axis label 
        plt.ylabel("Current (A)") #y axis label
        plt.legend() #to show what line is what
        plt.show() #shows the graph
    if resistor.get() == True:
        voltages_resistor = np.linspace(0, 5.0, 100)
        currents_resistor = voltages_resistor / 10.0 #Ohm's Law with R=10 ohms
        plt.plot(voltages, currents, color='blue', label='User Graph') #plots the two lists as x and y
        plt.plot(voltages_resistor, currents_resistor, color='green', label='Resistor (R=10Ω)') #plots the resistor graph
        plt.scatter(voltages, currents, color='red') #marks the actual points plotted
        plt.title("I-V Curve with Resistor Comparison")#title of the graph
        plt.xlabel("Voltage (V)") #x axis label 
        plt.ylabel("Current (A)") #y axis label
        plt.legend() #to show what line is what
        plt.show() #shows the graph
    if capacitor.get() == True:
        voltages_capacitor = np.linspace (0, 5.0, 100)
        #more complex I-V curve for capacitor, not linear
        #currents_capacitor = 0.02 * np.sin(voltages_capacitor * (np.pi / 5)) #simple sinusoidal approximation for capacitor I-V curve (THIS WAS GENERATED FOR CURIOSITY PURPOSES, IT WILL NOT APPEAR IN THE FINAL RESULTS BECAUSE IT'S NOT MY WORK)
        currents_capacitor = 0.01 * voltages_capacitor #simple approximation for capacitor I-V curve
        plt.plot(voltages, currents, color='blue', label='User Graph') #plots the two lists as x and y
        plt.plot(voltages_capacitor, currents_capacitor, color='purple', label='Capacitor') #plots the capacitor graph
        plt.scatter(voltages, currents, color='red') #marks the actual points plotted
        plt.title("I-V Curve with Capacitor Comparison")#title of the graph
        plt.xlabel("Voltage (V)") #x axis label
        plt.ylabel("Current (A)") #y axis label
        plt.legend() #to show what line is what
        plt.show() #shows the graph
    
text_voltage = Label(root, text="Voltage (V)") #text that labels the voltage point side (x)
text_voltage.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

text_current = Label(root, text="Current (A)") #text that labels the current point side (y)
text_current.grid(row=0, column=0, padx=10, pady=10, sticky="ne")

point_list_voltage = [] #store the amount of points made for voltage

point_list_current = [] #store amount of points made for current

point_entry_Voltage = Frame(root) #create a frame for the application, specifically this widget

point_entry_Voltage.grid(row=0, column=0, padx=10, pady=50, sticky="nw") # placement of frame

point_entry_Current = Frame(root)

point_entry_Current.grid(row=0, column=0, padx=10, pady=50, sticky="ne")

add_point = Button(root, text="Add point", command=add_entry)
add_point.grid(row=1, column=2, padx=0, pady=0, sticky="n")

remove_point = Button(root, text="Remove point", command=remove_entry)
remove_point.grid(row=1, column=2, padx=0,pady=50, sticky="n") 

#padx and pady refer to the placement of the buttons, row and column refer to the grid system

save_button = Button(root, text="Save Points", command=user_data)
save_button.grid(row=1,column=0,padx=0,pady=0, sticky="s")

button_graph = Button(root, text="Generate Graph", command=user_graph)
button_graph.grid(row=1, column=1, padx=0, pady=50, sticky="n")

#now checkbox to add different electrical component graphs

text_graphs = Label(root, text="Which component graph are you comparing to?")
text_graphs.grid(row=0, column=1, pady=100, padx=0, sticky="s")

#to access whether or not the box is checked or not for future case use in user_graph function
solar_cell = BooleanVar()
solar_cell.set(False)
resistor = BooleanVar()
resistor.set(False)
capacitor = BooleanVar()
capacitor.set(False)

check_solar = Checkbutton(root, text="Solar Cell", variable=solar_cell) #creates checkbox for solar cell
check_solar.grid(row=0, column=1, pady=60, padx=0, sticky="s") #placement of checkbox
check_resistor = Checkbutton(root, text="Resistor", variable=resistor) #creates checkbox for resistor
check_resistor.grid(row=0, column=1, pady=30, padx=0, sticky="s")
#but what if they use a different value resistor? maybe have a text box pop up if checked? could be for a future iteration
check_capacitor = Checkbutton(root, text="Capacitor", variable=capacitor) #creates checkbox for capacitor
check_capacitor.grid(row=0, column=1, pady=0, padx=0, sticky="s")

root.mainloop() #begins the application
