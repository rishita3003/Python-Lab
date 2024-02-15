# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''Rishita Agarwal 220150016
Created on 29-01-24 
Python Lab 2 - code along'''

#Q1
first_name="first"
last_name="last"
roll_number="123456789"
introduction=f"My name is {first_name} {last_name} and roll no. is {roll_number}"
print(introduction)

in_values=[1,2,3,4,5,6,7,8,9,10]
out_values=[2,4,5,4,5,8,10,9,11,14]

s_in=in_values[0]+in_values[1]+in_values[2]+in_values[3]+in_values[4]+in_values[5]+in_values[6]+in_values[7]+in_values[8]+in_values[9]

print(len(in_values))

m_in=s_in/10 #10 is the length of the in_values

s_out=out_values[0]+out_values[1]+out_values[2]+out_values[3]+out_values[4]+out_values[5]+out_values[6]+out_values[7]+out_values[8]+out_values[9]
m_out=s_out/10

print(len(out_values))

s_inout = in_values[0] * out_values[0] + in_values[1] * out_values[1] + in_values[2] * out_values[2] + in_values[3] * out_values[3] + in_values[4] * out_values[4] + in_values[5] * out_values[5] + in_values[6] * out_values[6] + in_values[7] * out_values[7] + in_values[8] * out_values[8] + in_values[9] * out_values[9]

s_in_sq = in_values[0] * in_values[0] + in_values[1] * in_values[1] + in_values[2] * in_values[2] + in_values[3] * in_values[3] + in_values[4] * in_values[4] + in_values[5] * in_values[5] + in_values[6] * in_values[6] + in_values[7] * in_values[7] + in_values[8] * in_values[8] + in_values[9] * in_values[9]

#Q3
#sh is the slope of linear regression
sh = (10 * s_inout -s_in * s_out) / \
    (10 * s_in_sq -s_in * s_in)
#the backslash was to move to the next line for the same operator

#ts is the intercept of linear regression
ts = m_out -sh * m_in

print("sh: ",sh)
print("ts: ",ts)


#Q4 --> performing the above operation for our own function

roll_digits=[2,2,0,1,5,0,0,1,6]
out_values_mod=[roll_digits[0]**2,roll_digits[1]**2,roll_digits[2]**2,roll_digits[3]**2,roll_digits[4]**2,roll_digits[5]**2,roll_digits[6]**2,roll_digits[7]**2,roll_digits[8]**2]

s_in_mod=roll_digits[0]+roll_digits[1]+\
    roll_digits[2]+roll_digits[3]+\
        roll_digits[4]+roll_digits[5]+roll_digits[6]+\
            roll_digits[7]+roll_digits[8]

s_out_mod=out_values_mod[0]+out_values_mod[1]+\
    out_values_mod[2]+out_values_mod[3]+\
        out_values_mod[4]+out_values_mod[5]+out_values_mod[6]+\
            out_values_mod[7]+out_values_mod[8]

m_in_mod=s_in_mod/9

m_out_mod=s_out_mod/9

s_inout_mod=roll_digits[0]*out_values_mod[0]+roll_digits[1]*out_values_mod[1]+roll_digits[2]*out_values_mod[2]+roll_digits[3]*out_values_mod[3]+roll_digits[4]*out_values_mod[4]+roll_digits[5]*out_values_mod[5]+roll_digits[6]*out_values_mod[6]+roll_digits[7]*out_values_mod[7]+roll_digits[8]*out_values_mod[8]

s_in_sq_mod=roll_digits[0]*roll_digits[0]+roll_digits[1]*roll_digits[1]+roll_digits[2]*roll_digits[2]+roll_digits[3]*roll_digits[3]+roll_digits[4]*roll_digits[4]+roll_digits[5]*roll_digits[5]+roll_digits[6]*roll_digits[6]+roll_digits[7]*roll_digits[7]+roll_digits[8]*roll_digits[8]

sh_mod= (9 * s_inout_mod -s_in_mod * s_out_mod) / \
    (9 * s_in_sq_mod -s_in_mod * s_in_mod)

ts_mod=m_out_mod -sh_mod * m_in_mod

print("Modified sh: ",sh_mod)
print("Modified ts: ",ts_mod)


