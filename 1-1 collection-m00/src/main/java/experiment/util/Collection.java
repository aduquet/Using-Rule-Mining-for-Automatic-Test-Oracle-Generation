package experiment.util;

/**
 * Collection interface; the root of all 1.2 collections.
 */
public interface Collection extends java.io.Serializable
{
    /**
     * Returns the number of items in this collection.
     * @return the number of items in this collection.
     */
    int size( );
    
    /**
     * Tests if this collection is empty.
     * @return true if the size of this collection is zero.
     */
    boolean isEmpty( );
    
    /**
     * Tests if some item is in this collection.
     * @param x any object.
     * @return true if this collection contains an item equal to x.
     */
    boolean contains( Object x );
    
    /**
     * Adds an item to this collection.
     * @param x any object.
     * @return true if this item was added to the collection.
     */
    boolean add( Object x );
    
    /**
     * Removes an item from this collection.
     * @param x any object.
     * @return true if this item was removed from the collection.
     */
    boolean remove( Object x );
    
    /**
     * Change the size of this collection to zero.
     */
    void clear( );
    
    /**
     * Obtains an Iterator object used to traverse the collection.
     * @return an iterator positioned prior to the first element.
     */
    Iterator iterator( );
    
    /**
     * Obtains a primitive array view of the collection.
     * @return the primitive array view.
     */
    Object [ ] toArray( );
}
