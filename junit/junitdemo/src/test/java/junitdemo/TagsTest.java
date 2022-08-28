package junitdemo;

import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

public class TagsTest {
    @Test
    @Tag("add")
    void addAssert() {
        assertEquals(3, Math.addExact(1,2));
    }

    @Test
    @Tag("multiply")
    void multiplyAssert() {
        assertNotEquals(8, Math.multiplyExact(2,3));
    }
}
