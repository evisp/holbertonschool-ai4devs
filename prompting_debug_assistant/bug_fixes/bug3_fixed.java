// Bug3_fixed.java
// Category: Runtime Exceptions

import java.util.ArrayList;

public class Bug3_fixed {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Alice");
        names.add("Bob");

        // Fix 1: use i < names.size() to avoid IndexOutOfBoundsException
        for (int i = 0; i < names.size(); i++) {
            System.out.println(names.get(i).toUpperCase());
        }

        // Fix 2: avoid calling length() on null
        String value = null;
        if (value != null) {
            System.out.println(value.length());
        } else {
            System.out.println(0);
        }

        // Tests (simple checks)
        assert names.size() == 2;
        assert "Alice".toUpperCase().equals("ALICE");
    }
}
