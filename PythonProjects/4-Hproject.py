#Isaac Pohl

from graphics import *
from random import *
    
    
def createwindow():
    window = GraphWin("White",640,640)
    window.setBackground("white")
    window.setCoords(0,0,100,100)
    return(window)

def Dataanalyzer(window):
    from TextClass import Textenter
    Textenter(50,15,50, 50, 50, 70, 50, 30, 85,   'Entername', 'Enter Your Name to print the certificate of your success', 'Click anywhere on the screen once name is entered', 'Congratulation to', 'For Completion' )

    return(window)


def Words(window):
    #Printing Intructions 
    x5,x6 = 50,90
    Text1 = Text(Point(x5,x6), "Click on any Animal to learn more").draw(window)
    Line1 = Line(Point(x5-20, x6 -2) , Point(x5 + 20 , x6 - 2)).draw(window)
    QuitButton = Text(Point(94,94), "Quit").draw(window)
    Rectangle(Point(90,90), Point(98,98)).draw(window)
    MiddleBoxReset(window)
    MiddleBoxText = Text(Point(50,70) , "Once you have clicked and read all the animal tabs").draw(window)
    MiddleBoxText2 = Text(Point(50,60) , "then click the test button below").draw(window)
    MiddleBoxText3 = Text(Point(50,50) , "to pass the test which will only").draw(window)
    MiddleBoxText4 = Text(Point(50,40) , "show after completion of 1 activity").draw(window)
    return(window)


def MiddleBoxReset(window):
    MiddleBox = Rectangle(Point(20,20), Point(80,80)).draw(window)
    MiddleBox.setFill("white")
    return(window) 

def BigWindowReset(window):
    BigWindow = Rectangle(Point (0,0), Point(100,80)).draw(window)
    BigWindow.setFill("white")
    
