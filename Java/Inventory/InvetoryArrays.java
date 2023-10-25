import java.util.Scanner;
public class Invetory {
    public static void main(String[] args) {
        //Program that keeps track of the animals at the Vet
        //    add , insert,  remove,  replace, clear the db
        //    if the user types in quit -> the program ends
        String[] petList = new String[0];
        Scanner ui = new Scanner(System.in);
        String userInput = "";
        String secondUi = "";
        while(!userInput.equals("q")){
            System.out.println("what would you like to do? (a)dd, (i)nsert, (r)remove , Re(p)lace , (C)lear, (v)iew or (q)uit");
            userInput = ui.nextLine();

            if (userInput.equals("a")){
                System.out.println("What would you like to add?");
                userInput = ui.nextLine();
                //System.out.println(petList.length);
                petList = addInFormat(petList,petList.length,userInput);
                
            }
            else if (userInput.equals("i")){
                System.out.println("What place do you want to insert this into (Give number, EX; 1,2,3,4?");
                secondUi = ui.nextLine();
                System.out.println("What would you like to insert?");
                userInput = ui.nextLine();
                if (Integer.parseInt(secondUi)<=petList.length){
                    petList = addInFormat(petList,Integer.parseInt(secondUi),userInput);
                }
                else{
                    System.out.println("Index is out of range");
                }
          

            }
            else if (userInput.equals("r")){
                System.out.println("What do you want to remove?");
                userInput = ui.nextLine();

                
                petList = removeFormat(petList,userInput);

                //petList.remove(userInput);
                
            }
            else if (userInput.equals("p")){
                System.out.println("What name do you want to replace?");
                secondUi = ui.nextLine();
                System.out.println("What do you want to replace it with?");
                userInput = ui.nextLine();
                petList = replaceFormat(petList,secondUi,userInput);

              

            }
            else if (userInput.equals("c")){
                //System.out.println("clear");
                petList = new String[0];

            }
            else if (userInput.equals("v")){
                //System.out.println("view");
                printArray(petList);
              
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
    public static String[] addInFormat(String[] arr , int indexNumber, String newString){
        int incr = 0;
        String[] petList = new String[arr.length+1];

        for (int i=0;i<=arr.length;i++){
            if (i == indexNumber){
                petList[i] = newString;
            }
            else{
                petList[i] = arr[incr];
                incr+=1;
            }
         }    
         return(petList);

    }
    public static String[] removeFormat(String[] arr , String ui){
        String[] petList = new String[arr.length-1];

        for (int i=0;i<=arr.length-1;i++){
            int incr = 0;
            if (arr[i].equals( ui)){
                //petList[i] = newUi;
            }
            else{
                petList[incr] = arr[i];
                incr+=1;
            }
         }    
         return(petList);

    }
    public static String[] replaceFormat(String[] arr , String ui, String newUi){
        String[] petList = new String[arr.length];

        for (int i=0;i<=arr.length-1;i++){
            //int incr = 0;
            if (arr[i].equals( ui)){
                petList[i] = newUi;
            }
            else{
                petList[i] = arr[i];
                //incr+=1;
            }
         }    
         return(petList);

    }
    public static void printArray(String[] arr){
        for (int i=0; i<arr.length;i++){
            System.out.println(arr[i]);
         }
    }

}
