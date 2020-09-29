set package=%1
set testclasspath=%package:.=\%

javac -d .\target\test-classes -classpath .;C:\Users\duquet\Documents\Installers\junit-4.13.jar;target\classes\;target\test-classes\ src\test\java\%testclasspath%\test\RegressionTest-9\*_%2Test_%3_%4_*.java

java -Dseed=%3 -Dlimit=%4 -classpath .;;C:\Users\duquet\Documents\Installers\junit-4.13.jar;C:\Users\duquet\Documents\Installers\hamcrest-core-1.3.jar;target\classes\;target\test-classes\ org.junit.runner.JUnitCore %1.test.Regression_%2Test_%3_%4_