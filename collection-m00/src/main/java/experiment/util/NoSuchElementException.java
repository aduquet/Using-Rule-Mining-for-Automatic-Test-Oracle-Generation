package experiment.util;

public class NoSuchElementException extends RuntimeException
{
    /**
     * Constructs a NoSuchElementException with no detail message.
     */
    public NoSuchElementException( )
    {
    }
    
    /*
     * Constructs a NoSuchElementException with a detail message.
     * @param msg the detail mesage pertaining to this exception.
     */
    public NoSuchElementException( String msg )
    {
        super( msg );
    }
}