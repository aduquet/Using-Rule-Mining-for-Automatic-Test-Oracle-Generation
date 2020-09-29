package experiment.util;

public class EmptyStackException extends RuntimeException
{
    /**
     * Constructs a EmptyStackException with no detail message.
     */
    public EmptyStackException( )
    {
    }
    
    /*
     * Constructs a EmptyStackException with a detail message.
     * @param msg the detail mesage pertaining to this exception.
     */
    public EmptyStackException( String msg )
    {
        super( msg );
    }
}