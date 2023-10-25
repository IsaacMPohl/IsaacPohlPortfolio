import java.util.Scanner;
public class midPointTable {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter 2 coordinates");
        double x1 = ui.nextDouble();
        double y1 = ui.nextDouble();
        System.out.println("Enter 2 coordinates");
        double x2 = ui.nextDouble();
        double y2 = ui.nextDouble();
        System.out.println("Enter 2 coordinates");
        double x3 = ui.nextDouble();
        double y3 = ui.nextDouble();
        System.out.println("Enter 2 coordinates");
        double x4 = ui.nextDouble();
        double y4 = ui.nextDouble();
        System.out.println("Enter 2 coordinates");
        double x5 = ui.nextDouble();
        double y5 = ui.nextDouble();
        System.out.println("Enter 2 coordinates");
        double x6 = ui.nextDouble();
        double y6 = ui.nextDouble();
        System.out.println("Enter 2 coordinates");
        double x7 = ui.nextDouble();
        double y7 = ui.nextDouble();
        System.out.println("Enter 2 coordinates");
        double x8 = ui.nextDouble();
        double y8 = ui.nextDouble();
        System.out.println("Enter 2 coordinates");
        double x9 = ui.nextDouble();
        double y9 = ui.nextDouble();
        System.out.println("Enter 2 coordinates");
        double x10= ui.nextDouble();
        double y10 = ui.nextDouble();
        System.out.printf("\ta\t    b\t\tMiddle Point \n     (%s,%s)\t(%s,%s)\t(%s,%s)\n     (%s,%s)\t(%s,%s)\t(%s,%s)\n     (%s,%s)\t(%s,%s)\t(%s,%s)\n     (%s,%s)\t(%s,%s)\t(%s,%s)\n     (%s,%s)\t(%s,%s)\t(%s,%s)\n",x1,y1,x2,y2,((x1+x2)/2),((y1+y2)/2),x3,y3,x4,y4,((x3+x4)/2),((y3+y4)/2),x5,y5,x6,y6,((x5+x6)/2),((y5+y6)/2),x7,y7,x8,y8,((x7+x8)/2),((y7+y8)/2),x9,y9,x10,y10,((x9+x10)/2),((y9+y10)/2));
    }
}
