// bug3.java
// Category: Runtime Exceptions

import java.util.ArrayList;

public class Bug3 {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("Alice");
        names.add("Bob");

        for (int i = 0; i <= names.size(); i++) {
            System.out.println(names.get(i).toUpperCase());
        }

        String value = null;
        System.out.println(value.length());
    }
}