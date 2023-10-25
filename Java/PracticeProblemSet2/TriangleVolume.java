import java.util.Scanner;
public class triangleVolume {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter the length of the sides and height of the Equilateral triangle: ");
        double sideDimension = ui.nextDouble();
        //System.out.println((Math.pow(sideDimension,2)));
        //System.out.println((Math.sqrt(3)/4 ));
        double area = ((Math.sqrt(3)/4 ) * (Math.pow(sideDimension,2)));
        double volume = area * sideDimension;
        System.out.printf("The area is %2.2f%n ", area);
        System.out.printf("The volume of the Triangular prism is %2.2f%n ", volume);

    }
}
