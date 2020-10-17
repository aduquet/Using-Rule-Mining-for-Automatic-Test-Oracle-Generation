java -classpath target\classes;target\test-classes;bin;C:\Users\duquet\Documents\RuleMining_TestOracle\randoop-all-4.2.3.jar randoop.main.Main gentests --testclass=%1.%2TestDriver --junit-output-dir=src/test/java/ --regression-test-basename=Regression_%2Test_%3_%4_ --error-test-basename=Error_%2Test_%3_%4_ --junit-package-name=%1.test --randomseed=%3 --output-limit=%4 --junit-before-each=before_snippet
set package=%1
set path2Delete=%package:.=\%
REM del %path2Delete%\test\*.class
del *seed0_limit0.csv
