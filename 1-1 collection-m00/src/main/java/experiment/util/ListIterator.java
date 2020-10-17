package experiment.util;

/**
 * ListIterator interface for List interface.
 */
public interface ListIterator extends Iterator
{
    /**
     * Tests if there are more items in the collection
     * when iterating in reverse.
     * @return true if there are more items in the collection
     *  when traversing in reverse.
     */
    boolean hasPrevious( );
    
    /**
     * Obtains the previous item in the collection.
     * @return the previous (as yet unseen) item in the collection
     *  when traversing in reverse.
     */
    Object previous( );
     
    /**
     * Remove the last item returned by next or previous.
     * Can only be called once after next or previous.
     */
    void remove( );
}
