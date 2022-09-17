package junitdemo;


import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.DisplayNameGenerator;
import org.junit.jupiter.api.IndicativeSentencesGeneration;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;


public class DisplayNameTest {
    @Nested
    @DisplayName("DisplayName测试")
    @DisplayNameGeneration(DisplayNameGenerator.Standard.class)
    class Hello_World1 {
        @Test
        void my_name_is_haha1() {
        }
    }

    @Nested
    @DisplayNameGeneration(DisplayNameGenerator.Simple.class)
    class Hello_World2 {
        @Test
        void my_name_is_haha2() {
        }
    }

    @Nested
    @DisplayNameGeneration(DisplayNameGenerator.ReplaceUnderscores.class)
    class Hello_World3 {
        @Test
        void my_name_is_haha3() {
        }
    }

    @Nested
    @IndicativeSentencesGeneration(separator = ", ", generator = DisplayNameGenerator.ReplaceUnderscores.class)
    class Hello_World4 {
        @Test
        void my_name_is_haha4() {
        }
    }
}
