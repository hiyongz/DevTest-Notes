package junitdemo;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;
import static org.junit.jupiter.api.Assumptions.assumeFalse;
import static org.junit.jupiter.api.Assumptions.assumingThat;

import org.junit.jupiter.api.Test;

public class AssumptionTest {
    @Test
    void trueAssumption() {
        assumeTrue(2 > 1, () -> "跳过测试");
        assertEquals(1 + 1, 2); //assumption为true时才执行
        System.out.println("2 > 1 为True");
    }

    @Test
    void falseAssumption() {
        assumeFalse(2 < 1);
        assertEquals(1 + 1, 2); // assumption为false时才执行
        System.out.println("2 < 1为False");
    }

    @Test
    void assumptionThat() {
        String someString = "Just a string";
        assumingThat(
                someString.equals("Just a string"),
                () -> assertEquals(2 + 2, 4)
        );
        assertEquals(1+1, 2); // 不管assumption是否为true，都会执行
        System.out.println("1 + 1 = 2");
    }
}
