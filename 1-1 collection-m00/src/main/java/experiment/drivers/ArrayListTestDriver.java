package experiment.drivers;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;



/**
 * Generated class that is intended to be used as test driver for class {@link ArrayList}.
 *
 * @author generated code
 *
 */
public class ArrayListTestDriver {
 
    protected static final Logger logger = Logger.getLogger(ArrayListTestDriver.class.getName());

    private static Writer writer;
    static {
    	try {
			writer = new FileWriter("ArrayListTestDriverData.csv");
		} catch (IOException e) {
			throw new ExceptionInInitializerError(e.getMessage());
		}
    }
    
    private experiment.util.ArrayList classUnderTest;
    

    public boolean add(java.lang.Object arg0) {
	    try {
          return getClassUnderTest().add(arg0);

		} finally {
			writeInternalState("add", new String[]{arg0.toString()});
		}
    }

    public java.lang.Object remove(int arg0) {
	    try {
          return getClassUnderTest().remove(arg0);

		} finally {
			writeInternalState("remove", new String[]{java.lang.Integer.toString(arg0)});
		}
    }

    public boolean remove(java.lang.Object arg0) {
	    try {
          return getClassUnderTest().remove(arg0);

		} finally {
			writeInternalState("remove", new String[]{arg0.toString()});
		}
    }

    public java.lang.Object get(int arg0) {
	    try {
          return getClassUnderTest().get(arg0);

		} finally {
			writeInternalState("get", new String[]{java.lang.Integer.toString(arg0)});
		}
    }

    public void clear() {
	    try {
          getClassUnderTest().clear();

		} finally {
			writeInternalState("clear", new String[]{});
		}
    }

    public boolean contains(java.lang.Object arg0) {
	    try {
          return getClassUnderTest().contains(arg0);

		} finally {
			writeInternalState("contains", new String[]{arg0.toString()});
		}
    }

    public experiment.util.Iterator iterator() {
	    try {
          return getClassUnderTest().iterator();

		} finally {
			writeInternalState("iterator", new String[]{});
		}
    }

    public int size() {
	    try {
          return getClassUnderTest().size();

		} finally {
			writeInternalState("size", new String[]{});
		}
    }

    public java.lang.Object set(int arg0, java.lang.Object arg1) {
	    try {
          return getClassUnderTest().set(arg0,arg1);

		} finally {
			writeInternalState("set", new String[]{java.lang.Integer.toString(arg0),arg1.toString()});
		}
    }

    public experiment.util.ListIterator listIterator(int arg0) {
	    try {
          return getClassUnderTest().listIterator(arg0);

		} finally {
			writeInternalState("listIterator", new String[]{java.lang.Integer.toString(arg0)});
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
   		state.add(methodName);
		state.add(String.join("_",parametersAsString));
        return String.join(",", state) + "\n";
     }

    protected experiment.util.ArrayList getClassUnderTest() {
        if(classUnderTest == null) {
            classUnderTest = new experiment.util.ArrayList();
        }
        return classUnderTest;
    }

}

