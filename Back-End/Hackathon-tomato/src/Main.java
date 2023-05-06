import java.lang.reflect.Array;
import java.util.Scanner;
import java.util.ArrayList;
// THIS IS PAMS CODE WE TRANSLATED TO PYTHON
public class Main {
    public static void main(String[] args) {
        //------------------------------------------------------------
        // Experiment code 1
        Scanner scan= new Scanner(System.in);

        System.out.println("");
        System.out.print("Enter the Temperature:");
        int tempInput = scan.nextInt();

        System.out.print("");
//        int wateramount = scan.nextInt();

        if (tempInput >= 65 && tempInput <=85) {
            System.out.println("Water plant once in the morning, daily");
        }else if (tempInput < 65 && tempInput >=50){
            System.out.println("Water plant once, every other day");
        } else if (tempInput < 50) {
            System.out.println("Weather unstable, plant will not grow");
        } else if (tempInput > 85 && tempInput >=95) {
            System.out.println("Water plant twice, every day");
        }else if (tempInput > 95){
            System.out.println("Weather unstable, plant will not grow");
        }


//            if (wateramount ){
//                System.out.println("Please do not water");
//            }
//            System.out.println("Level is ideal");
//        }else {
//            if (wateramount == )



    }
}//end of main