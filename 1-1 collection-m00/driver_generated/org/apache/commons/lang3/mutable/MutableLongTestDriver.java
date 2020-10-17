package org.apache.commons.lang3.mutable;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;



/**
 * Generated class that is intended to be used as test driver for class {@link MutableLong}.
 * 
 * @author generated code
 *
 */
public class MutableLongTestDriver {
 
    protected static final Logger logger = Logger.getLogger(MutableLongTestDriver.class.getName());
   
    private static Writer writer;
    static {
    	try {
			writer = new FileWriter("MutableLongTestDriverData.csv");
		} catch (IOException e) {
			throw new ExceptionInInitializerError(e.getMessage());
		}
    }
    
    private org.apache.commons.lang3.mutable.MutableLong classUnderTest;
    

    public void decrement() {
	    try {
          getClassUnderTest().decrement();

		} finally {
			writeInternalState("decrement", new String[]{});
		}
    }

    public void subtract(long arg0) {
	    try {
          getClassUnderTest().subtract(arg0);

		} finally {
			writeInternalState("subtract", new String[]{java.lang.Long.toString(arg0)});
		}
    }

    public void subtract(java.lang.Number arg0) {
	    try {
          getClassUnderTest().subtract(arg0);

		} finally {
			writeInternalState("subtract", new String[]{arg0.toString()});
		}
    }

    public java.lang.Long toLong() {
	    try {
          return getClassUnderTest().toLong();

		} finally {
			writeInternalState("toLong", new String[]{});
		}
    }

    public void add(long arg0) {
	    try {
          getClassUnderTest().add(arg0);

		} finally {
			writeInternalState("add", new String[]{java.lang.Long.toString(arg0)});
		}
    }

    public void add(java.lang.Number arg0) {
	    try {
          getClassUnderTest().add(arg0);

		} finally {
			writeInternalState("add", new String[]{arg0.toString()});
		}
    }

    public boolean equals(java.lang.Object arg0) {
	    try {
          return getClassUnderTest().equals(arg0);

		} finally {
			writeInternalState("equals", new String[]{arg0.toString()});
		}
    }

    public java.lang.String toString() {
	    try {
          return getClassUnderTest().toString();

		} finally {
			writeInternalState("toString", new String[]{});
		}
    }

    public int hashCode() {
	    try {
          return getClassUnderTest().hashCode();

		} finally {
			writeInternalState("hashCode", new String[]{});
		}
    }

    public int compareTo(java.lang.Object arg0) {
	    try {
          return getClassUnderTest().compareTo(arg0);

		} finally {
			writeInternalState("compareTo", new String[]{arg0.toString()});
		}
    }

    public int compareTo(org.apache.commons.lang3.mutable.MutableLong arg0) {
	    try {
          return getClassUnderTest().compareTo(arg0);

		} finally {
			writeInternalState("compareTo", new String[]{arg0.toString()});
		}
    }

    public int intValue() {
	    try {
          return getClassUnderTest().intValue();

		} finally {
			writeInternalState("intValue", new String[]{});
		}
    }

    public long longValue() {
	    try {
          return getClassUnderTest().longValue();

		} finally {
			writeInternalState("longValue", new String[]{});
		}
    }

    public float floatValue() {
	    try {
          return getClassUnderTest().floatValue();

		} finally {
			writeInternalState("floatValue", new String[]{});
		}
    }

    public double doubleValue() {
	    try {
          return getClassUnderTest().doubleValue();

		} finally {
			writeInternalState("doubleValue", new String[]{});
		}
    }



    public void increment() {
	    try {
          getClassUnderTest().increment();

		} finally {
			writeInternalState("increment", new String[]{});
		}
    }

    public void setValue(java.lang.Object arg0) {
	    try {
          getClassUnderTest().setValue(arg0);

		} finally {
			writeInternalState("setValue", new String[]{arg0.toString()});
		}
    }

    public void setValue(java.lang.Number arg0) {
	    try {
          getClassUnderTest().setValue(arg0);

		} finally {
			writeInternalState("setValue", new String[]{arg0.toString()});
		}
    }

    public void setValue(long arg0) {
	    try {
          getClassUnderTest().setValue(arg0);

		} finally {
			writeInternalState("setValue", new String[]{java.lang.Long.toString(arg0)});
		}
    }

    public long getAndAdd(long arg0) {
	    try {
          return getClassUnderTest().getAndAdd(arg0);

		} finally {
			writeInternalState("getAndAdd", new String[]{java.lang.Long.toString(arg0)});
		}
    }

    public long getAndAdd(java.lang.Number arg0) {
	    try {
          return getClassUnderTest().getAndAdd(arg0);

		} finally {
			writeInternalState("getAndAdd", new String[]{arg0.toString()});
		}
    }



    public long incrementAndGet() {
	    try {
          return getClassUnderTest().incrementAndGet();

		} finally {
			writeInternalState("incrementAndGet", new String[]{});
		}
    }

    public long decrementAndGet() {
	    try {
          return getClassUnderTest().decrementAndGet();

		} finally {
			writeInternalState("decrementAndGet", new String[]{});
		}
    }

    public long addAndGet(java.lang.Number arg0) {
	    try {
          return getClassUnderTest().addAndGet(arg0);

		} finally {
			writeInternalState("addAndGet", new String[]{arg0.toString()});
		}
    }

    public long addAndGet(long arg0) {
	    try {
          return getClassUnderTest().addAndGet(arg0);

		} finally {
			writeInternalState("addAndGet", new String[]{java.lang.Long.toString(arg0)});
		}
    }


	private void writeInternalState(String methodName, String[] parametersAsString)  {
		String internalState =  getInternalState(methodName, parametersAsString);
		if(writer == null) return;
		try {
			writer.write(internalState);
			writer.flush();
		} catch(IOException e) {
			e.printStackTrace();
		}
	}

    private String getInternalState(String methodName, String[] parametersAsString) {
   		List<String> state = new ArrayList<>();
   		state.add(getClassUnderTest().getValue().toString());
   		state.add(getClassUnderTest().getValue().toString());
   		state.add(java.lang.Long.toString(getClassUnderTest().getAndIncrement()));
   		state.add(java.lang.Long.toString(getClassUnderTest().getAndDecrement()));
   		state.add(methodName);
		state.add(String.join("_",parametersAsString));
        return String.join(",", state) + "\n";
     }

    protected org.apache.commons.lang3.mutable.MutableLong getClassUnderTest() {
        if(classUnderTest == null) {
            classUnderTest = new org.apache.commons.lang3.mutable.MutableLong();
        }
        return classUnderTest;
    }

}

