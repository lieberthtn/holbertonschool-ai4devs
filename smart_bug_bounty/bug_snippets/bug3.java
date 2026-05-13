public class Main {
    public static void main(String[] args) {
        String text = null;
        // Səhv: Null olan obyektin metodu çağırılır
        if (text.equals("hello")) {
            System.out.println("Match!");
        }
    }
}
