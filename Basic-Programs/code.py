# --------------
class_1=['Geoffrey Hinton' , 'Andrew Ng' , 'Sebastian Raschka' , 'Yoshua Bengio']
class_2=['Hilary Mason' , 'Carla Gentry' , 'Corinna Cortes' ] 
new_class= class_1 + class_2

print(new_class)

new_class.append('Peter Warden')

print (new_class)
new_class.remove('Carla Gentry')




# --------------
# Code starts here
courses= {"Math":65,"English":70,"History":80,"French":70,"Science":60}
total = courses["Math"]+courses["English"]+courses["History"]+courses["French"]+courses["Science"]
print(total)
percentage = (total/500)*100
print(percentage)


# --------------
mathematics = {"Geoffrey Hinton":78,"Andrew Ng":95,
"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,
"Peter Warden":75}

topper= max(mathematics,key = mathematics.get)
print(topper)



# --------------
# Given string
topper = 'andrew ng'
x= topper.split()
print(x)
first_name= topper[0:6]
last_name= topper[7:9]
print(first_name)
print(last_name)
full_name = 'ng '+ '' + 'andrew'
print(full_name)

certificate_name = 'NG ' + '' + 'ANDREW'
print(certificate_name.upper())



