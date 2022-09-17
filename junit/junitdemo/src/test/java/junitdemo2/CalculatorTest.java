package junitdemo2;

import junitdemo.Calculator;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;

@DisplayName("计算测试demo")
public class CalculatorTest {
    private final Calculator _calculator = new Calculator();

    @BeforeAll
    public static void initAll() {
        System.out.println("@BeforeAll: 所有测试用例之前执行一次");
    }

    @BeforeEach
    public void init() {
        System.out.println("@BeforeEach: 每条测试用例之前执行");
    }

    @AfterAll
    public static void tearDownAll() {
        System.out.println("@AfterAll: 所有测试用例之后执行一次");
    }

    @AfterEach
    public void tearDown() {
        System.out.println("@AfterEach: 每条测试用例之后执行");
    }

    @Test
    @DisplayName("加法测试")
    public void testAddition(){
        System.out.println("testAddition");
        int actualResult = _calculator.add(1, 2);
        Assertions.assertEquals(3, actualResult);
    }

    @Test
    @DisplayName("除法测试")
    public void testdivision(){
        System.out.println("testdivision");
        int actualResult = _calculator.div(6, 3);
        Assertions.assertEquals(2, actualResult);
    }

    @Test
    @Disabled("跳过")
    public void skippedTest(){
        System.out.println("skippedTest");
    }
}
