import numpy as np

# Inflows and outflows based on diagram
# Net inflow must equal net outflow
in1 = int(input("Enter inflow for Street 1: "))
out1 = int(input("Enter outlfow for Street 1: "))
in2 = int(input("Enter inflow for Street 2: "))
out2 = int(input("Enter outlfow for Street 2: "))
in3 = int(input("Enter inflow for Street 3: "))
out3 = int(input("Enter outlfow for Street 3: "))
in4 = int(input("Enter inflow for Street 4: "))
out4 = int(input("Enter outlfow for Street 4: "))
net_inflow = in1 + in2 + in3 + in4
net_outflow = out1 + out2 + out3 + out4
while(net_inflow != net_outflow):
    print("Net inflow does not equal net outflow!")
    in1 = int(input("Enter inflow for Street 1: "))
    out1 = int(input("Enter outlfow for Street 1: "))
    in2 = int(input("Enter inflow for Street 2: "))
    out2 = int(input("Enter outlfow for Street 2: "))
    in3 = int(input("Enter inflow for Street 3: "))
    out3 = int(input("Enter outlfow for Street 3: "))
    in4 = int(input("Enter inflow for Street 4: "))
    out4 = int(input("Enter outlfow for Street 4: "))
    net_inflow = in1 + in2 + in3 + in4
    net_outflow = out1 + out2 + out3 + out4

# Shut down block AD in Street 1:
AD1 = 0
BA1 = out3 - in1
CB1 = out2 - in3 + BA1
DC1 = - out1 + in4
max1 = max(BA1, CB1, DC1)
min1 = min(BA1, CB1, DC1)
print("Flows AD, CB, BA, DC with Block AD, Street 1 closed:")
print(AD1, BA1, CB1, DC1)

# Shut down block CB in Street 2
CB2 = 0
BA2 = - out2 + in3
DC2 = out4 - in2
AD2 = out1 - in4 + DC2
max2 = max(BA2, DC2, AD2)
min2 = min(BA2, DC2, AD2)
print("Flows AD, CB, BA, DC with Block CB, Street 2 closed:")
print(AD2, BA2, CB2, DC2)

# Shut down block BA in Street 3
BA3 = 0
AD3 = - out3 + in1
CB3 = out2 - in3
DC3 = out4 - in2 + CB3
max3 = max(AD3, CB3, DC3)
min3 = min(AD3, CB3, DC3)
print("Flows AD, CB, BA, DC with Block BA, Street 3 closed:")
print(AD3, BA3, CB3, DC3)

# Shut down block DC in Street 4
DC4 = 0
CB4 = - out4 + in2
AD4 = out1 - in4
BA4 = out3 - in1 + AD4
max4 = max(AD4, CB4, DC4)
min4 = min(AD4, CB4, DC4)
print("Flows AD, CB, BA, DC with Block DC, Street 4 closed:")
print(AD4, BA4, CB4, DC4)

if (min1 < 0 and min2 < 0 and min3 < 0 and min4 < 0):
    print("No block can be shut down.")
else:
    if (max1 >= max2 and max1 >= max3 and max1 >= max4 and min1>= 0):
        print("Block AD should be shut down.")
    if (max2 >= max1 and max2 >= max3 and max2 >= max4 and min2>= 0):
        print("Block CB should be shut down.")
    if (max3 >= max1 and max3 >= max2 and max3 >= max4 and min3>= 0):
        print("Block BA should be shut down.")
    if (max4 >= max1 and max4 >= max2 and max4 >= max3 and min4>= 0):
        print("Block DC should be shut down.")
