""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

AUTHOR :- ASHUTOSH KUMAR
COMPLETED ON :- 23/02/2023
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG.  FIX IT
    return introcs.RGB(255-rgb.red,255-rgb.green, 255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    # pass
    
    str_value = str(value)
    if len(str_value) < 5 and '.' in str_value:
        return str_value + ('0')*(5-len(str_value))
    elif len(str_value) < 5 and '.' not in str_value:
        return (str_value)+'.'+('0')*(4-len(str_value))
    elif len(str_value) == 5 and '.' in str_value:
        return str_value
    elif '.' not in str_value:
        return str(round(value))+'.'+'0'*(4-len(str(round(value))))    
    else:
        a=str_value.find('.')           # Finding index of '.' 
        if len(str(round(value,3-(a-1))))<5:
            return str(round(value,3-(a-1)))+'0'*(5-len(str(round(value,3-(a-1)))))
        else:
            return str(round(value,3-(a-1)))





def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    # pass
    att_1=cmyk.cyan
    att_2=cmyk.magenta
    att_3=cmyk.yellow
    att_4=cmyk.black
    return "("+str5(att_1)+', '+str5(att_2)+', '+str5(att_3)+', '+str5(att_4)+")"



def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    # pass
    att_1=hsv.hue
    att_2=hsv.saturation
    att_3=hsv.value
    return "("+str5(att_1)+', '+str5(att_2)+', '+str5(att_3)+")"


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    # pass
    r=rgb.red/255.0
    g=rgb.green/255.0
    b=rgb.blue/255.0
    k1=1-max(r,g,b)
    if k1==1.0:
        c,m,y,k=0.0,0.0,0.0,k1*100.0
    else:
        c=((1-r-k1)/(1-k1))*100
        m=((1-g-k1)/(1-k1))*100
        y=((1-b-k1)/(1-k1))*100
        k=k1*100.0
    re_cmyk=introcs.CMYK(c,m,y,k)
    return re_cmyk  

def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    # pass
    r=round(255*(1-(cmyk.cyan/100))*(1-(cmyk.black/100)))
    g=round(255*(1-(cmyk.magenta/100))*(1-(cmyk.black/100)))
    b=round(255*(1-(cmyk.yellow/100))*(1-(cmyk.black/100)))
    re_rgb=introcs.RGB(r,g,b)
    return re_rgb


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    # pass
    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255
    M = max(r, g, b)
    m = min(r, g, b)
    if M == m:
        H = 0.0
        #print('line 196 a3')
    elif M == r and g >= b:
        H = 60.0 * (g - b) / (M - m)
        #print('line 199 a3')

    elif M == r and g < b:
        H=60.0 * (g - b) / (M - m) + 360.0
        #print('line 203 a3')
    elif M == g:
        H=60.0 * (b - r) / (M - m) + 120.0
        #print('line 206 a3')
    else:
        H=60.0 * (r - g) / (M - m) + 240.0
        #print('line 209 a3')
    if M == 0.0:
        S = 0.0
    else:
        S = 1 - m / M
    V=float(M)
    #print(H)
    #print(H,S,V)
    re_hsv = introcs.HSV(H,S,V)
    return re_hsv




def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    # pass
    H = math.floor(hsv.hue / 60)
    f = hsv.hue / 60 - H
    p = hsv.value * (1 - hsv.saturation)
    q = hsv.value * (1 - f * hsv.saturation)
    t = hsv.value * (1 - (1 - f) * hsv.saturation)
    if H == 0 or H == 5:
        r = hsv.value
    elif H == 1:
        r = q
    elif H == 2 or H == 3:
        r = p
    elif H == 4:
        r = t
    if H == 0:
        g = t
    elif H == 1 or H == 2:
        g = hsv.value
    elif H == 3:
        g = q
    elif H == 4 or H == 5:
        g = p
    if H == 0 or H == 1:
        b = p
    elif H == 2:
        b = t
    elif H == 3 or H == 4:
        b = hsv.value
    elif H == 5:
        b = q
    R = round(r * 255)
    G = round(g * 255)
    B = round(b * 255)
    obj_rgb = introcs.RGB(R, G, B)
    return obj_rgb



def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart, 
    with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    # pass
    c=contrast
    x=value
    if -1 <= c <1:
        if x < 0.25 + 0.25 * c:
            y = ((1-c)/(1+c)) * x
        elif x > 0.75 - 0.25 * c:
            y = ((1-c)/(1+c))*(x-(3-c)/4)+(3+c)/4
        else:
            y=((1+c)/(1-c))*(x-(1+c)/4)+(1-c)/4
    else:
        if x >= 0.5:
            y = 1
        else:
            y = 0
    return y
            


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    # pass

    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255
    new_r = round(contrast_value(r, contrast)*255)
    new_g = round(contrast_value(g, contrast)*255)
    new_b = round(contrast_value(b, contrast)*255)
    rgb.red = new_r
    rgb.green = new_g
    rgb.blue = new_b
    
    



    