def mainprogram(window):
    x1,x2 = 10,12
    chickenbutton = Text(Point(x1,x2), "Chicken").draw(window)
    Rectangle(Point(x1-7,x2-4), Point(x1+7,x2+4)).draw(window)
    x3,x4 = 10,24
    cowbutton = Text(Point(x3,x4), "Cow").draw(window)
    Rectangle(Point(x3-7,x4-4), Point(x3+7,x4+4)).draw(window)
    x5,x6 = 10, 36
    rabbitbutton = Text(Point(x5,x6), "Rabbit").draw(window)
    Rectangle(Point(x5-7,x6-4), Point(x5+7,x6+4)).draw(window)
    x7,x8 = 10, 48
    Pigbutton = Text(Point(x7,x8), "Pig").draw(window)
    Rectangle(Point(x7-7,x8-4), Point(x7+7,x8+4)).draw(window)
    x9,x10 = 10, 60
    Goatbutton = Text(Point(x9,x10), "Goat").draw(window)
    Rectangle(Point(x9-7,x10-4), Point(x9+7,x10+4)).draw(window)
    x11,x12 = 10, 72
    Sheepbutton = Text(Point(x11,x12), "Sheep").draw(window)
    Rectangle(Point(x11-7,x12-4), Point(x11+7,x12+4)).draw(window)
    p1 = window.getMouse()

    while p1.getX()> 0 and p1.getX()< 90 and p1.getY()> 0 and p1.getY()< 90:
        p1 = window.getMouse()
        MiddleBoxReset(window)
        MiddleBoxText = Text(Point(50,70) , "Once you have clicked and read all the animal tabs").draw(window)
        MiddleBoxText2 = Text(Point(50,60) , "then click the on the test button down below").draw(window)
        MiddleBoxText3 = Text(Point(50,50) , "to try to pass the test which will only").draw(window)
        MiddleBoxText4 = Text(Point(50,40) , "show up after completion of this activity").draw(window)
        Testbutton = Text(Point(50,30),"Test").draw(window)
        Rectangle(Point(45,25), Point(55,35)).draw(window)


        #Chicken Window
        if p1.getX()> x1-7 and p1.getX()< x1+7 and p1.getY()> x2-4 and p1.getY()< x2+4:
            MiddleBoxReset(window)
            Chickentext6 = Text(Point(50,70) , "Benefits of raising Chickens").draw(window)
            Chickentext7 = Text(Point(50,60) , "People raise chickens mostly for the eggs").draw(window)
            Chickentext8 = Text(Point(50,53) , "and the enjoyment of having them around.").draw(window)
            Chickentext9 = Text(Point(50,46) , "Another benefit of raising chickens include").draw(window)
            Chickentext10 = Text(Point(50,39) , "the manure used for garden fertilizer.").draw(window)

            Chickennextbutton = Text(Point(74,25) , "Next").draw(window)
            Rectangle(Point(70,22), Point(78,28)).draw(window)
            p2 = window.getMouse()
            if p2.getX()> 70 and p2.getX()< 78 and p2.getY()> 22 and p2.getY()< 28:
                MiddleBoxReset(window)
                Chickentext11 = Text(Point(50,70) , "Taking Care Of Chicken").draw(window)
                Chickentext12 = Text(Point(50,60) , "Chickens need to be watch so they don't overheat.").draw(window)
                Chickentext13 = Text(Point(50,53) , "They need feed and water everyday.").draw(window)
                Chickentext14 = Text(Point(50,46) , "Each chicken should have at least 10").draw(window)
                Chickentext15 = Text(Point(50,39) , "square feet of outdoor space.").draw(window)
      
                Chickennextbutton = Text(Point(74,25) , "Next").draw(window)
                Rectangle(Point(70,22), Point(78,28)).draw(window)
                p3 = window.getMouse()
                if p3.getX()> 70 and p3.getX()< 78 and p3.getY()> 22 and p3.getY()< 28:
                    MiddleBoxReset(window)
                    Chickentext11 = Text(Point(50,70) , "Showing Chickens at the fair").draw(window)
                    Chickentext12 = Text(Point(50,60) , "Chicken should be worked with many ").draw(window)
                    Chickentext13 = Text(Point(50,53) , "months before the fair. When at the fair").draw(window)
                    Chickentext14 = Text(Point(50,46) , "chickens should have clean beeding and water.").draw(window)
                    Chickentext15 = Text(Point(50,39) , "Judges look at all parts of the chicken.").draw(window)
                    Chickennextbutton = Text(Point(74,25) , "Exit").draw(window)
                    Rectangle(Point(70,22), Point(78,28)).draw(window)
                    chickenbutton.setFill("grey")
                else:
                    MiddleBoxReset(window)
                    Chickentext5 = Text(Point(50,50) , "Please Retry").draw(window)        
            else:
                MiddleBoxReset(window)
                Chickentext3 = Text(Point(50,50) , "Please Retry").draw(window)

                    
        #Cow window
        elif p1.getX()> x3-7 and p1.getX()< x3+7 and p1.getY()> x4-4 and p1.getY()< x4+4:
            MiddleBoxReset(window)
            Cowtext6 = Text(Point(50,70) , "Different types of  Cows").draw(window)
            Cowtext7 = Text(Point(50,60) , "There are two types of cows meat and dairy.").draw(window)
            Cowtext8 = Text(Point(50,53) , "Both are commonly showed at the fair and raised on").draw(window)
            Cowtext9 = Text(Point(50,46) , "farms. Besides the two types of cows there are more").draw(window)
            Cowtext10 = Text(Point(50,39) , "than 250 different breeds of cows.").draw(window)

            Cownextbutton = Text(Point(74,25) , "Next").draw(window)
            Rectangle(Point(70,22), Point(78,28)).draw(window)
            p2 = window.getMouse()
            if p2.getX()> 70 and p2.getX()< 78 and p2.getY()> 22 and p2.getY()< 28:
                MiddleBoxReset(window)
                Cowtext11 = Text(Point(50,70) , "Taking Care Of Cows").draw(window)
                Cowtext12 = Text(Point(50,60) , "A cow needs 1 to 2 acres for grazing.").draw(window)
                Cowtext13 = Text(Point(50,53) , "Cows should be feed with hay during winter months,").draw(window)
                Cowtext14 = Text(Point(50,46) , "if pregnant, or when there is lack of grazing area.").draw(window)
                Cownextbutton = Text(Point(74,25) , "Next").draw(window)
                Rectangle(Point(70,22), Point(78,28)).draw(window)
                p3 = window.getMouse()
                if p3.getX()> 70 and p3.getX()< 78 and p3.getY()> 22 and p3.getY()< 28:
                    MiddleBoxReset(window)
                    Cowtext11 = Text(Point(50,70) , "Showing Cows at the Fair").draw(window)
                    Cowtext12 = Text(Point(50,60) , "Showing a cow at the fair takes time and preparation.").draw(window)
                    Cowtext13 = Text(Point(50,53) , "The most important thing is to get the cow familiar").draw(window)
                    Cowtext14 = Text(Point(50,46) , "with you. Make sure the cow is familar").draw(window)
                    Cowtext15 = Text(Point(50,39) , "with a halter and show stick." ).draw(window)
                    Cownextbutton = Text(Point(74,25) , "Exit").draw(window)
                    Rectangle(Point(70,22), Point(78,28)).draw(window)
                    cowbutton.setFill("grey")
                else:
                    MiddleBoxReset(window)
                    Cowtext5 = Text(Point(50,50) , "Please Retry").draw(window)        
            else:
                MiddleBoxReset(window)
                Cowtext3 = Text(Point(50,50) , "Please Retry").draw(window)

        #Rabbit Window
        elif p1.getX()> x5-7 and p1.getX()< x5+7 and p1.getY()> x6-4 and p1.getY()< x6+4:
            MiddleBoxReset(window)
            Rabbittext6 = Text(Point(50,70) , "Taking care of Rabbits").draw(window)
            Rabbittext7 = Text(Point(50,60) , "There are hundreds of different species of").draw(window)
            Rabbittext8 = Text(Point(50,53) , "rabbits and picking the right one for you is").draw(window)
            Rabbittext9 = Text(Point(50,46) , "so important. People assume that rabbits require the").draw(window)
            Rabbittext10 = Text(Point(50,39) , "least about of work but that is not true; rabbits need").draw(window)
            Rabbittext16 = Text(Point(50,32) , "attention to remain tame.").draw(window)

            Nextbutton = Text(Point(74,25) , "Next").draw(window)
            Rectangle(Point(70,22), Point(78,28)).draw(window)
            p2 = window.getMouse()
            if p2.getX()> 70 and p2.getX()< 78 and p2.getY()> 22 and p2.getY()< 28:
                MiddleBoxReset(window)
                Rabbittext11 = Text(Point(50,70) , "Rabbit requirements").draw(window)
                Rabbittext12 = Text(Point(50,60) , "Rabbits require enough space in their cage ").draw(window)
                Rabbittext13 = Text(Point(50,53) , "to stand up straight and to hoop around.").draw(window)
                Rabbittext14 = Text(Point(50,46) , "Rabbit essentials include hay, pellets, and water.").draw(window)
                Rabbittext15 = Text(Point(50,39) , "Rabbits also need fans during hot months.").draw(window)
                Cownextbutton = Text(Point(74,25) , "Next").draw(window)
                Nextbutton = Text(Point(74,25) , "Next").draw(window)
                Rectangle(Point(70,22), Point(78,28)).draw(window)
                p3 = window.getMouse()
                if p3.getX()> 70 and p3.getX()< 78 and p3.getY()> 22 and p3.getY()< 28:
                    MiddleBoxReset(window)
                    Rabbittext11 = Text(Point(50,70) , "Showing Rabbits at the Fair").draw(window)
                    Rabbittext12 = Text(Point(50,60) , "Rabbits require training months before the fair.").draw(window)
                    Rabbittext13 = Text(Point(50,53) , "Rabbits need brushing to keep them clean.").draw(window)
                    Rabbittext14 = Text(Point(50,46) , "Practice flipping your rabbit upside down so").draw(window)
                    Rabbittext15 = Text(Point(50,39) , "that the judge can see the underside." ).draw(window)
                    Nextbutton = Text(Point(74,25) , "Exit").draw(window)
                    Rectangle(Point(70,22), Point(78,28)).draw(window)
                    rabbitbutton.setFill("grey")
                else:
                    MiddleBoxReset(window)
                    Rabbittext5 = Text(Point(50,50) , "Please Retry").draw(window)        
            else:
                MiddleBoxReset(window)
                Rabbittext3 = Text(Point(50,50) , "Please Retry").draw(window)

        #Pig Window
        elif p1.getX()> x7-7 and p1.getX()< x7+7 and p1.getY()> x8-4 and p1.getY()< x8+4:
            MiddleBoxReset(window)
            Pigtext6 = Text(Point(50,70) , "Why get a Pig").draw(window)
            Pigtext7 = Text(Point(50,60) , "Pigs are good for meat and").draw(window)
            Pigtext8 = Text(Point(50,53) , "showing at 4-H. Pigs are one of the most  ").draw(window)
            Pigtext9 = Text(Point(50,46) , "intelligent animals. You can train them to").draw(window)
            Pigtext10 = Text(Point(50,39) , "live in your house and be potty trained.").draw(window)
            Nextbutton = Text(Point(74,25) , "Next").draw(window)
            Rectangle(Point(70,22), Point(78,28)).draw(window)
            p2 = window.getMouse()
            if p2.getX()> 70 and p2.getX()< 78 and p2.getY()> 22 and p2.getY()< 28:
                MiddleBoxReset(window)
                Pigtext11 = Text(Point(50,70) , "Different types of Pigs").draw(window)
                Pigtext12 = Text(Point(50,60) , "There are 16 different types of pigs.").draw(window)
                Pigtext13 = Text(Point(50,53) , "The most common type is the Yorkshire.").draw(window)
                Pigtext14 = Text(Point(50,46) , "Some types of pigs get bigger and are more").draw(window)
                Pigtext15 = Text(Point(50,39) , "for show than others. ").draw(window)
                Nextbutton = Text(Point(74,25) , "Next").draw(window)
                Rectangle(Point(70,22), Point(78,28)).draw(window)
                p3 = window.getMouse()
                if p3.getX()> 70 and p3.getX()< 78 and p3.getY()> 22 and p3.getY()< 28:
                    MiddleBoxReset(window)
                    Pigtext11 = Text(Point(50,70) , "Showing Pigs at the Fair").draw(window)
                    Pigtext12 = Text(Point(50,60), "Show pigs are feed with pellets to").draw(window)
                    Pigtext13 = Text(Point(50,53) , "fatten them up. Pigs also require unlimited").draw(window)
                    Pigtext14 = Text(Point(50,46) , "water and cooling during the summer, including").draw(window)
                    Pigtext15 = Text(Point(50,39) , "fans and water misters. Pigs are so fun to show at" ).draw(window)
                    Pigtext16 = Text(Point(50,32) , "the fair, but need to be worked with." ).draw(window)

                    Nextbutton = Text(Point(74,25) , "Exit").draw(window)
                    Rectangle(Point(70,22), Point(78,28)).draw(window)
                    Pigbutton.setFill("grey")
                else:
                    MiddleBoxReset(window)
                    Pigtext5 = Text(Point(50,50) , "Please Retry").draw(window)        
            else:
                MiddleBoxReset(window)
                Pigtext3 = Text(Point(50,50) , "Please Retry").draw(window)
                
        #Goat Wndow
        elif p1.getX()> x9-7 and p1.getX()< x9+7 and p1.getY()> x10-4 and p1.getY()< x10+4:
            MiddleBoxReset(window)
            Goattext6 = Text(Point(50,70) , "Why show a Goat").draw(window)
            Goattext7 = Text(Point(50,60) , "Goats make people smile because of their").draw(window)
            Goattext8 = Text(Point(50,53) , "playing and jumping ability. ").draw(window)
            Goattext9 = Text(Point(50,46) , "Goats can also be used for meat milk, and fur.").draw(window)
    

            Nextbutton = Text(Point(74,25) , "Next").draw(window)
            Rectangle(Point(70,22), Point(78,28)).draw(window)
            p2 = window.getMouse()
            if p2.getX()> 70 and p2.getX()< 78 and p2.getY()> 22 and p2.getY()< 28:
                MiddleBoxReset(window)
                Nextbutton = Text(Point(74,25) , "Next").draw(window)
                Goattext11 = Text(Point(50,70) , "Showing Goats at the Fair").draw(window)
                Goattext12 = Text(Point(50,60) , "Goats require being lead on a leash").draw(window)
                Goattext13 = Text(Point(50,53) , "many weeks before the fair, and they require").draw(window)
                Goattext14 = Text(Point(50,46) , "proper trimming and shaving. Goats ").draw(window)
                Goattext15 = Text(Point(50,39) , "require much time to be worked with by their owners.").draw(window)
                Rectangle(Point(70,22), Point(78,28)).draw(window)
                p3 = window.getMouse()
                if p3.getX()> 70 and p3.getX()< 78 and p3.getY()> 22 and p3.getY()< 28:
                    MiddleBoxReset(window)
                    Goattext11 = Text(Point(50,70) , "Fun facts about Goats").draw(window)
                    Goattext12 = Text(Point(50,60), "Goats were one of the first animals to be tamed by").draw(window)
                    Goattext13 = Text(Point(50,53) , "humans and were herded 9,000 years ago.").draw(window)
                    Goattext14 = Text(Point(50,46) , "Goats are very intelligent and curious animals and").draw(window)
                    Goattext15 = Text(Point(50,39) , "have a constant desire to explore anything unfamiliar." ).draw(window)
                    Nextbutton = Text(Point(74,25) , "Exit").draw(window)
                    Rectangle(Point(70,22), Point(78,28)).draw(window)
                    Goatbutton.setFill("grey")
                else:
                    MiddleBoxReset(window)
                    Goattext5 = Text(Point(50,50) , "Please Retry").draw(window)        
            else:
                MiddleBoxReset(window)
                Goattext3 = Text(Point(50,50) , "Please Retry").draw(window)

        #Sheep Window
        elif p1.getX()> x11-7 and p1.getX()< x11+7 and p1.getY()> x12-4 and p1.getY()< x12+4:
            MiddleBoxReset(window)
            Sheeptext6 = Text(Point(50,70) , "Why get a Sheep").draw(window)
            Sheeptext7 = Text(Point(50,60) , "Sheep are related to goats. Sheep are used").draw(window)
            Sheeptext9 = Text(Point(50,53) , "for fur and meat. Sheep are gentle and").draw(window)
            Sheeptext10 = Text(Point(50,46) , "trainable making it a perfect choice for many people.").draw(window)
            Nextbutton = Text(Point(74,25) , "Next").draw(window)
            Rectangle(Point(70,22), Point(78,28)).draw(window)
            p2 = window.getMouse()
            if p2.getX()> 70 and p2.getX()< 78 and p2.getY()> 22 and p2.getY()< 28:
                MiddleBoxReset(window)
                Sheeptext11 = Text(Point(50,70) , "Showing Sheep at the Fair").draw(window)
                Sheeptext12 = Text(Point(50,60) , "You have to train sheep by leading them.").draw(window)
                Sheeptext13 = Text(Point(50,53) , "Sheep require a supply of feed, water, and").draw(window)
                Sheeptext14 = Text(Point(50,46) , "hay. Some sheep will need their ").draw(window)
                Sheeptext15 = Text(Point(50,39) , "wool shaved before the show.").draw(window)
                   
                Nextbutton = Text(Point(74,25) , "Next").draw(window)
                Rectangle(Point(70,22), Point(78,28)).draw(window)
                p3 = window.getMouse()
                if p3.getX()> 70 and p3.getX()< 78 and p3.getY()> 22 and p3.getY()< 28:
                    MiddleBoxReset(window)
                    Sheeptext11 = Text(Point(50,70) , "Fun facts about Sheep").draw(window)
                    Sheeptext12 = Text(Point(50,60), "There wool will keep growing so shave when needed.").draw(window)
                    Sheeptext13 = Text(Point(50,53) , "They have nearly 360 degree vision.").draw(window)
                    Sheeptext14 = Text(Point(50,46) , "There are over 1 billion sheep in the world.").draw(window)
                    Sheeptext15 = Text(Point(50,39) , "When giving brith, it is usually twins." ).draw(window)
                     
                    Nextbutton = Text(Point(74,25) , "Exit").draw(window)
                    Rectangle(Point(70,22), Point(78,28)).draw(window)
                    Sheepbutton.setFill("grey")
                else:
                    MiddleBoxReset(window)
                    Sheeptext5 = Text(Point(50,50) , "Please Retry").draw(window)        
            else:
                MiddleBoxReset(window)
                Sheeptext3 = Text(Point(50,50) , "Please Retry").draw(window)

      

        #Test Program
        elif p1.getX()> 45 and p1.getX()< 65 and p1.getY()> 25 and p1.getY()< 35:
            answersright = 0
            questionleft = 7
            question1, question2, question3, question4, question5, question6, question7 = True, True, True, True, True, True, True
            TopBox = Rectangle(Point(0,80), Point(100,100)).draw(window)
            TopBox.setFill("white")
            
            for i in range (7):

                BigWindowReset(window)
                MiddleLine = Line(Point(50,0) , Point(50,65)).draw(window)
                Testtext = Text(Point(50,90) , "Test").draw(window)
                answersrightboxtext = Text(Point(10,90) , "Answers right").draw(window)
                answersleftboxtext = Text(Point(90,90) , "Answers left").draw(window)
                number1 = randrange(1,8)
                while number1 == 1 and question1 == False or number1 == 2 and question2 == False or number1 == 3 and question3 == False or number1 == 4 and question4 == False or number1 == 5 and question5 == False or number1 == 6 and question6 == False or number1 == 7 and question7 == False:
                    number1 = randrange(1,8)
                answersrightbox = Rectangle(Point(7,81), Point(13,87)).draw(window)
                questionsleftbox = Rectangle(Point(87,81), Point(93,87)).draw(window)

        
                if number1 == 1:
                    Question1Text = Text(Point(50,75) , "True or false Goats are used for meat, milk, and fur?").draw(window)
                    answer1 = Text(Point(25,35) , "True").draw(window)
                    answer2 = Text(Point(75,35) , "False").draw(window)
                    p2 = window.getMouse()

                    if p2.getX()> 0 and p2.getX()< 50 and p2.getY()> 0 and p2.getY()< 80:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("green")
                        Rightanswertext = Text(Point(50,70) , "You got the answer right").draw(window)
                        answersright = answersright + 1
                        time.sleep(2)
                        question1 = False
                    else:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("red")
                        Wronganswertext = Text(Point(50,70) , "You got the answer wrong").draw(window)
                        time.sleep(2)


                elif number1 == 2:
                    Question2Text = Text(Point(50,75) , "Goats are closley related to what animal?").draw(window)
                    answer1 = Text(Point(25,17.5) , "Sheep").draw(window)
                    answer2 = Text(Point(75,17.5) , "Cow").draw(window)
                    answer3 = Text(Point(25,52.5) , "Pig").draw(window)
                    answer4 = Text(Point(75,52.5) , "Chicken").draw(window)
                    MiddleAcrossLine = Line(Point(0,35),Point(100,35)).draw(window)
                    p2 = window.getMouse()
                    if p2.getX()> 0 and p2.getX()< 50 and p2.getY()> 0 and p2.getY()< 35:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("green")
                        Rightanswertext = Text(Point(50,70) , "You got the answer right").draw(window)
                        answersright = answersright + 1
                        time.sleep(2)
                        question2 = False
                        
                    else:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("red")
                        Wronganswertext = Text(Point(50,70) , "You got the answer wrong").draw(window)
                        time.sleep(2)

                elif number1 == 3:
                    Question2Text = Text(Point(50,75) , "True or false Pigs are intelligent animals? ").draw(window)
                    answer1 = Text(Point(25,35) , "True").draw(window)
                    answer2 = Text(Point(75,35) , "False").draw(window)
                    p2 = window.getMouse()
                    if p2.getX()> 0 and p2.getX()< 50 and p2.getY()> 0 and p2.getY()< 80:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("green")
                        Rightanswertext = Text(Point(50,70) , "You got the answer right").draw(window)
                        answersright = answersright + 1
                        time.sleep(2)
                        question3 = False
                    else:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("red")
                        Wronganswertext = Text(Point(50,70) , "You got the answer wrong").draw(window)
                        time.sleep(2)

                elif number1 == 4:
                    Question2Text = Text(Point(50,75) , "What animal needs at least 10 square feet of outdoor space?").draw(window)
                    answer1 = Text(Point(25,17.5) , "Sheep").draw(window)
                    answer2 = Text(Point(75,17.5) , "Pig").draw(window)
                    answer3 = Text(Point(25,52.5) , "Chicken").draw(window)
                    answer4 = Text(Point(75,52.5) , "Rabbit").draw(window)
                    MiddleAcrossLine = Line(Point(0,35),Point(100,35)).draw(window)

                    p2 = window.getMouse()
                    if p2.getX()> 0 and p2.getX()< 50 and p2.getY()> 35 and p2.getY()< 80:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("green")
                        Rightanswertext = Text(Point(50,70) , "You got the answer right").draw(window)
                        answersright = answersright + 1
                        time.sleep(2)
                        question4 = False
                        
                    else:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("red")
                        Wronganswertext = Text(Point(50,70) , "You got the answer wrong").draw(window)
                        time.sleep(2)

                elif number1 == 5:
                    Question2Text = Text(Point(50,75) , "True or False Cows need at least 10 acres each?").draw(window)
                    answer1 = Text(Point(25,35) , "False").draw(window)
                    answer2 = Text(Point(75,35) , "True").draw(window)
                    p2 = window.getMouse()
                    if p2.getX()> 0 and p2.getX()< 50 and p2.getY()> 0 and p2.getY()< 80:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("green")
                        Rightanswertext = Text(Point(50,70) , "You got the answer right").draw(window)
                        answersright = answersright + 1
                        time.sleep(2)
                        question5 = False
                        
                    else:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("red")
                        Wronganswertext = Text(Point(50,70) , "You got the answer wrong").draw(window)
                        time.sleep(2)

                elif number1 == 6:
                    Question2Text = Text(Point(50,75) , "Which species have 16 different types?").draw(window)
                    answer1 = Text(Point(25,17.5) , "Sheep").draw(window)
                    answer2 = Text(Point(75,17.5) , "Cow").draw(window)
                    answer3 = Text(Point(25,52.5) , "Goats").draw(window)
                    answer4 = Text(Point(75,52.5) , "Pigs").draw(window)
                    MiddleAcrossLine = Line(Point(0,35),Point(100,35)).draw(window)

                    p2 = window.getMouse()
                    if p2.getX()> 50 and p2.getX()< 100 and p2.getY()> 35 and p2.getY()< 80:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("green")
                        Rightanswertext = Text(Point(50,70) , "You got the answer right").draw(window)
                        answersright = answersright + 1
                        time.sleep(2)
                        question6 = False
                        
                    else:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("red")
                        Wronganswertext = Text(Point(50,70) , "You got the answer wrong").draw(window)
                        time.sleep(2)

                elif number1 == 7:
                    Question2Text = Text(Point(50,75) , "True or False You don't have to work with rabbits before the fair?").draw(window)
                    answer1 = Text(Point(25,35) , "True").draw(window)
                    answer2 = Text(Point(75,35) , "False").draw(window)
                    p2 = window.getMouse()
                    if p2.getX()> 50 and p2.getX()< 100 and p2.getY()> 0 and p2.getY()< 80:
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("green")
                        Rightanswertext = Text(Point(50,70) , "You got the answer right").draw(window)
                        answersright = answersright + 1
                        time.sleep(2)
                        question7 = False
                    else:
                       
                        MiddleBox = Rectangle(Point(0,0), Point(100,80)).draw(window)
                        MiddleBox.setFill("red")
                        Wronganswertext = Text(Point(50,70) , "You got the answer wrong").draw(window)
                        time.sleep(2)

                #Questions left and right box display
                questionleft = questionleft - 1
                if answersright == 1:
                    answersrightbox.setFill("white")
                    questionsrighttop = Text(Point(10,84) , "1").draw(window)
                elif answersright == 2:
                    answersrightbox.setFill("white")
                    questionsrighttop = Text(Point(10,84) , "2").draw(window)
                elif answersright == 3:
                    answersrightbox.setFill("white")
                    questionsrighttop = Text(Point(10,84) , "3").draw(window)
                elif answersright == 4:
                    answersrightbox.setFill("white")
                    questionsrighttop = Text(Point(10,84) , "4").draw(window)
                elif answersright == 5:
                    answersrightbox.setFill("white")
                    questionsrighttop = Text(Point(10,84) , "5").draw(window)
                elif answersright == 6:
                    answersrightbox.setFill("white")
                    questionsrighttop = Text(Point(10,84) , "6").draw(window)
                else:
                #answersright == 7:
                    answersrightbox.setFill("white")
                    questionsrighttop = Text(Point(10,84) , "7").draw(window)

                if questionleft ==6:
                    questionsleftbox.setFill("white")
                    questionslefttop = Text(Point(90,84) , "6").draw(window)
                elif questionleft ==5:
                    questionsleftbox.setFill("white")
                    questionslefttop = Text(Point(90,84) , "5").draw(window)
                elif questionleft ==4:
                    questionsleftbox.setFill("white")
                    questionslefttop = Text(Point(90,84) , "4").draw(window)
                elif questionleft ==3:
                    questionsleftbox.setFill("white")
                    questionslefttop = Text(Point(90,84) , "3").draw(window)
                elif questionleft ==2:
                    questionsleftbox.setFill("white")
                    questionslefttop = Text(Point(90,84) , "2").draw(window)
                else:
                    #questionleft ==1:
                    questionsleftbox.setFill("white")
                    questionslefttop = Text(Point(90,84) , "1").draw(window)
                if answersright == 7:
                    Youwonmessage = Text(Point(50,60) , "You won").draw(window)
                    Dataanalyzer(window)

                elif questionleft ==0 and answersright != 7:
                    Youlostmessage = Text(Point(50,60) , "You lost").draw(window)  
                    
                   # Dataanalyzer(window)


       
                if questionleft ==0:
                    questionsleftbox.setFill("white")
                    questionslefttop = Text(Point(90,84) , "0").draw(window)
                    time.sleep(3)
                    ManualReset = Rectangle(Point (0,0), Point(100,100)).draw(window)
                    ManualReset.setFill("white")
                    chickenbutton = Text(Point(x1,x2), "Chicken").draw(window)
                    Rectangle(Point(x1-7,x2-4), Point(x1+7,x2+4)).draw(window)
                    cowbutton = Text(Point(x3,x4), "Cow").draw(window)
                    Rectangle(Point(x3-7,x4-4), Point(x3+7,x4+4)).draw(window)
                    rabbitbutton = Text(Point(x5,x6), "Rabbit").draw(window)
                    Rectangle(Point(x5-7,x6-4), Point(x5+7,x6+4)).draw(window)
                    Pigbutton = Text(Point(x7,x8), "Pig").draw(window)
                    Rectangle(Point(x7-7,x8-4), Point(x7+7,x8+4)).draw(window)
                    Goatbutton = Text(Point(x9,x10), "Goat").draw(window)
                    Rectangle(Point(x9-7,x10-4), Point(x9+7,x10+4)).draw(window)
                    Sheepbutton = Text(Point(x11,x12), "Sheep").draw(window)
                    Rectangle(Point(x11-7,x12-4), Point(x11+7,x12+4)).draw(window)                 
                    Words(window)

    #Close window
    window.close()
    print("The program is closed")
                             
                    

def main():
    window = createwindow()
    window = Words(window)
    window = mainprogram(window)
    

main()
