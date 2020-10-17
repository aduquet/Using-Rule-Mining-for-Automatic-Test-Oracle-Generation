package experiment.util;

public class ConcurrentModificationException extends RuntimeException
{
    /**
     * Constructs a ConcurrentModificationException with no detail message.
     */
    public ConcurrentModificationException( )
    {
    }
    
    /*
     * Constructs a ConcurrentModificationException with a detail message.
     * @param msg the detail mesage pertaining to this exception.
     */
    public ConcurrentModificationException( String msg )
    {
        super( msg );
    }
}