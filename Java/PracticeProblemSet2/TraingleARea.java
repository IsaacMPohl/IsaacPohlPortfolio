import java.util.Scanner;
import java.io.BufferedReader;
public class traingleARea {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter the coordinates of three points seperated by spaces like x1 y1 x2 y2 x3 y3");
        String coordinates = ui.nextLine();
        //nextLine = coordinates.nextInt();
        //int blank = coordinates.indexOf(" ");
        String parts[] = coordinates.split(" ");
        //credit to slack overflow for this idea of []
        //System.out.print(Integer.parseInt(parts[2])+Integer.parseInt(parts[1]));
        double side1 = Math.sqrt(Math.pow(Double.parseDouble(parts[2])-Double.parseDouble(parts[0]),2)+Math.pow(Double.parseDouble(parts[3])-Double.parseDouble(parts[1]),2));
        double side2 = Math.sqrt(Math.pow(Double.parseDouble(parts[4])-Double.parseDouble(parts[0]),2)+Math.pow(Double.parseDouble(parts[5])-Double.parseDouble(parts[1]),2));
        double side3 = Math.sqrt(Math.pow(Double.parseDouble(parts[4])-Double.parseDouble(parts[2]),2)+Math.pow(Double.parseDouble(parts[5])-Double.parseDouble(parts[3]),2));
        double s = ((side1+side2+side3)/2);
        double area = Math.sqrt(s*(s-side1)*(s-side2)*(s-side3));
        //double side1 = Math.sqrt(Integer.parseInt(parts[2])-Integer.parseInt(parts[0]));
        //System.out.println("");

        //System.out.println(side1 + " " + side2 + " " + side3);
        System.out.printf("%2.2f%n",area);
        //int s = (parts);
    }

    //x1 = ui.nextInt();  1 1 1 1 1 1
}
