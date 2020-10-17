# Batch Scripts for Unittest Generation and Execution
## Description
For generating Unittests with Randoop based on Testdrivers and executing tests grouped by Class, Seed and Limit to generate well-named csv-outputs.

Scripts `testsuite.bat` and `randoop-call.bat` are designed to take 4 Arguments in the following order:
* Package of the class (see below), e.g. `experiment.util`
* Class the Tests should run again, e.g. `Stack`
* Randomseed as Integer
* Output Limit as Integer

Scripts `run-randoop.bat` and `run-junit.bat` are created to call one of the above mentioned scripts with different arguments.

Script `run-all.bat` uses intermediate script `fullrun.bat` to run `randoop-call.bat`, then `testsuite.bat` for a given set of arguments.

## Usage
### Prerequisites:
* JAVA_HOME should be set to a JDK (check output in commandline)
* Testdrivers should be generated into src/test/java
* Drivers and implementations should be compiled, expected locations are target/classes and target/test-classes (compiling can be done with e.g. mvn verify). Make sure there are no deprecated *Driver.class files in /target/classes/ or subdirectories.
* `junit.jar` (JUnit 4) and `hamcrest-core.jar` are available (necessary for running the tests)
  - Please set environment variables JUNIT and HAMCREST  to the absolute paths of the jar files (e.g. `<path-to-jar>\hamcrest-core-1.3.jar`)
  - Alternatively, replace %JUNIT% and %HAMCREST% in `testsuite.bat` by correct paths to jar files.

### Using the Scripts separately
1. Prepare Randoop Generations by collecting all calls in `run-randoop.bat` - follow the format `call randoop-call.bat <Packagename> <Classname> <Seed> <Limit>`
2. Execute `run-randoop.bat` to generate the Unittests. They are automatically generated into src/test/java/<packagepath>/test and get the Classname, Seed and Limit encoded into their names.
3. Prepare JUnit Executions by collecting the calls in `run-junit.bat`. Follow the format `call testsuite.bat <Packagename> <Classname> <Seed> <Limit>` for all combinations a csv should be generated for.
4. Execute `run-junit.bat` to execute the Tests and generate well-named .csv-Files. They should appear in the same directory as the batch scripts.

### Using the Scripts for complete execution
1. Prepare Generation and Execution by collecting all calls in `run-all.bat` - follow the format `call fullrun.bat <Packagename> <Classname> <Seed> <Limit>`
2. Execute run-all.bat to generate and execute the Unittests. Unittests are generated into src/test/java/<packagepath>/test and get the Classname, Seed and Limit encoded into their names. Well-named .csv-Files from Test Execution should appear in the same directory as the batch script.