#Rishita Agarwal 18/1/2024 Lab Assignment 1

#Q1
print("Q1")
first_name="Rishita"
last_name="Agarwal"
roll_no=220150016
print(f"Good Evening,\nI am {first_name} {last_name}.\nI am a B.Tech 2nd year student in DSAI department.\nMy roll number is {roll_no}.\n")

#Q2
print("Q2")
#forming 2 lists named in and out
inn=[1,2,3,4,5,6,7,8,9,10]
out=[2,4,5,4,5,8,10,9,11,14]

#storinng the sum of elements of inn list by accessing the elements by index
s_in=inn[0]+inn[1]+inn[2]+inn[3]+inn[4]+inn[5]+inn[6]+inn[7]+inn[8]+inn[9]
#mean of the values in the in list
m_in=s_in/10

#storing the sum of elements of out list by accessing the elements by index
s_out=out[0]+out[1]+out[2]+out[3]+out[4]+out[5]+out[6]+out[7]+out[8]+out[9]
#mean of the value in the out list
m_out=s_out/10

#multiplication of the corresponding elements of the inn and the out list
s_inout=inn[0]*out[0]+inn[1]*out[1]+inn[2]*out[2]+inn[3]*out[3]+inn[4]*out[4]+inn[5]*out[5]+inn[6]*out[6]+inn[7]*out[7]+inn[8]*out[8]+inn[9]*out[9]
#squaring the elements of the inn list
s_in_sq=inn[0]*inn[0]+inn[1]*inn[1]+inn[2]*inn[2]+inn[3]*inn[3]+inn[4]*inn[4]+inn[5]*inn[5]+inn[6]*inn[6]+inn[7]*inn[7]+inn[8]*inn[8]+inn[9]*inn[9]

#calculating sh and ts (slope and intercept)
sh = (10 * s_inout - s_in * s_out) / (10 * s_in_sq - s_in * s_in)
ts = m_out - sh * m_in

print(f"The values of slope and intercept are {sh} and {ts} respectively.\n")

#Q3
print("Q3")
print(f"This program is for least square fitting in linear regression.\nFor an equation like y=a*x+b, where a is the slope and b is the intercept.\nThe slope is represented by the variable sh and the intercept is represented by ts.\nHere we are trying to fit the line on our points from inn and the out list by the method of least squares in linear regression.")

