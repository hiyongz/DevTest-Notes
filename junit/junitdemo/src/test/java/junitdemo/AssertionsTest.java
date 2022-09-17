package junitdemo;

import static java.time.Duration.ofMillis;
import static java.time.Duration.ofMinutes;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeAll;

import java.time.Duration;
import java.util.concurrent.CountDownLatch;

import java.lang.Math;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

public class AssertionsTest {
    private final Calculator calculator = new Calculator();
    private static final String KEY = "key";
    private static final String VALUE = "value";
    private static Map<String, String> map;

    private static Person person;

    @BeforeAll
    public static void InitMap() {
        map = new HashMap<>();
        map.put(KEY, VALUE);

    }

    @Test
    void standardAssertions() {
        assertEquals(3, Math.addExact(1,2));
        assertNotEquals(8, Math.multiplyExact(2,3));
    }

    @Test
    void BooleanAssertions() {
        assertTrue(map.containsKey(KEY),() -> String.format("The map doesn't contain the key: %s", KEY));
        assertFalse(!map.containsKey(KEY),() -> String.format("The map does contain the key: %s", KEY));

        assertFalse(false, "The boolean is not false");
    }

    @Test
    void nullAssertions() {
        assertNull(null);
        assertNotNull(new Object());
    }

    @Test
    void sameObjectAssertions() {
        Object ACTUAL = new Object();
        Object EXPECTED = ACTUAL;
        assertSame(EXPECTED, ACTUAL);

        Object ACTUAL2 = new Object();
        Object EXPECTED2 = new Object();
        assertNotSame(EXPECTED2, ACTUAL2);
    }

    @Test
    void arrayAssertions() {
        int[] ACTUAL = new int[]{2, 5, 7};
        int[] EXPECTED = new int[]{2, 5, 7};
        assertArrayEquals(EXPECTED, ACTUAL);
    }

    @Test
    void iterableAssertions() {
        List<Integer> FIRST = Arrays.asList(1, 2, 3);
        List<Integer> SECOND = Arrays.asList(1, 2, 3);
        assertIterableEquals(FIRST, SECOND);
    }

    @Test
    void exceptionsAssertions() {
        assertThrows(
                NullPointerException.class,
                () -> { throw new NullPointerException(); }
        );

        final NullPointerException thrown = assertThrows(
                NullPointerException.class,
                () -> { throw new NullPointerException("Hello World!"); }
        );
        assertEquals("Hello World!", thrown.getMessage());

        assertDoesNotThrow(() -> {});
        String message = assertDoesNotThrow(() -> { return "Hello World!"; } );
        assertEquals("Hello World!", message);

    }

    @Test
    void timeoutAssertions() {
        final String message = assertTimeout(Duration.ofMillis(50), () -> {
            Thread.sleep(20);
            return "Hello World!";
        });
        assertEquals("Hello World!", message);

        final String message2 = assertTimeoutPreemptively(Duration.ofMillis(50), () -> {
            Thread.sleep(20);
            return "Hello World!";
        });
        assertEquals("Hello World!", message2);
    }


    @Test
    void groupAssertions() {
        final String FIRST_NAME = "Jane";
        final String LAST_NAME = "Doe";
        person = new Person();
        person.setFirstName(FIRST_NAME);
        person.setLastName(LAST_NAME);

        assertAll("name",
                () -> assertEquals(FIRST_NAME,
                        person.getFirstName(),
                        "The first name is incorrect"
                ),
                () -> assertEquals(LAST_NAME,
                        person.getLastName(),
                        "The last name is incorrect"
                )
        );
    }




}
