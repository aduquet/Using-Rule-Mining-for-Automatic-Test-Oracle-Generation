package experiment.util;

/**
 * Balanced search tree implementation of the Map.
 */
public class TreeMap extends MapImpl
{
    /**
     * Construct an empty TreeMap with default comparator.
     */
    public TreeMap( )
    {
        super( new TreeSet( ) );
    }
    
    /**
     * Construct a TreeMap using comparator.
     * @param comparator the comparator.
     */
    public TreeMap( Comparator comparator )
    {
        super( new TreeSet( ) );
        cmp = comparator;
    }
        
    /**
     * Construct a TreeMap with same key/value pairs
     * and comparator as another map..
     * @param other the other map.
     */
    public TreeMap( Map other )
    {
        super( other );
    }
    
    /**
     * Gets the comparator; returns null if default.
     * @return the comparator or if null if default is used.
     */
    public Comparator comparator( )
    {
        if( cmp == Collections.DEFAULT_COMPARATOR )
            return null;
        else
            return cmp;    
    }
    
    protected Map.Entry makePair( Object key, Object value )
    {
        return new Pair( key, value );
    }
    
    protected Set makeEmptyKeySet( )
    {
    	
    	// fix: comparator() returns null if DEFAULT_COMPARATOR, TreeSet requires a non-null cmp
    	
    	Comparator cmp = ((TreeSet)getSet( ) ).comparator( );
    	if (cmp == null) {
    		cmp = Collections.DEFAULT_COMPARATOR;
    	}
        return new TreeSet( cmp );
        
        //return new TreeSet( ((TreeSet)getSet( ) ).comparator( ) );
        
    	// end fix
        
    }
    
    protected Set clonePairSet( Set pairSet )
    {
        return new TreeSet( pairSet );
    }
    
    private final class Pair implements Map.Entry, Comparable
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
                
        public int compareTo( Object other )
        {
            return cmp.compare( getKey( ), ((Map.Entry) other).getKey( ) );
        }
        
        private Object key;
        private Object value;
    }
    
    private Comparator cmp = Collections.DEFAULT_COMPARATOR;
}
