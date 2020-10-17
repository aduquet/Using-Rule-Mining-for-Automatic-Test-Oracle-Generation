package experiment.util;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;


/**
 * Generated class that is intended to be used as test driver for class {@link Stack}.
 * 
 * @author generated code
 *
 */
public class StackTestDriver {
 
    protected static final Logger logger = Logger.getLogger(StackTestDriver.class.getName());
   
    private static Writer writer;
    static {
    	try {
    	    String seed = System.getProperty("seed", "0");
    		String limit = System.getProperty("limit", "0");
			writer = new FileWriter(String.format("StackTestDriverData_seed%s_limit%s.csv", seed, limit));
			//write header line    
	    	writer.write("testId,instanceId,isEmpty,size,peek,calledMethod,arguments"+"\n");
	    	writer.flush();
			
		} catch (IOException e) {
			throw new ExceptionInInitializerError(e.getMessage());
		}
    }
    
    private Stack classUnderTest;
    private String instanceId;
    private String testId;
    
    public StackTestDriver() {
    	this.classUnderTest = new Stack();
    	this.instanceId = String.valueOf(java.time.Instant.now().toEpochMilli()+":"+java.util.UUID.randomUUID().toString());
    	this.testId = System.getProperty("testId", "unknown");
    	
    	writeInternalState("CTOR", new String[0]);
    }
    

    public void clear() {
	    try {
          getClassUnderTest().clear();

		} finally {
			writeInternalState("clear", new String[]{});
		}
    }

    public Object pop() {
	    try {
          return getClassUnderTest().pop();

		} finally {
			writeInternalState("pop", new String[]{});
		}
    }

    public Object push(Object arg0) {
	    try {
          return getClassUnderTest().push(arg0);

		} finally {
			writeInternalState("push", new String[]{arg0.toString()});
		}
    }

	private void writeInternalState(String methodName, String[] parametersAsString)  {
		String internalState =  getInternalState(methodName, parametersAsString);
		if(writer == null) return;
		try {
			writer.write(internalState);
			writer.flush();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}

    private String getInternalState(String methodName, String[] parametersAsString) {
   		List<String> state = new ArrayList<>();
   		//todo add test identifier
   		state.add(testId);
   		state.add(instanceId);
    	try {
	   		state.add(Boolean.toString(getClassUnderTest().isEmpty()));
        } catch (Exception e) {
        	//e.printStackTrace();
        	state.add("EXC");
        }
    	try {
	   		state.add(Integer.toString(getClassUnderTest().size()));
        } catch (Exception e) {
        	//e.printStackTrace();
        	state.add("EXC");
        }
    	try {
	   		state.add(getClassUnderTest().peek().toString());
        } catch (Exception e) {
        	//e.printStackTrace();
        	state.add("EXC");
        }
		state.add(methodName);
		state.add(String.join("_",parametersAsString));
        return String.join(",", state) + "\n";
     }
	     
	     
    protected Stack getClassUnderTest() {
        return this.classUnderTest;
    }

}

