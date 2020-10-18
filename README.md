# Using-Rule-Mining-for-Automatic-Test-Oracle-Generation

# Using Rule Mining for Automatic Test Oracle Generation

Software testing is essential for checking the quality of software but it is also a costly and time-consuming activity. The mechanism to determine the correct output of the System Under Test (SUT) for a given input space is called test oracle. The test oracle problem is a known bottleneck in situations where tests are generated automatically and no model of the correct behaviour of the SUT exists. To overcome this bottleneck, we developed a method which generates test oracles by comparing information extracted from object state data created during the execution of two subsequent versions of the SUT. In our initial proof-ofconcept, we derive the relevant information in the form of rules by using the Association Rule Mining (ARM) technique. As a proof-of-concept, we validate our method on the Stack class from a custom version of the Java Collection classes and discuss the lessons learned from our experiment. The test suite that we use in our experiment to execute the different SUT version is automatically generated using Randoop. Other approaches to generate object state data could be used instead. Our proof-of-concept demonstrates that our method is applicable and that we can detect the presence of failures that are missed by regression testing alone. Automatic analysis of the set of violated association rules provides valuable information for localizing faults in the SUT. This kind of information cannot be found in the execution traces of failing tests.

# Repository Organization

- The data realated to the state of the Stack and the modifications can be founf in folder 1 - State Data - Stack
- Java collection classes used for the experiments can be found in 1-1 collection-m00
- File 1-2 Report state data provides an overview of the state data generated
- File 1-3 Regression Test-Reports are the output from the regression test generated by Random
- Ruleset generated can be found  in 2-Ruleset generated file
- The data set used to validate against the ruleset can be found in folder 3 - New unique rows
- The data used for the fault localisation part is in the folder 4-Fault localization

