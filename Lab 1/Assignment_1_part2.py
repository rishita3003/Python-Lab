
#Q4
print("Q4")
#making inn list from the digits of my roll number and out list as the square of those digits
inn=[2,2,0,1,5,0,0,1,6]
out=[4,4,0,1,25,0,0,1,36]

#storing the sum of elements of in list by accessing the elements by index
s_in=inn[0]+inn[1]+inn[2]+inn[3]+inn[4]+inn[5]+inn[6]+inn[7]+inn[8]
#mean of the values in the in list
m_in=s_in/9

#storing the sum of elements of out list by accessing the elements by index
s_out=out[0]+out[1]+out[2]+out[3]+out[4]+out[5]+out[6]+out[7]+out[8]
#mean of the value in the out list
m_out=s_out/9

#multiplication of the corresponding elements of the in and the out list
s_inout=inn[0]*out[0]+inn[1]*out[1]+inn[2]*out[2]+inn[3]*out[3]+inn[4]*out[4]+inn[5]*out[5]+inn[6]*out[6]+inn[7]*out[7]+inn[8]*out[8]
#squaring the elements of the in list
s_in_sq=inn[0]*inn[0]+inn[1]*inn[1]+inn[2]*inn[2]+inn[3]*inn[3]+inn[4]*inn[4]+inn[5]*inn[5]+inn[6]*inn[6]+inn[7]*inn[7]+inn[8]*inn[8]

#calculating the slope and intercept
sh = (9 * s_inout - s_in * s_out) / (9 * s_in_sq - s_in * s_in)
ts = m_out - sh * m_in

print(f"The values of slope and intercept are {sh} and {ts} respectively, using the updated inn and out lists.")

