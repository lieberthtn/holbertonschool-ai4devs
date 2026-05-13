/**
 * BUG BOUNTY CASE #3
 * Language: Java
 * Intended: Safely validate a user token.
 * Current issue: Potential NullPointerException on method call.
 */

public class TokenValidator {
    public static void main(String[] args) {
        String userToken = null;

        System.out.println("Initiating validation sequence...");

        // CRITICAL BUG: This will throw a NullPointerException 
        // because userToken is explicitly null.
        if (userToken.equals("ADMIN_ACCESS_2026")) {
            System.out.println("Access granted to the system.");
        } else {
            System.out.println("Access denied.");
        }
    }
}
