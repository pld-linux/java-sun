/**
 * Class for testing Class Version this JVM is able to load
 * We test this by compiling class and looking it's version.
 */

import java.util.*;

public class Test {
    public static void main(String[] args) {
		Properties p = System.getProperties();
		System.err.println(p.get("java.class.version"));
	}
}
