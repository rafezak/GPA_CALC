#noteert alle cijfers en slaat ze op in een variabel.



cijfer1 = float (input("Wat is uw cijfer van k1 of k2?"))
cijfer2 = float (input("Wat is uw cijfer van foundation1?"))
cijfer3 = float (input("Wat is uw cijfer van k3 of k4"))
cijfer4 = float (input("Wat is uw cijfer van foundation2?"))
cijfer5 = float (input("Wat is uw cijfer van core5?"))
cijfer6 = float (input("Wat is uw cijfer van foundation3?"))
cijfer7 = float (input("Wat is uw cijfer van core6?"))
cijfer8 = float (input("Wat is uw cijfer van foundation4?"))
cijfer9 = float (input("Wat is uw cijfer van internship?"))
cijfer10 = float (input("Wat is uw cijfer van MinorA?"))
cijfer11 = float (input("Wat is uw cijfer van MinorB?"))
cijfer12 = float (input("Wat is uw cijfer van MinorC?"))
cijfer13 = float (input("Wat is uw cijfer van MinorD?"))
cijfer14 = float (input("Wat is uw cijfer van Graduation Project?"))
#Het aantal studiepunten waarmee het cijfer vermenigvuldigd moet worden
Gewicht1= 10
Gewicht2= 5
Gewicht3= 10
Gewicht4= 5
Gewicht5= 10
Gewicht6= 5
Gewicht7= 10
Gewicht8= 5
Gewicht9= 30
Gewicht10= 15
Gewicht11= 15
Gewicht12= 15
Gewicht13= 15
Gewicht14= 30

#controleert of het cijfer een onvoldoende is. Zoniet, wordt deze niet meegeteld 

if cijfer1 <5.5:
    Gewicht1 = 0

if cijfer2 <5.5:
    Gewicht2 = 0

if cijfer3  <5.5:
    Gewicht3 = 0

if cijfer4  <5.5:
    Gewicht4 = 0

if cijfer5  <5.5:
    Gewicht5 = 0
    
if cijfer6 <5.5:
    Gewicht6 = 0 

if cijfer7  <5.5:
    Gewicht7 = 0

if cijfer8 <5.5:
    Gewicht8 = 0
    
if cijfer9 <5.5:
    Gewicht9 = 0 

if cijfer10 <5.5:
    Gewicht10 = 0

if cijfer11 <5.5:
    Gewicht11 = 0
    
if cijfer12 <5.5:
    Gewicht12 = 0 

if cijfer13 <5.5:
    Gewicht13 = 0

if cijfer14 <5.5:
    Gewicht14 = 0

Gewicht_totaal = Gewicht1 +  Gewicht2 + Gewicht3 + Gewicht4 + Gewicht5 + Gewicht6 + Gewicht7 + Gewicht8 + Gewicht9 + Gewicht10 + Gewicht11 + Gewicht12 + Gewicht13 + Gewicht14
  
    
  
#vermenigvuldigd alle cijfers met de bijbehorende studentpunten.
ec1 = cijfer1 * Gewicht1
ec2 = cijfer2 * Gewicht2
ec3 = cijfer3 * Gewicht3
ec4 = cijfer4 * Gewicht4
ec5 = cijfer5 * Gewicht5
ec6 = cijfer6 * Gewicht6
ec7 = cijfer7 * Gewicht7
ec8 = cijfer8 * Gewicht8
ec9 = cijfer9 * Gewicht9
ec10 = cijfer10 * Gewicht10
ec11 = cijfer11 * Gewicht11
ec12 = cijfer12 * Gewicht12
ec13 = cijfer13 * Gewicht13
ec14 = cijfer14 * Gewicht14



#telt alle  (vermenigvuldigde) studentpunten bij elkaar op.
ec_totaal = ec1 + ec2 + ec3 + ec4 + ec5 + ec6 + ec7 + ec8 + ec9 + ec10 + ec11 + ec12 + ec13 + ec14


#deelt het  totale (vermenigvuldigd) aantal studentpunten door het totale (onvermenigvuldigd) studentenpunten (AKA het gewicht) 
nederlands_cijfer = ec_totaal / Gewicht_totaal

gpa = 0

#checkt bij welke GPA het nederlandse cijfer hoort en print deze uit.
if nederlands_cijfer >= 0  and nederlands_cijfer <= 4.49:
    gpa = 0
    print("Uw gpa is " + str (gpa))

if nederlands_cijfer >= 4.50  and nederlands_cijfer <= 5.39:
    gpa = 1
    print("Uw gpa is " + str (gpa))

if nederlands_cijfer >= 5.40  and nederlands_cijfer <= 5.59:
    gpa = 1.3
    print("Uw gpa is " + str (gpa)) 

if nederlands_cijfer >= 5.60  and nederlands_cijfer <= 5.99:
    gpa = 1.7
    print("Uw gpa is " + str (gpa)) 
    
if nederlands_cijfer >= 6  and nederlands_cijfer <= 6.39:
    gpa = 2
    print("Uw gpa is " + str (gpa)) 


if nederlands_cijfer >= 6.40  and nederlands_cijfer <= 6.69:
    gpa = 2.3
    print("Uw gpa is " + str (gpa)) 


if nederlands_cijfer >= 6.70  and nederlands_cijfer <= 6.99:
    gpa = 2.7
    print("Uw gpa is " + str (gpa)) 


if nederlands_cijfer >= 7  and nederlands_cijfer <= 7.39:
    gpa = 3
    print("Uw gpa is " + str (gpa)) 


if nederlands_cijfer >= 7.40  and nederlands_cijfer <= 7.69:
    gpa = 3.3
    print("Uw gpa is " + str (gpa)) 

if nederlands_cijfer >= 7.70  and nederlands_cijfer <= 7.99:
    gpa = 3.7
    print("Uw gpa is " + str (gpa)) 

if nederlands_cijfer >= 8  and nederlands_cijfer <= 8.59:
    gpa = 4
    print("Uw gpa is " + str (gpa)) 

if nederlands_cijfer >= 8.60  and nederlands_cijfer <= 10:
    gpa = 4
    print("Uw gpa is " + str (gpa)) 

