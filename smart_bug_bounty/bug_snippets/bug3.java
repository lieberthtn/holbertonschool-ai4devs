/**
 * Bug Bounty Challenge - Case 3
 * This Java snippet demonstrates a NullPointerException.
 * The code attempts to call a method on a null object reference.
 */

public class BuggyApp {
    public static void main(String[] args) {
        String inputData = null;

        System.out.println("Checking input consistency...");
        
        // Critical Issue: Calling .equals() on a null object
        // This will crash the JVM at runtime.
        try {
            if (inputData.equals("VALID_TOKEN")) {
                System.out.println("Access Granted");
            }
        } catch (NullPointerException e) {
            System.err.println("Error: " + e.toString());
        }
    }
}
