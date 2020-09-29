package experiment.util;

/**
 * Iterator interface.
 */
public interface Iterator
{
    /**
     * Tests if there are items not yet iterated over.
     * @return true if there are more items in the collection.
     */
    boolean hasNext( );
    
    /**
     * Obtains the next (as yet unseen) item in the collection.
     * @return the next (as yet unseen) item in the collection.
     */
    Object next( );
    
    /**
     * Remove the last item returned by next.
     * Can only be called once after next.
     */
    void remove( );
}
