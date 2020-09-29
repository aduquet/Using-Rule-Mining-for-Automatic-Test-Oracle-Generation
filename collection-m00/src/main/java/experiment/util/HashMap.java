package experiment.util;

/**
 * Hash table implementation of the Map.
 */
public class HashMap extends MapImpl
{
    /**
     * Construct an empty HashMap.
     */
    public HashMap( )
    {
        super( new HashSet( ) );
    }
    
    /**
     * Construct a HashMap with same key/value pairs as another map.
     * @param other the other map.
     */
    public HashMap( Map other )
    {
        super( other );
    }
    
    protected Map.Entry makePair( Object key, Object value )
    {
        return new Pair( key, value );
    }
    
    protected Set makeEmptyKeySet( )
    {
        return new HashSet( );
    }
    
    protected Set clonePairSet( Set pairSet )
    {
        return new HashSet( pairSet );
    }
    
    private static final class Pair implements Map.Entry
    {
        public Pair( Object k, Object v )
        {
            key = k;
            value = v;
        }
        
        public Object getKey( )
        {
            return key;
        }
        
        public Object getValue( )
        {
            return value;
        }
        
        public int hashCode( )
        {
//            return key.hashCode( );
        	return (key == null) ? 0 : key.hashCode();		// fix: npe if key is null
        }
        
        public boolean equals( Object other )
        {
            if( other instanceof Map.Entry )
            	
            	// begin fix: npe if key is null
            	if ((getKey() == null) && (((Map.Entry)other).getKey() == null)) {
            		return true;
            	} else if (getKey() == null) {
            		return false;
            	} else if (((Map.Entry)other).getKey() == null) {
            		return false;
            	} else {
            	// end fix
            		
            		return getKey( ).equals( ((Map.Entry) other).getKey( ) );

            	}
            
            else
                return false;    
        }
        
        private Object key;
        private Object value;
    }
}
