package experiment.util;

/**
 * SortedSet interface.
 */
public interface SortedSet extends Set
{
    /**
     * Return the comparator used by this SortedSet.
     * @return the comparator or null if the default comparator is used.
     */
    Comparator comparator( );
    
    /**
     * Find the smallest item in the set.
     * @return the smallest item.
     * @throws NoSuchElementException if the set is empty.
     */
    Object first( );

    /**
     * Find the largest item in the set.
     * @return the largest item.
     * @throws NoSuchElementException if the set is empty.
     */
    Object last( );
}
