package experiment.util;

/**
 * Instanceless class contains static methods that operate on collections.
 */
public class Collections
{
    private Collections( )
    {
    }
    
    /**
     * Returns the maximum object in the collection, using default ordering
     * @param coll the collection.
     * @return the maximum object.
     * @throws NoSuchElementException if coll is empty.
     * @throws ClassCastException if objects in collection cannot be compared.
     */
    public static Object max( Collection coll )
    {
        return max( coll, DEFAULT_COMPARATOR );
    }
    
    /**
     * Returns the maximum object in the collection, using comparator.
     * @param coll the collection.
     * @param cmp the comparator.
     * @return the maximum object.
     * @throws NoSuchElementException if coll is empty.
     * @throws ClassCastException if objects in collection cannot be compared.
     */
    public static Object max( Collection coll, Comparator cmp )
    {
        if( coll.size( ) == 0 )
            throw new NoSuchElementException( );
            
        Iterator itr = coll.iterator( );
        Object maxValue = itr.next( );
        
        while( itr.hasNext( ) )
        {
            Object current = itr.next( );
            if( cmp.compare( current, maxValue ) > 0 )
                maxValue = current;
        }
        
        return maxValue;    
    }
    
    
    /*
     * Returns a comparator that imposes the reverse of the
     * default ordering on a collection of objects that
     * implement the Comparable interface.
     * @return the comparator.
     */
    public static Comparator reverseOrder( )
    {
        return new ReverseComparator( );
    }
    
    private static class ReverseComparator implements Comparator
    {
        public int compare( Object lhs, Object rhs )
        {                
            return -( (Comparable) lhs ).compareTo( rhs );
        }
    }
        
    
    static class DefaultComparator implements Comparator
    {
        public int compare( Object lhs, Object rhs )
        {          
        	// fix: does not handle null values
        	// begin fix
        	if ((lhs == null) && (rhs == null)) {
        		return 0;
        	} else if (lhs == null) {
        		return -1;
        	} else if (rhs == null) {
        		return 1;
        	} else {
        	// end fix
        		
        		return ( (Comparable) lhs ).compareTo( rhs );
        		
        	}
        }
    }
    
    static final Comparator DEFAULT_COMPARATOR = new DefaultComparator( );
}
