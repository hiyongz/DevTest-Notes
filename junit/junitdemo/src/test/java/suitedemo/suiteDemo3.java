package suitedemo;

import org.junit.platform.runner.JUnitPlatform;
import org.junit.platform.suite.api.SelectPackages;
import org.junit.platform.suite.api.ExcludePackages;
import org.junit.platform.suite.api.SuiteDisplayName;
import org.junit.runner.RunWith;

@RunWith(JUnitPlatform.class)
@SuiteDisplayName("JUnit Platform Suite Demo")
@SelectPackages({"junitdemo", "junitdemo2"})
@ExcludePackages("junitdemo.AssertionsTest")
public class suiteDemo3 {

}
