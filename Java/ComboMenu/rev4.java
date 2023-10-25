import java.util.Scanner;

//import com.sun.org.apache.xpath.internal.operations.Bool;
public class rev0 {
    public static void main(String[] args) {
        Scanner ui2 = new Scanner(System.in);
        Scanner ui = new Scanner(System.in);
        String items = "";
        String prices = "";
        Double totalPrice = 0.00;
        Double totalOrderPrice = 0.00;
        String item = "";
        int ketchup = 0;
        String keepOrdering = "yes";
        String tempOrdering = "";
        int orderNum = 1;
        
        while (keepOrdering.equals("yes")){
        items+=("Order ");
        //System.out.println(items);
        System.out.print("Would you like a sandwhich? (\"tofu\"-$5.75 ) or (\"chicken\"-$5.25 ) or (\"beef\"-$6.25 ) or (\"no\")");
        item = ui.nextLine();
        if ((item.toLowerCase()).equals("tofu")){
            items+="tofu_sandwhich ";
            prices+="$5.75 ";
        }
        else if ((item.toLowerCase()).equals("chicken")){
            items+="chicken_sandwhich ";
            prices+="$5.25 ";
        }
        else if ((item.toLowerCase()).equals("beef")){
            items+="beef_sandwhich ";
            prices+="$6.25 ";
        }
        System.out.print("Would you like fries? (\"small\"-$1 ) or (\"medium\"-$1.75 ) or (\"large\"-$2.25 )  or (\"no\")");
        item = ui.nextLine();
        if ((item.toLowerCase()).equals("small")){
            items+="small_fries ";
            prices+="$1.00 ";
        }
        else if ((item.toLowerCase()).equals("medium")){
            items+="medium_fries ";
            prices+="$1.75 ";
        }
        else if ((item.toLowerCase()).equals("large")){
            items+="large_fries ";
            prices+="$2.25 ";
        }
        System.out.print("Would you like a drink? (\"small\"-$1 ) or (\"medium\"-$1.50 ) or (\"large\"-$2.00 )  or (\"no\")");
        item = ui.nextLine();
        if ((item.toLowerCase()).equals("small")){
            items+="small_drink ";
            prices+="$1.00 ";
        }
        else if ((item.toLowerCase()).equals("medium")){
            items+="medium_drink ";
            prices+="$1.50 ";
        }
        else if ((item.toLowerCase()).equals("large")){
            
            System.out.println("Would like to upgrade to a child size for $.38 more? \"Yes\" \"No\"");
            item = ui.nextLine();
            if ((item.toLowerCase()).equals("yes")){
                items+="childsize_drink ";
                prices+="$2.38 ";
                
            }
            else{
                items+="large_drink ";
                prices+="$2.00 ";

            }


        }

       

        System.out.println("How many ketchup packets do you want?");
        //thanks slack overflow for this idea
        while (! ui2.hasNextInt()){
            ui2.next();
            System.out.println("How many ketchup packets do you want?");
            
        }

        ketchup = ui2.nextInt();
        if (ketchup!=0){
            prices+=("$" + Double.toString(ketchup*.25) + " ");
            items+=(Integer.toString(ketchup)+"_ketchup ");
        }
        
        System.out.println("Do you want to keep ordering (\"yes\" or \"no\")");
        tempOrdering=ui.nextLine();
        if (tempOrdering.equals("no")){
            keepOrdering="no";
        }
        else{
            keepOrdering="yes";
            
        }

    }

        //System.out.println(items);
        //System.out.println(prices);

        

        
        while(prices.indexOf("$") != -1){         //loop while indexOf(f) finds an f
            if (items.substring(0, items.indexOf(" ")).equals("Order")){
                
                if (orderNum!=1){
                    System.out.printf("\tTotal For Order %s $ %2.2f%n ",orderNum,totalOrderPrice);
                    System.out.printf("\tTotal For Order %s $ %2.2f%n ",orderNum,totalOrderPrice);


                    totalOrderPrice=0.00;
                    
                }
                System.out.printf("\n\tOrder number %s \n", orderNum);
                
                items = items.substring(items.indexOf(" ")+1) + " ";
                if (items.contains("sandwhich") && items.contains("drink") && items.contains("fries")){
                    System.out.printf("\t$1 dollar discount is applied!\n");
                    totalPrice =-1.00;
                    totalOrderPrice =-1.00;

                }
                orderNum+=1;
                
                
            }
            totalPrice += Double.parseDouble(prices.substring(prices.indexOf("$")+1,prices.indexOf(" ")));
            totalOrderPrice += Double.parseDouble(prices.substring(prices.indexOf("$")+1,prices.indexOf(" ")));
            System.out.printf("\t%s - %s \n"  , items.substring(0,items.indexOf(" ")) , prices.substring(0,prices.indexOf(" ")));
            prices = prices.substring(prices.indexOf(" ")+1,prices.length());
            items = items.substring(items.indexOf(" ")+1) + " ";
            //System.out.println(items.substring(items.indexOf(" "),item.length()));
            //System.out.println(items.substring(items.indexOf(" ")));
            

       }
       System.out.printf("\tTotal For Order %s $ %2.2f%n ",orderNum,totalOrderPrice);
       System.out.printf("\tTotal For Order %s $ %2.2f%n ",orderNum,totalOrderPrice);

       System.out.println("");
       System.out.printf("\tSubtotal is is $ %2.2f%n ",totalPrice);
       System.out.printf("\tTax is $ %2.2f%n ",totalPrice*.07);
       System.out.printf("\tTotal is $ %2.2f%n ",totalPrice*1.07);


       //System.out.println(prices);
       




        
    }
}
