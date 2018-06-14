# coding: utf-8
inputs = []
print("input anything you want, end with ctrl-d")
while True:
    try:
        inputs.append(input())
    except:
        inputs.reverse()
        for val in inputs:
            print(val)
        break
    
             
