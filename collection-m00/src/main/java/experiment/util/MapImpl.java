package experiment.util;

/**
 * MapImpl implements the Map on top of a set.
 * It should be extended by TreeMap and HashMap, with
 * chained calls to the constructor.
 */
abstract class MapImpl implements Map
{
    private Set theSet;
    
    protected abstract Map.Entry makePair( Object key, Object value );
    protected abstract Set makeEmptyKeySet( );
    protected abstract Set clonePairSet( Set pairSet );
    
    private Map.Entry makePair( Object key )
    {
        return makePair( key, null );
    }
        
    protected MapImpl( Set s )
    {
        theSet = s;
    }
    
    protected MapImpl( Map m )
    {
        theSet = m.entrySet( );
    }
    
    /**
     * Returns the number of keys in this map.
     * @return the number of keys in this collection.
     */
    public int size( )
    {
        return theSet.size( );
    }
    
    /**
     * Tests if this map is empty.
     * @return true if the size of this map is zero.
     */
    public boolean isEmpty( )
    {
        return theSet.isEmpty( );
    }

    /**
     * Tests if this map contains a given key.
     * @param key the key to search for.
     * @return true if the map contains the key.
     */
    public boolean containsKey( Object key )
    {
        return theSet.contains( makePair( key ) );
    }

    /**
     * Returns the value in the map associated with the key.
     * @param key the key to search for.
     * @return the value that matches the key or null
     * if the key is not found. Since null values are allowed,
     * checking if the return value is null may not
     * be a safe way to ascertain if the key is present in the map.
     */
    public Object get( Object key )
    {
        Object match = theSet.getMatch( makePair( key ) );
        
        if( match == null )
            return null;
        else
            return ( (Map.Entry) match ).getValue( );    
    }

    /**
     * Adds the key value pair to the map, overriding the
     * original value if the key was already present.
     * @param key the key to insert.
     * @param value the value to insert.
     * @return the old value associated with the key, or
     * null if the key was not present prior to this call.
     */
    public Object put( Object key, Object value )
    {
    	// Object oldValue = get( key );
    	
    	// fix: overriding does not work in the set since duplicates are not allowed
    	Object oldValue = null;					
    	if (containsKey(key)) {				
    		oldValue = remove(key);    		
    	}
    	// end of fix
    	
    	theSet.add( makePair( key, value ) );
    	return oldValue;
    }
        

    /**
     * Remove the key and its value from the map.
     * @param key the key to remove.
     * @return the previous value associated with the key,
     * or null if the key was not present prior to this call.
     */
    public Object remove( Object key )
    {
        Object oldValue = get( key );
        
        // fix: remove fails if the value is null because it cannot be distinguished from get(key); see JDK Javadoc
        
        //if( oldValue != null )
        if (containsKey(key))
        
        // end of fix
        	
            theSet.remove( makePair( key ) );
    	
        return oldValue;    
    }

    /**
     * Removes all key value pairs from the map. 
     */
    public void clear( )
    {
        theSet.clear( );
    }

    /**
     * Returns the keys in the map.
     * These semantics are different from those in java.util because
     * in this class, changes made to the returned key set do not cause
     * changes to be reflected in the map.
     * @return the keys in the map.
     */
    public Set keySet( )
    {
        Iterator itr = theSet.iterator( );
        Set result = makeEmptyKeySet( );
        
        while( itr.hasNext( ) )
            result.add( ( (Map.Entry) itr.next( ) ).getKey( ) );

        return result;
    }

    /**
     * Returns the values in the map. There may be duplicates.
     * These semantics are different from those in java.util because
     * in this class, changes made to the returned value collection
     * do not cause changes to be reflected in the map.
     * @return the values in the map.
     */
    public Collection values( )
    {
        Iterator itr = theSet.iterator( );
        Collection result = new ArrayList( );
        
        while( itr.hasNext( ) )  
            result.add( ( (Map.Entry) itr.next( ) ).getValue( ) );

        return result;
    
    }

    /**
     * Return a set of Map.Entry objects corresponding to
     * the key/value pairs in the map.
     * These semantics are different from those in java.util because
     * in this class, changes made to the returned key/value set do not cause
     * changes to be reflected in the map.
     * @return the key/value pairs in the map.
     */ 
    public Set entrySet( )
    {
        return clonePairSet( theSet );
    }

    /**
     * Return a reference to the underlying set.
     */
    protected Set getSet( )
    {
        return theSet;
    }
}
