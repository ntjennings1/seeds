//package Java.examples.3evenOdd.src.java;

/**
 * Represents the main function of example 3.
 * 
 * @author Noah Jennings
 * @author ntjennings1@gmail.com
 */
class Main{
    public static void main(String[] args) {
        
        int x = 13; 
        int y = 14; 

        int sum = x + y;
        
        if (sum % 2 == 0){

            System.out.println("Their sum is even.");
            System.out.printf("The sum equals: " + sum);

        }
        else{

            System.out.println("Their sum is odd.");
            System.out.printf("The sum equals: " + sum);

        }
    }
}