package experiment.util;

/**
 * List interface.
 * The version in java.util places the
 * union of sensible LinkedList and ArrayList methods in
 * this interface. We place the useful intersection here
 * instead, which is arguably empty.
 */
public interface List extends Collection
{    
    /**
     * Returns the item at position idx.
     * @param idx the index to search in.
     * @throws IndexOutOfBoundsException if index is out of range.
     */
    Object get( int idx );
        
    /**
     * Changes the item at position idx.
     * @param idx the index to change.
     * @param newVal the new value.
     * @return the old value.
     * @throws IndexOutOfBoundsException if index is out of range.
     */
    Object set( int idx, Object newVal );
    
    /**
     * Obtains a ListIterator object used to traverse the collection bidirectionally.
     * @return an iterator positioned prior to the requested element.
     * @param idx the index to start the iterator. Use size() to do complete
     * reverse traversal. Use 0 to do complete forward traversal.
     * @throws IndexOutOfBoundsException if idx is not between 0 and size(), inclusive.
     */
    ListIterator listIterator( int idx );
}
