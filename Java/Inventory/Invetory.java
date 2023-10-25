import java.util.Scanner;
import java.util.ArrayList;
public class Invetory {
    public static void main(String[] args) {
        //Program that keeps track of the animals at the Vet
        //    add , insert,  remove,  replace, clear the db
        //    if the user types in quit -> the program ends
        ArrayList<String> petList = new ArrayList<String>();
        Scanner ui = new Scanner(System.in);
        String userInput = "";
        String secondUi = "";
        while(!userInput.equals("q")){
            System.out.println("what would you like to do? (a)dd, (i)nsert, (r)remove , Re(p)lace , (C)lear, (v)iew or (q)uit");
            userInput = ui.nextLine();

            if (userInput.equals("a")){
                System.out.println("What would you like to add?");
                userInput = ui.nextLine();
                petList.add(userInput);

                
            }
            else if (userInput.equals("i")){
                System.out.println("What place do you want to insert this into (Give number, EX; 1,2,3,4?");
                secondUi = ui.nextLine();
                System.out.println("What would you like to insert?");
                userInput = ui.nextLine();
                if (Integer.parseInt(secondUi)<=petList.size()){
                    petList.add(Integer.parseInt(secondUi),userInput);
                }
                else{
                    System.out.println("Index was out of range, please try again");
                }

            }
            else if (userInput.equals("r")){
                System.out.println("What do you want to remove?");
                userInput = ui.nextLine();
                petList.remove(userInput);

            }
            else if (userInput.equals("p")){
                System.out.println("What name do you want to replace?");
                secondUi = ui.nextLine();
                System.out.println("What do you want to replace it with?");
                userInput = ui.nextLine();
                if (petList.indexOf(secondUi)!=-1 ){
                    petList.set(petList.indexOf(secondUi), userInput);
            }
                else{
                    System.out.println("The word was not found, please try again");
                }
              

            }
            else if (userInput.equals("c")){
                //System.out.println("clear");
                petList.clear();
            }
            else if (userInput.equals("v")){
                System.out.println("view");
                for(int r=0;r<petList.size();r++){
                    System.out.println(petList.get(r));
                }
            }
            else if (userInput.equals("q")){
                System.out.println("quit");
            }
            else{
                System.out.println("Please choose a correct answer");
                userInput = ui.nextLine();


            }

        }
        System.out.println("bye bye");
    }
}
