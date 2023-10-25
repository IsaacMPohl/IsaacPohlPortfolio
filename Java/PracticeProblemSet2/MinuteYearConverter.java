import java.util.Scanner;
public class minuteYearConverter {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter the number of minutes: ");
        double numMin = ui.nextDouble();
        double days =  (numMin/60/24);
        double years = days/365;
        double daysLeft = days - (int)years*365;

        System.out.printf("%s minutes is approximately %s years and %s days \n", numMin, (int)years, (int)daysLeft );
        //1000000000
    }
}
