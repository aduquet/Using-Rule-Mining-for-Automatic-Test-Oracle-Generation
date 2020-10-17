package experiment.util;

import java.io.Serializable;

/**
 * Map interface.
 * A map stores key/value pairs.
 * In our implementations, duplicate keys are not allowed.
 */
public interface Map extends Serializable
{
    /**
     * Returns the number of keys in this map.
     * @return the number of keys in this collection.
     */
    int size( );
    
    /**
     * Tests if this map is empty.
     * @return true if the size of this map is zero.
     */
    boolean isEmpty( );

    /**
     * Tests if this map contains a given key.
     * @param key the key to search for.
     * @return true if the map contains the key.
     */
    boolean containsKey( Object key );

    /**
     * Returns the value in the map associated with the key.
     * @param key the key to search for.
     * @return the value that matches the key or null
     * if the key is not found. Since null values are allowed,
     * checking if the return value is null may not
     * be a safe way to ascertain if the key is present in the map.
     */
    Object get( Object key );

    /**
     * Adds the key value pair to the map, overriding the
     * original value if the key was already present.
     * @param key the key to insert.
     * @param value the value to insert.
     * @return the old value associated with the key, or
     * null if the key was not present prior to this call.
     */
    Object put( Object key, Object value );

    /**
     * Remove the key and its value from the map.
     * @param key the key to remove.
     * @return the previous value associated with the key,
     * or null if the key was not present prior to this call.
     */
    Object remove( Object key );

    /**
     * Removes all key value pairs from the map. 
     */
    void clear( );

    /**
     * Returns the keys in the map.
     * @return the keys in the map.
     */
    Set keySet( );

    /**
     * Returns the values in the map. There may be duplicates.
     * @return the values in the map.
     */
    Collection values( );

    /**
     * Return a set of Map.Entry objects corresponding to
     * the key/value pairs in the map.
     * @return the key/value pairs in the map.
     */ 
    Set entrySet( );

    /**
     * The interface used to access the key/value pairs in a map.
     * From a map, use entrySet().iterator to obtain a iterator
     * over a Set of pairs. The next() method of this iterator yields
     * objects of type Map.Entry.
     */
    public interface Entry extends Serializable
    {
        /**
         * Obtains this pair's key.
         * @return the key associated with this pair.
         */
        Object getKey( );

        /**
         * Obtains this pair's value.
         * @return the value associated with this pair.
         */
        Object getValue( );
    }
}
